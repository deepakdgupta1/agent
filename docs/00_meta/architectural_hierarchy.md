# Architectural Hierarchy v2

This document tracks the evolution of the Master AI Agent Blueprint framework.
Version: v2

## Version history

| Version | Phase | Agents folded in | Source reports |
| --- | --- | --- | --- |
| v0 | 0 | (seed) | `AI Agent Feature Hierarchy Development.md` |
| v1 | 1 | [AIDER], [BABYAGI] | `aider_research.md`, `babyagi_research.md` |
| **v2** | 2 | + [CLAUDE] (claw-code) | `claude_code_research_part1.md`, `claude_code_research_part2.md` |

## Scope of v2

Version v2 incorporates Phase 2 findings from `docs/_research/claude_code_research_part1.md` and `docs/_research/claude_code_research_part2.md`. It builds on v1 (which folded in Phase 1: Aider and archived BabyAGI) without reverting any v1 refinement.

> **Source-of-truth note**: the [CLAUDE] research is grounded in the local clone at `/Users/deepg/Desktop/agent/claw-code/` pinned at HEAD `a389f8dff1d591d2eafc2f48747313cd556412ee`. The harness lives in the **Rust** workspace under `rust/crates/`. Where claw-code diverges from upstream Claude Code documentation, the research and synthesis report **source reality** (e.g., 5 `PermissionMode` variants vs. upstream's 3 modes; 3 hook events vs. upstream's 9; project-only `CLAUDE.md` discovery; `.claw/`-branded settings root; default mode `DangerFullAccess`). These divergences are called out in-line in the module documents.

## The v2 Framework Mapped to the 8-Module Structure

### Level 1: Macro-Architecture and Ecosystem Autonomy
Mapped to:
- `docs/01_core_loop/`
- `docs/06_orchestration/`
- `docs/07_permissions_and_governance/`

Refinement from v1: macro-architecture now includes a third top-level operating mode — **the multi-tool-call turn** [CLAUDE]. One user message into `ConversationRuntime::run_turn` produces an arbitrary internal trajectory of LLM calls + tool dispatches before returning, and the model itself decides termination by emitting a text-only assistant response. This sits alongside Aider's user-steered edit loop and archived BabyAGI's objective task loop. [AIDER] [BABYAGI] [CLAUDE]

The orchestration module now includes a real **sub-agent spawning primitive**: `Agent` spawns a child `ConversationRuntime` in a `clawd-agent-{id}` thread with a reduced tool set, fresh `Session`, and isolated `PermissionPolicy`. Communication back to the parent is file-based (`<agent_id>.md` + `<agent_id>.json` manifest). [CLAUDE]

### Level 2: Sensory Perception and Input Processing
Mapped to:
- `docs/08_user_interaction/input_processing.md`
- `docs/03_context_engine/`

Refinement from v1: input processing now documents the **three-tier REPL interception model** (slash command → bare-skill bypass → `run_turn`) [CLAUDE]. Slash commands are intercepted before the model sees the input — one of 139 spec-table entries / ~30 parser categories — and `/skills`'s `Invoke(prompt)` is the **one** slash-command path that ends up calling the model. [CLAUDE] Aider's command-first preprocessing remains the conversational analog. [AIDER]

### Level 3: Context and Retrieval Engine
Mapped to:
- `docs/03_context_engine/context_assembly.md`
- `docs/03_context_engine/repo_map_and_indexing.md`
- `docs/03_context_engine/retrieval_strategies.md`
- `docs/03_context_engine/token_economics.md`

Refinement from v1: the context engine now distinguishes **prompt-time discovery** [CLAUDE] from per-call retrieval. Claude Code builds the system prompt **once per turn** via `SystemPromptBuilder::build`, walking cwd ancestors for `CLAUDE.md`/`CLAUDE.local.md`/`.claw/CLAUDE.md`/`.claw/instructions.md`, deduping by content hash, and capping each file at 4_000 chars and the whole block at 12_000 chars (`prompt.rs:43-44, 144-166`). [CLAUDE] Retrieval per call is *not* used; instead, the full `session.messages` is cloned into every iteration's `ApiRequest` until auto-compaction kicks in. [CLAUDE]

### Level 4: The Core Cognitive Engine
Mapped to:
- `docs/01_core_loop/`
- `docs/02_cognition/`

Refinement from v1: cognition now includes a **structurally-emergent reasoning pattern** [CLAUDE] — interleaved text and tool-use blocks (`build_assistant_message`, `conversation.rs:706-753`), `TodoWrite` as a metacognitive scratch-pad, `Skill` for packaged routines, `AskUserQuestion` for ambiguity escalation, `EnterPlanMode`/`ExitPlanMode` for posture switching, and `StructuredOutput` for JSON-typed thinking. There is no explicit `Thinking` content block or `extended_thinking` flag in claw-code at HEAD `a389f8d`. [CLAUDE] Self-correction emerges from `is_error: true` tool results re-entering the model context on the next iteration — there is no harness-level retry counter. [CLAUDE]

