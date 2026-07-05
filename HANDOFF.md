# Handoff — SDLC First-Principles project

_A living, Socratic, first-principles derivation of what makes a software-development
lifecycle **reliable, predictable, resilient, and secure** — captured as one source-of-truth
markdown file and a local dark-themed website that renders it live._

Written for a **fresh Claude session** picking this up cold. Read this, then read the
source-of-truth file.

---

## 1. Read these first, in order

1. **`sdlc-first-principles-canvas.md`** — the **source of truth**. It contains the whole
   derived model, an **`▶ RESUME INSTRUCTIONS`** section (the method — obey it), a
   `§11 Current frontier` (where to resume), an iteration log, and the machine-readable
   diagram data. The file is designed to be resumed from *by itself*.
2. **This file** (`HANDOFF.md`) — project map + how to run the website.
3. Memory: `/Users/deepg/.claude/projects/-Users-deepg-Desktop-agent/memory/` →
   `socratic-first-principles-living-doc.md` (how the user likes to learn/architect).

## 2. File map

| path | role |
|---|---|
| `sdlc-first-principles-canvas.md` | **source of truth** — model, resume instructions, log, embedded diagram data |
| `index.html` | the website — renders the markdown live, turns diagram blocks into editable canvases |
| `.claude/launch.json` | preview server config — the **`canvas`** entry serves the folder on port 4321 |
| `HANDOFF.md` | this file |

## 3. Run the website (localhost only)

The page **must be served over http** (it `fetch()`es the markdown; `file://` is blocked).

- **In Claude Code:** `preview_start` with name **`canvas`** (already in `.claude/launch.json`),
  then open the preview. It runs `python3 -m http.server 4321` at the repo root.
- **Manually:** from the repo root, `python3 -m http.server 4321` → open
  `http://localhost:4321`.

## 4. What the website does

- **Hot-linked content.** Fetches `sdlc-first-principles-canvas.md` with `cache:no-store` on
  load and **polls every 3.5 s** (the *Auto-sync* toggle in the header). Edit the markdown and
  the site updates within a few seconds; the *Refresh* button forces a reload. Auto-sync pauses
  while you're renaming a node or in fullscreen so it never clobbers an in-progress edit.
- **Rendering.** Markdown via `marked`; auto-built sidebar TOC + scrollspy, top progress bar,
  section reveal-on-scroll, dark "glass" styling.
- **Interactive diagrams.** Any fenced ` ```pipeline-graph ` block in the markdown is *hoisted*
  out of the prose and rendered as a live **Cytoscape** canvas in the "Interactive model
  canvas" panel (one tab per diagram).

### Diagram controls (per canvas)
- **Navigate:** drag background to pan · scroll to zoom · drag a node to move it.
- **Edit:** double-click a node to **rename** · double-click empty space to **add** a node ·
  select + **Delete** to remove · **Connect** mode = click source then target to add an edge.
- **Toolbar:** `＋ Node` · `⇢ Connect` · `✕ Delete` · `⊹ Fit` · `✦ Tidy` (auto-layout) ·
  `⟲ Reset` (reload from the markdown) · `⤓ Export` (copy JSON to clipboard) ·
  `⛶ Pop out` (toggle **full-screen** canvas — same editable instance; `Esc` exits).

### Persisting diagram edits back to the markdown
In-browser edits are client-side/ephemeral. To make them permanent: click **⤓ Export** on a
diagram → it copies a ` ```pipeline-graph ` block to the clipboard → paste it over the matching
block in `sdlc-first-principles-canvas.md` (they live in the **"## Interactive diagrams"**
appendix at the end of the file). This keeps "visuals regenerable from the file," which is the
doc's stated philosophy.

## 5. Diagram data model (to add or change a diagram)

Add a fenced block to the markdown:

~~~
```pipeline-graph
{
  "title": "My diagram",
  "nodes": [ {"id":"a","label":"A","group":"beat","x":0,"y":0} ],
  "edges": [ {"source":"a","target":"b","dashed":true,"label":"…","member":true} ]
}
```
~~~

