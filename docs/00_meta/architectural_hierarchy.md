# Architectural Hierarchy v5

This document tracks the evolution of the Master AI Agent Blueprint framework.
Version: v5

## Version history

| Version | Phase | Agents folded in | Source reports |
| --- | --- | --- | --- |
| v0 | 0 | (seed) | `AI Agent Feature Hierarchy Development.md` |
| v1 | 1 | [AIDER], [BABYAGI] | `aider_research.md`, `babyagi_research.md` |
| v2 | 2 | + [CLAUDE] (claw-code) | `claude_code_research_part1.md`, `claude_code_research_part2.md` |
| v3 | 3 | + [CODEX] | `codex_research.md` |
| v4 | 4 | + [CLINE], [ROO] | `cline_research.md`, `roo_code_research.md` |
| **v5** | 5 | + [KILO], [OPENCODE] | `kilo_code_research.md`, `opencode_research.md` |

## Scope of v5

Version v5 incorporates Phase 5 findings from `docs/_research/kilo_code_research.md` and `docs/_research/opencode_research.md`. Five structural additions dominate v5:

1. **Task lifecycle populated from stub.** `docs/06_orchestration/task_lifecycle.md` is no longer a stub — it documents Kilo Code's plan→code handoff pipeline (structured `PlanFollowup` with LLM-generated handover summaries, cross-session todo persistence, and code model resolution), OpenCode's git-based snapshot system (separate snapshot repo at `~/.local/share/kilo/snapshot/` with `track` → `patch` → `restore` → `revert` operations), and Kilo's AI code review system (`/local-review` with structured severity/confidence thresholds and post-review mode routing). [KILO] [OPENCODE]

2. **Config-file protection as a fifth permission paradigm.** The permission taxonomy now has five paradigms: mode-based [CLAUDE], two-dimensional matrix [CODEX], per-action approval [CLINE], mode-as-permission [ROO], and config-file protection [KILO]. Kilo's `ConfigProtection` layer intercepts `edit` and `external_directory` permissions targeting agent config files, with the "Always Allow" UI disabled for config paths. The `drainCovered` mechanism auto-resolves permissions across concurrent sub-agents. Per-agent bash rulesets (`bash` full-access vs `readOnlyBash` deny-default) provide granular command filtering. [KILO]

3. **Proxy-first multi-provider routing.** Model routing gains the Kilo Gateway (`@kilocode/kilo-gateway`) — a proxy provider wrapping OpenRouter, Anthropic, OpenAI, Alibaba, and OpenAI-compatible backends behind a single `createKilo()` factory. Provider-specific patches (Anthropic beta headers, Cerebras 3rd-party headers, Azure endpoint overrides) are applied transparently. A custom `buildTimeoutSignal()` prevents aborting healthy streaming responses. OpenCode's `customLoaders` system provides the extensible provider foundation. [KILO] [OPENCODE]

4. **Named-agent system alongside mode framework.** Kilo defines six native agents (`code`, `plan`, `debug`, `ask`, `orchestrator`, `explore`) with per-agent permission rulesets composed via `Permission.fromConfig()` + `Permission.merge()`. This parallels but is structurally distinct from Roo's `ModeConfig` YAML system — Kilo uses TypeScript-defined permission merging with explicit composition order (defaults → agent-specific → user config → deny overrides), while Roo uses tool-group RBAC with file-regex restrictions. [KILO]

5. **Git worktree multi-session orchestration.** The Agent Manager (VS Code extension) uses git worktrees for OS-level filesystem isolation of parallel agent sessions. Each worktree has its own branch, working directory, and `kilo serve` backend. Multi-version exploration spawns N worktrees with the same prompt but different models. Selective apply/revert operates at the file level across worktrees. This is the only agent in the blueprint with OS-level session isolation. [KILO]

Additional v5 refinements:

