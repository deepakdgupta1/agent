# SDLC First-Principles Canvas — Living State Document

> **What this is:** the evolving, self-contained state of a Socratic, first-principles
> derivation of *what constitutes a resilient, reliable, predictable software-engineering
> SDLC, and why every piece is logically required.* It is written so the whole journey can
> be resumed from this file alone, with a fresh/cleared context.

- **Last updated:** iteration 17 (artifacts rendered as interactive diagrams; living website `index.html` built)
- **Status:** bedrock complete (7 stones); artifacts derivation done (root + per-beat carriers as diagrams); living website built. Next: map onto the real setup.

---

## ▶ RESUME INSTRUCTIONS (read first on a fresh context)

You are the assistant resuming a Socratic teaching journey with the user. Do this:

1. Read this entire document — it is the complete derived model and the current frontier.
2. **Method (do not break it):** Socratic + first-principles + handholding. *Ask, let the
   user reason, then reflect/sharpen their answer and slot it into the model.* Do not
   lecture or hand over answers unless the user explicitly asks ("what's the answer?").
   Maintain an evolving visual when it helps; visuals are regenerable from this file, so
   they are disposable.
3. Go to **§9 Current frontier** and continue from the **pending question** there.
4. After each meaningful step, **update this document** (the model sections + §9 + §10 log).
   This file — not the chat history — is the source of truth.

---

## 1. The core question

From first principles: what are the irreducible pieces of an SDLC that make it
**resilient, reliable, and predictable**, and *why is each piece logically required* (i.e.
forced into existence, not adopted by convention)?

## 2. The destination — three properties (the apex)

Three *distinct* properties, each guarding a different failure. Reliability and
predictability are **independent axes** (proven by two thought experiments: Setup A =
correct-but-unforeseeable = reliable-not-predictable; Setup B = foreseeable-but-wrong =
predictable-not-reliable). Resilience is **not a peer** — it is the *envelope* around the
other two, measured along a third axis (context hardness × time).

| property | plain meaning | guards against | measured | produced by (see §6) |
|---|---|---|---|---|
| **reliable** | faithful to intent; correct output, nothing missing or invented | "it gave the wrong thing" | at a point (one task, one context) | a loop that **converges** |
| **predictable** | foreseeable; low variance; you can call the output & timing in advance | "I couldn't foresee / plan around it" | at a point | a loop that is **bounded** |
| **resilient** | withstands **and recovers** across the range of contexts and over time; the envelope that keeps the other two alive | "it collapsed on a hard context and couldn't recover" | along the context-hardness / time axis | loops that **nest & escalate** |

## 3. The bedrock — brute facts that force everything

First principles = the unavoidable truths about reality that make the work hard. Stages and
tools are *responses* to these. **Facts are not 1:1 with stages** — one fact drives several
responses (finiteness → scope *and* plan; complexity → design *and* decompose).