- `group` → colour: **beat** (purple) · **element** (teal) · **stone** (coral) ·
  **repertoire** (amber) · **property** (pink) · **terminal** (gray).
- `edge.dashed` = pink dashed feedback edge · `edge.member` = faint structural link (no arrow) ·
  `edge.label` = small caption.
- `x`/`y` are preset positions (nodes stay draggable).

## 6. The model in one breath (so you have the gist)

**Eight bedrock stones** (brute facts: intent-hidden · finite · complex · we-err · change ·
uncertain · **distributed & perishable** · **adversarial actors**; **+ a conditional second-order #9, `reflexivity`, for the automated autonomous multi-agent case**) **force** a single control loop
**`define → do → check → reflect ↺`**, where `reflect` = **analyze** (frame + root-cause) then
**decide** (*accept* a known issue · *re-target* · *escalate*). The loop is **staffed by
verb-named elements** (specify, scope, design, implement, verify, observe, analyze, decide) —
and **every element is itself the same loop** (the down-fractal), so beats are
scale-invariant while elements get finer. The loop's **behaviours** produce **four emergent apex
properties** in two families — **point** (at one context): reliable (loop *converges*) · predictable
(loop *bounded*); **envelope** (over context-hardness × time): resilient (loop *nests & escalates*, vs
**random** hardness #5/#6) · **secure** (loop *preempts* — red-teams its own inputs, vs a **directed**
adversary #8). An **evolve** feedback re-targets the whole thing (the Ouroboros). Stone #7 forces
**artifacts** — the persistent, explicit carriers of a loop's target/result/lesson across the *time*
and *agent* boundaries. A rule is a **hard gate** (non-waivable) iff a single violation is **non-local**
(adversary-amplified · irreversible · machinery-degrading); else it is a **graded target** (§10.4). Full
derivation is in the canvas file.

## 7. Method — DO NOT BREAK IT

This is a **Socratic + first-principles + handholding** teaching journey. **Ask, let the user
reason, then reflect/sharpen their answer and slot it into the model.** Do **not** lecture or
hand over answers unless the user explicitly asks. After each meaningful step, **update the
canvas file** — it, not the chat, is the source of truth. The canvas's `▶ RESUME
INSTRUCTIONS` section is authoritative; follow it.

## 8. Where we are / what's next

**Purpose reminder (important — set iteration 28).** This canvas derives the **ideal MUST-HAVE**
SDLC: what *any* such lifecycle is logically forced to contain. It is **not** a map of the user's
current setup — auditing a concrete stack against the ideal was **descoped** on purpose, so the ideal
stays uncontaminated by what a given setup already has or lacks. (The general residue of that dropped
thread survives as open tracks T2/T3/T4.)

**Done (recent arc, iterations 19–31):** **stone #9 `reflexivity`** (**§3**, T5 closed — a *conditional
second-order* stone for the autonomous multi-agent case: a correlated checker is an echo-chamber, so an
autonomous loop can't be its own ground truth); `observe` as the forced sensor (**§10.6**, T4 closed — telemetry
= detector + `analyze`-operand; graded coverage, gated only at non-compensatory seams; **T1 = memory / T4
= senses**); `reflect` as the forced-MUST-HAVE beat (**§10.5**, T1 closed — its artifact is the loop's
only *backward* channel; unwritten ⇒ machinery-degrading ⇒ hard gate); the mechanism of Done (canvas
**§10**); design-as-a-bet +
stub-composition (**§10.1**, **R2 closed**); the premise-B lever / two quality bars (**§10.2**); the
**4th apex property `secure`** (**§2** — the envelope *sibling* of `resilient`: resilient guards against
*random* hardness #5/#6, secure against a *directed* adversary #8); its loop-behaviour **`preempts`**
(**§4/§8**); its **every-seam recursion** as the forbidden-output wall (**§10.3**); and the **hard-gate =
non-compensatory-leaf** law + three amplifiers + predictive rule (**§10.4**). Bedrock is **8 stones + a conditional 2nd-order 9th (reflexivity, autonomous case — §3 #9)**;
the apex is now **four properties**; the behaviour→property map is complete; the living website still
renders the diagrams live.

**T1 closed (iteration 29) — `reflect` is the forced-MUST-HAVE beat; see canvas §10.5.** Running the
artifact-*absence* trace in the two directions `reflect` feeds settled it: *within-loop* (the **agent**
face) a green-leaves composite (§10) can't be root-caused once the composition hypothesis (§10.1) is
unwritten → `analyze` **starved** → `reflect` collapses into `check`; *next-loop* (the **time** face) no
post-mortem → the Ouroboros **evolve** edge is **unfed** → the failure-class recurs and the loop can't
raise its floor. Both are **one transient reflect-output failure through the two faces of stone #7**
(agent = ADR, time = post-mortem) — so the reflect-artifact is **machinery-degrading if unwritten (§10.4)
→ a forced hard gate**, confirming the working hypothesis. General law folded out: an artifact's *forced*
durability scales with **producer→consumer boundary-distance** (§9/§12) — `reflect`, the only
backward-feeding beat, is the extreme case where the artifact is the **sole channel**, not insurance.

**T4 closed (iteration 30) — `observe` is the forced sensor; see canvas §10.6.** Pressing the T1 coupling
held with a twist: telemetry is `analyze`'s *actual* operand **and** `observe`'s detector, so its absence
blinds `observe` *and* starves `analyze` (machinery-degrading, one beat upstream of the ADR) — absent it,
detection is outsourced to the end user (silent churn · no WHY · no artifact, #7). What's forced: `observe`
**owns a sensor**; *coverage* is graded, hard-gated only at non-compensatory seams (not wholesale like
`secure`). Coupling: **T1 = the loop's memory, T4 = its senses.** Deferred deep-dive parked as **T11**.

**T5 closed (iteration 31) — reflexivity admitted as a conditional second-order stone #9 (canvas §3).** A
check is only worth the *information* it adds beyond the doer's belief, so a checker whose errors are
*correlated* with the doer's is an echo-chamber (`verify` → *declare*). The property is **independence**;
reflexivity is the brute fact it is never total — irreducible to #4 (joint vs marginal). Flagged
**second-order** (about the solver, not the task) and **conditional**: it bites only in the automated
autonomous multi-agent case — with a human escape-hatch it stays bounded, so **an autonomous loop cannot
be its own ground truth.** Rippled through §2–§8 + §12; partly closes T6.

**Active frontier — between tracks.** T1, T4, T5 are closed; next is the user's pick from canvas §11
(T2 · T3 · T6 · T11, plus structural T7–T10).

**All open work lives in canvas §11 — the "Open-tracks register" (T1–T11).** That register is the single
source of what remains; read it there. Headlines:
- **T1** `reflect` as a MUST-HAVE — **closed (iteration 29 → canvas §10.5)** · **T4**
  observability-as-sensor — **closed (iteration 30 → canvas §10.6)**.
- **T2** proxy-leaves graded-vs-gated (sharpened by T4) · **T3** stone-#5 change: regression + rollback ·
  **T11** observability graded-vs-gated (deferred deep-dive, spun out of T4).
- **T5** reflexivity — **closed (iter 31 → conditional 2nd-order stone #9, §3)** · **T6** bedrock
  pressure-test (9th-stone sub-question now answered).
- **T7–T10** structural backlog (implement/lifecycle · the orphaned `plan` · resilience-formula &
  artifacts-diagram janitorial).

## 9. Notes & caveats

- **CDN dependencies:** `marked@12` and `cytoscape@3.30.2` load from jsDelivr, and the font
  from Google Fonts — the site needs internet even though it's hosted on localhost. Vendor
  them locally if you need it fully offline.
- **Harmless console warnings:** a custom wheel-sensitivity note and `label` width/height
  deprecation (Cytoscape 3.30 — still functional; version is pinned). Not errors.
- **Pop-out fullscreen** uses the Fullscreen API — works in a normal browser tab on a user
  gesture; a sandboxed preview iframe may block it.
- **Never** open `index.html` via `file://` — the markdown fetch will fail (the page shows a
  hint telling you to serve over http).
