# Skills Discovery Mechanism

This document defines the standard for skill discovery, skill routing, context optimization, and skill authoring across all local AI coding agents. It serves as the single source of truth for how skills are structured, discovered, installed, and enforced.

---

## 1. Architecture Overview

### Shared Skills Directory

All agents share a single canonical skills directory:

```
~/.agents/skills/           <-- single source of truth
  |- <skill-name>/SKILL.md  <-- one directory per skill
  |- _backup/               <-- retired/superseded skills
  |- _catalogs/             <-- skill catalogs
  |- .system/               <-- system-managed skills (skill-installer, etc.)
```

Agent-specific directories symlink to this shared location:

| Agent | Symlink Path | Target |
|-------|-------------|--------|
| Claude Code | `~/.claude/skills/` | `~/.agents/skills/` |
| Codex | `~/.codex/skills` | `~/.agents/skills/` |
| Antigravity | via `~/.agents/skills/` | (direct access) |
| AMP Code | `~/.amp/skills` | `~/.agents/skills/` |
| Gemini | `~/.gemini/skills` | `~/.agents/skills/` |
| Kilocode | `~/.kilocode/skills` | `~/.agents/skills/` |

The `~/.agents/_portable/relink_agent_symlinks.sh` script recreates all symlinks if they break.

### Discovery Flow

```
Task arrives
    |
    v
[1] Scan system reminder / skill list (description matching)
    |
    v
[2] Check routing rules (phase -> skill chain, mandatory, proactive)
    |
    v
[3] No match? -> invoke find-skills fallback
    |
    v
[4] Load SKILL.md -> execute skill
```

---

## 2. Skill Description Standard (Layer 1)

The skill description is the **primary discovery surface**. It appears in the system reminder / skill list that agents scan when deciding which skill to invoke. A well-written description is the highest-ROI investment for discoverability.

### The GOOD Pattern

Every skill description MUST follow this pattern:

```
[Purpose]. Use when [scenarios]. Triggers on [keywords].
```

Variations for special skill types:

```
# Proactive skill (auto-invoked without user asking)
[Purpose]. Use PROACTIVELY when [scenarios]. Triggers on [keywords].

# Mandatory skill (must always be invoked in scope)
[Purpose]. MUST BE USED for [scope]. Use when [scenarios]. Triggers on [keywords].

# Proactive + Mandatory
[Purpose]. MUST BE USED for [scope]. Use PROACTIVELY when [scenarios]. Triggers on [keywords].
```

### Examples

**Standard skill:**
```
Build data visualization and analytics dashboards. Use when creating charts,
KPI displays, metrics dashboards, or data visualization components. Triggers
on analytics, dashboard, charts, metrics, KPI, data visualization, Recharts.
```

**Proactive + Mandatory skill:**
```
Review code for security vulnerabilities, quality issues, and maintainability.
MUST BE USED for all code changes. Use PROACTIVELY immediately after writing
or modifying code. Triggers on code review, review code, check code, security
review, quality check, after writing code, after modifying code.
```

### Description Quality Criteria

| Criterion | Required | Example |
|-----------|----------|---------|
| Action-oriented purpose | Yes | "Build...", "Deploy...", "Review...", "Enforce..." |
| "Use when" clause | Yes | "Use when creating charts..." |
| "Triggers on" keyword list | Yes | "Triggers on analytics, dashboard, metrics..." |
| "PROACTIVELY" marker | If proactive | "Use PROACTIVELY when..." |
| "MUST BE USED" marker | If mandatory | "MUST BE USED for all code changes" |
| Concise (1-3 sentences) | Yes | Keep under ~300 characters |
| No emojis | Yes | Plain text only |

### What Makes a BAD Description

- Generic/vague: "A comprehensive verification system for Claude Code sessions"
- Missing triggers: "REST API design patterns including resource naming"
- Missing scenarios: Just a noun phrase with no "Use when"
- Too long: Multi-paragraph descriptions waste context tokens

---

## 3. SKILL.md File Format

Each skill lives in its own directory with a `SKILL.md` file:

```
~/.agents/skills/<skill-name>/SKILL.md
```

### Frontmatter (YAML)

```yaml
---
name: <skill-name>              # Required. Matches directory name.
description: <GOOD pattern>     # Required. Follows the standard above.
tools: ["Read", "Grep", ...]    # Optional. Tools the skill needs (Claude Code).
model: sonnet                   # Optional. Preferred model (Claude Code).
origin: ECC                     # Optional. Source attribution.
---
```

