# Multi-Agent Patterns
> Module: 06_orchestration | Status: Phase 2 | Last Agent: Claude Code Synthesis

## 1. Overview
Multi-agent patterns are mechanisms by which a parent agent delegates work to a subordinate agent — typically with a reduced tool set and an isolated context — and aggregates the result. This document specifies the [CLAUDE] sub-agent pattern as the Phase 2 reference. Phase 4 will add Roo Code's Boomerang orchestration alongside; Phase 6 will add AutoGPT-style autonomous spawning.

[CLAUDE] exposes **three distinct primitives** that the upstream task spec collapses into a single "Task" tool. None of them is named `Task` at the tool surface in claw-code; the spec's "Task" is closest to the **`Agent`** tool. The three primitives:

| Primitive | What it does | Spawns a runtime? |
| --- | --- | --- |
| **`Agent`** | Spawns a child `ConversationRuntime` in a worker thread with a reduced tool set. **This is the real "Task" analog.** | Yes — child Rust thread with full agentic loop. |
| **`TaskCreate` / `TaskGet` / `TaskList` / `TaskOutput` / `TaskStop` / `TaskUpdate`** | Pure in-memory `TaskRegistry` bookkeeping (`Arc<Mutex<HashMap>>`). | No — no LLM call anywhere in `task_registry.rs`. |
| **`WorkerCreate` / `WorkerObserve` / `WorkerSendPrompt` / …** | State-machine harness over an *externally* spawned coding-agent process; observed via screen-text events. | No — claw-code does not spawn the worker process. |

> **Important divergence from upstream**: upstream Claude Code's `Task` tool spawns a sub-agent. claw-code's `TaskCreate` only writes to a registry; **`Agent` is the tool that actually spawns**. Browser sub-agent (`Browser`, etc.) is **not implemented in claw-code at HEAD `a389f8d`** — `mcp__Claude_in_Chrome__*` and `mcp__Claude_Preview__*` are deferred MCP-side tools advertised via `ToolSearch`, not built-in browser sub-agents.

(claw-code: `rust/crates/tools/src/lib.rs:571-587, 3477-3617, 1571-1605`; `rust/crates/runtime/src/task_registry.rs:34-232`; `rust/crates/runtime/src/worker_boot.rs:30-410`.)

## 2. Blueprint Specification

### `Agent` tool — sub-runtime spawning [CLAUDE]
- **Spec**: `Agent { description, prompt, subagent_type?, name?, model? }` with `required_permission: DangerFullAccess` (Part 1 §2 catalog).
- **Entry**: `execute_agent_with_spawn(input, spawn_fn)` validates `description`/`prompt`, generates `agent_id`, writes a markdown manifest plus a JSON manifest under `agent_store_dir()`, then delegates to `spawn_agent_job(job)` (`tools/src/lib.rs:3481-3559`).
- **Spawn**: `spawn_agent_job` creates a thread named `clawd-agent-{id}` running `run_agent_job(&job)` (`tools/src/lib.rs:3561-3586`).
- **Child runtime construction** — `build_agent_runtime(job)` builds `ConversationRuntime<ProviderRuntimeClient, SubagentToolExecutor>` with (`tools/src/lib.rs:3597-3617`):
  - A fresh `Session::new()`.
  - The resolved model — `DEFAULT_AGENT_MODEL = "claude-opus-4-6"` (`tools/src/lib.rs:3473`).
  - The parent's filtered allowed-tools set, further reduced per `subagent_type` (see below).
  - An `agent_permission_policy()` derived from `mvp_tool_specs()` requirements.
  - System prompt from `build_agent_system_prompt(subagent_type)`.
- **Iteration cap**: `DEFAULT_AGENT_MAX_ITERATIONS = 32` via `with_max_iterations` (`tools/src/lib.rs:3475, 3589`). This is *much* tighter than the parent's `usize::MAX` default — sub-agents are hard-bounded.