- **Semantic search tool.** Kilo adds `semantic_search` (LanceDB vector search), `codebase_search` (multi-step intelligent code search via warpgrep), and `recall` (context memory) to the tool catalog. [KILO]
- **Plan→code handover generation.** The `compaction` agent generates structured handover summaries (Discoveries, Relevant Files, Implementation Notes) with a 60-second timeout, enabling curated knowledge transfer between planning and implementation sessions. [KILO]
- **`build → code` agent renaming.** OpenCode's `build` agent is renamed to `code` in Kilo with backward compatibility maintained via `resolveKey()` and `preprocessConfig()`. [KILO]

> **Source-of-truth note (v5)**: the [KILO] research is grounded in the local checkout of `kilocode` (the `kilocode/` directory in the workspace). Kilo Code is a fork of OpenCode — the `packages/opencode/` directory is shared upstream code, and Kilo-specific additions live in `packages/opencode/src/kilocode/` directories marked with `kilocode_change` comment markers. The [OPENCODE] research is grounded in the same repository's upstream `packages/opencode/` code. The `packages/kilo-vscode/` directory contains the VS Code extension including the Agent Manager.

## Scope of v4

Version v4 incorporates Phase 4 findings from `docs/_research/cline_research.md` and `docs/_research/roo_code_research.md`. Four structural additions dominate v4:

1. **IDE-embedded agent loop as a third macro-pattern.** The blueprint now recognises three distinct loop families: *interactive code-edit loop* (Aider, terminal-based), *tool-use protocol loop* (Claude Code, Rust runtime / Codex, Rust CLI), and *IDE-embedded per-action-approval loop* (Cline/Roo Code, VS Code extension). The IDE-embedded loop introduces per-action approval as the default, streaming partial tool presentation in the webview, mode-multiplexed prompt/tool-surface swapping (Roo), and VS Code extension lifecycle management. [CLINE] [ROO]

2. **Mode system as a first-class orchestration primitive.** Roo Code elevates persona-switching from a binary Plan/Act toggle (Cline) to a full `ModeConfig` framework — `(roleDefinition, groups, customInstructions, fileRegex restrictions)` — with five built-in modes (architect, code, debug, ask, orchestrator) and unlimited user-defined custom modes via `.roomodes` YAML files. Mode simultaneously controls system prompt persona, tool-group RBAC, file-write restrictions, and per-mode model routing. No other agent in the blueprint unifies all four axes into a single user-editable record. [ROO]

3. **Boomerang multi-agent delegation.** Roo Code's `new_task { mode, message, todos? }` implements a durable, persistent, mode-typed parent↔child delegation pattern where: the parent is flushed to disk and disposed; the child runs as a normal Task with the full UI/API stack; on `attempt_completion`, the child's summary is injected as a **synthetic `tool_result`** into the parent's API conversation history; the parent resumes as if `new_task` returned synchronously. [ROO]

4. **Per-action approval as a third permission paradigm.** The permission taxonomy now has four paradigms: mode-based (`PermissionMode` enum [CLAUDE]), two-dimensional matrix (`AskForApproval × SandboxPolicy` [CODEX]), per-action approval (`ask()` blocking with granular auto-approval categories [CLINE]), and mode-as-permission (tool-group RBAC with `fileRegex` restrictions [ROO]). [CLINE] [ROO]

> **Source-of-truth note (v4)**: the [CLINE] research is grounded in a local checkout of `cline/cline` (the `cline/` directory in the workspace). The [ROO] research is grounded in a local checkout of `RooVetGit/Roo-Code` (the `Roo-Code/` directory).

## Scope of v3

Version v3 incorporates Phase 3 findings from `docs/_research/codex_research.md`. Two structural additions dominate v3:

1. **Sandbox-first execution as a runtime property.** The blueprint now treats *containment* as a property of the runtime independent of *approval*. [CODEX]
2. **Two-dimensional autonomy: `AskForApproval × SandboxPolicy`.** The permission system gains a second axis. [CODEX]

> **Source-of-truth note (v3)**: the [CODEX] research is grounded in a local checkout of `openai/codex` at commit `87bc72408c5ef08f8d21f2cdd00c55451c3be33f`.

