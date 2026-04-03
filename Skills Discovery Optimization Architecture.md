**Findings**

- High: The document treats effectiveness and uplift estimates as facts without an evaluation method. [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):8 and [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):99 need a benchmark corpus, scoring rubric, and metrics like top-1/top-3 recall, false-positive rate, trigger timing, and mandatory-skill compliance.

- High: The quality baseline is internally inconsistent. The rubric says MEDIUM means “has usage context but lacks trigger keyword lists” at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):25, but the POOR bucket at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):32 includes skills whose descriptions already have clear usage context, such as [code-reviewer/SKILL.md](/home/deeog/.agents/skills/code-reviewer/SKILL.md):3, [python-reviewer/SKILL.md](/home/deeog/.agents/skills/python-reviewer/SKILL.md):3, [refactor-cleaner/SKILL.md](/home/deeog/.agents/skills/refactor-cleaner/SKILL.md):3, and [e2e-runner/SKILL.md](/home/deeog/.agents/skills/e2e-runner/SKILL.md):3. Re-score the inventory before acting on Layer 1.

- High: Layer 5 misuses `find-skills`. The fallback at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):150 says to invoke it for unmatched tasks, but [find-skills/SKILL.md](/home/deeog/.agents/skills/find-skills/SKILL.md):3 and [find-skills/SKILL.md](/home/deeog/.agents/skills/find-skills/SKILL.md):8 show it is for discovering and installing new ecosystem skills, not routing among installed local skills.

- High: There is no canonical registry / source of truth. The doc already uses a stale name, `nimble-web-tools`, at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):30, while the actual skill is [nimble-web-expert/SKILL.md](/home/deeog/.agents/skills/nimble-web-expert/SKILL.md):2. Local rules also still refer to `security-reviewer` in [claude-config.md](/home/deeog/.claude/rules/common/claude-config.md):18 even though the merged skill is [security-review/SKILL.md](/home/deeog/.agents/skills/security-review/SKILL.md):8. Adding another manual routing file at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):127 will increase drift unless it is generated.

- Medium: The proposed phase chains are too rigid for real agent behavior. The chain at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):50 and phase map at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):129 assume linear work, but existing routing guidance already spans multiple artifacts in [workflow.md](/home/deeog/.claude/rules/common/workflow.md):3 and [claude-config.md](/home/deeog/.claude/rules/common/claude-config.md):11, and many triggers are event-based, not phase-based.

- Medium: Several merge recommendations collapse distinct roles. `e2e-runner` explicitly points to `e2e-testing` for detailed patterns in [e2e-runner/SKILL.md](/home/deeog/.agents/skills/e2e-runner/SKILL.md):103, so runner vs reference is intentional. `web-design-guidelines` is a live audit workflow in [web-design-guidelines/SKILL.md](/home/deeog/.agents/skills/web-design-guidelines/SKILL.md):16, while `web-accessibility` is implementation guidance in [web-accessibility/SKILL.md](/home/deeog/.agents/skills/web-accessibility/SKILL.md):3. Merge only after modeling role types like `audit`, `reference`, `executor`, and `reviewer`.

- Medium: Layer 2 overstates enforcement. A PostToolUse reminder on writes at [skills-discovery-optimization.md](/home/deeog/skills-discovery-optimization.md):121 is advisory, not “impossible to skip.” The existing hook model already distinguishes PostToolUse from verification boundaries in [claude-config.md](/home/deeog/.claude/rules/common/claude-config.md):23. Mandatory skills need obligation tracking plus stop/final/commit gates.

**What I’d Change In The Design**

- Replace “optimize descriptions first” with “create a machine-readable skill manifest first.”
  Fields should include `canonical_id`, `aliases`, `capabilities`, `task_types`, `languages`, `file_globs`, `lifecycle_events`, `mandatory`, `proactive`, `prerequisites`, `conflicts_with`, `not_when`, and `cost`.

- Use a 2-stage router.
  Stage 1: candidate generation from task text, repo signals, edited files, and tool outcomes.
  Stage 2: policy scoring with confidence thresholds, negative triggers, and cooldowns to avoid over-firing.

- Generate all human-facing artifacts from the manifest.
  Descriptions, proactive tables, routing snippets, and enforcement rules should be derived outputs, not separate hand-maintained sources.

- Replace the `find-skills` fallback with a confidence-based unresolved-intent path.
  If no installed skill clears threshold, either proceed without a skill, ask for clarification, or only then use `find-skills` when the user actually needs new capability.

- Add observability before rollout.
  Log `skills_considered`, `skills_selected`, `reason_codes`, `mandatory_skills_missed`, `time_of_trigger`, and `user_override`. Without that, you cannot tune discovery.

**Better Priority Order**

1. Define scope and build the eval set.
2. Normalize IDs/aliases and create the manifest.
3. Re-score the current 67 skills from the manifest, not by hand.
4. Ship the router in shadow mode with telemetry.
5. Add enforcement gates for truly mandatory skills.
6. Rewrite descriptions and consolidate only where data shows confusion.

**Questions That Would Sharpen A Revised Draft**

- Is the router meant to cover only locally installed skills, or also plugin/system/marketplace skills?
- Are you free to add a generated manifest/index, or must the solution remain SKILL.md-only?
- Which failure hurts more today: under-triggering, late-triggering, or false-positive over-triggering?

If you want, I can turn this into a revised `skills-discovery-optimization.md` with a cleaner architecture and rollout plan.