### Child system prompt [CLAUDE]
`build_agent_system_prompt(subagent_type)` calls `load_system_prompt(cwd, DEFAULT_AGENT_SYSTEM_DATE, OS, "unknown")`, then appends:

```
You are a background sub-agent of type `<subagent_type>`. Work only on the
delegated task, use only the tools available to you, do not ask the user
questions, and finish with a concise result.
```

(`tools/src/lib.rs:3619-3632`.)

So the child **re-discovers `CLAUDE.md` etc. from its cwd** — the same memory hierarchy is inherited via path, not value-copied.

### Per-`subagent_type` tool subsets [CLAUDE]
`allowed_tools_for_subagent` (`tools/src/lib.rs:3642-3721`):

| Subagent type | Allowed tools |
| --- | --- |
| `Explore` | `read_file, glob_search, grep_search, WebFetch, WebSearch, ToolSearch, Skill, StructuredOutput` |
| `Plan` | Read-only set + `TodoWrite, SendUserMessage` |
| `Verification` | `bash, read_file, glob_search, grep_search, WebFetch, WebSearch, ToolSearch, TodoWrite, StructuredOutput, SendUserMessage, PowerShell` |
| `claw-guide` | Read-only + `Skill, SendUserMessage` |
| `statusline-setup` | `bash, read_file, write_file, edit_file, glob_search, grep_search, ToolSearch` |
| **Default** (any unrecognized) | Broad set incl. `bash, write_file, edit_file, REPL, PowerShell, Sleep, Config, NotebookEdit` |

### Context isolation [CLAUDE]
The child has a **brand-new `Session`**, its **own `ConversationRuntime`**, its **own `PermissionPolicy`** (defaulting to `DangerFullAccess` modulo per-tool `required_permission`), and a `SubagentToolExecutor` constrained to the `allowed_tools` set (`tools/src/lib.rs:3608-3614`). Parent and child do **not** share `Session::messages` or `usage_tracker`.

### Communication is file-based [CLAUDE]
There is **no parent-poll tool**. The child writes results to:

- **`output_file`** = `<agent_store_dir>/<agent_id>.md` — the assistant's final text output.
- **`manifest_file`** = `<agent_store_dir>/<agent_id>.json` — JSON manifest including `status: "completed" | "failed"` plus the final assistant text.

(`tools/src/lib.rs:3493-3496, 3593-3594, 3740-3760`.) The manifest path is returned in the synchronous `AgentOutput` value the `Agent` tool produces (`tools/src/lib.rs:3526-3543`); the parent must read the file (e.g. via `read_file`) to fetch results.

### `TaskRegistry` bookkeeping primitives [CLAUDE]
`TaskRegistry` is `Arc<Mutex<HashMap<String, Task>>>` with **no spawn, no runtime, no LLM call** (`task_registry.rs:34-232`):

- `create(prompt, description?)` allocates `task_id = format!("task_{:08x}_{}", ts, counter)` and stores `prompt, description, task_packet?, status, messages, output, team_id` (`task_registry.rs:79-120`).
- `update(task_id, message)` appends a user message.
- `append_output(task_id, text)` accumulates a string.
- `stop(task_id)` flips status with a terminal-state guard.
- `RunTaskPacket { objective, scope, repo, branch_policy, acceptance_tests, commit_policy, reporting_contract, escalation_policy }` routes through `TaskRegistry::create_from_packet` after `validate_packet` (`task_registry.rs:83-94`, `task_packet.rs`). Still in-registry — does not spawn a runtime.

The model uses these as *bookkeeping* tools to record TODOs the user can inspect via `/tasks` (which is parsed-but-stubbed in claw-code at HEAD).

### Worker harness primitives [CLAUDE]
`WorkerCreate(cwd, trusted_roots?, auto_recover_prompt_misdelivery?)` allocates `worker_id` and pushes a `Spawning` event but **spawns no process** (`worker_boot.rs:223-263`). `worker_boot::WorkerStatus`: `Spawning, TrustRequired, ReadyForPrompt, Running, Finished, Failed` (`worker_boot.rs:30-37`).