### Body (Markdown)

The body contains the full skill instructions. Structure:

1. **Role statement** -- one-line persona ("You are a senior code reviewer...")
2. **When to Activate** -- detailed trigger conditions (supplements the description)
3. **Process / Workflow** -- step-by-step instructions
4. **Checklists / Reference** -- quick-reference material
5. **Output format** -- how to present results

---

## 4. Routing Rules (Layer 3)

Routing rules map development phases to relevant skills and enforce mandatory invocations.

### Location per Agent

| Agent | File |
|-------|------|
| Claude Code | `~/.claude/rules/common/skill-routing.md` |
| Codex | `~/.agents/AGENTS.md` (Skill Routing section) |
| Antigravity | `~/.antigravity/rules.md` (Skill Routing section) |
| AMP Code | `~/.amp/skill-routing.md` |

### Routing Rules Content

#### Mandatory Skills
- **code-reviewer**: MUST invoke after ALL code changes
- **python-reviewer**: MUST invoke after ALL Python file changes

#### Phase -> Skill Chain

| Phase | Skills |
|-------|--------|
| Plan | planner, architect, prd |
| Design | api-design, ux-design-systems, mermaid-diagrams |
| Implement | tdd-guide, coding-standards, backend-patterns, frontend-patterns |
| Test | e2e-testing, python-testing |
| Review | code-reviewer, python-reviewer, security-review, database-reviewer |
| Deploy | vercel, railway, cloudflare, deployment-patterns, docker-patterns |
| Docs | doc-updater |

#### Proactive Skills (11 total)

These skills should be scanned for applicability before starting any work:

1. build-error-resolver
2. planner
3. code-reviewer
4. doc-updater
5. refactor-cleaner
6. architect
7. security-review
8. database-reviewer
9. e2e-testing
10. python-reviewer
11. honest-agent

#### Fallback Protocol

If no skill matches the current task, invoke **find-skills** to search the skills ecosystem before proceeding with unassisted work.

---

## 5. Enforcement Hooks (Layer 2)

### Claude Code (native hook support)

Claude Code supports shell-based PostToolUse hooks that fire after tool execution.

**Hook script:** `~/.claude/hooks/skill-enforcement.sh`

```bash
#!/usr/bin/env bash
# Receives tool input JSON on stdin. Outputs reminders to stderr.
# Skips .md files and .claude/ paths. Always exits 0 (advisory).
```

**Configuration in `~/.claude/settings.json`:**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "/home/deeog/.claude/hooks/skill-enforcement.sh",
            "timeout": 3000
          }
        ]
      }
    ]
  }
}
```

**Behavior:**
- After any Edit or Write on a code file: reminds to invoke `/code-reviewer`
- After Edit/Write on a `.py` file: additionally reminds to invoke `/python-reviewer`
- Silent for `.md` files and paths inside `.claude/`
- Advisory only (exit 0), never blocks

### Codex, Antigravity, AMP Code (instruction-based)

These agents lack native PostToolUse hooks. Enforcement is achieved through strong instructions in their rules files:

- **Codex**: `~/.agents/AGENTS.md` -- "MUST invoke after ALL code changes"
- **Antigravity**: `~/.antigravity/rules.md` -- same mandatory language
- **AMP Code**: `~/.amp/skill-routing.md` -- same mandatory language

---

## 6. Context Optimization (Layer 4)

### Consolidation Principles

- **Merge overlapping skills** rather than maintaining near-duplicates
- **Retire obsolete versions** (move to `_backup/`, keep originals recoverable)
- **Target: <65 active skills** to keep the system reminder scannable

### Consolidations Performed

| Kept | Absorbed | Rationale |
|------|----------|-----------|
| tdd-guide | tdd-workflow | Near-identical purpose |
| continuous-learning-v2 | continuous-learning (v1) | v1 obsolete |
| database-reviewer | postgres-patterns | Overlapping domain |
| web-standards (new) | web-accessibility + web-design-guidelines | Overlapping compliance |
| e2e-testing | e2e-runner | Execution + patterns unified |

### Token Budget

| Component | Tokens | Notes |
|-----------|--------|-------|
| Skill descriptions (system reminder) | ~4.6k | Same budget, better content |
| Routing rules file | ~150 | Compact bullet format |
| Enforcement hook | 0 | Shell script, not in context |
| Total overhead | ~4.75k | Down from ~5k+ pre-optimization |

### Retired Skills Location

All retired skills are preserved in `~/.agents/skills/_backup/` for reference.

---

## 7. Guide: Rewriting an Externally-Sourced Skill

When installing a skill from an external source (GitHub, skill catalog, community), rewrite it to conform to the standard before adding it to the shared skills directory.

### Step-by-Step Process

#### Step 1: Read the source skill
Read the full SKILL.md to understand purpose, triggers, scenarios, and body content.

#### Step 2: Rewrite the description field
Apply the GOOD pattern. Extract information from:
- The body's "When to Activate" or "Use when" sections
- Any keyword lists in the body
- The skill's actual purpose (what it does, not what it is)

**Template:**
```yaml
description: >-
  [Action verb] [what it does]. Use when [2-4 specific scenarios].
  Triggers on [5-15 comma-separated keywords].