## Scope of v2

Version v2 incorporates Phase 2 findings from `docs/_research/claude_code_research_part1.md` and `docs/_research/claude_code_research_part2.md`.

> **Source-of-truth note**: the [CLAUDE] research is grounded in the local clone at `/Users/deepg/Desktop/agent/claw-code/` pinned at HEAD `a389f8d`.

## The v5 Framework Mapped to the 8-Module Structure

### Level 1: Macro-Architecture and Ecosystem Autonomy
Mapped to:
- `docs/01_core_loop/`
- `docs/06_orchestration/`
- `docs/07_permissions_and_governance/`

Refinement from v5: macro-architecture now recognises **four distinct loop families**: (1) interactive code-edit loop [AIDER], (2) tool-use protocol loop [CLAUDE] [CODEX], (3) IDE-embedded per-action-approval loop [CLINE] [ROO], and (4) TUI/CLI-driven session loop [OPENCODE] [KILO] where the agentic loop runs within a session lifecycle managed by `SessionPrompt.loop()`. [OPENCODE] [KILO]

Refinement from v5: orchestration gains **git worktree multi-session orchestration** [KILO]. The Agent Manager enables OS-level filesystem isolation for parallel sessions, multi-version exploration, and selective file-level apply/revert across worktrees.

Refinement from v5: the task lifecycle module (`docs/06_orchestration/task_lifecycle.md`) is now fully populated with plan→code handoff, snapshot checkpointing, and AI code review. [KILO] [OPENCODE]

### Level 2: Sensory Perception and Input Processing
Mapped to:
- `docs/08_user_interaction/input_processing.md`
- `docs/03_context_engine/`

No structural change in v5. Kilo and OpenCode use the same slash-command system as Aider/Claude Code. The `/local-review` and `/local-review-uncommitted` commands [KILO] extend the command surface.

### Level 3: Context and Retrieval Engine
Mapped to:
- `docs/03_context_engine/context_assembly.md`
- `docs/03_context_engine/repo_map_and_indexing.md`
- `docs/03_context_engine/retrieval_strategies.md`
- `docs/03_context_engine/token_economics.md`

Refinement from v5: retrieval gains **semantic vector search** [KILO] via LanceDB indexing with natural-language queries. This joins Roo's Qdrant-backed `codebase_search` as a second embedded code-index pattern.

### Level 4: The Core Cognitive Engine
Mapped to:
- `docs/01_core_loop/`
- `docs/02_cognition/`

Refinement from v5: model routing gains the **Kilo Gateway proxy provider** pattern [KILO] — a unified API wrapping 5 AI SDK providers with custom auth, org scoping, provider-specific patches, and custom timeout handling. OpenCode's **custom loader system** [OPENCODE] provides the extensible foundation.

### Level 5: Metacognition, Feedback, and Self-Regulation
Mapped to:
- `docs/02_cognition/reasoning_patterns.md`
- `docs/08_user_interaction/feedback_loops.md`
- `docs/07_permissions_and_governance/`

Refinement from v5: feedback loops gain **AI code review as a structured feedback mechanism** [KILO]. The `/local-review` system produces severity-rated findings with confidence thresholds and offers mode-specific fix routing (code/debug/orchestrator), creating a structured quality gate within the development loop.

Refinement from v5: the plan→code handover with LLM-generated summaries [KILO] adds a **metacognitive handover** pattern — the system reflects on the planning conversation to distill high-entropy knowledge before transitioning to implementation.

### Level 6: Memory Architecture and Temporal Persistence
Mapped to:
- `docs/04_memory/`
- `docs/03_context_engine/retrieval_strategies.md`

Refinement from v5: persistence gains the **snapshot git repository** pattern [OPENCODE] [KILO]. A separate git repo at `~/.local/share/kilo/snapshot/` provides per-turn filesystem checkpointing with deterministic revert, independent of the user's project git history.