`WorkerObserve(worker_id, screen_text)` does string-pattern matching for trust-prompt detection, prompt-misdelivery detection (e.g. prompt landed in shell), and ready-cues; status transitions are state-machine-only (`worker_boot.rs:271-410`). The actual process is run by an external supervisor (terminal/tmux) — claw-code is the orchestrator, not the spawner.

### Teams [CLAUDE]
`TeamCreate(name, tasks)` allocates a `team_id` and tags each task with `assign_team(task_id, team_id)`; `TeamDelete` removes it (`tools/src/lib.rs:1571-1605`, `team_cron_registry.rs`). Pure bookkeeping; no execution semantics.

## 3. Logic Flow

### `Agent` spawn lifecycle
1. Model emits `ContentBlock::ToolUse { name: "Agent", input: { description, prompt, subagent_type? } }`.
2. Parent harness's permission gate authorizes (`DangerFullAccess` required).
3. `execute_agent_with_spawn` validates inputs and writes `<agent_id>.md` + `<agent_id>.json` placeholder manifests.
4. `spawn_agent_job` creates a `clawd-agent-{id}` thread.
5. Inside the thread:
   a. `build_agent_runtime(job)` constructs the child `ConversationRuntime`.
   b. Child calls `load_system_prompt(cwd, ...)` — re-discovering `CLAUDE.md` from disk.
   c. Child appends the sub-agent persona suffix.
   d. Child filters tools per `subagent_type`.
   e. Child runs `run_turn(prompt, prompter)` with `max_iterations: 32`.
   f. Child writes output to `output_file` and updates `manifest_file` on completion via `persist_agent_terminal_state`.
6. Parent thread receives `AgentOutput` containing the manifest path.
7. Parent typically calls `read_file` on the manifest path to fetch the result on the next iteration.

### `TaskRegistry` lifecycle (no runtime)
1. Model emits `ToolUse { name: "TaskCreate", input: { prompt, description? } }`.
2. Harness mutex-locks the registry, allocates `task_id`, stores the entry.
3. Returns the `task_id` immediately.
4. Subsequent `TaskUpdate` / `TaskGet` / `TaskList` / `TaskStop` / `TaskOutput` / `TaskUpdate` calls mutate or read the same registry — no LLM is involved.

## 4. Flowchart
```mermaid
flowchart TD
    A[Model emits ToolUse Agent] --> B[Permission DangerFullAccess]
    B --> C[execute_agent_with_spawn validates inputs]
    C --> D[Write manifest placeholder to agent_store_dir]
    D --> E[spawn_agent_job creates clawd-agent thread]
    E --> F[build_agent_runtime: fresh Session]
    F --> G[load_system_prompt rediscovers CLAUDE.md]
    G --> H[Append sub-agent persona suffix]
    H --> I[Filter tools per subagent_type]
    I --> J[Set max_iterations=32]
    J --> K[run_turn with prompter]
    K --> L{Loop terminates?}
    L -- yes --> M[persist_agent_terminal_state: write output_file + manifest]
    L -- no max_iterations exceeded --> M
    M --> N[Parent receives AgentOutput with manifest path]
    N --> O[Parent calls read_file on next iteration to fetch result]
```

