# Architectural Hierarchy v4

This document tracks the evolution of the Master AI Agent Blueprint framework.
Version: v4

## Version history

| Version | Phase | Agents folded in | Source reports |
| --- | --- | --- | --- |
| v0 | 0 | (seed) | `AI Agent Feature Hierarchy Development.md` |
| v1 | 1 | [AIDER], [BABYAGI] | `aider_research.md`, `babyagi_research.md` |
| v2 | 2 | + [CLAUDE] (claw-code) | `claude_code_research_part1.md`, `claude_code_research_part2.md` |
| v3 | 3 | + [CODEX] | `codex_research.md` |
| **v4** | 4 | + [CLINE], [ROO] | `cline_research.md`, `roo_code_research.md` |

## Scope of v4

Version v4 incorporates Phase 4 findings from `docs/_research/cline_research.md` and `docs/_research/roo_code_research.md`. Four structural additions dominate v4:

1. **IDE-embedded agent loop as a third macro-pattern.** The blueprint now recognises three distinct loop families: *interactive code-edit loop* (Aider, terminal-based), *tool-use protocol loop* (Claude Code, Rust runtime / Codex, Rust CLI), and *IDE-embedded per-action-approval loop* (Cline/Roo Code, VS Code extension). The IDE-embedded loop introduces per-action approval as the default, streaming partial tool presentation in the webview, mode-multiplexed prompt/tool-surface swapping (Roo), and VS Code extension lifecycle management. [CLINE] [ROO]

2. **Mode system as a first-class orchestration primitive.** Roo Code elevates persona-switching from a binary Plan/Act toggle (Cline) to a full `ModeConfig` framework — `(roleDefinition, groups, customInstructions, fileRegex restrictions)` — with five built-in modes (architect, code, debug, ask, orchestrator) and unlimited user-defined custom modes via `.roomodes` YAML files. Mode simultaneously controls system prompt persona, tool-group RBAC, file-write restrictions, and per-mode model routing. No other agent in the blueprint unifies all four axes into a single user-editable record. [ROO]

3. **Boomerang multi-agent delegation.** Roo Code's `new_task { mode, message, todos? }` implements a durable, persistent, mode-typed parent↔child delegation pattern where: the parent is flushed to disk and disposed; the child runs as a normal Task with the full UI/API stack; on `attempt_completion`, the child's summary is injected as a **synthetic `tool_result`** into the parent's API conversation history; the parent resumes as if `new_task` returned synchronously. This is structurally different from Claude Code's in-process `Agent` sub-agent (ephemeral, 32-iteration cap, file-based manifest) and from Cline's `new_task` (create-and-forget with no return path). [ROO]

4. **Per-action approval as a third permission paradigm.** The permission taxonomy now has four paradigms: mode-based (`PermissionMode` enum [CLAUDE]), two-dimensional matrix (`AskForApproval × SandboxPolicy` [CODEX]), per-action approval (`ask()` blocking with granular auto-approval categories [CLINE]), and mode-as-permission (tool-group RBAC with `fileRegex` restrictions [ROO]). Cline's `CommandPermissionController` adds pattern-based command allow/deny rules. Roo removes hooks entirely (Cline's 9 lifecycle hooks) in favour of MCP servers. [CLINE] [ROO]

Additional v4 refinements:

- **Browser automation populated.** `docs/05_action_and_tools/browser_interaction.md` is no longer a stub — it documents Cline's Puppeteer-based screenshot-driven browser automation (the only first-party browser integration in the blueprint) and Roo's deliberate removal of browser as a deprecated tool group in favour of MCP-based browser servers. [CLINE] [ROO]
- **MCP client comparison expanded.** `docs/05_action_and_tools/extensibility.md` now covers three MCP client implementations: Claude Code's Rust-based stdio-only `McpServerManager`, Cline's TypeScript `McpHub` with stdio+SSE+WebSocket transports, and Roo's mode-conditional variant with `alwaysAllow`, `disabledTools`, and silent deduplication. [CLINE] [ROO]
- **Feedback loops expanded.** `docs/08_user_interaction/feedback_loops.md` adds Cline's per-action approval as a feedback mechanism, the `didRejectTool` cascade, `attempt_completion` as a bidirectional feedback gate, and Roo's mode-driven feedback patterns (debug mode's structured diagnosis flow, Boomerang completion feedback). [CLINE] [ROO]

> **Source-of-truth note (v4)**: the [CLINE] research is grounded in a local checkout of `cline/cline` (the `cline/` directory in the workspace). The [ROO] research is grounded in a local checkout of `RooVetGit/Roo-Code` (the `roo/` directory). Where Roo Code diverges from its Cline fork (mode system, Boomerang delegation, browser deprecation, hooks removal), these divergences are documented as deliberate architectural choices, not bugs.

## Scope of v3

Version v3 incorporates Phase 3 findings from `docs/_research/codex_research.md`. Two structural additions dominate v3:

1. **Sandbox-first execution as a runtime property.** The blueprint now treats *containment* as a property of the runtime independent of *approval*. A sandbox is no longer "a feature of a tool" (as it was implicit in v2's `bash` schema fields) — it is a per-platform OS-level layer (`Seatbelt` on macOS, `bubblewrap + seccomp` on Linux via the standalone `codex-linux-sandbox` helper, `restricted-token + Job Object` on Windows) selected from a shared `SandboxPolicy` enum on the wire protocol. See [sandboxing.md](../07_permissions_and_governance/sandboxing.md). [CODEX]
2. **Two-dimensional autonomy: `AskForApproval × SandboxPolicy`.** The permission system gains a second axis. v2's [CLAUDE] mode collapses both questions into one variant; v3 [CODEX] decomposes them. `Never` no longer implies "unsandboxed" — containment is decided by `SandboxPolicy` independently. The five `AskForApproval` × four `SandboxPolicy` product is materialised through three named presets (`read-only`, `auto`, `full-access`) and one explicit unsafe escape hatch (`--dangerously-bypass-approvals-and-sandbox`). [CODEX]

A third refinement runs through every loop-related document: **approval is now a wire-protocol round-trip**. v1's Aider used in-process Python `confirm_ask`; v2's claw-code used a runtime `prompter` callback; v3's [CODEX] emits `EventMsg::ExecApprovalRequest` / `ApplyPatchApprovalRequest` and parks the turn until matching `Op::ExecApproval` / `Op::PatchApproval` arrives on the submission queue. This is what lets the same `core` crate drive a TUI, a headless `exec`, an MCP-server-as-Codex, and an IDE/app-server front-end without code changes.

> **Source-of-truth note (v3)**: the [CODEX] research is grounded in a local checkout of `openai/codex` at commit `87bc72408c5ef08f8d21f2cdd00c55451c3be33f` (`/tmp/codex-review`). The harness lives in the **Rust** workspace under `codex-rs/` (80+ crates). Where the present `task.md` description ("3 autonomy levels: suggest / auto-edit / full-auto") and the source diverge, the v3 docs report source reality: five `AskForApproval` variants, four `SandboxPolicy` variants, three named presets, and the `--full-auto` flag is **not** the same as the `auto` preset.

## Scope of v2

Version v2 incorporates Phase 2 findings from `docs/_research/claude_code_research_part1.md` and `docs/_research/claude_code_research_part2.md`. It builds on v1 (which folded in Phase 1: Aider and archived BabyAGI) without reverting any v1 refinement.

> **Source-of-truth note**: the [CLAUDE] research is grounded in the local clone at `/Users/deepg/Desktop/agent/claw-code/` pinned at HEAD `a389f8dff1d591d2eafc2f48747313cd556412ee`. The harness lives in the **Rust** workspace under `rust/crates/`. Where claw-code diverges from upstream Claude Code documentation, the research and synthesis report **source reality** (e.g., 5 `PermissionMode` variants vs. upstream's 3 modes; 3 hook events vs. upstream's 9; project-only `CLAUDE.md` discovery; `.claw/`-branded settings root; default mode `DangerFullAccess`). These divergences are called out in-line in the module documents.

## The v4 Framework Mapped to the 8-Module Structure

### Level 1: Macro-Architecture and Ecosystem Autonomy
Mapped to:
- `docs/01_core_loop/`
- `docs/06_orchestration/`
- `docs/07_permissions_and_governance/`

Refinement from v4: macro-architecture now recognises **three distinct loop families**: (1) interactive code-edit loop [AIDER], (2) tool-use protocol loop [CLAUDE] [CODEX], and (3) IDE-embedded per-action-approval loop [CLINE] [ROO]. The IDE-embedded loop is entered via `startTask()` / `resumeTaskFromHistory()` → `initiateTaskLoop()` → `recursivelyMakeClineRequests()`, with streaming response parsing via `parseAssistantMessageV2()` and per-action approval via the `ask()` / `pWaitFor()` paradigm. [CLINE]

Refinement from v4: orchestration gains **two new delegation patterns**: Roo Code's Boomerang (`new_task { mode, message, todos? }` with persist-dispose-resume lifecycle, synthetic `tool_result` injection, and hierarchical nesting via `HistoryItem.childIds` / `parentTaskId`) and Cline's parallel `use_subagents` (up to 5 in-process subagents in a single turn). These join Claude Code's in-process `Agent` tool. [ROO] [CLINE]

Refinement from v4: the mode system (`docs/06_orchestration/workflow_modes.md`) is now a fully-populated module documenting five built-in modes, custom mode definitions via `.roomodes`, `TOOL_GROUPS` registry, `isToolAllowedForMode` validation, per-mode model routing, and `switch_mode` / `new_task` as the two mode-change primitives. [ROO]

### Level 2: Sensory Perception and Input Processing
Mapped to:
- `docs/08_user_interaction/input_processing.md`
- `docs/03_context_engine/`

No structural change in v4. Cline and Roo Code use the same `ask()` / `say()` paradigm for input processing. The Plan/Act mode toggle [CLINE] and the mode-aware system prompt [ROO] extend input processing within the existing framework.

### Level 3: Context and Retrieval Engine
Mapped to:
- `docs/03_context_engine/context_assembly.md`
- `docs/03_context_engine/repo_map_and_indexing.md`
- `docs/03_context_engine/retrieval_strategies.md`
- `docs/03_context_engine/token_economics.md`

Refinement from v4: context assembly gains **mode-aware prompt construction** [ROO]. The system prompt is assembled per-mode: `roleDefinition` as the leading line, MCP capabilities conditional on the mode's `mcp` group, `modesSection` listing all available modes for the orchestrator picker, and mode-scoped rule directories `.roo/rules-${mode}/*`. This is structurally different from [CLAUDE]'s single system-prompt assembly per turn and [CODEX]'s AGENTS.md root→leaf injection.

Refinement from v4: retrieval gains an **embedded code-index** via `codebase_search` [ROO] — a Qdrant-backed vector store with 8 embedder backends (OpenAI, Fireworks, Gemini, Ollama, etc.) providing semantic code search within the `read` tool group.

### Level 4: The Core Cognitive Engine
Mapped to:
- `docs/01_core_loop/`
- `docs/02_cognition/`

Refinement from v4: the model client gains a **multi-provider, per-mode routing pattern** [ROO]. `ProviderSettingsManager.getModeConfigId(mode)` returns a saved API config per mode, enabling patterns like GPT-5 for `code` mode, Claude Opus for `architect` mode, and a cheaper model for `ask` mode. This is distinct from [AIDER]'s per-call architect/editor split and [CLINE]'s single-model-per-task configuration.

### Level 5: Metacognition, Feedback, and Self-Regulation
Mapped to:
- `docs/02_cognition/reasoning_patterns.md`
- `docs/08_user_interaction/feedback_loops.md`
- `docs/07_permissions_and_governance/`

Refinement from v4: feedback loops gain **per-action approval as a feedback mechanism** [CLINE]. The `ask()` / `say()` paradigm creates a bidirectional feedback channel at every tool use. The `didRejectTool` cascade, `attempt_completion` as a feedback gate, and the `consecutiveMistakeCount` / `mistake_limit_reached` escalation add structured error-feedback paths. Nine lifecycle hooks (`PreToolUse`, `PostToolUse`, etc.) provide a programmable feedback surface with `contextModification` injection. [CLINE]

Refinement from v4: metacognition gains **mode-driven feedback patterns** [ROO]. Debug mode's structured "reflect → distill → validate → confirm" cycle, architect mode's "end with switch_mode to request implementation" forwarding, and Boomerang completion feedback (child summary as synthetic `tool_result`) provide three distinct prompt-encoded feedback strategies. [ROO]

Refinement from v4: the hooks system **diverges** between Cline and Roo. Cline has 9 lifecycle hooks executed as external processes with JSON I/O. Roo removes hooks entirely — `RooCodeEventName.*` events are for in-process API/bridge consumers only. Where Cline uses hooks for extensibility, Roo's answer is "use MCP servers." [CLINE] [ROO]

### Level 6: Memory Architecture and Temporal Persistence
Mapped to:
- `docs/04_memory/`
- `docs/03_context_engine/retrieval_strategies.md`

Refinement from v4: context-window management gains two patterns: Cline's `summarize_task` auto-condense (summarises conversation when context nears capacity) and standard truncation (removes a quarter of conversation from `conversationHistoryDeletedRange`). [CLINE] [ROO]

Refinement from v4: the Boomerang lifecycle introduces **cross-task memory persistence** [ROO]. Parent and child task histories are independently persisted to disk. The parent's API conversation history survives child execution across arbitrary clock time. `ghost_snapshots` (Codex) vs. `HistoryItem.childIds / parentTaskId / awaitingChildId` (Roo) represent two persistence strategies for multi-agent coordination.

### Level 7: Action Orchestration and Executable Skill Libraries
Mapped to:
- `docs/05_action_and_tools/`
- `docs/07_permissions_and_governance/permission_model.md`

Refinement from v4: the action layer gains **browser automation as a first-class tool** [CLINE]. Puppeteer-based `BrowserSession` with headless + remote CDP modes, six browser actions (`launch`, `click`, `type`, `scroll_down`, `scroll_up`, `close`), screenshot-driven visual reasoning (screenshot as image content block after every action), and `waitTillHTMLStable()` page stability mechanism. This is the only agent in the blueprint with built-in browser automation. [CLINE]

Refinement from v4: the action layer gains **browser deprecation as an architectural policy** [ROO]. `deprecatedToolGroups = ["browser"]` with `groupEntryArraySchema` silent-strip preprocessor demonstrates the "MCP eats the agent's first-party tool surface" pattern — if a capability can be an MCP server, push it to the protocol layer. [ROO]

Refinement from v4: MCP client comparison expands to three implementations: Claude Code (Rust, stdio-only), Cline (TypeScript, stdio+SSE+WebSocket), Roo (TypeScript, mode-conditional with `alwaysAllow`/`disabledTools`/deduplication). [CLINE] [ROO]

### Level 8: Governance, Guardrails, and Alignment
Mapped to:
- `docs/07_permissions_and_governance/`
- `docs/08_user_interaction/`

Refinement from v4: the permission taxonomy expands to **four paradigms**: mode-based [CLAUDE], two-dimensional matrix [CODEX], per-action approval [CLINE], and mode-as-permission [ROO]. Cline's `CommandPermissionController` adds pattern-based command allow/deny rules via `CLINE_COMMAND_PERMISSIONS` environment variable. Roo's `isToolAllowedForMode` validation with `fileRegex` restrictions adds file-level write enforcement per mode. [CLINE] [ROO]

Refinement from v4: governance gains the **"MCP servers replace hooks" divergence** — Cline has 9 lifecycle hooks as external processes; Roo explicitly removes them. This is documented as a design philosophy difference, not a missing feature. [CLINE] [ROO]

## What Changed from v3 (v4 deltas)

| Change | Why it changed in v4 | Phase 4 evidence |
| :--- | :--- | :--- |
| IDE-embedded agent loop recognised as a **third macro-pattern**. | Terminal loops (Aider) and Rust-runtime loops (Claude Code, Codex) don't capture the VS Code extension lifecycle, streaming webview UI, or per-action approval-as-default. | `src/core/task/index.ts::recursivelyMakeClineRequests`, `ask()` / `pWaitFor()` polling, `parseAssistantMessageV2()`. [CLINE] |
| **Mode system** elevated to a first-class orchestration primitive. | Cline's binary Plan/Act toggle doesn't generalise. Roo's `ModeConfig` framework provides personas × tool-RBAC × file-RBAC × model-routing in a single user-editable YAML record. | `packages/types/src/mode.ts`, `src/core/tools/validateToolUse.ts`, `CustomModesManager.ts`, `.roomodes`. [ROO] |
| **Boomerang delegation** as a durable multi-agent pattern. | Claude Code's `Agent` tool is ephemeral (in-process, 32-iteration cap). Roo's `new_task` persists the parent to disk, disposes it, runs the child with the full stack, and on `attempt_completion` injects a synthetic `tool_result` to resume the parent. | `ClineProvider.ts:3231-3560`, `NewTaskTool.ts`, `AttemptCompletionTool.ts`, `new-task-isolation.spec.ts`. [ROO] |
| **Per-action approval** as a third permission paradigm. | Claude Code's mode-based and Codex's matrix-based models don't capture the "every tool blocks until approved" pattern with granular auto-approve categories. | `ask()` / `say()` paradigm, `AutoApprove` class, `autoApprovalSettings`, `didRejectTool`. [CLINE] |
| **Browser automation populated** from stub. | No prior agent had built-in browser automation. Cline's Puppeteer integration and Roo's deliberate removal are both significant. | `BrowserSession.ts`, `BrowserDiscovery.ts`, `deprecatedToolGroups = ["browser"]`. [CLINE] [ROO] |
| **MCP client comparison** expanded to three implementations. | Claude Code's stdio-only Rust client is architecturally distinct from Cline/Roo's TypeScript multi-transport `McpHub`. Mode-conditional MCP gating is unique to Roo. | `McpHub.ts`, `mcp_settings.json`, `shouldIncludeMcp`. [CLINE] [ROO] |
| **Mode-as-permission** as a fourth permission paradigm. | Roo's tool-group RBAC + `fileRegex` is structurally different from Claude Code's mode-based, Codex's matrix-based, and Cline's per-action models. | `isToolAllowedForMode`, `FileRestrictionError`, `ALWAYS_AVAILABLE_TOOLS`. [ROO] |
| **Hooks divergence documented.** | Cline has 9 lifecycle hooks; Roo removes them. This design philosophy difference ("hooks vs. MCP servers for extensibility") is a significant architectural fork. | Cline `hooks.ts`, Roo's `RooCodeEventName` (in-process only). [CLINE] [ROO] |
| **Feedback loops enriched** with per-action and mode-driven patterns. | Aider's reflected-message and BabyAGI's task-result feedback don't capture the bidirectional approval-as-feedback loop or the mode-scoped diagnosis workflow. | `ask()` paradigm, `didRejectTool`, `attempt_completion` feedback, debug mode instructions. [CLINE] [ROO] |

## What Changed from v2 (v3 deltas)

| Change | Why it changed in v3 | Phase 3 evidence |
| :--- | :--- | :--- |
| Sandbox elevated to a **runtime-level property** with shared `SandboxPolicy` enum, three OS backends, and a single `manager.rs` dispatcher. | Phase 2's [CLAUDE] surfaced sandbox-shaping fields on `bash` but did not enforce them. Codex shows the proper pattern: containment is the runtime's job, not a tool's option. | `codex-rs/sandboxing/src/{manager,seatbelt}.rs`, `codex-rs/linux-sandbox/src/*`, `codex-rs/protocol/src/protocol.rs::SandboxPolicy`. [CODEX] |
| Permission model becomes **two-dimensional** (`AskForApproval × SandboxPolicy`). | Collapsing both questions into one variant (claw-code's `PermissionMode`) loses the distinction between "no prompts" and "no containment." Codex shows them are independent. | `core/src/safety.rs`, `core/src/exec_policy.rs`, `utils/approval-presets/src/lib.rs`. [CODEX] |
| Approval becomes a **wire-protocol round-trip** rather than an in-process callback. | Phase 1/2 approval flows are tied to a single host process. Codex's queue-mediated approval lets the same `core` crate drive TUI, headless `exec`, MCP-server-as-Codex, and IDE/app-server unchanged. | `Op::ExecApproval` / `Op::PatchApproval`, `EventMsg::ExecApprovalRequest` / `EventMsg::ApplyPatchApprovalRequest`, `ReviewDecision`. [CODEX] |
| `apply_patch` envelope as a **freeform-grammar custom tool**. | Aider has many text-protocol edit formats; claw-code has typed `edit_file`. Codex finds a middle ground: multi-file/multi-action grammar-constrained payload that is the patch text itself. | `codex-rs/apply-patch/`, `codex-rs/tools/src/{tool_apply_patch.lark,apply_patch_tool.rs}`. [CODEX] |
| Vendor-neutral project-doc convention (`AGENTS.override.md` > `AGENTS.md`, root → leaf, `--- project-doc ---` separator, byte-budget *truncation*). | Both Aider's repo-map and claw-code's `CLAUDE.md` bake the agent brand into the filename. Codex picks a vendor-neutral name and walks root → leaf so the leaf wins. | `core/src/agents_md.rs`. [CODEX] |
| Memento-style auto-compaction with `ghost_snapshots` for `Op::Undo`. | claw-code's compaction asks the model for a fresh summary. Codex's compaction reuses the structured turn-end summary that the prompt design already requires the model to emit, and preserves pre-compaction history for undo. | `core/src/compact.rs`, `COMPACT_USER_MESSAGE_MAX_TOKENS = 20_000`, `InitialContextInjection::{DoNotInject, BeforeLastUserMessage}`. [CODEX] |
| Standalone sandbox helper-binary pattern (`codex-linux-sandbox`). | Restricting the long-lived parent CLI is wrong; restricting the per-command child via a separate executable is right. The helper handles bwrap then re-execs itself for seccomp. | `codex-rs/linux-sandbox/`. [CODEX] |
| Provider-locked Responses-API client with WebSocket-primary + HTTP-SSE fallback. | Aider's LiteLLM gives provider portability; claw-code is Anthropic-locked; Codex is OpenAI-Responses-locked but gains first-class `function_call` items including freeform `apply_patch`. The trade-off is documented as a real axis of variation, not a defect. | `core/src/client.rs`. [CODEX] |
| `Granular(GranularApprovalConfig)` per-category approval gating. | Phase 2's mode + rules system has rule-level granularity but not *category-level* on/off (sandbox approval, exec rules, skill approval, request_permissions, MCP elicitations). | `protocol/src/protocol.rs::AskForApproval::Granular`. [CODEX] |

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

## v4 Phase 4 Gaps (carried into Phase 5+)

After v4, the following remain as placeholders or partial stubs:

- **Task lifecycle** (`docs/06_orchestration/task_lifecycle.md`) — Phase 5 [KILO] will populate this with checkpoint/diff patterns. claw-code's `TaskRegistry` is bookkeeping only.
- **Episodic memory** (`docs/04_memory/episodic_memory.md`) — Phase 6 [AUTOGPT] will populate this with execution-trace memory.
- **Output formatting** (`docs/08_user_interaction/output_formatting.md`) — Phase 5 [OPENCODE] and Phase 6 [PI] will populate this with TUI rendering and terminal UI architecture.
- **Safety guardrails** (`docs/07_permissions_and_governance/safety_guardrails.md`) — Phase 6 [AUTOGPT] will populate this with budget limits and safety constraints.
- **Reasoning patterns** beyond Phase 2 — Phase 6 [AUTOGPT] will add explicit self-critique loops; Claude Code's pattern is structurally emergent rather than prompt-engineered.
- **Plugin paradigm contrast** (`docs/05_action_and_tools/extensibility.md`) — Phase 6 [AUTOGPT] will add the *code-based* plugin pattern alongside the *protocol-based* MCP pattern.
- **OpenRouter multi-provider routing** (`docs/02_cognition/model_routing.md`) — Phase 5 [KILO] will add this. Roo's per-mode model routing is the Phase 4 reference.
- **File-level permissions** (`docs/07_permissions_and_governance/permission_model.md`) — Phase 5 [KILO] will add this as a fifth permission paradigm.

The hierarchy will be revised in v5 (Phase 5, [KILO] + [OPENCODE]) with file-level permissions, checkpoint/diff lifecycle, TUI architecture, and OpenRouter multi-provider routing as the central additions.