```

**Checklist:**
- [ ] Starts with an action verb (Build, Deploy, Review, Enforce, Generate...)
- [ ] Has "Use when" with 2-4 concrete scenarios
- [ ] Has "Triggers on" with 5-15 relevant keywords
- [ ] If proactive: includes "Use PROACTIVELY"
- [ ] If mandatory: includes "MUST BE USED for [scope]"
- [ ] Under 300 characters total
- [ ] No emojis

#### Step 3: Normalize the frontmatter
Ensure the frontmatter has at minimum:
```yaml
---
name: <skill-name>           # lowercase, kebab-case, matches directory name
description: <rewritten>     # from Step 2
---
```

Optional fields to preserve if present: `tools`, `model`, `origin`.

#### Step 4: Check for overlap
Before installing, check if an existing skill covers the same domain:
- Read descriptions of similar skills
- If >70% overlap: merge content into the existing skill instead of adding a new one
- If partial overlap: ensure trigger keywords don't collide

#### Step 5: Validate the body
- Remove any agent-specific instructions that don't apply (e.g., Cursor-specific, Copilot-specific)
- Ensure the body has: role statement, trigger conditions, process/workflow
- Keep the body under 800 lines
- Do not add emojis

### Example Rewrite

**Before (external source):**
```yaml
---
name: my-api-skill
description: Helps with API stuff
---
```

**After (conforming to standard):**
```yaml
---
name: my-api-skill
description: >-
  Design and implement GraphQL APIs with schema-first methodology.
  Use when creating GraphQL schemas, writing resolvers, implementing
  subscriptions, or optimizing query performance. Triggers on GraphQL,
  schema, resolver, mutation, subscription, Apollo, query optimization,
  N+1, dataloader.
---
```

---

## 8. Guide: Installing a Skill for All Local Agents

### Step-by-Step Process

#### Step 1: Create the skill directory
```bash
mkdir -p ~/.agents/skills/<skill-name>
```

#### Step 2: Write the SKILL.md
Place the rewritten SKILL.md (from Section 7) into the directory:
```
~/.agents/skills/<skill-name>/SKILL.md
```

#### Step 3: Verify symlinks
All agents should already have symlinks to `~/.agents/skills/`. Verify:
```bash
readlink ~/.claude/skills    # should show ~/.agents/skills or equivalent
readlink ~/.codex/skills     # should show ../.agents/skills or equivalent
readlink ~/.amp/skills       # should show ~/.agents/skills or equivalent
```

If any symlink is missing, run the relink script:
```bash
~/.agents/_portable/relink_agent_symlinks.sh
```

Or create the missing symlink manually:
```bash
ln -snf ~/.agents/skills ~/.{agent}/skills
```

#### Step 4: Verify discovery

**Claude Code:** The skill should appear in the system reminder skill list after restarting or starting a new conversation. Verify by checking if the skill name appears in the available skills.

**Codex:** Skills are loaded from `~/.codex/skills/` (symlink). Verify by asking Codex to list available skills or invoking the skill by name.

**Antigravity:** Skills are accessible via `~/.agents/skills/`. Reference them from the agent's context.

**AMP Code:** Skills are accessible via `~/.amp/skills` (symlink). Reference them from the agent's context.

#### Step 5: Update routing rules (if applicable)

If the new skill is:
- **Proactive**: Add it to the proactive skills list in ALL routing rule files
- **Mandatory**: Add it to the mandatory skills section in ALL routing rule files
- **Phase-specific**: Add it to the appropriate phase in ALL routing rule files

Files to update:
1. `~/.claude/rules/common/skill-routing.md`
2. `~/.agents/AGENTS.md` (Skill Routing section)
3. `~/.antigravity/rules.md` (Skill Routing section)
4. `~/.amp/skill-routing.md`

#### Step 6: Add enforcement hook (Claude Code only)

If the skill is mandatory, update `~/.claude/hooks/skill-enforcement.sh` to include a reminder for the new skill. For example, to add a mandatory Go reviewer:

```bash
if [[ "$file_path" == *.go ]]; then
  echo "REMINDER: Invoke /code-reviewer and /go-reviewer for this Go change" >&2