## 5. Sequence Diagram
```mermaid
sequenceDiagram
    participant ParentModel as Parent Model
    participant ParentRuntime as Parent ConversationRuntime
    participant Spawn as spawn_agent_job
    participant ChildThread as clawd-agent thread
    participant ChildRuntime as Child ConversationRuntime
    participant FS as Filesystem (agent_store_dir)
    participant ChildModel as Child Model

    ParentModel-->>ParentRuntime: ToolUse(Agent, {description, prompt, subagent_type})
    ParentRuntime->>ParentRuntime: permission gate (DangerFullAccess)
    ParentRuntime->>FS: write <agent_id>.md + .json placeholders
    ParentRuntime->>Spawn: spawn_agent_job(job)
    Spawn->>ChildThread: thread "clawd-agent-{id}"
    ChildThread->>ChildRuntime: build_agent_runtime(job)
    ChildRuntime->>FS: load_system_prompt rediscovers CLAUDE.md from cwd
    ChildRuntime->>ChildRuntime: filter tools per subagent_type; max_iterations=32

    loop child loop bounded by 32 iterations
        ChildRuntime->>ChildModel: stream(child messages)
        ChildModel-->>ChildRuntime: ToolUse / Text
        ChildRuntime->>ChildRuntime: dispatch tools (subset only)
    end

    ChildRuntime->>FS: persist_agent_terminal_state writes output + manifest
    Spawn-->>ParentRuntime: AgentOutput{manifest_path}
    ParentRuntime->>ParentRuntime: append ToolResult with manifest path

    Note over ParentRuntime,FS: No streaming back to parent.
    Note over ParentRuntime,FS: Parent must call read_file to fetch results.
    ParentRuntime->>FS: (next iteration) read_file(manifest_path)
    FS-->>ParentRuntime: child output
```

## 6. Variations & Trade-offs

| Pattern | Benefit | Trade-off |
| --- | --- | --- |
| **`Agent` spawning a fresh `ConversationRuntime`** [CLAUDE] | Real context isolation: child can't pollute parent's `Session::messages` or `usage_tracker`; child has its own permission policy. | No live streaming back: parent must poll the manifest file. Child's discovery re-walks the filesystem — duplicate work if many agents share the same cwd. |
| **Per-`subagent_type` tool subsets** [CLAUDE] | A `Plan` agent can't accidentally write files; an `Explore` agent can't run `bash`. Predictable safety floor. | Subset is hard-coded in Rust — adding a new type requires harness changes. |
| **`max_iterations = 32` cap on children** [CLAUDE] | Bounds runaway sub-agents. | Children that need long trajectories will hit the cap and emit a `RuntimeError` — caller must check the manifest. |
| **File-based handoff (manifest + output)** [CLAUDE] | Result survives parent crashes; manifest is human-inspectable; no IPC complexity. | Parent must spend extra tool calls (`read_file`) to surface child results into its context. |
| **`TaskRegistry` (no spawn)** [CLAUDE] | Cheap bookkeeping; user can inspect TODOs without paying for inference. | Easy to confuse with the `Agent` tool — naming is upstream-divergent in claw-code. |
| **`WorkerObserve` state machine** [CLAUDE] | Lets the agent supervise *external* coding agents (terminal/tmux) without being the spawner. | Detection is string-pattern based — fragile if the external agent's prompts change. |
| **`Browser` sub-agent absent** [CLAUDE] | Surface area is smaller; fewer permission tiers to manage. | Browser-driven workflows (Cline-style) require MCP shims (`mcp__Claude_in_Chrome__*`). |

## 7. Agent Attribution Table

| Agent | Source-backed contribution |
| --- | --- |
| [CLAUDE] | `Agent` tool spawning a child `ConversationRuntime` in a `clawd-agent-{id}` thread; `DEFAULT_AGENT_MODEL = "claude-opus-4-6"`; `DEFAULT_AGENT_MAX_ITERATIONS = 32`; per-`subagent_type` tool subsets (`Explore`, `Plan`, `Verification`, `claw-guide`, `statusline-setup`, default); fresh `Session` + isolated `PermissionPolicy` per child; sub-agent persona suffix appended to a re-discovered system prompt; file-based result handoff via `<agent_id>.md` + `<agent_id>.json` manifest under `agent_store_dir()`; separate `TaskRegistry` bookkeeping primitives (`TaskCreate` etc.) with no LLM invocation; `WorkerCreate`/`WorkerObserve` state machine for externally-spawned coding agents; `TeamCreate`/`TeamDelete` task tagging. |

> Phase 4 [ROO]'s Boomerang orchestration will be added alongside; Phase 6 [AUTOGPT]'s self-spawning loop will provide a third pattern.
