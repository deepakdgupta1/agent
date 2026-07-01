# Handoff — SDLC First-Principles project

_A living, Socratic, first-principles derivation of what makes a software-development
lifecycle **resilient, reliable, and predictable** — captured as one source-of-truth
markdown file and a local dark-themed website that renders it live._

Written for a **fresh Claude session** picking this up cold. Read this, then read the
source-of-truth file.

---

## 1. Read these first, in order

1. **`sdlc-first-principles-canvas.md`** — the **source of truth**. It contains the whole
   derived model, an **`▶ RESUME INSTRUCTIONS`** section (the method — obey it), a
   `§9 Current frontier` (where to resume), an iteration log, and the machine-readable
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

Seven **bedrock stones** (brute facts: intent-hidden · finite · complex · we-err · change ·
uncertain · **distributed & perishable**) **force** a single control loop
**`define → do → check → reflect ↺`**, where `reflect` = **analyze** (frame + root-cause) then
**decide** (*accept* a known issue · *re-target* · *escalate*). The loop is **staffed by
verb-named elements** (specify, scope, design, implement, decompose, verify, observe, analyze,
decide) — and **every element is itself the same loop** (the down-fractal), so beats are
scale-invariant while elements get finer. The loop's **behaviours** (converges / bounded /
nests & escalates) produce the emergent **properties** (reliable / predictable / resilient),
and an **evolve** feedback re-targets the whole thing (the Ouroboros). Stone #7 forces
**artifacts** — the persistent, explicit carriers of a loop's target/result/lesson across the
*time* and *agent* boundaries. Full derivation + reasoning is in the canvas file.

## 7. Method — DO NOT BREAK IT

This is a **Socratic + first-principles + handholding** teaching journey. **Ask, let the user
reason, then reflect/sharpen their answer and slot it into the model.** Do **not** lecture or
hand over answers unless the user explicitly asks. After each meaningful step, **update the
canvas file** — it, not the chat, is the source of truth. The canvas's `▶ RESUME
INSTRUCTIONS` section is authoritative; follow it.

## 8. Where we are / what's next

**Done:** bedrock complete at 7 stones; the loop (define/do/check/reflect), the reflect split
(analyze/decide), the cross-cutting resilience repertoire, graded targets + metric/proxy (with
the a-priori `specify` vs a-posteriori `analyze` resolution), the two-planes distinction, the
artifacts derivation (root + per-beat carriers), and the living website.

**Open frontier** (see canvas `§9 Next frontiers`, resume from the first):
1. _(minor polish)_ Formalize the per-beat **artifacts** as a numbered prose section in the
   canvas — right now they live as the two interactive diagrams + the chat table.
2. **Map the model onto the user's real setup** — Ouroboros, the governance hard-gates,
   mandatory TDD, verification skills, LiteLLM routing — to find **undefended stones** (risks)
   and **elements with no stone** (vestigial ceremony). This is the main next step.

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