fi
```

### Quick Reference: Install Checklist

- [ ] Skill directory created at `~/.agents/skills/<name>/`
- [ ] SKILL.md follows the GOOD description pattern
- [ ] No overlap with existing skills (or merged if overlapping)
- [ ] Symlinks verified for all agents
- [ ] Routing rules updated if proactive/mandatory/phase-specific
- [ ] Enforcement hook updated if mandatory (Claude Code)
- [ ] Body content is agent-agnostic (works across all platforms)

---

## 9. Agent-Specific Configuration Reference

### Claude Code

| Component | Location |
|-----------|----------|
| Global instructions | `~/.claude/CLAUDE.md` |
| Skills | `~/.claude/skills/` -> `~/.agents/skills/` |
| Routing rules | `~/.claude/rules/common/skill-routing.md` |
| Enforcement hook | `~/.claude/hooks/skill-enforcement.sh` |
| Hook config | `~/.claude/settings.json` (PostToolUse) |

**Discovery mechanism:** Skills appear in the system reminder as a list with truncated descriptions. Claude matches task keywords against these descriptions to decide invocation. The PostToolUse hook provides an additional enforcement layer for mandatory skills.

### Codex (OpenAI)

| Component | Location |
|-----------|----------|
| Global instructions | `~/.agents/AGENTS.md` |
| Skills | `~/.codex/skills` -> `~/.agents/skills/` |
| Routing rules | `~/.agents/AGENTS.md` (Skill Routing section) |
| Config | `~/.codex/config.toml` |

**Discovery mechanism:** Codex loads `AGENTS.md` as model instructions (configured via `model_instructions_file` in config.toml). Skills are discovered by scanning the skills directory. The routing section in AGENTS.md guides invocation.

### Antigravity

| Component | Location |
|-----------|----------|
| Rules | `~/.antigravity/rules.md` |
| Skills | Via `~/.agents/skills/` (direct access) |
| Routing rules | `~/.antigravity/rules.md` (Skill Routing section) |

**Discovery mechanism:** Antigravity loads rules.md as system instructions. Skills are accessed from the shared directory. The routing section in rules.md guides invocation.

### AMP Code (Sourcegraph)

| Component | Location |
|-----------|----------|
| Integrity standards | `~/.amp/analysis-integrity-standards.md` |
| Skills | `~/.amp/skills` -> `~/.agents/skills/` |
| Routing rules | `~/.amp/skill-routing.md` |

**Discovery mechanism:** AMP reads its rules files from the config directory. The skill-routing.md file provides routing guidance. Skills are accessed via the symlink.

---

## 10. Maintenance

### Adding a New Skill
Follow Section 8 (installation guide).

### Retiring a Skill
1. Move the skill directory to `~/.agents/skills/_backup/`
2. Remove from routing rules if listed
3. Remove from enforcement hooks if referenced

### Merging Overlapping Skills
1. Identify the dominant skill (more complete, better maintained)
2. Read both SKILL.md files fully
3. Merge unique content from the secondary into the primary
4. Update the primary's description to cover both domains
5. Move the secondary to `_backup/`
6. Update routing rules to use the merged skill name

### Periodic Audit
Use the `skill-stocktake` skill to audit for:
- Skills with poor descriptions
- Overlapping skills that should be merged
- Stale or unused skills
- Skills missing from routing rules

### Relinking After System Changes
If symlinks break (e.g., after OS reinstall or home directory changes):
```bash
~/.agents/_portable/relink_agent_symlinks.sh
```
