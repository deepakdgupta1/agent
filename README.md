# 🧠 Master AI Agent Blueprint

![Master Agent Blueprint Hero](assets/hero.png)

> **Architecting the Next Generation of Agentic Systems.**

A comprehensive, modular, and technically deep documentation suite defining the functional and technical architecture of modern AI agents. This blueprint has been synthesized from source-backed analysis of **14 reference agents** — spanning terminal-native coders, IDE-embedded assistants, autonomous goal-seekers, and editor-native AI — to create a unified, high-fidelity specification for agentic behavior.

---

## ✅ Project Status: Complete

The Master Blueprint **v_FINAL** has passed all quality criteria:

| Metric | Result |
|---|---|
| Module documents | **30/30** populated (100%) |
| Required sections | **210/210** (100% completeness) |
| Mermaid diagrams | **92** (50 flowcharts + 42 sequence diagrams) |
| Agent attributions | **1,466** entries across 14 agents |
| Broken cross-references | **0** |
| Architectural hierarchy | **v_FINAL** (evolved through v0 → v1 → … → v6 → v_FINAL) |

> Full audit details in [`docs/00_meta/quality_report.md`](docs/00_meta/quality_report.md).

---

## 🎯 Project Objectives

- **Reverse Engineering**: Analyze real-world implementations to ground theoretical agentic concepts.
- **Unified Framework**: Create a modular 8-pillar architecture that covers everything from core loops to governance.
- **Architectural Synthesis**: Progressively evolve a "Master Blueprint" that captures the best-of-breed patterns across all referenced agents.
- **Technical Fidelity**: Provide flowchart-level detail, sequence diagrams, and agent attribution tables for each capability.

---

## 🏛️ The 8 Pillars of Agent Architecture

The blueprint is organized into 8 modular pillars, each defining a critical dimension of an autonomous agent:

| Module | Focus Area | Key Concepts | Docs |
| :--- | :--- | :--- | :--- |
| **01 Core Loop** | Turn Lifecycle | Agentic loops, Prompt orchestration, Handoffs | 3 |
| **02 Cognition** | Reasoning | Task decomposition, Planning, Model routing | 4 |
| **03 Context Engine** | State Management | Repo-maps, Retrieval strategies, Token economics | 4 |
| **04 Memory** | Persistence | Working vs. Persistent memory, Semantic retrieval | 4 |
| **05 Action & Tools** | Execution | Tool architecture, Sandboxed execution, Browser interaction | 5 |
| **06 Orchestration** | Multi-Agent | Workflow modes, Sub-agent spawning, Task lifecycle | 3 |
| **07 Governance** | Safety & Trust | Permission models, Sandboxing, Security guardrails | 4 |
| **08 User Interaction** | Human-in-the-Loop | Slash commands, Feedback loops, Output streaming | 3 |

---

## 📁 Reference Agent Registry

This project reverse-engineers the following agents to populate the blueprint:

| Agent | Source | Core Contribution |
| :--- | :--- | :--- |
| **Aider** | [Aider-AI/aider](https://github.com/Aider-AI/aider) | Repo-maps, Edit formats, Architect/Editor pattern |
| **Claude Code** | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Advanced Tool-use, Permission models, MCP |
| **OpenCode** | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TUI agent, Client/Server architecture, Built-in agent personas |
| **Pi Agent** | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | Modular agent runtime, Unified multi-LLM API, Tool-calling architecture |
| **Cline** | [cline/cline](https://github.com/cline/cline) | IDE-embedded loops, Browser automation |
| **Roo Code** | [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | Agentic Modes (Persona switching), Boomerang orchestration |
| **Codex** | [openai/codex](https://github.com/openai/codex) | Sandbox-first architecture, Autonomy levels |
| **AutoGPT** | [sig-grav/autogpt](https://github.com/significant-gravitas/autogpt) | Autonomous goal decomposition, Plugin systems |
| **BabyAGI** | [yoheinakajima/babyagi_archive](https://github.com/yoheinakajima/babyagi_archive) + [yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) | Classic minimal task loop baseline; current functionz/self-building delta |
| **Kilo Code** | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | Checkpoint/Diff system, Task workflows |
| **Continue** | [continuedev/continue](https://github.com/continuedev/continue) | Provider-agnostic IDE integration, CI-agent loops |
| **Hermes Agent** | [Nous/hermes-agent](https://github.com/NousResearch/hermes-agent) | Self-improving patterns, Model-specific tuning |
| **OpenClaw** | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Cross-platform abstraction patterns |
| **Zed** | [zed-industries/zed](https://github.com/zed-industries/zed) | Editor-native UI/Agent coupling |

---

## 📈 Roadmap & Progress

All 8 phases complete. Full task breakdown in [`task.md`](task.md).

- [x] **Phase 0: Scaffolding** — `docs/` tree, meta-files, 30 stub documents.
- [x] **Phase 1: Foundation** — Aider + BabyAGI research & synthesis → hierarchy v1.
- [x] **Phase 2: Claude Code** — Tool-use loop, permissions, hooks, MCP, sub-agents → hierarchy v2.
- [x] **Phase 3: OpenAI Codex** — Sandbox-first architecture, autonomy levels → hierarchy v3.
- [x] **Phase 4: Cline + Roo Code** — IDE-embedded loops, browser automation, Boomerang orchestration → hierarchy v4.
- [x] **Phase 5: Kilo Code + OpenCode** — Checkpoints, diffs, TUI agents, client/server model → hierarchy v5.
- [x] **Phase 6: AutoGPT + Pi Agent** — Autonomous goal decomposition, modular runtimes → hierarchy v6.
- [x] **Phase 7: Specialist Agents** — Continue, Hermes, OpenClaw, Zed → hierarchy v_FINAL.
- [x] **Phase 8: Quality Assurance** — Cross-reference verification, completeness audit, remediation.

---

## 📂 Repository Structure

```
.
├── docs/                          # Blueprint documentation suite (30 module docs + 3 meta files)
│   ├── 00_meta/                   # architectural_hierarchy.md, agent_registry.md, glossary.md, quality_report.md
│   ├── 01_core_loop/              # agentic_loop, prompt_orchestration, turn_lifecycle
│   ├── 02_cognition/              # task_decomposition, planning_strategies, reasoning_patterns, model_routing
│   ├── 03_context_engine/         # context_assembly, repo_map_and_indexing, token_economics, retrieval_strategies
│   ├── 04_memory/                 # working_memory, persistent_memory, episodic_memory, semantic_memory
│   ├── 05_action_and_tools/       # tool_architecture, code_modification, command_execution, browser_interaction, extensibility
│   ├── 06_orchestration/          # multi_agent_patterns, workflow_modes, task_lifecycle
│   ├── 07_permissions_and_governance/  # permission_model, sandboxing, safety_guardrails, audit_and_observability
│   ├── 08_user_interaction/       # input_processing, output_formatting, feedback_loops
│   └── _research/                 # 12 intermediate research reports (one per agent/group)
├── assets/                        # Brand assets and graphics
├── [agent-clones]/                # Reference source code for all 14 analyzed agents
├── task.md                        # Master execution checklist (21 tasks, all complete)
├── implementation_plan.md         # Detailed technical roadmap
└── references.md                  # External sources and links
```

---

## 🛠️ How to Use This Repository

**For humans:** Browse the [`docs/`](docs/) folder to explore the synthesized architectural specifications. Start with [`architectural_hierarchy.md`](docs/00_meta/architectural_hierarchy.md) for the high-level framework, then dive into any of the 8 pillars.

**For AI agents:** Refer to [`task.md`](task.md) for the task structure. All 21 tasks are complete — the blueprint is ready for consumption or extension.

---

> [!NOTE]
> The Master Blueprint v_FINAL is complete. The architectural hierarchy evolved through 8 versions (v0 → v_FINAL) as each agent was analyzed. Full version history is in [`docs/00_meta/architectural_hierarchy.md`](docs/00_meta/architectural_hierarchy.md).