Refinement from v5: cross-session memory gains **todo persistence** [KILO]. Todos created during planning persist across sessions and are injected into implementation sessions as markdown checklists.

### Level 7: Action Orchestration and Executable Skill Libraries
Mapped to:
- `docs/05_action_and_tools/`
- `docs/07_permissions_and_governance/permission_model.md`

Refinement from v5: the tool catalog gains **semantic search** (`semantic_search` via LanceDB), **intelligent code search** (`codebase_search` via warpgrep), and **recall** tools [KILO]. The `question` tool gains structured options with mode-switching capability.

Refinement from v5: the `suggest` tool [KILO] is conditionally registered (CLI and VS Code clients only), demonstrating client-aware tool surface adaptation.

### Level 8: Governance, Guardrails, and Alignment
Mapped to:
- `docs/07_permissions_and_governance/`
- `docs/08_user_interaction/`

Refinement from v5: the permission taxonomy expands to **five paradigms**: mode-based [CLAUDE], two-dimensional matrix [CODEX], per-action approval [CLINE], mode-as-permission [ROO], and **config-file protection** [KILO]. Kilo's `ConfigProtection` layer adds path-based interception of config edits, `DISABLE_ALWAYS_KEY` for per-edit-only approval, and `drainCovered` for cross-sub-agent permission resolution. Per-agent bash rulesets (`bash` vs `readOnlyBash`) add command-level filtering. [KILO]

## What Changed from v4 (v5 deltas)

| Change | Why it changed in v5 | Phase 5 evidence |
| :--- | :--- | :--- |
| **Task lifecycle populated** from stub with plan→code handoff, snapshot checkpointing, and AI review. | v4 flagged this as a Phase 5 gap. Kilo introduces the most structured task lifecycle in the blueprint. | `plan-followup.ts`, `snapshot/index.ts`, `review/review.ts`, `worktree-diff.ts`. [KILO] [OPENCODE] |
| **Config-file protection** as a fifth permission paradigm. | No prior agent protected its own config files from agentic modification. Kilo's `ConfigProtection` is the most granular config-file guard. | `config-paths.ts`, `drain.ts`, `routes.ts`, `DISABLE_ALWAYS_KEY`. [KILO] |
| **Proxy-first multi-provider routing** via Kilo Gateway. | v4's model routing was limited to direct provider connections and per-mode selection. Kilo adds a unified proxy with auth, org scoping, and provider-specific patches. | `kilo-gateway/src/provider.ts`, `patchCustomLoaderResult`, `buildTimeoutSignal`. [KILO] |
| **Named-agent system** paralleling Roo's mode framework. | Kilo and Roo independently developed persona-switching systems with different architectures (TypeScript permission merging vs YAML mode records). | `kilocode/agent/index.ts`, `patchAgents()`, `Permission.merge()`. [KILO] |
| **Git worktree multi-session orchestration** as a unique pattern. | No prior agent uses OS-level filesystem isolation for parallel sessions. | `kilo-vscode/src/agent-manager/`, `WorktreeManager.ts`, `GitOps.ts`. [KILO] |
| **Semantic vector search** as an additional retrieval strategy. | v4 had Roo's Qdrant-backed `codebase_search`; Kilo adds LanceDB-based `semantic_search` as a second embedded index. | `kilocode/tool/semantic-search.ts`, `kilocode/indexing`. [KILO] |
| **Model routing updated** from Phase 1 to Phase 5. | `model_routing.md` had only [AIDER] and [BABYAGI] content. Now includes Kilo Gateway, OpenCode custom loaders, and Roo per-mode routing. | `kilo-gateway/src/provider.ts`, `kilocode/provider/provider.ts`. [KILO] [OPENCODE] |
| **Workflow modes expanded** with Kilo's named-agent comparison table. | Documents the structural difference between Kilo's `patchAgents()` and Roo's `ModeConfig` — two parallel solutions to the same problem. | `kilocode/agent/index.ts` vs `packages/types/src/mode.ts`. [KILO] vs [ROO] |

## What Changed from v3 (v4 deltas)