### Level 5: Metacognition, Feedback, and Self-Regulation
Mapped to:
- `docs/02_cognition/reasoning_patterns.md`
- `docs/08_user_interaction/feedback_loops.md`
- `docs/07_permissions_and_governance/`

Refinement from v1: metacognition now includes the **hooks system** as a programmable feedback surface [CLAUDE]. Three lifecycle events (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`) — flat `string[]` config without matcher syntax — let shell scripts intercept every tool call, override the permission decision, rewrite tool inputs (`updatedInput`), or inject `additionalContext` into the conversation. [CLAUDE] The complementary `SessionTracer` provides hot-path telemetry without subprocess cost. [CLAUDE]

### Level 6: Memory Architecture and Temporal Persistence
Mapped to:
- `docs/04_memory/`
- `docs/03_context_engine/retrieval_strategies.md`

Refinement from v1: persistent memory is **promoted to a first-class mechanism** [CLAUDE]. `discover_instruction_files(cwd)` walks ancestors and probes four filenames per directory in fixed order; root-most-first load order; content-hash dedupe; rendered as `# Claude instructions` with `## <filename> (scope: <dir>)` subheadings. [CLAUDE] Auto-compaction at `cumulative input_tokens >= 100_000` (default) replaces older messages with a system summary while preserving the last 4 verbatim (`compact.rs:71-183`). [CLAUDE] **Notably absent in claw-code at HEAD `a389f8d`**: user-home memory file, enterprise memory file, `@include` directives, auto-write-back from `/memory`. [CLAUDE]

### Level 7: Action Orchestration and Executable Skill Libraries
Mapped to:
- `docs/05_action_and_tools/`
- `docs/07_permissions_and_governance/permission_model.md`

Refinement from v1: the action layer now has a **typed-spec registry** [CLAUDE] — `ToolSpec { name, description, input_schema, required_permission }` aggregated by `GlobalToolRegistry` from three sources (50 built-in specs + plugin tools + runtime MCP tools), filtered by `--allowedTools`, sent on `MessageRequest.tools` with `tool_choice: Auto`. [CLAUDE] Tool calls and results travel as `ContentBlock::ToolUse` / `ContentBlock::ToolResult` correlated by `tool_use_id`. [CLAUDE]

The **MCP integration** is now documented: `mcpServers` settings shape with six transport variants, but only `stdio` actually connects at HEAD `a389f8d`. Qualified-name format `mcp__<server>__<tool>` brings runtime-discovered tools into the same model-facing surface as built-ins. [CLAUDE]

### Level 8: Governance, Guardrails, and Alignment
Mapped to:
- `docs/07_permissions_and_governance/`
- `docs/08_user_interaction/`

Refinement from v1: governance now has a **mode-based permission system** with rule grammar and override layers [CLAUDE]. Five `PermissionMode` variants (three CLI-exposed: `read-only`, `workspace-write`, `danger-full-access`) plus deny/allow/ask rule lists with `ToolName(matcher)` grammar; ordered authorization (`deny → hook → ask → mode/allow → default deny`); `PermissionEnforcer` workspace-boundary check; `is_read_only_command` heuristic for `bash` under `ReadOnly`. [CLAUDE] **Notable divergences**: claw-code's default mode is `DangerFullAccess` (upstream defaults to a safer mode); managed/enterprise policy paths are **not implemented**; `--dangerously-skip-permissions` is "skip the prompter and mode-escalation gate" — it does **not** bypass deny rules, hook denies, or workspace-boundary checks. [CLAUDE]

## What Changed from v1 and Why

| Change | Why it changed in v2 | Phase 2 evidence |
| :--- | :--- | :--- |
| Promoted **multi-tool-call turn** as a first-class macro pattern. | One user message can drive an arbitrary internal trajectory; the model decides termination by emitting text-only. This is structurally different from Aider's reflected-message retry and BabyAGI's queue iteration. | `ConversationRuntime::run_turn` and the iterate-until-no-tool-use loop. [CLAUDE] |
| Added **typed-spec tool registry** to Level 7. | Phase 1's edit-protocol-as-tools (Aider) and no-tool baseline (BabyAGI) didn't define a tool architecture. Claude Code introduces `ToolSpec`/`GlobalToolRegistry`/`ToolExecutor` as the structural primitives. | `tools::mvp_tool_specs()` 50 built-ins; `MessageRequest.tools` with `tool_choice: Auto`. [CLAUDE] |
| Added **mode-based permission system** with rule grammar to Level 8. | Phase 1's user-confirmation gates (Aider) and no-permission baseline (BabyAGI) didn't define a policy layer. Claude Code introduces `PermissionMode` + `PermissionRule` + `PermissionEnforcer` as the permission triad. | `permissions.rs:175-292`, `permission_enforcer.rs:108-201`. [CLAUDE] |
| Added **hooks system** to Level 5. | Reflected messages (Aider) are model-driven; BabyAGI has no metacognition layer. Hooks introduce a programmable, harness-driven feedback surface that can override decisions, rewrite inputs, and inject context. | `hooks.rs:21-37, 588-657`. [CLAUDE] |
| Added **filesystem-backed persistent memory** to Level 6. | Aider's chat history and BabyAGI's vector recall don't cover instruction-file-based persistence. Claude Code's `discover_instruction_files` introduces this paradigm. | `prompt.rs:203-224, 331-403`. [CLAUDE] |
| Added **sub-agent spawning** to Level 1. | Phase 1 had no sub-agent primitive. Claude Code's `Agent` tool spawns child runtimes in threads with isolated state and per-`subagent_type` tool subsets. | `tools/src/lib.rs:3477-3721`. [CLAUDE] |
| Added **MCP extensibility** to Level 7. | Phase 1 had no plugin/extension surface. Claude Code's MCP integration provides a standard JSON-RPC-over-stdio extension paradigm. | `mcp_stdio.rs`, `mcp.rs`, `mcp_tool_bridge.rs`. [CLAUDE] |
| Promoted **slash-command interception** to Level 2. | Phase 1's `Commands.run()` (Aider) was the precursor; Claude Code generalizes it with a 139-entry spec table, ~30 parsed categories, hard-coded REPL exits, and the bare-skill bypass. | `main.rs:3579-3617`, `commands/src/lib.rs:1207, 1290-1496`. [CLAUDE] |

## v2 Phase 2 Gaps (carried into Phase 3+)

The following remain as placeholders or partially-populated stubs after Phase 2:

- **Sandboxing** (`docs/07_permissions_and_governance/sandboxing.md`) — Phase 3 [CODEX] will populate this richly. claw-code's `bash` schema has sandbox-shaping fields (`namespaceRestrictions`, `isolateNetwork`, `filesystemMode`, `allowedMounts`) but the actual enforcement layer is permission rules + hooks, not a kernel-level sandbox.
- **Browser interaction** (`docs/05_action_and_tools/browser_interaction.md`) — Phase 4 [CLINE] will populate this. claw-code does not implement a `Browser` sub-agent; `mcp__Claude_in_Chrome__*` are deferred MCP tools, not built-ins.
- **Workflow modes** (`docs/06_orchestration/workflow_modes.md`) — Phase 4 [ROO] will populate this with the mode-system architecture (Code, Architect, Debug, Ask, Orchestrator).
- **Task lifecycle** (`docs/06_orchestration/task_lifecycle.md`) — Phase 5 [KILO] will populate this with checkpoint/diff patterns. claw-code's `TaskRegistry` is bookkeeping only.
- **Episodic memory** (`docs/04_memory/episodic_memory.md`) — Phase 6 [AUTOGPT] will populate this with execution-trace memory.
- **Output formatting** (`docs/08_user_interaction/output_formatting.md`) — Phase 6 [OI] will populate this with streaming architecture.
- **Safety guardrails** (`docs/07_permissions_and_governance/safety_guardrails.md`) — Phase 6 [OI]/[AUTOGPT] will populate this with safe mode and budget limits.
- **Reasoning patterns** beyond Phase 2 — Phase 6 [AUTOGPT] will add explicit self-critique loops; Claude Code's pattern is structurally emergent rather than prompt-engineered.
- **Plugin paradigm contrast** (`docs/05_action_and_tools/extensibility.md`) — Phase 6 [AUTOGPT] will add the *code-based* plugin pattern alongside the *protocol-based* MCP pattern documented in Phase 2.
- **Per-action approval** (`docs/07_permissions_and_governance/permission_model.md`) — Phase 4 [CLINE] will add this as a third permission paradigm alongside Claude Code's modes and (Phase 3) Codex's autonomy levels.
- **OpenRouter multi-provider routing** (`docs/02_cognition/model_routing.md`) — Phase 5 [KILO] will add this. Aider's architect/editor model split is the Phase 1 reference; Claude Code uses one provider per session.

The hierarchy will be revised in v3 (Phase 3, [CODEX]) with the sandbox-first architecture and autonomy-level system as central additions.