1. **Intent is hidden** — the real need isn't given; what's asked ≠ what's needed.
2. **Unbounded vs finite** — infinite possible scope against finite resources.
3. **Complexity > one step** — systems exceed any single mind / single step.
4. **Humans & models err** — translating intent → artifact is lossy and mistake-prone.
5. **Reality keeps changing** — the target moves over *time*. *(resilience engine #1)*
6. **Reality is uncertain / varied** — you can't know which reality will materialise at any
   moment. *(resilience engine #2)*
7. **Knowledge is distributed & perishable** — it lives in separate private stores (no direct
   transfer between minds / context windows) *and* decays over time (memory fades, context
   clears). Two faces — *distributed* (agent crossing) + *perishable* (time crossing).
   *(forces artifacts; flushed by the artifacts derivation, iteration 16)*

> **Self-test the model uses:** if a needed element rests on *no* stone, a stone is missing;
> if a stone has *no* element defending it, there is a gap. The model currently passes for
> stones 1–7.

## 4. The atom — the unit control loop

Everything reduces to one feedback loop:

```
set target  →  do  →  check  →  reflect  →  (re-target ↺)
```

- It is **bounded**: a few tries, then stop — because each turn costs.
- **`check` is graded, not binary:** it measures *how well* on a quality range (via an
  objective metric, or a **proxy** when the true quality isn't directly measurable) and
  compares that to a **target threshold** → *done = measured ≥ threshold*.
- **`reflect` (was "correct"/"understand")** is the loop-closing beat. It **analyzes**
  (frames the issue — e.g. "loop can't converge" — and root-causes it), then **decides**:
  *accept* the gap as a known issue, or *re-target* (re-iterate by re-defining the target).
  Escalation is the third, cross-cutting exit. Investigation + judgement, not a mechanical fix.
- **Non-convergence is information**, not just failure: after honest tries, suspect the
  **target** (the spec), not only the build → escalate *up*.
- **The responses are cross-cutting, not a beat:** escalate · degrade · recover · roll back
  are a **repertoire** invoked from `reflect` at *any* element and *any* scale (mostly at
  run-time). They are forced by the two resilience stones (#5 change, #6 uncertainty) and are
  exactly what manufactures the **resilient** property.
- **The loop nests *down* as well as up:** every element (specify, design, implement, …) is
  *itself* a define → do → check → reflect loop with its own graded target and its own
  metric/proxy.
- **Escape hatch:** escalation ultimately ends at a human.
- **"Definition of done"** = the target the `check` compares against — *a threshold on a
  quality range, not a yes/no*. It is *composite*:
  - **scope** sets the boundary (*how much / which items*),
  - **specify** sets correctness (*what's right*), across the **set of potential
    realities** → which is how one act sets targets for all three properties:
    expected reality → reliability, adverse realities → resilience, all enumerated up
    front → predictability.

**Loop behaviour → property:** converges → reliable · bounded → predictable · nests &
escalates → resilient.

## 5. The fractal — the loop nests at every scale

The same shape repeats **in both directions**. *Outward* across scope (decompose, forced
by complexity, creates this nesting); and *inward* into every element — addressing a single
element (e.g. specify) is itself a full define → do → check → reflect loop with its own
graded target and metric/proxy. **Two planes, then:** the *beats* (define → do → check →
reflect) are scale-invariant — the same four recur at every level; the *elements* (specify …
decide) are the **outermost** loop's staffing of those beats, re-instantiated by finer
activities at each level down. A stuck inner loop escalates to the loop above; the
outermost escape hatch is a human.

```
action ⊂ feature ⊂ stage ⊂ release ⊂ product       ← outward (scope)
every beat ⊃ its own define → do → check → reflect → inward (each element)
```

## 6. The elements — the loop, fully staffed

The elements are not a checklist; they are the **anatomy of the loop**, each forced by a
stone. **Plane distinction:** the left column lists the scale-invariant *beats*; the middle
column lists the *elements* — the **outermost** SDLC loop's concrete staffing of each beat.
`analyze`/`decide` are the elements that instantiate the `reflect` beat *at the outermost
level*; they are not the beat itself (which recurs, staffed differently, at every deeper
level).

| loop beat | element | forced by (stone) |
|---|---|---|
| **define** (set target) | specify | intent is hidden |
| **define** | scope (& prioritise) | unbounded vs finite |
| **define** | design | complexity > one step |
| **do** | implement | (the build itself) |
| **do** | decompose | complexity > one step |
| **check** | verify (build-time) | humans & models err |
| **check** | observe (run-time) | reality is uncertain |
| **reflect** | analyze — frame + root-cause the gap | humans & models err |
| **reflect** | decide — accept (known issue) or re-target | unbounded vs finite |
| **repeat over time** | version · integrate (CI/CD) · regression-test | reality keeps changing |

**Cross-cutting — the resilience repertoire (not beats).** Invoked from `reflect` at any
element and any scale; realised mostly at run-time. Each is forced by a resilience stone, and
together they manufacture the **resilient** property:

| response | what it does | concrete example | forced by |
|---|---|---|---|
| **escalate** | hand up when bounded tries are exhausted; ends at a human | retries for one email domain keep failing → page on-call | loop can't converge |
| **degrade** | fail partial, not total (error handling / graceful degradation) | email provider down → queue the request + "arriving shortly" instead of a 500 | reality is uncertain |
| **recover** | spares · replicas · retries so the function survives a failure (redundancy) | second email provider takes over when the primary fails | reality is uncertain |
| **roll back** | revert to the last known-good state | new reset-email template spikes bounces → redeploy the previous one | reality keeps changing |

## 7. The process flow (with nested loops)

```
discover → define → design → plan
   → BUILD     [feature loop:  do  ⇄  check vs graded 'done'  →  reflect  ↺ re-target ]
   → verify    (stage gate against 'done')
   → release
   → OPERATE   [runtime loop:  observe  ⇄  recover / degrade / escalate   ↺ watch ]
   ⟲ PRODUCT LOOP:  operate → learn → evolve target → back to discover   (the Ouroboros)

solid = forward flow (the lifecycle)   ·   dashed = loops / feedback (at every scale)
```

## 8. The complete circuit (synthesis)

The three properties are **emergent**, not installed — manufactured by a system of bounded,
nested feedback loops, themselves built from elements forced by brute facts.

```
        ┌──────────────── evolve  (feedback) ◄────────────────┐
        ▼                                                      │
   reliable        predictable        resilient   ◄── 3 properties (emergent)
      ▲                 ▲                  ▲
  converges          bounded        nests + escalates   ◄── loop behaviours
      └──────────────── THE LOOP ───────────────┘
              (set target → do → check → reflect ↺)
                          ▲  force
   bedrock:  intent-hidden · finite · complex · we-err · change · uncertain
```

## 9. Current frontier & next steps

**Just completed (through iteration 15):** synthesised the model into a master visual;
reworked the loop's fourth beat; switched to all-verb elements; separated the two planes; and
resolved the metrics frontier (below).

**Decisions locked in:**
- **`correct` → `understand` → `reflect`.** The fourth beat is *diagnosis + judgement*:
  **analyze** (frame the issue — e.g. "loop can't converge" — and root-cause it) then
  **decide** — accept the gap as a *known issue*, or **re-target** (re-iterate into the next
  **define**). Escalation is the cross-cutting third exit.
- **All elements are verbs now** (specify · scope · design · implement · decompose · verify ·
  observe · analyze · decide), to match the action each names.
- **The responses are cross-cutting, not a beat.** escalate · degrade · recover · roll back
  form a **resilience repertoire** invoked from `reflect` at any element and any scale (mostly
  run-time). They are what manufactures the **resilient** property.
- **The loop nests *down* into every element**, not just up across scope. Each element is its
  own define → do → check → reflect loop.

**Resolved — graded targets & measurement.** A target is *not* binary; it is a **threshold on
a quality range**, and `check` is a *measurement* against it (*done = measured ≥ threshold*).
Most metrics are **proxies** (coverage ≈ "well-tested", NPS ≈ "trust", latency ≈ "feels
fast").

- **The proxy failure & where it's caught — `specify` (a-priori) vs `analyze` (a-posteriori).**
  `specify` catches every proxy↔intent gap that is *deducible at t0* — but it can only *reason
  about the risk*, never *measure a gap that isn't a fact yet*. Measurement is inherently a
  posteriori. The residue `specify` cannot reach (so `analyze`, fed by `observe`, must) has
  three sources:
  1. **Goodhart / induced** — the gap is *created* by optimising the proxy; it doesn't exist
     until you iterate. *(#5 change, via the feedback of use)*
  2. **Reality-contingent** — the proxy↔intent map runs through reality not yet observed.
     *(#1 hidden, #6 uncertain)*
  3. **Intent drift** — the proxy was faithful to t0-intent; real intent has since moved.
     *(#1, #5)*
- **Why it matters:** if none of the three held, `specify` would catch everything and the loop
  would **collapse to a single forward pass**. `analyze`/`reflect` exist *only* because the
  stones guarantee an irreducible a-posteriori residue.

**Next frontiers (resume from the first):**
- The **artifacts** derivation: *why must an artifact exist at all? What does writing-it-down
  buy a loop that holding it in a head does not?* (Expected to flush the suspected stone
  **"knowledge is distributed & perishable."**)
- Map this model onto the user's **real setup** (Ouroboros, governance hard-gates, mandatory
  TDD, verification skills, LiteLLM routing) — find undefended stones (risks) and elements
  with no stone (vestigial ceremony).

## 10. Key laws & insights derived along the way

- **Shift-left:** cost of a defect grows ~exponentially with detection latency ⇒ verify at
  *every* stage, while deviations are cheap and local. (Hence verification is a cross-cutting
  layer, not a step bolted on after "build".)
- **Verification is a comparison** (actual vs expected) ⇒ it *requires* an objective "done";
  you cannot verify against nothing.
- **Properties are emergent**, produced by the loop's behaviours — they are not bolt-on
  features.
- **Facts ≠ stages (many-to-many):** one brute fact drives several responses.
- **Non-convergence points at the target:** a loop that won't converge often signals a wrong
  spec, not just a buggy build.
- **"Done" is graded, not binary:** it is a *threshold on a quality range*; `check` is a
  measurement (*done = measured ≥ threshold*), which is why it needs a metric.
- **Metrics are often proxies; proxies invite Goodhart:** optimising the proxy can diverge
  from true intent ⇒ `reflect`/`observe` must check proxy-vs-intent, not just
  actual-vs-proxy.
- **The corrective responses are cross-cutting, not a beat:** escalate / degrade / recover /
  roll back are a repertoire invoked at any element & scale; together they *are* the
  resilient property's machinery.
- **The fractal runs *both* ways:** the loop nests up across scope *and* down into every
  element.
- **`decide` is where the loop's behaviours become a choice:** *accept* (stop — the
  *bounded* / predictable exit) · *re-target* (refine — the *converges* / reliable exit) ·
  *escalate* (hand up — the *nests & escalates* / resilient exit).
- **`specify` is a-priori, `analyze` is a-posteriori:** `specify` *reasons about* what should
  be true; `analyze` *measures* what turned out true. Pure logic at `specify` catches only
  *deducible* gaps — it cannot measure a gap that isn't a fact yet.
- **A proxy gap is often not a fact at t0:** it is induced by optimisation (Goodhart),
  contingent on unobserved reality, or relative to drifted intent — so measuring it is
  irreducibly a-posteriori.
- **The loop exists because of that residue:** with no residue (intent known & fixed, reality
  predictable, proxy immune to its own use), the loop collapses to one forward pass.
- **Artifacts are forced by boundary-crossings (stone #7):** a loop's information must cross
  *time* (→ defeated by **persistence**) and *agent* (→ defeated by an **explicit / external**
  form). An *artifact* = the **persistent, explicit carrier** of a loop's target / result /
  lesson across those boundaries; the loop-level hand-off is just these two at fine grain.
- **Shared understanding is the *output*, distribution is the *fact*:** knowledge isn't shared
  by default because it's distributed across private stores; the artifact manufactures the
  shared copy.

## 11. Iteration log (compressed)

1. Distinguished reliable / predictable / resilient (three failures, not one word).
2. Proved reliability ⊥ predictability (Setup A vs Setup B).
3. Placed resilience as the envelope on a third axis (context hardness × time).
4. Found the bedrock brute facts; saw facts ≠ stages 1:1.
5. Derived element #1 verification + shift-left; saw the verify *gate* = a feedback loop.
6. Split "done" into scope (boundary) + specification (correctness across realities).
7. Saw specification set targets for all three properties at once; surfaced stone #6.
8. Closed the loop (correct beat), bounded + escalation + non-convergence-as-signal.
9. Revealed the fractal: one loop, nested at every scale.
10. Mapped loop behaviours → properties (converge/bound/nest); drew the complete circuit.
11. Finished the elements band (organised by loop-beat).
12. Drew the giant process flow chart; created this living document.
13. Built the master synthesis visual; reframed beat 4 `correct`→`understand` (diagnose →
    re-target); lifted escalate/degrade/redundancy/rollback into a cross-cutting resilience
    repertoire; saw the loop also nests *downward* into each element (graded targets +
    metric/proxy); opened the metrics/Goodhart deep-dive.
14. Switched all elements to verb names (specify, implement, decompose, …); `understand` →
    `reflect`; split `reflect` into **analyze** (frame + root-cause) and **decide** (accept a
    known issue · or re-target), with escalate as the cross-cutting third exit.
15. Distinguished the two planes (scale-invariant *beats* vs the outermost loop's *elements*);
    resolved the metrics frontier — `specify` catches the a-priori/deducible proxy-risk,
    `analyze` (via `observe`) measures the a-posteriori residue (Goodhart / reality-contingent
    / intent-drift); saw the loop is irreducible precisely because that residue can't be zeroed.
16. Opened the artifacts derivation and flushed the **7th stone — knowledge is distributed &
    perishable** (the §3 suspect): artifacts are forced because a loop's information must cross
    the *agent* boundary (distributed → needs an explicit/external form) and the *time* boundary
    (perishable → needs persistence). Root derived: artifact = persistent, explicit carrier of
    a loop's info across boundaries.
17. Enumerated the per-beat artifacts (spec/target · code · tests + telemetry · postmortem /
    ADR · version history · runbooks) and captured them as the two interactive `pipeline-graph`
    diagrams below. Built the **living website** (`index.html`) — dark, hot-linked to this file
    (live fetch + auto-sync), diagrams interactive/editable with an embedded↔fullscreen toggle.

---

## Interactive diagrams

> These fenced `pipeline-graph` blocks are the **machine-readable snapshot** of the model.
> `index.html` renders each as a live, editable canvas (drag · rename · add/remove nodes &
> edges · pop out to full-screen). Edit here, or edit on the site and use **Export** to copy
> the JSON back over the matching block — the visuals stay regenerable from this file.

```pipeline-graph
{
  "title": "The unit loop",
  "nodes": [
    {"id":"define","label":"define","group":"beat","x":0,"y":0},
    {"id":"do","label":"do","group":"beat","x":210,"y":0},
    {"id":"check","label":"check","group":"beat","x":420,"y":0},
    {"id":"reflect","label":"reflect","group":"beat","x":630,"y":0},
    {"id":"specify","label":"specify","group":"element","x":0,"y":95},
    {"id":"scope","label":"scope","group":"element","x":0,"y":165},
    {"id":"design","label":"design","group":"element","x":0,"y":235},
    {"id":"implement","label":"implement","group":"element","x":210,"y":95},
    {"id":"decompose","label":"decompose","group":"element","x":210,"y":165},
    {"id":"verify","label":"verify (build)","group":"element","x":420,"y":95},
    {"id":"observe","label":"observe (run)","group":"element","x":420,"y":165},
    {"id":"analyze","label":"analyze","group":"element","x":630,"y":95},
    {"id":"decide","label":"decide","group":"element","x":630,"y":165},
    {"id":"accept","label":"accept · known issue","group":"terminal","x":630,"y":240},
    {"id":"escalate","label":"escalate","group":"repertoire","x":0,"y":350},
    {"id":"degrade","label":"degrade","group":"repertoire","x":210,"y":350},
    {"id":"recover","label":"recover","group":"repertoire","x":420,"y":350},
    {"id":"rollback","label":"roll back","group":"repertoire","x":630,"y":350}
  ],
  "edges": [
    {"source":"define","target":"do"},
    {"source":"do","target":"check"},
    {"source":"check","target":"reflect"},
    {"source":"reflect","target":"define","dashed":true,"label":"re-target ↺"},
    {"source":"decide","target":"accept","label":"accept"},
    {"source":"define","target":"specify","member":true},
    {"source":"define","target":"scope","member":true},
    {"source":"define","target":"design","member":true},
    {"source":"do","target":"implement","member":true},
    {"source":"do","target":"decompose","member":true},
    {"source":"check","target":"verify","member":true},
    {"source":"check","target":"observe","member":true},
    {"source":"reflect","target":"analyze","member":true},
    {"source":"reflect","target":"decide","member":true}
  ]
}
```

```pipeline-graph
{
  "title": "The complete circuit",
  "nodes": [
    {"id":"evolve","label":"evolve (Ouroboros)","group":"terminal","x":360,"y":0},
    {"id":"reliable","label":"reliable","group":"property","x":100,"y":100},
    {"id":"predictable","label":"predictable","group":"property","x":360,"y":100},
    {"id":"resilient","label":"resilient","group":"property","x":620,"y":100},
    {"id":"converges","label":"converges","group":"beat","x":100,"y":215},
    {"id":"bounded","label":"bounded","group":"beat","x":360,"y":215},
    {"id":"nests","label":"nests & escalate","group":"beat","x":620,"y":215},
    {"id":"loop","label":"the loop","group":"beat","x":360,"y":320},
    {"id":"intent","label":"intent hidden","group":"stone","x":-40,"y":440},
    {"id":"finite","label":"finite","group":"stone","x":120,"y":440},
    {"id":"complex","label":"complex","group":"stone","x":270,"y":440},
    {"id":"err","label":"we err","group":"stone","x":420,"y":440},
    {"id":"change","label":"change","group":"stone","x":560,"y":440},
    {"id":"uncertain","label":"uncertain","group":"stone","x":710,"y":440},
    {"id":"distributed","label":"distributed & perishable","group":"stone","x":880,"y":440}
  ],
  "edges": [
    {"source":"intent","target":"loop","member":true},
    {"source":"finite","target":"loop","member":true},
    {"source":"complex","target":"loop","member":true},
    {"source":"err","target":"loop","member":true},
    {"source":"change","target":"loop","member":true},
    {"source":"uncertain","target":"loop","member":true},
    {"source":"distributed","target":"loop","member":true},
    {"source":"loop","target":"converges"},
    {"source":"loop","target":"bounded"},
    {"source":"loop","target":"nests"},
    {"source":"converges","target":"reliable"},
    {"source":"bounded","target":"predictable"},
    {"source":"nests","target":"resilient"},
    {"source":"reliable","target":"evolve"},
    {"source":"predictable","target":"evolve"},
    {"source":"resilient","target":"evolve"},
    {"source":"evolve","target":"loop","dashed":true,"label":"re-target"}
  ]
}
```