| Change | Why it changed in v4 | Phase 4 evidence |
| :--- | :--- | :--- |
| IDE-embedded agent loop recognised as a **third macro-pattern**. | Terminal loops (Aider) and Rust-runtime loops (Claude Code, Codex) don't capture the VS Code extension lifecycle. | `src/core/task/index.ts::recursivelyMakeClineRequests`. [CLINE] |
| **Mode system** elevated to a first-class orchestration primitive. | Cline's binary Plan/Act toggle doesn't generalise. Roo's `ModeConfig` framework provides personas × tool-RBAC × file-RBAC × model-routing. | `packages/types/src/mode.ts`, `CustomModesManager.ts`. [ROO] |
| **Boomerang delegation** as a durable multi-agent pattern. | Claude Code's `Agent` tool is ephemeral. Roo's `new_task` persists parent to disk. | `ClineProvider.ts`, `NewTaskTool.ts`. [ROO] |
| **Per-action approval** as a third permission paradigm. | Claude Code's mode-based and Codex's matrix-based don't capture per-tool blocking. | `ask()` / `say()` paradigm, `AutoApprove` class. [CLINE] |

## What Changed from v2 (v3 deltas)

| Change | Why it changed in v3 | Phase 3 evidence |
| :--- | :--- | :--- |
| Sandbox elevated to a **runtime-level property**. | Phase 2 didn't enforce sandbox. Codex shows the proper pattern. | `codex-rs/sandboxing/`. [CODEX] |
| Permission model becomes **two-dimensional**. | Collapsing both questions into one variant loses the distinction. | `core/src/safety.rs`, `core/src/exec_policy.rs`. [CODEX] |

## What Changed from v1 and Why

| Change | Why it changed in v2 | Phase 2 evidence |
| :--- | :--- | :--- |
| Promoted **multi-tool-call turn** as a first-class pattern. | Structurally different from Aider's retry and BabyAGI's queue. | `ConversationRuntime::run_turn`. [CLAUDE] |
| Added **typed-spec tool registry** to Level 7. | Phase 1 didn't define a tool architecture. | `tools::mvp_tool_specs()`. [CLAUDE] |
| Added **mode-based permission system** to Level 8. | Phase 1 didn't define a policy layer. | `permissions.rs`. [CLAUDE] |
| Added **hooks system** to Level 5. | Hooks introduce programmable feedback. | `hooks.rs`. [CLAUDE] |
| Added **filesystem-backed persistent memory** to Level 6. | Instruction-file-based persistence. | `prompt.rs`. [CLAUDE] |
| Added **sub-agent spawning** to Level 1. | Phase 1 had no sub-agent primitive. | `tools/src/lib.rs`. [CLAUDE] |
| Added **MCP extensibility** to Level 7. | Phase 1 had no plugin surface. | `mcp_stdio.rs`. [CLAUDE] |

## v5 Phase 5 Gaps (carried into Phase 6+)

After v5, the following remain as placeholders or partial stubs:

- **Episodic memory** (`docs/04_memory/episodic_memory.md`) — Phase 6 [AUTOGPT] will populate this with execution-trace memory.
- **Output formatting** (`docs/08_user_interaction/output_formatting.md`) — Phase 6 [PI] will populate this with TUI rendering and terminal UI architecture.
- **Safety guardrails** (`docs/07_permissions_and_governance/safety_guardrails.md`) — Phase 6 [AUTOGPT] will populate this with budget limits and safety constraints.
- **Reasoning patterns** beyond Phase 2 — Phase 6 [AUTOGPT] will add explicit self-critique loops.
- **Plugin paradigm contrast** (`docs/05_action_and_tools/extensibility.md`) — Phase 6 [AUTOGPT] will add the *code-based* plugin pattern alongside the *protocol-based* MCP pattern.

The hierarchy will be revised in v6 (Phase 6, [AUTOGPT] + [PI]) with budget-based safety, episodic memory, self-critique loops, and code-based plugins as the central additions.
