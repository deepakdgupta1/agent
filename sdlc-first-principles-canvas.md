# SDLC First-Principles Canvas — Living State Document

> **What this is:** the evolving, self-contained state of a Socratic, first-principles
> derivation of *what constitutes a reliable, predictable, resilient, and secure software-engineering
> SDLC, and why every piece is logically required.* It is written so the whole journey can
> be resumed from this file alone, with a fresh/cleared context.

- **Last updated:** iteration 32 (**backported design-doc Ch 6.4 → the inward base case / reducibility law, §10.7**): a beat responds to a stone (§3), so where the stone is absent for a node it adds **zero information** and the inner loop **collapses toward bare `do`** — the inward dual of §10's outward termination; the collapse is itself a `decide` (ceremony = insurance, premium ∝ `P(error)×cost(error)`, §10.2/§10.7), with two overrides that delete `accept` — **hard gate** (§10.4) and **non-convergence** (§4). Advances **T2** (graded ⇒ collapsible · gated ⇒ non-waivable). Frontier: **between tracks** — T2 advanced; next is the user's pick (T3 · T6 · T11). **Prior — iteration 31 (T5 closed → conditional second-order 9th stone: reflexivity, §3 #9):** A check is only worth the **information** it adds beyond the doer's own belief, so a checker whose errors are **correlated** with the doer's is an **echo-chamber** (zero bits; `verify` collapses into *declare*). The property at stake is **independence** — what lets stacked checks drive error → 0 (→ `reliable`); reflexivity is the brute fact that independence is **never total** (a common-mode floor; even formal proof only relocates the blind spot to the spec). **Irreducible to #4** (marginal error vs the *joint* correlated-error fact). Flagged **second-order** (a fact about the *solver*, not the task) and **conditional** — it bites only in the **automated autonomous multi-agent** pipeline: with a human escape-hatch (§4/§5) reflexivity is bounded; remove the human and independence at the terminal → 0, so **an autonomous loop cannot be its own ground truth.** Forces independence-seeking (non-removable external/human terminal · adversarial review — §6 `red-team`, double-duty with #8). Rippled through §2/§3/§4/§5/§6/§8 (+ circuit diagram)/§12. **Partly closes T6.** Frontier: **between tracks** — user picks next. *(Prior: iter 30 closed T4 §10.6; iter 29 closed T1 §10.5.)*
- **Status:** canvas = **ideal MUST-HAVE** derivation (concrete-setup audit descoped, iteration 28). Apex **four properties** (reliable · predictable · resilient · secure); behaviour→property map complete (**preempts→secure**); `secure` recurses every seam (§10.3); hard gate = non-compensatory leaf, 3 amplifiers (§10.4); **`reflect` = forced-MUST-HAVE beat / only *backward* channel (§10.5)**; **`observe` = forced sensor; telemetry = detector + analyze-operand, graded-with-gates (§10.6)**; bedrock **8 stones + a conditional 2nd-order 9th (reflexivity, autonomous case — §3 #9)**; artifacts (§9, + boundary-distance law); Done / design-as-a-bet / two bars (§10–§10.2). **All open work: §11 Open-tracks register.** Active: **T3/T7/T8/T11 closed (iter 33 → §10.8/§10.9/§10.10) + the *existence-hard / fidelity-graded* convergent law (§12); T9 folded.** Next: **T6 (bedrock pressure-test) — a sub-agent derivation draft is ready, held for the user's decision**; janitorial T10 (artifacts / rollback-node diagram).

---

## ▶ RESUME INSTRUCTIONS (read first on a fresh context)

You are the assistant resuming a Socratic teaching journey with the user. Do this:

1. Read this entire document — it is the complete derived model and the current frontier.
2. **Method (do not break it):** Socratic + first-principles + handholding. *Ask, let the
   user reason, then reflect/sharpen their answer and slot it into the model.* Do not
   lecture or hand over answers unless the user explicitly asks ("what's the answer?").
   Maintain an evolving visual when it helps; visuals are regenerable from this file, so
   they are disposable.
3. Go to **§11 Current frontier** and continue from the **pending question** there.
4. After each meaningful step, **update this document** (the model sections + §11 frontier + §13 log).
   This file — not the chat history — is the source of truth.

---

## 1. The core question

From first principles: what are the irreducible pieces of an SDLC that make it
**reliable, predictable, resilient, and secure**, and *why is each piece logically required* (i.e.
forced into existence, not adopted by convention)?

## 2. The destination — four properties (the apex)

Four *distinct* properties in **two families**, each guarding a different failure.

**Point-properties — measured at a single point** (one task, one context). **reliable** and
**predictable** are **independent axes** (proven by two thought experiments: Setup A =
correct-but-unforeseeable = reliable-not-predictable; Setup B = foreseeable-but-wrong =
predictable-not-reliable).

**Envelope-properties — measured along the third axis** (**context-hardness × time**); each is
the envelope that keeps the point-properties alive across the *range* of contexts. §2 first named
a single envelope (*resilient*); **stone #8 splits the hardness axis by its source**, and the two
halves force **two sibling envelopes**:
- **natural / random hardness** — reality *changes* (#5) and is *uncertain* (#6); it **samples**
  the context-space blindly. Envelope against it → **resilient**.
- **directed / adversarial hardness** — an adversary (#8) **searches** the context-space for the
  worst case. Envelope against it → **secure**.

*Same shape, different opponent.* Both are envelopes over context-hardness — one against a blind
sampler, one against a directed optimiser — so **`secure` takes a fourth seat *beside* `resilient`,
not a slot *under* it.** It is **not** "resilience on the hardest context": the statistical
machinery that manufactures resilience (redundancy · retries · graceful degrade) *fails* against a
directed opponent (retries just feed a DoS — §12), so a distinct **security repertoire** (§6) is
required. And neither point-property is a peer of the two envelopes. **secure ⊥ resilient** the same
way §2 proves reliable ⊥ predictable — two setups: *resilient-but-insecure* (auto-failover + self-heal
under random load, behind an open auth bypass) and *secure-but-fragile* (hardened + authz-per-request,
but no redundancy, so a random outage kills it). Both exist → a fourth independent seat.

| property | family | plain meaning | guards against | measured | produced by (see §6) |
|---|---|---|---|---|---|
| **reliable** | point | faithful to intent; correct output, nothing missing or invented | "it gave the wrong thing" | at a point (one task, one context) | a loop that **converges** |
| **predictable** | point | foreseeable; low variance; you can call the output & timing in advance | "I couldn't foresee / plan around it" | at a point | a loop that is **bounded** |
| **resilient** | envelope · vs **random** | withstands **and recovers** across the range of contexts and over time; the envelope against *natural* hardness (#5 change, #6 uncertain) | "it collapsed on a hard context and couldn't recover" | along the context-hardness / time axis | loops that **nest & escalate** — the **resilience repertoire** |
| **secure** | envelope · vs **directed** | withstands a *directed* adversary hunting the worst case; the envelope against *adversarial* hardness (#8) | an attacker drove it to emit an output **outside its allowed set** — leaked secret · downtime (DoS) · forged / intercepted message | along the context-hardness axis, the **adversarial slice** | a loop that **preempts** — red-teams its own inputs for forbidden outputs, then forecloses them (the **security repertoire**, §6) |

> **Reflexivity caveat (stone #9, §3 — autonomous case).** `reliable` is manufactured by a loop that
> **converges**, which silently assumes the checker is *independent* of the doer. In the automated
> autonomous multi-agent regime that assumption fails (the second-order stone #9): the loop can converge to
> a **confident wrong fixed point** — a green check over a real defect — so `reliable` is the property
> reflexivity most directly erodes.

> **Schedule caveat (stone #5, §10.10 — the time axis).** Boundedness (§4) buys `predictable` only its
> *cost* face (the loop terminates within a bound); *outcome* is bought by tight contracts (§10.2); but
> *schedule/timing* — "call *when* it ships" — is an **aggregate over the time axis**, not this
> point-property. It is manufactured by a **schedule bet** (`plan` = `scope`+`specify` projected onto time —
> estimate = the stub of a task; critical-path = stub-composition on time, §10.10), whose written baseline is
> existence-hard / content-graded (**plan : predictable :: ADR : reliable**).

## 3. The bedrock — brute facts that force everything

First principles = the unavoidable truths about reality that make the work hard. Stages and
tools are *responses* to these. **Facts are not 1:1 with stages** — one fact drives several
responses (finiteness → scope *and* decide; "we err" → verify *and* analyze).

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
8. **Adversarial actors** — reality contains agents who *actively search for and exploit* weakness.
   Not accidental (that's #4, *our* error) and not neutral variance (that's #6, which *samples* the
   value-domain at random): an adversary is a **directed optimiser** that *hunts* the worst case —
   the exact premise-B residue (§10.2) your sampling missed. *(forces the security repertoire, §6;
   admitted iteration 23 when the security Hard Gates — SQLi · XSS · CSRF · credential theft — were
   found resting on no stone.)*
9. **Reflexivity — the checker shares the doer's fault** *(second-order · conditional — autonomous
   multi-agent pipelines only)* — the agents that staff `check`/`reflect` are the same kind of erring
   agent as the doer (#4), so their errors are **correlated**, not independent: a checker sharing the
   doer's blind spot is an **echo-chamber** that adds **zero information** (`verify` collapses into
   *declare*). Independence — the property that lets stacked checks drive error → 0 (→ `reliable`) — is
   **never total**; a **common-mode floor** remains that no iteration crosses (even formal proof only
   *relocates* the shared blind spot to the spec). **Irreducible to #4:** #4 is the *marginal* fact
   (each errs); reflexivity is the *joint* fact (errors correlate). **Unlike #1–#8 (facts about the
   problem/reality), this is a fact about the *solver*** — a **second-order** stone — and it **only bites
   in the automated, autonomous, multi-agent pipeline:** with a human-in-the-loop the §4/§5
   **escape-hatch** is a partially-independent terminal and reflexivity stays bounded; remove the human
   (an executor staffing `escalate`/`decide` too) and independence at the terminal → 0, so **an autonomous
   loop cannot be its own ground truth.** *(Admitted iteration 31, T5 — the first second-order stone.)*

> **Self-test the model uses:** if a needed element rests on *no* stone, a stone is missing;
> if a stone has *no* element defending it, there is a gap. The model passes for **first-order stones
> 1–8** (unconditional) and admits a **conditional second-order #9 (reflexivity)** for the autonomous
> case, which forces **independence-seeking** in `check`/`reflect` (the non-removable external/human
> terminal · adversarial review — §6 `red-team`, doing double duty with #8). **The second direction has
> fired twice:** the security gates rested on *no* stone → they exposed #8; and the loop's own checker
> rested on an *unguaranteed* independence → it exposed #9.
>
> **Licensed exception — the base act (§10.10).** The first direction exempts **`implement`** (and its
> seam-analogue **`release`**): it is not a *response* to a stone but the **operand the loop controls** — the
> plant, not the controller. A control loop must have something to control, and that something rests on no
> difficulty (it *is* the thing made difficult, §10.7's inward leaf). The exception makes the self-test
> *sound* rather than flag a false positive.

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
- **Escape hatch:** escalation ultimately ends at a human — the loop's one *independent* terminal. Stone
  #9 (§3) makes this load-bearing: **remove the human (full autonomy) and the checker's independence → 0**,
  so an autonomous loop cannot be its own ground truth.
- **"Definition of done"** = the target the `check` compares against — *a threshold on a
  quality range, not a yes/no*. It is *composite*:
  - **scope** sets the boundary (*how much / which items*),
  - **specify** sets correctness (*what's right*), across the **set of potential
    realities** → which is how one act sets targets for all three properties:
    expected reality → reliability, adverse realities → resilience, all enumerated up
    front → predictability.

**Loop behaviour → property:** converges → reliable · bounded → predictable · nests &
escalates → resilient · **preempts** (adversarially self-searches) → **secure**.

## 5. The fractal — the loop nests at every scale

The same shape repeats **in both directions**. *Outward* across scope — **design** (forced by
complexity) carves the whole into parts, and each part becomes its own loop, which *is* the
nesting; and *inward* into every element — addressing a single
element (e.g. specify) is itself a full define → do → check → reflect loop with its own
graded target and metric/proxy. **Two planes, then:** the *beats* (define → do → check →
reflect) are scale-invariant — the same four recur at every level; the *elements* (specify …
decide) are the **outermost** loop's staffing of those beats, re-instantiated by finer
activities at each level down. A stuck inner loop escalates to the loop above; the
outermost escape hatch is a human. *(Under full autonomy that independent terminal is gone — stone #9, §3.)*

```
action ⊂ feature ⊂ stage ⊂ release ⊂ product       ← outward (scope)
every beat ⊃ its own define → do → check → reflect → inward (each element)
```

**The inward nesting has a base case (§10.7).** A node whose forcing stone (§3) is absent collapses to
bare `do` — no `check`, no `reflect` (a keystroke can't be *wrong* in a way worth a loop). So the fractal
bottoms out on **both** axes: *outward* at a leaf `check` can judge without splitting (§10), *inward* at a
stone-free node. The only overrides that forbid the inward collapse are the **hard gates** (§10.4 — a
non-local violation) and **non-convergence** (a step judged trivial that keeps failing reveals a hidden
stone → re-expand).

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
| **define** | design (carves the decomposition) | complexity > one step |
| **do** | implement | (the build itself) |
| **check** | verify (build-time) | humans & models err |
| **check** | observe (run-time) | reality is uncertain |
| **reflect** | analyze — frame + root-cause the gap | humans & models err |
| **reflect** | decide — accept (known issue) or re-target | unbounded vs finite |
| **repeat over time** | version · integrate (CI/CD) · regression-test | reality keeps changing |

> **`decompose` folded into `design` (iteration 18).** Both once rested on stone #3; but
> `design`'s output *is* the decomposition, the fractal re-applies the loop to each part it
> carves, and `reflect → re-target(design)` (shift-left) carries any implement→design
> complexity feedback. A separate `decompose` did no work the loop wasn't already doing and
> owned no artifact — so it was vestigial. `do` is now execution-only.

**Cross-cutting — the resilience repertoire (not beats).** Invoked from `reflect` at any
element and any scale; realised mostly at run-time. Each is forced by a resilience stone, and
together they manufacture the **resilient** property:

| response | what it does | concrete example | forced by |
|---|---|---|---|
| **escalate** | hand up when bounded tries are exhausted; ends at a human | retries for one email domain keep failing → page on-call | loop can't converge |
| **degrade** | fail partial, not total (error handling / graceful degradation) | email provider down → queue the request + "arriving shortly" instead of a 500 | reality is uncertain |
| **recover** | spares · replicas · retries so the function survives a failure (redundancy) | second email provider takes over when the primary fails | reality is uncertain |
| **roll back** | revert to the last known-good state | new reset-email template spikes bounces → redeploy the previous one | reality keeps changing |

> **Compact form (T9, §10.8).** One **structural up-exit** — `escalate` (leaves the loop → parent / human
> terminal) — versus three **in-place** trades for liveness: `degrade` (completeness), `recover`
> (spares/redundancy), `roll back` (newness). `degrade`/`recover` are the **#6 context pair**; **`roll back`
> + `regression`** (build-time) are the **#5 time pair** (§10.8). And `regression-test` (elements table
> above) is the forced **`reflect → verify` bridge** — the *executable* time-face of the §10.5
> reflect-artifact — not a standalone element.

**Cross-cutting — the security repertoire (not beats), forced by stone #8 (adversarial actors).**
Where the resilience repertoire withstands *random* adverse reality (#5/#6), the security repertoire
withstands a *directed* adversary who hunts the worst case. Also invoked at every element and scale,
spanning design → build → run-time:

| response | what it does | concrete example | forced by |
|---|---|---|---|
| **authenticate / authorize** | prove identity + gate every action by least-privilege | signed-in ≠ allowed; check permission per request | adversary impersonates / escalates |
| **sanitize / validate** | narrow every boundary contract; never trust external data (the premise-B **narrow-lever** aimed at an attacker) | parameterized queries (SQLi) · output-encode (XSS) · CSRF tokens | adversary injects via untrusted input |
| **minimise surface / harden** | least exposure; secrets in a vault; no info-leak in errors | secrets from Keychain; generic error messages | adversary probes any exposed weakness |
| **threat-model / red-team** | search for your *own* worst case *before* the adversary does | pen-test; abuse-case review at design | adversary is a directed optimiser |

> **The seam with §10.2:** `sanitize/validate` *is* the premise-B **narrow-lever** — but here its
> floor is set by an *attacker*, not by natural variance, which is *why* "never trust external data"
> is a **hard gate** and not merely advisory.

> **Double duty with stone #9 (§3):** `threat-model / red-team` is also the response to **reflexivity** —
> an *independent, adversarial* checker deliberately not sharing the builder's assumptions is exactly what
> breaks the doer↔checker correlation. Same response, two sources: #8 (external attacker) and #9 (internal
> shared blind spot). This is why an autonomous pipeline must inject independence deliberately (diverse /
> adversarial reviewers, a human terminal) — it has no free escape-hatch to fall back on.

## 7. The process flow (with nested loops)

```
discover → define → design → plan
   → BUILD     [feature loop:  do  ⇄  check vs graded 'done'  →  reflect  ↺ re-target ]
   → verify    (stage gate against 'done')
   → release
   → OPERATE   [runtime loop:  observe  ⇄  recover / degrade / roll back / escalate   ↺ watch ]
   ⟲ PRODUCT LOOP:  operate → learn → evolve target → back to discover   (the Ouroboros)

solid = forward flow (the lifecycle)   ·   dashed = loops / feedback (at every scale)
```

> **§7 is a *projection* (§10.10), not new primitives.** These stages are the §6 elements laid on wall-clock
> at product scale — a *view*. `plan` = `scope`+`specify` on the time axis (a **schedule bet**, §10.10);
> `implement`/BUILD = the **base act**; `release` = the build→operate **seam** (its #5 governance = §10.8 /
> T3); OPERATE = a **phase-loop** (observe + repertoire, now incl. `roll back`); evolve = the **Ouroboros**.
> Only the control-elements are stone-defended primitives — reading nine stages as nine primitives
> double-counts.

## 8. The complete circuit (synthesis)

The four properties are **emergent**, not installed — manufactured by a system of bounded,
nested feedback loops, themselves built from elements forced by brute facts.

```
        ┌────────────── evolve  (feedback) ◄──────────────────────────┐
        ▼                                                             │
  reliable     predictable      resilient        secure   ◄── 4 properties (emergent)
     ▲              ▲               ▲                ▲
 converges       bounded     nests+escalate     preempts   ◄── loop behaviours
     └──────────────────── THE LOOP ─────────────────┘
              (set target → do → check → reflect ↺)
                          ▲  force
   bedrock:  intent-hidden · finite · complex · we-err · change · uncertain · distributed · adversarial
             · [#9 reflexivity — 2nd-order, autonomous only → erodes reliable]

   point-properties: reliable · predictable   |   envelope-properties: resilient (vs random #5/#6) · secure (vs directed #8)
```

## 9. The artifacts — what each loop leaves behind

Stone #7 (**knowledge is distributed & perishable**) forces every loop to hand its information
across **two boundaries**: *time* (perishable → defeated by **persistence**) and *agent*
(distributed → defeated by an **explicit, external** form). An **artifact** is exactly the
**persistent, explicit carrier** of a loop's target / result / lesson across those two
boundaries — shared understanding is the *output*, distribution is the *fact*, and the artifact
manufactures the shared, durable copy a head cannot.

There is **one artifact per beat**, plus **two for the cross-cutting machinery** (the over-time
loop and the resilience repertoire):

| beat / cross-cut | elements it carries | artifact | crosses *time* (persist) | crosses *agent* (make explicit) |
|---|---|---|---|---|
| **define** | specify · scope · design | **spec / target doc** ("definition of done") — incl. `design`'s **interface contracts + composition hypothesis**, executable-as-stubs (§10.1) | outlives the moment it was framed | a different builder can build from it |
| **do** | implement | **code** | persists as the running system | a different maintainer can read it |
| **check** | verify · observe | **tests + telemetry** — *tests* = `verify`'s build-time carrier (#4); *telemetry* = `observe`'s run-time sensor (#6), the loop's own detector (§10.6, may **not** be outsourced to the user) | a repeatable, re-runnable check | someone else can run & interpret it |
| **reflect** | analyze · decide | **reflect-output** = **ADR** (the written composition hypothesis, §10.1) + **post-mortem** (the failure lesson) — *one category, one carrier per boundary-face* (§10.5) | **post-mortem** carries the lesson to the *next iteration* | **ADR** carries the *why* to a *later root-causer* |
| **repeat over time** | version · integrate · regression | **version history** | *is itself* the durable time-axis | bisect / blame across contributors |
| **resilience repertoire** | escalate · degrade · recover · roll back | **runbooks** | know-how outlives the on-call who learned it | whoever's paged next, not just the first responder |

- **The loop-level hand-off is the same two crossings at fine grain:** whenever one loop passes
  its target/result to the next (or to a parent/child loop), it is persisting + making explicit
  — an artifact in miniature.
- **Why per-beat, not per-element:** a beat is the smallest unit whose output must survive a
  boundary. `design` shares the `define` beat's spec/target doc rather than owning a *separate*
  one — but its **load-bearing content within that artifact is the interface contracts + the
  composition hypothesis** (§10.1, R2); that is *not* the same as owning no artifact. (A standalone
  `decompose`, by contrast, added no content the loop wasn't already carrying, so it was folded
  away — see §11.)
- **Forced-durability scales with boundary-distance — and `reflect` is the extreme case (§10.5).** A
  forward beat's output is consumed by the *next beat in the same iteration* (spec→code→test): producer
  and consumer are **adjacent**, so the hand-off can be *live* and the written artifact merely **insures**
  the output against boundaries it might cross later. `reflect` alone feeds **backward** — its only
  consumers are a *later agent* doing root-cause (the **ADR**, the *agent* face) and a *future
  iteration*'s `define` (the **post-mortem**, the *time* face), both across a stone-#7 boundary **by
  construction**. So for `reflect` the artifact is not insurance but the **sole channel**: omit a forward
  artifact and a future re-reader is inconvenienced; omit `reflect`'s and the output reaches *no one*.
  **General law: the durability an artifact is *forced* to carry scales with the producer→consumer
  boundary-distance** — adjacent ⇒ optional-but-insuring; backward / cross-iteration ⇒
  mandatory-as-sole-channel. (This is the law the artifacts diagram should show — janitorial **T10**, §11.)
- **This is the flush of stone #7:** artifacts are not convention or process hygiene; they are
  *logically forced* the moment a loop's information must cross a boundary it cannot cross in a
  head.

## 10. The mechanism of Done — how each element's target is set

§4 said a Done is a *graded threshold on a quality range*; §5 said every element is a loop with
"its own graded target." This section derives **how that per-element target is actually set** —
and shows the mechanism is software-independent.

**Origination → propagation → termination.**
- **Origination (the root).** The top Done has no parent to inherit from; it is **elicited from
  hidden intent by `specify`** (stone #1). This is the one *contingent seed* — it cannot be
  derived, only drawn out.
- **Propagation (internal nodes).** `design` decomposes a parent Done *P* into child Dones
  {L₁…Lₙ}, one per element, each cast on the **universal four-axis schema** — *scope · reliable
  · resilient · predictable* (the same composite §4 forced at the top; it is **scale-invariant**).
  So `Done(element) = Done(parent), decomposed onto this element's slice`.
- **Termination (the leaf).** Decomposition stops where a Done is checkable *without further
  decomposition* — its `check` yields a **binary verdict** (`measured ≥ threshold`); the grading
  bottoms out into pass/fail. Two leaf kinds: **deterministic** (logic → an assertion / unit
  test) and **statistical** (an irreducible proxy → a threshold on a *sampled* value, "done with
  confidence ≥ c"). The statistical leaf is where stones #6 (uncertain) and #5 (change) keep the
  check from ever being purely deterministic — the a-posteriori residue of §11 made concrete.

**The composition hypothesis (load-bearing).** To decompose *P* into {Lᵢ} is to *assert* a
conjecture:

> **(L₁ ∧ L₂ ∧ … ∧ Lₙ) ⟹ P** — "if every part is done, the whole is done."

This is **not a deduction**; it is a **hypothesis** `design` makes, and where *P* is qualitative
("feels trustworthy," "is intuitive") it rests on **human judgment**. So *decomposition and
proxy-construction are the same act*: the conjunction of leaf Dones **is a constructed proxy**
for the parent Done, inheriting every proxy pathology from §11 (Goodhart, reality-contingent,
intent-drift). "All units pass" is a proxy for "the feature works"; the gap is the residue.

**Bottom-up verification & failure routing.** Leaves are checked directly (binary). A composite
is done iff (a) its leaves pass *and* (b) the composition hypothesis holds — the latter confirmed
at qualitative nodes by **human acceptance**. If a composite **fails acceptance while its leaves
are green**, the parts kept their promise but the whole did not → the **composition hypothesis is
falsified**. `analyze` root-causes to *that hypothesis*; `decide` **re-targets `design`** to
re-decompose — *not* the leaves. This is "non-convergence points at the target, not the build"
(§4), now **localized** to the decomposition.

**Traceability forces the hypothesis to be an artifact.** To trace a composite failure *back* to
the hypothesis that licensed the decomposition, that hypothesis must be **written** — it is the
crux of the `design` / ADR artifact (§9). Left unwritten (as it usually is), the failure is
untraceable. Stone #7 once more: persist it + make it explicit, or lose the trace.

**So — can Done be generalized regardless of the software? Yes, along a clean seam:**
- **Universal (form):** the four-axis schema, the *elicit-root → decompose → bottom-out*
  mechanism, the composition-hypothesis structure, and the *failure-routes-to-the-hypothesis*
  rule. All forced by the stones.
- **Contingent (content):** the specific thresholds, which proxies, and *which decomposition*
  `design` bets on. Only the **root** is elicited; every internal Done is **derived by
  decomposition** — yet each decomposition injects a fresh, judgment-laden hypothesis.

### 10.1 Design-as-a-bet — the composition hypothesis is cheaply, one-sidedly falsifiable (iteration 21)

If the composition hypothesis `(∧Lᵢ) ⟹ P` is design's central artifact, then **`design` is not
"draw the structure" — it is "state and defend a bet"**: a decomposition into components, the
**interface contracts** between them, and the conjecture that they compose to *P*. The reframe's
force is that this bet is **cheaply and one-sidedly falsifiable *before* the build**, via
**stub-composition**.

- **Stub-composition (the design sub-loop's own `check`).** Replace each component with a **stub**
  — its interface contract with the *behavior deleted* (right shape, computes nothing) — and check
  the stubs wire together. This is the `check` beat of the **`design` sub-loop** (the fractal, §5):
  a genuine check, yet still **a-priori** with respect to the outer build. It is **shift-left**
  (§12) aimed at the composition hypothesis itself — the earliest, cheapest place to execute the bet.
- **It discharges the *arrow*, suspends the *premises* — a conditional proof.** A green
  stub-composition tests only the **⟹** (that the contracts are *mutually coherent* — what A emits
  is what B accepts, across the graph). It is **assume-guarantee reasoning**: each stub is the
  "guarantee" half of a contract; composing them checks the guarantees *link up* while taking the
  guarantees themselves **on credit**. It is one-sided — it can only **fail cheap** (kill a bad
  decomposition) or **survive**; it never *confirms*.
- **It factors risk; it does not reduce it.** After a green stub-check, provably **zero** design
  risk lives in the wiring, and **all** of it has been relocated into two named, attackable premises:
  - **Premise A — the leaves are real** (each stub ≈ the real component). Discharged at
    **build-time `verify`** (a unit test on the real leaf) → the §10 **deterministic leaf**.
  - **Premise B — the contract holds across its *whole* value-domain** ("all permutations and
    combinations" over the interface = §4's **set of potential realities** at the seam: expected →
    reliable, adverse → resilient, enumerated → predictable). Only **sampled** at build (property
    tests), residue caught at **run-time `observe`** (telemetry) → the §10 **statistical leaf**.
- **Why stub-composition reaches *neither* premise — the single reason.** It is an **a-priori** act
  in `define`, and a **stub is a proxy for a component that does not exist yet**. Both premises are
  claims about *behavior* — the one thing a stub deletes by construction — so neither becomes a
  *fact* until the real thing is built and run. Both therefore **collapse into one root**: the
  **stub↔real (proxy↔real) gap**, unmeasurable until the real exists. This is exactly §11's seam
  (**`specify`/`define` a-priori: reason about the risk; `verify`/`observe` a-posteriori: measure
  what turned out true**) and the **proxy** thread (§10): the stub↔real gap is the
  **reality-contingent residue** of §11 — the proxy↔intent map running through reality not yet observed.
- **Where it sits in the machinery.** Stub-composition is the layer *above* Done-propagation: its
  **failure routes straight back to `design`** (re-decompose — "non-convergence points at the
  target," now at design-time), and its **survival hands the two premises *down*** to the
  deterministic (`verify`) and statistical (`observe`) leaf-checks of §10.

**R2 resolved.** §9 said `design` owns no *separate* artifact; §10 said the composition hypothesis
*must* be written — no contradiction once stated precisely: the design artifact **is** part of the
define-beat spec/target doc, and its load-bearing content is exactly **the interface contracts +
the composition hypothesis, written in a form executable as stubs**. Unwritten, a composite failure
can't be traced back to the decomposition that licensed it (§10, traceability); written-and-
stubbable, the bet is *runnable* and fails cheap.

### 10.2 The two quality bars of a good bet — "fails cheap" + "tightest-sufficient contracts" (iteration 22)

§10.1 gave design's *first* quality bar (**fails cheap**: the wiring bet is one-sidedly falsifiable
by stub-composition). The **premise-B lever** gives the *second*. Premise B — "the contract holds
across its whole value-domain" — is **not a fixed cost**; its *size* is something `design`
**chooses**, by how tight it draws each interface contract.

- **A tight contract manufactures `predictable` at the seam.** Premise B's residue *is*
  unpredictability at the interface (the unforeseen permutations), so §2's apex property
  `predictable` reappears *locally* at every contract. Tightening dials premise B between the §10
  leaf-kinds: **loose** → a domain too big to exhaust (**statistical leaf**, sampled at `observe`,
  residue > 0); **tight** → a domain small enough to exhaust (**deterministic leaf** at `verify`,
  residue → 0); **type-encoded** → illegal values can't be *constructed* (discharged **a-priori**,
  never reaching run-time). Contract-tightness sets how much of premise B is pre-paid
  deterministically at design-time vs. left as a-posteriori residue.
- **The contract governs the WHAT, not the HOW** — it constrains the leaf's observable I/O while
  leaving its interior free, which is exactly why a *stub* can stand in (keep the WHAT, drop the
  HOW) and why premises A and B were separable at all. Encapsulation, first-principled.
- **There is a floor, so the bar is *tightest-sufficient*, not *tightest*.** Even with free,
  infinite prediction, tightening past the **set of realities the leaf must serve** (§4) rejects a
  *valid* input the real need sends → the leaf returns the wrong thing / nothing on a legitimate
  reality → **`reliable` breaks** (and on the *adverse-but-valid* realities, **`resilient`**). The
  contract's domain must equal the **required set of realities — no wider** (needless premise-B
  residue) **, no narrower** (excluded reality → unreliable).
- **Synthesis — all three §2 properties re-instantiate at every seam.** The contract's *floor*
  (which realities MUST cross) = **reliable** (expected) + **resilient** (adverse); its *downward
  pressure* (how foreseeably they cross) = **predictable**. The optimum contract is **maximal
  predictability subject to admitting the whole required set of realities** — §2's three-property
  tension, projected onto the interface.

**So a good design bet meets two bars:** (1) **fails cheap** — the composition hypothesis is
stub-falsifiable (§10.1); (2) **tightest-sufficient contracts** — every interface as predictable as
possible without excluding a required reality, minimising the premise-B residue handed to `observe`
(§10.2).

### 10.3 Secure re-instantiates at every seam too — the forbidden-output wall (iteration 26)

§10.2 showed reliable · resilient · predictable reappear at every interface (the contract's **floor**:
which realities MUST cross). `secure` is the **complement, on the output side**: not "admit the whole
required *input* set" but "**forbid the whole illegal *output* set**" — a **wall / ceiling** dual to the
floor. So every seam's Done is **four**-axed, and the apex-vs-recursive question closes: `secure`
recurses exactly like the other three, along *both* axes (the §5 element-fractal **and** the §10.2 seam)
— because the decomposition tree's nodes *are* its seams.

- **It fails at the *composition* node, green leaves and all — the security composition-hypothesis.**
  A design can be insecure *no matter how correctly each leaf is built*: the flaw is in the
  **decomposition**, not the parts. Worked example — storing a credential in a repo `.env` (plaintext)
  and `.gitignore`-ing it: each leaf is green (the reader works; git *does* exclude it), yet the whole
  leaks the instant an **un-modelled egress** opens — a full-disk backup syncing the working tree to
  Drive before an OS upgrade. The forbidden output (secret readable at rest, off-box) is **reachable**,
  so the hypothesis `(∧Lᵢ) ⟹ secure` is **falsified with green leaves** → root-cause to the
  *decomposition*, **re-target `design`** (`.env` → Keychain). This is §10's "green-leaves-but-rejected
  composite" rule on the **secure** axis — proof `secure` lives at the **design / composition** node,
  not only in the leaves. (MITM is the same shape at the *network-topology* seam; SQLi is the
  leaf-level, build-stage instance.)
- **So it staffs every beat, like the other three:**

| beat | `secure` instantiation | the forbidden output it walls |
|---|---|---|
| **specify** | abuse-cases / elicit the **forbidden set** (the negative of the user story) | "must never leak PII / escalate privilege" |
| **scope** | **minimise attack surface** — every feature admitted is surface to defend (YAGNI as a control) | the unused endpoint that becomes the way in |
| **design** | a **secure decomposition** — the composition wall (the `.env` / topology example) | secret at rest · unauthenticated path |
| **implement** | injection-safe code (parameterise · output-encode) | SQLi · XSS |
| **verify** | **red-team / SAST / pen-test** — where `preempts` actually *executes* | any reachable breach, found before ship |
| **observe** | IDS · audit log · anomaly detection — the adversary is **live** and **adapts** (#8 × #5) | a breach in progress |
| **reflect** | incident response — root-cause to the **breached seam**; `decide` may **not** waive | a repeat of the same class |
| **evolve** | patch · rotate secrets · **security-regression** on every integrate | a newly-published CVE |

- **Why the recursion is *forced* — harder than for the other three.** The opponent is a **directed
  optimiser that enters at the least-defended seam**, so security of the whole is the **weakest link**,
  not the average. A single undefended stage is not a *local* degradation (as one weak leaf is for
  reliability) — it is the *whole* envelope's hole, because the attacker *finds* it and pivots. So
  `secure` cannot be defended "mostly": it holds at **every** seam or it does not hold. (And the `.env`
  leak was *accidental*, yet still a security defect — #8 assumes the residue **will** be found, so
  "unlikely to sync to Drive" is not "walled": the directed optimiser collapses the probability the
  random sampler #6 would have discounted.)

### 10.4 The hard gate — a non-compensatory leaf (iteration 27)

§10 gave `decide` three exits (**accept** a known issue · **re-target** · **escalate**). A **hard gate**
is a leaf where the **accept** exit is *deleted*. The model now says exactly *when* a leaf earns that:
**iff a single violation is *non-local* — no amount of green elsewhere buys it back (non-compensatory).**
Three amplifiers make a violation non-local:

1. **Adversarial (#8)** — a directed optimiser turns *any* hole into a whole compromise. Amplification is
   **guaranteed**, which is why **all** of `secure` is hard, wholesale (§10.3).
2. **Irreversible** — the damage escapes `recover`/`rollback` (data loss; a *leaked* secret can't be
   un-leaked), so the run-time repertoire can't undo it after the fact.
3. **Machinery-degrading** — the violation blinds the loop's own `check`/`observe`, or couples leaves so
   one corrupts another: a swallowed error (no signal), an un-instrumented call (no telemetry), a
   retrofitted test (can't falsify), a mutation (shared-state coupling). Non-local *by construction* —
   it disables the very thing that would have caught it.

**This resolves the parked question.** `secure` is **not** the only non-gradable property — it is the
only one hard **wholesale**; `reliable`/`predictable` stay graded *except* at their irreversible or
machinery-degrading leaves. Non-compensability is the general phenomenon; a *guaranteed* amplifier is
what promotes a whole property to hard.

**The predictive rule (the whole R5 residue, derived not asserted).** To classify *any* candidate
constraint, ask: **"is a single violation *non-local* — adversary-amplified, irreversible, or does it
blind the loop?"** Yes → **hard gate** (delete `decide`'s *accept*). No → **graded target** (keep
`decide`'s discretion). Corollary: a *graded proxy* mis-declared a gate (e.g. a coverage % — a
statistical-leaf proxy, §10 / §12) invites Goodhart; and a hard gate with **no amplifier** behind it is
mis-typed. This rule is exactly what the ideal stack uses to decide *which* leaves are gates.

> **Scope note (iteration 28).** This canvas derives the **ideal MUST-HAVE** stack only. Auditing any
> *concrete* setup against it — labelling real rules, finding a given stack's undefended stones or
> vestigial ceremony — is a **separate exercise**, deliberately kept out so the ideal stays
> uncontaminated by what a setup happens to have. The *general* questions such an audit surfaces
> (proxy-vs-gate, the change-axis machinery, observability-as-sensor) live as open tracks in §11.

### 10.5 `reflect` is the forced-MUST-HAVE beat — its artifact is the loop's only *backward* channel (iteration 29)

**T1, closed.** The question was: *what must the ideal `reflect` produce, and is that output forced
non-optional?* Answer: `reflect`'s output — the **reflect-output** artifact of §9 (**ADR** + **post-mortem**)
— is a **forced MUST-HAVE**, gated by the **machinery-degrading** amplifier (§10.4). The proof runs the
artifact's *absence* in the two directions `reflect` feeds, and both break as the **same** failure.

- **Within the loop — the *agent* crossing.** A composite fails acceptance with **green leaves** (§10): the
  parts kept their promises, so the fault is in the **composition**, not any leaf. Root-cause is therefore
  *"recover the composition hypothesis `(∧Lᵢ)⟹P` and find which assumption it lost"* — that hypothesis is
  the **sole** object `analyze` has (green leaves say where the fault *isn't*, never where it *is*).
  Unwritten, it was **intent-hidden** at birth (#1) and **perished** at the design-moment (#7), so `analyze`
  has **no input** — not a *slower* root-cause but a **starved** one (the symptom fits a dozen lost bets and
  nothing on hand separates them). `reflect` can't run its analyze half; it **collapses into `check`** ("we
  know it broke," not *why*).
- **Into the next loop — the *time* crossing.** The same failure-class returns. With no durable post-mortem
  the loop meets it as novel and re-pays the whole discovery cost (re-trigger → re-analyze — *if it even
  can* → re-decide): it **re-derives instead of remembering**. And the Ouroboros **evolve** edge (§7/§8),
  which re-targets `define` from accumulated lessons, has reflect-output as its **only** feed — unfed, the
  loop **cannot raise its own floor**. The recurrence is not bad luck but **structural**: a circle, not a
  spiral.
- **Same failure, not a coincidence — one stone, two faces.** §9/#7 forces artifacts because a loop's
  information must cross **time** (perishable) *and* **agent** (distributed) — §3 spells #7 as exactly those
  two faces. The two directions *are* those faces: the **ADR** is the agent-face carrier (design-moment →
  analyze-moment), the **post-mortem** the time-face carrier (this iteration → next). Deleting reflect's
  artifact re-opens **precisely the two gaps stone #7 says are always open unless an artifact bridges them**
  — one transient-output failure, refracted through the two boundaries of one stone.
- **Why forced *hardest* — the backward-feed proof (the §9 boundary-distance law at its extreme).** Every
  forward beat can hand its output off **live** to the next beat in the same iteration, so its artifact
  merely *insures* against later crossings. `reflect` is the **only backward-feeding beat**: its consumers
  (a later root-causer; a future `define`) are across a #7 boundary *by construction*, so its artifact is
  the **sole channel**, not insurance — omit it and the output reaches **no one**. *Backward-feeding ⟹ every
  consumer is across a #7 boundary ⟹ the artifact is mandatory.* This is the very asymmetry that makes
  `reflect` the loop's only *learning* beat: what loops backward is exactly what must be made durable.
- **Classification (via §10.4).** The harm is not one bad local artifact; it **disables the loop's own
  correcting machinery** — `analyze` can't root-cause a composite, `evolve` can't raise the floor. That is
  amplifier #3 (**machinery-degrading**, "disables the very thing that would have caught it") to the letter:
  skipping the artifact silently demotes `define→do→check→reflect` to **`define→do→check`** — a loop that can
  **detect** failure but neither **explain** it (dir 1) nor **prevent its recurrence** (dir 2). One skipped
  artifact costs not one lesson but the **beat**. Non-compensatory ⇒ `decide`'s **accept** is deleted ⇒
  **hard gate**. *(Secondary amplifier on the agent side: the **capture window is irreversible** — the
  hypothesis perishes at the design-moment (#7), so unlike a re-runnable test the chance to persist it never
  returns.)* §10.3's `reflect` row already gated this **wholesale on the secure axis** ("`decide` may **not**
  waive | a repeat of the same class"); T1 generalizes that instance to `reflect`-as-such.

### 10.6 `observe` is the forced sensor — telemetry detects the a-posteriori residue no test can reach (iteration 30)

**T4, closed.** T4 pressed the **T1 coupling** and it held with a twist. `analyze` (root-cause) is a
**comparison** — *intended vs actual* — the same shape §12 gives `verify` ("can't verify against
nothing"). T1 forced the *intended* operand (the ADR/bet, §10.5); T4 forces the **actual** operand — the
**run-time telemetry** `observe` emits — and telemetry turns out to do **two jobs**, so its absence bites
**one beat further upstream** than the ADR's.

- **The failure class `observe` owns has no test, by construction.** `verify` (build-time, stone **#4**)
  checks the composition hypothesis against the realities *enumerated at build*; anything it can catch
  fails *before* ship. `observe` (run-time, stone **#6**) exists for the **a-posteriori residue** —
  premise-B's unmodelled realities (§10.1), the Goodhart / reality-contingent / intent-drift gaps (§11)
  that `verify` **provably cannot** reach. So for the failure `observe` is the sensor *for*, there is **no
  build-time test**: if one existed it would have failed at build and never shipped.
- **Without telemetry the loop is blind, not merely un-diagnostic.** Worked example: an unhandled network
  timeout renders a blank page. `verify` is green (it never modelled the timeout — an adverse reality that
  should have tripped `degrade`, §6, but didn't). Who knows it broke? The **end user** — but *the user
  knowing ≠ the loop knowing.* Their pain is a signal trapped in a head (stone #7 again: perishable +
  distributed, no artifact); it reaches the loop only if they **report** it — lossy ("it's broken"),
  delayed, *usually never* (they churn). So the fallback sensor for `observe`'s whole class is **the
  users' suffering**: detection becomes *probabilistic* (silent churn), *non-diagnostic* (no WHY), and it
  crosses the agent boundary with nothing written. **Telemetry is the loop building its own `observe`
  instead of outsourcing detection to whoever gets hurt.**
- **Two jobs ⇒ two beats blinded.** Telemetry is (a) `observe`'s **input**, so it is what lets the
  run-time `check` fire at all → **THAT** it broke; and (b) `analyze`'s **actual operand** → **WHY** it
  broke. The ADR starved *one* beat (`analyze`); missing telemetry blinds `observe` **and** starves
  `analyze` — same amplifier (**machinery-degrading**, §10.4, which names "un-instrumented call (no
  telemetry)"), one step deeper: *you cannot diagnose a failure you never detected, and you cannot detect
  the residue without the sensor.*
- **Classify by the stone, not the station.** `verify` and `observe` are **both** the `check` beat; filed
  by *where they run* they look interchangeable, which is the trap ("a check will catch it"). Filed by the
  **stone each defends** they are non-substitutable — `verify`/#4 (*did we build what we specified?*) is
  structurally **blind** to `observe`/#6 (*did reality match what we modelled?*). This is T4's second
  claim, and it is the antidote to the substitution slip.
- **The coupling, pressed to the floor — senses vs memory.** ADR and telemetry are not two separate
  "floors"; they are the **two operands of one comparison** in `analyze` (intended · actual), and that one
  diff feeds *both* re-target (this loop) and evolve (next loop). So: **T1 forced the loop's *memory*
  (reflect-output); T4 forces the loop's *senses* (observe/telemetry).** §11 already says the loop exists
  *only* because of an irreducible a-posteriori residue (else it collapses to a single forward pass); to
  handle that residue it needs an organ to **sense** it and one to **remember** it, and *sense ⊳ diagnose
  ⊳ remember* — telemetry is upstream of the ADR. Remove either organ and the loop slides back toward an
  open forward pass: **blind** (no T4) or **amnesiac** (no T1). This closes the `observe`/#6 "thin climax":
  `observe` is the sense-organ for the very residue that makes the loop a loop.
- **What is forced vs. what is graded (the gate's shape).** The **forced MUST-HAVE** is that `observe`
  **owns a real sensor of its own** — the loop may not outsource detection to the user; an *empty*
  `observe` is machinery-degrading. But *how much* to instrument is a **graded target** (more coverage =
  higher confidence, diminishing returns) — an instance of the T2 proxy-graded-not-gated pattern — with
  **hard gates only at non-compensatory seams** (a path whose *silent* failure is irreversible,
  adversary-amplified, or itself machinery-degrading, §10.4). So `observe`-instrumentation is **not**
  wholesale-hard like `secure` (§10.3): the *existence* of the sensor is the forced floor; its *coverage*
  is graded, gated only where blindness is non-local. [Deferred deep-dive: **T11**, §11.]

### 10.7 The inward base case — ceremony is reducible where the stone is absent (iteration 32)

**Backported from the design doc's Ch 6.4.** The fractal (§5) nests *inward* — each element is its own
`define → do → check → reflect`. Ch 6.4 forced the cost question: *is that full ceremony always
MUST-HAVE?* Derived answer: **no.** A beat is a **response to a stone** (§3); where the stone is absent
for a node, the beat it forces adds **zero information**, and running it is pure cost — so the inner loop
**collapses toward bare `do`.** This *generalizes* the loop's known collapse (§11/§12: "degrades toward a
single forward pass") from the `reflect`/`observe` pair to **all four beats**:

- `specify` collapses when the target is already unambiguous & singular (no #1) · `scope` when the whole
  fits budget uncut (no #2) · `design` when the work is atomic — one step, no parts (no #3).
- `verify` collapses when the step is provably correct / cheap-to-redo (no #4) · `observe` when reality is
  fully modelled — no residue (no #6).
- `analyze` collapses when it converges first-try — no gap (no #4) · `decide` when exactly one exit is
  possible (no #2).
- The residue is **bare `do` = `implement`**, the base act that defends no stone (T7) — the **inward leaf**.

**Two base cases, one per fractal axis (duals).** *Outward* depth already terminates in §10 (split stops
at a leaf `check` can judge without splitting). *Inward* ceremony stops here (run a beat only while its
stone bites). The fractal hits bedrock on both.

**The collapse is itself a `decide`.** Ceremony is **insurance**: weigh its cost against
`P(undetected error) × cost(error)`, and skip the premium when the covered loss is small or improbable —
the same *tightest-sufficient* move as §10.2 (pay just enough to admit the required realities → *run just
enough loop to cover the residual risk*). A **graded** target (§10.4) is precisely one whose premium is
negotiable.

**Two overrides delete `accept` / forbid collapse** (both already derived):

1. **Hard gate (§10.4)** — a *non-local* violation (adversary-amplified · irreversible ·
   machinery-degrading). The adversary removes the "low-stakes / cheap-to-redo" premise, so `secure` work
   (§10.3) can't be reduced. Self-referential gates: skipping `observe` (§10.6) or the written
   `reflect`-artifact (§10.5) is *itself* machinery-degrading — beats about the loop's **own machinery**,
   non-waivable at any cost.
2. **Non-convergence (§4).** A step judged trivial that keeps failing falsifies the judgement "no stone
   bites here" → a hidden stone is present → **re-expand**. Non-convergence-as-signal now also polices the
   reducibility bet.

**Net — ceremony is proportional, not fixed:** pay it where a stone bites, buy it down where none does,
*except at the gates,* where a single miss is uncompensable and the premium is not yours to negotiate.
This supplies **T2** its general frame (**graded ⇒ collapsible ceremony · gated ⇒ non-waivable**); the
fine-grained *which-seam-is-gated* classification stays the open residue (T2 / T11).

### 10.8 The change-axis machinery — regression (memory-ratchet) & rollback (reversibility net) (iteration 33)

**T3, closed.** Stone #5 (change) bites the over-time loop in **two** time-faces, forcing two dual organs —
the #5 counterpart of the #6 pair `degrade`/`recover` (§6).

- **Face 1 — change re-opens closed holes.** Every later `do` (#4) can silently re-introduce a fixed
  failure-class *F*. Run §10.5 on this face: the fix's lesson perishes (#7) unless persisted, and a *prose*
  post-mortem is a **passive** memory that degrades to "re-derive, not remember" under continuous change. To
  fire **automatically on every future iteration** it must be persisted not as prose but as a **re-runnable
  check** — the post-mortem's WHY compiled into `verify`. That is a **regression test**: *the executable
  time-face of the §10.5 reflect-artifact* — the forced **`reflect → verify` bridge**, not a new element (cf.
  the `decompose → design` fold). It **accumulates monotonically** (each *F* adds a guard, none dropped): the
  ratchet that makes fixes *stick*, turning the Ouroboros from a **circle into a spiral** (§10.5). **Gate:**
  the ratchet's *existence* is a **hard gate** — deleting the loop's memory-of-fixes is **machinery-degrading**
  (§10.4), inheriting §10.5's gate exactly (**not** irreversibility); its *coverage* is a **graded** proxy
  (Goodhartable → T2), hard only at non-compensatory seams (the §10.6 shape).
- **Face 2 — change lands on a live system.** A bad deploy/migration degrades a *currently-working* system,
  and the fault is *in the new artifact itself*, so the #6 in-place responses miss (redundancy just runs more
  copies of the bad version; degrade just serves less of the broken thing). The only restoring move is
  **backward in version-space — rollback**: forced by #5 (change lands live) + #6/#4 (harm is a-posteriori,
  §10.6) + #7 (a live system's value is *perishable* — breakage accrues cost every moment, and the
  forward-fix is too slow to stop the bleed).

**Rollback ⟺ the irreversibility amplifier are dual.** §10.4 *defines* that amplifier as "damage escapes
recover/**rollback**," so **irreversibility ≡ the region beyond rollback's reach.** Hence:
- **Reversible** (rollback reaches it) ⇒ a bad outcome is recoverable ⇒ `decide` keeps its **accept**
  discretion ⇒ **graded** (the §10.7 insurance: rollback makes `cost(error)` small ⇒ negotiable premium).
- **Irreversible** (rollback's reach ends — destructive migration · secret exposure · sent message ·
  irreversible payment) ⇒ the insurance has lapsed ⇒ **accept** deleted ⇒ **hard gate**, discharged as a
  *pre-execution* control (backup · reversible-migration check · staged rollout · confirmation).

So **rollback itself is a *graded* repertoire response; the hard gate falls at rollback's *limit*.** The
§10.4 irreversibility amplifier gets its concrete home here.

**The inversion (the sharpest result).** The two organs point opposite ways along the same time axis and
gate via *different* amplifiers: **rollback keeps *code changes* reversible** (gate at its irreversible
*limit*); **regression keeps *lessons* irreversible** (gate on the ratchet's *existence*,
machinery-degrading). You want bad changes not to stick and good fixes not to un-stick — which **corrects
T3's own guess** that both halves gate "via irreversibility": only rollback's does.

**They manufacture `resilient`'s "over time" clause (§2).** The 2×2: contexts/#6 → withstand `degrade`,
recover `recover`; over-time/#5 → recover **rollback**, stays-recovered **regression**. Without regression
the envelope is *momentary* — it leaks every time change re-opens an old hole; regression is what makes it
*hold over time*. **Stations:** regression fires in **BUILD/verify** (the integrate gate); rollback fires in
**OPERATE** (run-time). *(Optional corollary — reversibility-as-design-investment: since rollback's reach
**is** the graded region, the ideal loop **widens the reversible envelope** — expand-contract migrations ·
flags · immutable deploys — to shrink the irreversible-gate residue: the change-axis "tightest-sufficient"
(§10.2) / "fails cheap" (§10.1).)*

**T9 (resilience-repertoire compact form), folded in.** The four responses have a 2-part structure:
**escalate = the one *structural up-exit*** (it leaves the loop → parent / §4 human terminal; forced by
"loop can't converge"), while **degrade · recover · roll back = *in-place*** — three axes of graceful
degradation distinguished by *what they trade for liveness*: degrade trades *completeness* (#6), recover
trades *spares/redundancy* (#6), roll back trades *newness* (#5). degrade/recover are the **#6 context
pair**; rollback (+ regression, at build-time) the **#5 time pair**.

### 10.9 Observability coverage — the silent-failure gate & telemetry's every-seam emission (iteration 33)

**T11, closed** (§10.6 deferred this deep-dive to here; three candidate promotions are parked as forks in
§11). §10.6 fixed the *shape* — `observe` must own a sensor (existence forced, machinery-degrading), while
*how much* to instrument is graded, gated only at non-compensatory seams. The depth, in three parts:

- **(a) The gate rule is §10.4 with one substitution — "silent failure" for "violation."** The object
  classified is not "the path fails" but "the path fails *and emits no telemetry*." A seam's instrumentation
  is a **hard gate iff its silent (un-observed) failure is non-local**, via the three amplifiers under that
  substitution: **irreversible-seam** (the unseen loss *compounds while unseen* — detection-latency *bounds*
  it; the sensor is the only lever between the first unit of loss and an unbounded one), **adversarial-seam**
  (a security-relevant signal — auth · privileged action · trust-boundary — **inherits** `secure`'s wholesale
  every-seam wall (§10.3): the blind spot *is* the attack surface), **machinery-seam** (a path carrying the
  loop's *own* control signal — sensor health · gate-firing · escalation trigger — whose silent failure
  **blinds the loop to its own blindness**). *Test:* "failed + emitted nothing → irreversible /
  adversary-amplified / self-blinding?" **Else graded** — coverage ∝ `P(silent failure) × cost`, collapsible
  to zero where #6 is absent (§10.7: nothing to detect on a fully-modelled, reversible, local path).
- **(b) Emission character is forced by the carried fact's temporal type.** The ADR (§10.5) carries a
  **static point-fact** (the design bet, true/false at *one* moment; #7 forces capture *then*, but **one
  write suffices permanently**) → **one-shot, single-locus**. Telemetry carries a **dynamic envelope-fact** —
  "does reality keep matching the model?" — which #5/#6 **regenerate on every execution** and whose location
  is **unknown a-priori** (that is what "a-posteriori" means) → **continuous, every-seam**. So each
  un-instrumented path is a *standing* blind spot, re-exposed every run — giving observe-coverage `secure`'s
  **every-seam form** (§10.3), but for a *different reason*: not a directed optimiser *hunting* the hole, but
  the residue *landing* on the path you didn't model. The **opponent** splits the verdict — across the
  majority it is a **blind sampler** (#5/#6 → `resilient`-shaped → **graded**, point-gated only where rule (a)
  makes it non-local); at the security seams of (a) it is **directed** (#8) and collapses to `secure`'s
  **wholesale** wall. "Instrument once" is *category-incoherent*: the fact to be sensed did not exist at
  instrument-time.
- **(c) Coverage-% is a Goodhartable statistical-leaf proxy** for the true target — "can we actually *detect
  the residue* when it surfaces?" The two come apart: 100 % "coverage," still blind — the signal is *wrong* (a
  log that says "entered function," not "output correct-for-intent"), *unmonitored* (emitted, but nothing
  alerts on it — a log no one reads is #7 again), or *drowned* (alert fatigue). So **gate the *per-seam
  binary* signal** ("does named seam *S* emit detector-grade signal σ?" — a deterministic, binary fact about
  a named path, from rule (a)) and **grade the *aggregate* — never gate the roll-up** (gating "≥ 90 %
  coverage" diverts effort to the *cheap* paths and starves the residue-bearing ones rule (a) says to gate).
  This is the concrete resolution of **T2**'s long-open "deterministic-gate vs must-stay-graded-proxy" seam,
  for observability: **gate the per-seam binary, grade the aggregate.**

### 10.10 The lifecycle is a projection; a plan is a schedule bet (iteration 33)

**T7 + T8, closed.** Two results — what §7 *is*, and what `plan` *is*.

- **`implement` is the base act; §7 is a projection (T7).** Every §6 element earns its seat by neutralising
  one stone (specify←#1 · scope←#2 · design←#3 · verify/analyze←#4 · observe←#6 · decide←#2 · version←#5).
  `implement` is the **sole exception** — its "forced by" column reads *"(the build itself)."* This is **not**
  a self-test violation: the stones make *governing* an act hard and force the scaffolding beats built
  *around* it; `implement` **is that act** — the **operand the loop controls** (the plant, not the
  controller), which rests on no difficulty because it *is* the thing made difficult (§10.7's inward leaf).
  So the §3 self-test's first direction (*element on no stone ⇒ a missing stone*) gets **one licensed
  exception — the base act** — which makes the test *sound* rather than flag a false positive. The §7
  lifecycle is then the §6 elements **projected onto wall-clock at product scale**, in execution order — a
  *view*, not new primitives, with **four node-kinds**: *control-elements* (discover/define/design/verify →
  §6), the *base act* (BUILD → `implement`), a *seam* (`release`, the build→operate hand-off — the base
  **transition**, whose governance is the derived #5 machinery of §10.8, → T3), a *phase-loop* (OPERATE →
  observe + repertoire), and the *Ouroboros* (evolve → reflect@product). Only control-elements are
  stone-defended primitives; reading nine stages as nine primitives double-counts.
- **A plan is a schedule bet (T8).** §2's `predictable` conflates three things. Boundedness (§4) buys only
  **cost-predictability** (the loop terminates within a bound); **outcome**-predictability is bought by tight
  contracts (§10.2); **schedule/timing** — "call *when* it ships" — is an **aggregate over the time axis**
  (the *envelope* family's axis), **not** the §2 *point*-property, so it needs its own mechanism. That
  mechanism is a **schedule bet**, the time-axis twin of the design bet (§10.1): `plan` decomposes the
  deliverable *over time* into time-boxed tasks + milestone contracts and asserts **`(∧ task i lands in slot
  tᵢ) ⟹ ship S by D`** — the `(∧Lᵢ) ⟹ P` shape, new axis. Two identities fall out: **an estimate is the stub
  of a task** (shape/duration kept, work deleted), and **critical-path / capacity feasibility is
  stub-composition on the time axis** — a-priori, one-sided (infeasible → re-plan · or internally-consistent,
  never confirming delivery). It factors risk into **premise A** (each estimate real → checked per-task at
  completion, verify-like; #4) and **premise B** (the schedule holds across the whole space of futures →
  residue at OPERATE velocity/slip, observe-like; #5/#6); failure ⇒ **re-plan** (re-target). So `plan` is
  **`scope`+`specify` projected onto the time axis** — no new stone ⇒ **no new element** (exactly as
  design-as-a-bet revealed the *character* of #3's `design` without minting a primitive). The **forecast** is
  this bet's premise B (`predictable`'s a-priori face, the twin of `specify` for `reliable`); the
  **commitment** is the written schedule bet as a #7 artifact crossing the agent boundary so others can plan
  around it. **Gate:** its *existence as a written baseline* is a **hard gate** (no baseline ⇒ a slip is
  *undetectable* — "on-time" was never recorded — blinding the loop's own schedule-check ⇒
  machinery-degrading, the §10.5 argument); its *content* (the dates) is a **graded** statistical-leaf proxy
  (hard-gating a forecast invites Goodhart — cut scope/quality to "hit the date"; T2). **plan : predictable
  :: ADR : reliable.**

**The convergent law (found independently by tracks T3, T11, T7/T8).** Across the **ADR** (`reliable`,
§10.5), **telemetry** (`observe`, §10.6/§10.9), the **regression ratchet** (`resilient`, §10.8), and the
**plan** (`predictable`, above), the *same* shape recurs: the forced artifact's **existence is a hard gate**
(its absence is machinery-degrading — it blinds the loop's own `analyze`/`check`), while its **fidelity /
coverage / content is a graded, Goodhartable proxy**. The intended-operand that `analyze` compares against
must **exist** (non-waivable) but need only be **as accurate as the residual risk warrants** (negotiable).
**plan : predictable :: ADR : reliable :: regression : resilient :: telemetry : observe.** (Promoted to §12.)

## 11. Current frontier & next steps

**Recent arc (historical; through iteration 22 — newer work 23–28 is in the §13 log):** the **premise-B lever & design's two quality bars** (§10.2)
— a good bet must (1) *fail cheap* (§10.1) **and** (2) carry **tightest-sufficient contracts**:
tightening a contract manufactures `predictable` at the seam and dials premise B
statistical→deterministic→a-priori, but the **floor is `reliable`** (tighten past the required set of
realities and a valid input is rejected) — so *tightest-sufficient*, not tightest; all three §2
properties re-instantiate at every interface. Before that (21): the **design-as-a-bet reframe** (§10.1)
— `design` states
a bet (interface contracts + composition hypothesis) that **stub-composition** falsifies cheaply and
one-sidedly, discharging the wiring (⟹) and **factoring** the risk into premise A (leaves real →
`verify`/deterministic leaf) and premise B (whole value-domain → `observe`/statistical leaf); the
single reason it reaches neither is that it is a-priori and a stub is a *proxy* for a not-yet-built
real (§11 seam + proxy thread); **R2 closed**. Before that (19): derived the **mechanism of Done** (§10) — an
element's target is *inherited by decomposition* from its parent (root elicited by `specify`),
bottoming out in binary leaf-checks; each decomposition asserts a *composition hypothesis*
`(∧Lᵢ) ⟹ P` that is really a proxy, and a green-leaves-but-rejected composite *falsifies that
hypothesis* → re-target `design`. Earlier (18): the artifacts (§9), the `decompose` fold, and the
interactive fractal/process-flow diagrams.

**Decisions locked in:**
- **`correct` → `understand` → `reflect`.** The fourth beat is *diagnosis + judgement*:
  **analyze** (frame the issue — e.g. "loop can't converge" — and root-cause it) then
  **decide** — accept the gap as a *known issue*, or **re-target** (re-iterate into the next
  **define**). Escalation is the cross-cutting third exit.
- **All elements are verbs now** (specify · scope · design · implement · verify · observe ·
  analyze · decide), to match the action each names.
- **`decompose` removed (folded into `design`).** Two elements rested on stone #3; but
  `design` already outputs the decomposition, the fractal applies the loop to each part, and
  `reflect → re-target(design)` (shift-left) carries the implement→design feedback — so a
  standalone `decompose` was vestigial. `do` is now execution-only (`implement`).
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

**Open-tracks register (consolidated, iteration 28).** Every thread opened and not yet closed,
deduplicated into one list. `active` = current derivation · `open` = queued · `janitorial` = cleanup ·
`descoped` = deliberately out of scope. (Historical "next frontiers" prose folded into the §13 log.)

_Active frontier_
- **— between tracks (iteration 31).** **T5 closed** → admitted as **stone #9 (reflexivity, §3)**: a
  *conditional, second-order* stone (about the *solver*, not the task) that bites only in the **automated
  autonomous multi-agent** pipeline. A correlated checker is an **echo-chamber** (zero information;
  `verify` → *declare*); **independence** is what lets stacked checks drive error → 0, and reflexivity is
  the brute fact that it is never total — irreducible to #4 (joint vs marginal). Rippled through
  §2/§3/§4/§5/§6/§8/§12. **Pending question for the user: which track is next?** Candidates below (T2 · T3 ·
  T6 · T11), plus structural T7–T10. **· Iteration 32:** added **§10.7 — the inward base case / reducibility
  law** (advanced **T2**). **· Iteration 33 (parallel sub-agent fold-in):** closed **T3** (§10.8 change-axis —
  regression + rollback), **T11** (§10.9 observability silent-failure gate) and **T7/T8** (§10.10
  lifecycle-projection + plan-as-schedule-bet); folded **T9**; surfaced the **existence-hard / fidelity-graded**
  convergent law (§12). **Active frontier now → T6 (bedrock pressure-test):** a full derivation draft is ready
  (sub-agent, iteration 33) and is **held for the user's decision** — the one track deliberately *not* folded
  in, because it would renumber the bedrock and formalize a 'second-order' stone class. Remaining janitorial:
  **T10** (artifacts / rollback-node diagram).

_Open derivation frontiers_
- **T2 · Proxy-leaves: graded by default, gated only at non-compensatory seams** *(open; ex-G1,
  generalized; sharpened by T4)*. A *proxy* quality bar (coverage · NPS · latency ≈ intent) is a
  **statistical leaf that stays gradable** (`analyze` checks proxy-vs-intent; an absolute gate invites
  Goodhart) — **except** where a single miss is non-local (§10.4), which earns a hard gate. **T4/§10.6
  confirmed this exact shape for observability** (instrument-coverage graded, gated only at
  non-compensatory seams). Still to pin down in general: the precise seam between a deterministic-leaf gate
  and a must-stay-graded proxy. [§10 leaf-kinds; §10.4 amplifiers; §12 proxy thread. Observability
  instance: **T11**.] **Iteration 32 (§10.7) supplied the general frame** — graded ⇒ ceremony collapsible ·
  gated ⇒ non-waivable; the residual *which-seam-is-gated* classification was **resolved for observability by
§10.9** (iter 33 — gate the per-seam binary, grade the aggregate); the fully-general cross-domain seam
classification remains the light residue.
- **T3 · Stone #5 (change): the regression + rollback machinery** *(**closed — iter 33 → §10.8**; ex-G3)*.
  **Answered — yes, both: the #5 time-axis pair.** Regression = the executable §10.5 artifact
  (existence-hard / coverage-graded); rollback = the reversibility net (graded, hard gate at its irreversible
  *limit*); the two halves gate by *different* amplifiers. Original question: does the
  ideal **over-time** loop MUST-HAVE an explicit **regression-suite** (catch re-introduced defects) and
  **rollback** (revert to known-good), and are they **hard gates** (via the irreversibility amplifier?)
  or graded? [§6 resilience repertoire; §7 OPERATE; folds in janitorial T9.]
- **T4 · Observability as a first-class sensor** → **moved to _Active frontier_ (above), iteration 29.**
- **T5 · Reflexivity — the reflexive-executor / circular-verifier** → **moved to _Active frontier_
  (above), iteration 30.**
- **T6 · Bedrock pressure-test** *(open; partly done iter-23 & iter-31)*. Is any stone **reducible** to
  another? The **9th** sub-question is now **answered** — reflexivity was admitted as a *conditional
  second-order* stone #9 (T5, §3, iter-31). Still open: is any stone reducible; are there **further**
  candidates (*incentives*, *cost-asymmetry*); and is "second-order" a distinct **class** of stone worth
  formalizing? (#8 adversarial was the 8th, iter-23; #9 reflexivity the 9th, iter-31.)
- **T11 · Observability: graded coverage vs non-compensatory gates** *(**closed — iter 33 → §10.9**)*.
  **Open forks (candidate promotions, for the user):** (1) does the sensor-as-adversarial-target force a
  distinct **tamper-evidence / append-only** MUST-HAVE, or just inherit §10.3? (2) is *emission-character =
  the §2 property-family of the carried fact* a forced law or an analogy? (3) is the graded/gated frame
  stable, or does observability tilt wholesale if '#6-absent' is not knowable a-priori? §10.6 fixed the
  *shape* — `observe`-instrumentation is a **graded target** (how
  much to instrument) with **hard gates only at non-compensatory seams**. Still to derive in depth: (a) the
  **decision rule** for *which* seams are gated (whose silent failure is irreversible / adversary-amplified
  / machinery-degrading, §10.4); (b) telemetry's **emission character** — the ADR is one-shot (design-time)
  but telemetry is **continuous / every-seam** (each un-instrumented path a fresh blind spot), a shape
  closer to `secure`'s every-seam wall (§10.3); (c) the coverage metric is itself a **proxy** (Goodhartable),
  tying back to **T2**. The concrete observability instance of T2.

_Structural backlog (external-review R-series; resolved ones dropped)_
- **T7 · R1 · `implement` + lifecycle stages under-derived** *(**closed — iter 33 → §10.10**: base act +
  projection; `release` = the build→operate seam → T3)*. Carve `implement`
  out of the §3 self-test (it is the **base act**, defends no stone); annotate §7 as the lifecycle
  **projection** of the derived elements; derive the genuinely-orphaned `plan` / `release`.
- **T8 · R6 · planning / predictability under-derived — the orphaned `plan`** *(**closed — iter 33 → §10.10**:
  a plan is a *schedule bet* — a time-axis projection of scope+specify, not a new element)*.
  Boundedness buys only *cost*-predictability; outcome / timing needs a **forecast / commitment**
  mechanism. New element, or scope+specify over the time axis? Reshaped by design-as-a-bet: **a plan is a
  schedule bet.** [Pairs with T7.]
- **T9 · R3 · resilience-repertoire formula cleanup** *(**done — iter 33, folded into §10.8**)*. Compact form — escalate = the
  structural up-exit; degrade / recover / roll back = in-place; add rollback to §7 OPERATE. [Folds into T3.]
- **T10 · R7 · artifacts diagram under-draws crossings** *(janitorial → upgraded, iteration 29)*. No
  longer just "draw both crossings" — there is now a **law to show**: an artifact's *forced* durability
  scales with **producer→consumer boundary-distance** (§9/§10.5). Forward-adjacent beats hand off *live*
  (artifact = insurance); `reflect` feeds **backward**, so its artifact is the **sole channel**. The
  diagram should draw reflect's two backward edges (**ADR** → a later root-causer = agent-face;
  **post-mortem** → the next `define` = time-face) visibly crossing **both** boundaries, while forward
  edges stay in-iteration.

_Descoped (iteration 28)_
- **Map-model-onto-a-concrete-setup** — *removed by decision.* This canvas is the **ideal**; auditing a
  real stack (any Ouroboros / TDD / routing / gate configuration) against it is a **separate** exercise,
  kept out so the ideal is not entangled with what a given setup already has or lacks. Its still-useful
  *general* residue survives as **T2 / T3 / T4**.

_Closed (for the record)_ — **T3 (change-axis regression+rollback → §10.8, iter 33)** · **T7/T8
(lifecycle-projection + plan-as-schedule-bet → §10.10, iter 33)** · **T9 (repertoire compact form → folded
into §10.8, iter 33)** · **T11 (observability silent-failure gate → §10.9, iter 33; promotion-forks open)** ·
**T5 (reflexivity → conditional 2nd-order stone #9, §3, iter 31)** · **T4
(`observe` is the forced sensor — §10.6, iter 30)** · **T1 (`reflect` is a forced MUST-HAVE — §10.5, iter
29)** · R2 (design's artifact, §10.1) · R4 (§8 bedrock line, iter 23) ·
R5 (hard gates, §10.4) · "does #8 force a 4th property" (§2, iter 24–25) · "does secure recurse every
seam" (§10.3) · "is secure the only non-gradable property" (§10.4). Full history in §13.

## 12. Key laws & insights derived along the way

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
- **Done is set by decomposition, not invention (§10):** `Done(element) = Done(parent)`
  decomposed onto its slice, cast on the universal four-axis schema (scope · reliable ·
  resilient · predictable). Only the **root** is *elicited* from hidden intent by `specify`;
  every internal Done is *derived*. **Form is universal, content is contingent** — which is why
  Done generalizes across any software.
- **A leaf Done is a binary verdict:** grading bottoms out into pass/fail, from either a
  *deterministic* measurement (logic → assertion) or a *statistical* one (proxy → threshold on a
  sampled value). The statistical leaf is the a-posteriori residue made concrete.
- **Decomposition = proxy-construction:** splitting *P* into leaves {Lᵢ} *asserts* the
  hypothesis `(∧Lᵢ) ⟹ P`; that conjunction **is a proxy** for *P*, so it inherits Goodhart /
  drift. Where *P* is qualitative, the hypothesis rests on human judgment.
- **A green-leaves-but-rejected composite falsifies the composition hypothesis:** the defect is
  in the *decomposition*, not the leaves ⇒ `analyze` → `decide` re-targets `design`. This
  localizes "non-convergence points at the target." Traceability *requires* the hypothesis be a
  written artifact (design/ADR) — unwritten, the failure can't be traced back.
- **Metrics are often proxies; proxies invite Goodhart:** optimising the proxy can diverge
  from true intent ⇒ `reflect`/`observe` must check proxy-vs-intent, not just
  actual-vs-proxy.
- **The corrective responses are cross-cutting, not a beat:** escalate / degrade / recover /
  roll back are a repertoire invoked at any element & scale; together they *are* the
  resilient property's machinery.
- **The fractal runs *both* ways:** the loop nests up across scope *and* down into every
  element — and the *up* nesting is not a separate act: `design` carves the parts, each part
  recurses, so the nesting is *emergent*, not staffed by its own element.
- **Two elements on one stone is a redundancy smell:** `design` and `decompose` both rested on
  stone #3 (complexity); since `design`'s output *is* the decomposition and the re-target edge
  carries the late feedback, `decompose` was ceremony and folded away. This *sharpens the §3
  self-test*: not only *stone-with-no-element* and *element-with-no-stone*, but also
  *two-elements-on-one-stone-where-one-is-derivable*.
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
- **Design is a bet, not a drawing (§10.1):** `design`'s deliverable is the **composition
  hypothesis + interface contracts**, and its first quality is *how cheaply it fails when wrong*.
- **Stub-composition = cheap, one-sided falsification of the *wiring*:** stubs are contracts with
  the behavior deleted, so composing them is **assume-guarantee** reasoning that discharges the
  **⟹** and suspends the premises. It **factors** risk (after green: none in the wiring, all in
  {leaves, interface value-domains}) — it does not reduce it. It is the `check` beat of the design
  sub-loop (a-priori w.r.t. the build), i.e. shift-left on the composition hypothesis.
- **A stub is a proxy for a not-yet-built real:** so the stub↔real gap is **a-posteriori by
  construction** (§11 seam + proxy thread), which is the single reason stub-composition reaches
  *neither* premise. The two premises discharge at *different* stations — A (leaf real) at `verify`
  = **deterministic leaf**; B (whole value-domain / "all permutations") at `observe` = **statistical
  leaf** (§10).
- **Design has two quality bars (§10.1–10.2):** (1) **fails cheap** — the composition hypothesis is
  stub-falsifiable; (2) **tightest-sufficient contracts** — every interface as predictable as
  possible without excluding a required reality, minimising the premise-B residue handed to `observe`.
- **A tight contract manufactures `predictable` at the seam:** it dials premise B from a
  **statistical leaf** (loose → sampled at `observe`) to a **deterministic leaf** (tight → exhausted
  at `verify`) to **a-priori** (type-encoded → illegal values unrepresentable). Premise B's residue
  *is* unpredictability at the interface.
- **The floor is `reliable` (with `resilient` on the adverse slice):** tighten a contract past the
  **required set of realities** (§4) and it rejects a valid input → wrong-thing-on-a-legitimate-
  reality. So contracts are *tightest-sufficient*, not tightest — and **all three §2 properties
  re-instantiate at every interface**: reliable + resilient set *which* realities must cross (the
  floor), predictable is bought by tightening toward it.
- **specify-cuts vs scope-cuts — the infinite-resources test:** when you cut work, ask *"would I
  still cut it if resources were infinite?"* **Yes** → a **specify** cut (excluded because it's
  *not what's wanted* — stone #1, correctness). **No** (you'd include it given infinite time/money)
  → a **scope** cut (excluded *only* for finiteness — stone #2). Scope-cuts *vanish* under infinite
  resources; specify-cuts *survive*. Operationalises §4's composite Done (scope = boundary ×
  specify = correctness) — and shows scope's true sibling is **`decide`** (both stone #2: scope
  bounds *before*, decide bounds *after*).
- **Stone #8 — the adversary is a *directed optimiser* over premise B:** where #6 (uncertain)
  *samples* the value-domain at random, an adversary *searches* it for the worst case — so
  statistical defenses (redundancy · retries · graceful degrade) that beat #6 **fail** against #8
  (retries just feed a DoS; the attacker targets the exact residue). It forces its own **security
  repertoire** (authn/authz · sanitize · harden · threat-model, §6), irreducible to #6. Found by the
  §3 self-test firing *in reverse*: the security Hard Gates rested on **no stone** ⇒ a stone was
  missing. And `sanitize/validate` = the §10.2 premise-B narrow-lever with its floor set by an
  attacker — which is why "never trust external data" is a *hard* gate.
- **`secure` recurses at every seam as the *output-wall* (§10.3):** dual to the input-floor of the other
  three — floor = admit the required inputs (reliable/resilient), wall = forbid the illegal outputs
  (secure). It fails at the **composition node with green leaves** (a bad *decomposition* is insecure
  however well the leaves are built — the security composition-hypothesis), and is **forced** to hold at
  *every* seam because a directed optimiser enters at the **weakest link**: one undefended stage is the
  whole envelope's hole, so `secure` is **non-compensatory** in a way the other three are not.
- **A hard gate = a non-compensatory leaf (§10.4):** `decide`'s **accept** exit is deleted **iff a single
  violation is non-local** — amplified by a directed adversary (#8, guaranteed → `secure` hard wholesale),
  *irreversible* (escapes recover/rollback), or *machinery-degrading* (blinds a `check`/`observe`, or
  couples leaves). So **non-compensability — not "importance" — is what makes a rule a gate;** a graded
  proxy mis-gated (80 % coverage) invites Goodhart, and an undefended stone (#7 / `reflect`) was the last
  open risk — **now closed (§10.5): the reflect-artifact is that gate.**
- **`reflect` is the forced-MUST-HAVE beat — its artifact is the loop's only *backward* channel (§10.5):**
  every forward beat hands its output *live* to the next beat in the same iteration (artifact = insurance),
  but `reflect` feeds **backward** — its consumers are a *later* root-causer (the **ADR**, agent-face) and a
  *future* iteration's `define` (the **post-mortem**, time-face), both across a stone-#7 boundary by
  construction. So its artifact is the **sole channel**, not insurance: unwritten, a composite failure is
  untraceable (`analyze` **starved** → `reflect` collapses into `check`) *and* the same class recurs
  (`evolve` **unfed** → the loop can't raise its floor). Same failure, **two faces of one stone** ⇒
  **machinery-degrading (§10.4) ⇒ forced hard gate**, not documentation hygiene.
- **Forced durability scales with boundary-distance (§9):** how durable an artifact is *forced* to be is a
  function of the **producer→consumer boundary-distance** — adjacent (forward, same iteration) ⇒ a live
  hand-off, the artifact merely insures; backward / cross-iteration ⇒ the artifact is the **sole channel**,
  mandatory. `reflect` is the extreme case; this is the law the §9 / T10 artifacts diagram should show.
- **`observe` is the forced sensor; telemetry does two jobs (§10.6):** `analyze` is a *comparison* —
  intended (the ADR, §10.5) vs **actual** (telemetry) — so telemetry is both `observe`'s **detector** (lets
  the run-time `check` fire → *THAT* it broke) and `analyze`'s **actual operand** (*WHY* it broke). Absent,
  the loop outsources detection to the **end user** (probabilistic churn · non-diagnostic · no artifact —
  stone #7), blinding `observe` **and** starving `analyze` — machinery-degrading (§10.4) one beat further
  upstream than the ADR. **What's forced is that `observe` owns a sensor at all;** *how much* to instrument
  is graded (T2), hard-gated only at non-compensatory seams (T11).
- **Classify each element by the stone it defends, not where it runs (§10.6):** `verify` (#4) and
  `observe` (#6) are both the `check` beat but are **non-substitutable** — #4's build-time sensor is
  structurally blind to #6's a-posteriori residue. Filing by station ("both are checks") is the trap that
  makes you think a test will catch a run-time reality gap.
- **Senses vs memory — the T1↔T4 coupling (§10.6):** the loop exists only for the irreducible a-posteriori
  residue (§11), so it needs an organ to **sense** it (observe/telemetry, T4) and one to **remember** it
  (reflect-output, T1); *sense ⊳ diagnose ⊳ remember.* Kill either and the loop degrades toward a single
  forward pass — **blind** or **amnesiac**.
- **Reflexivity — the checker shares the doer's fault (§3 #9, second-order · autonomous):** a check's worth
  is the **information** it adds beyond the doer's own belief, so a checker whose errors are **correlated**
  with the doer's is an **echo-chamber** (zero bits; `verify` → *declare*). **Independence** — what lets
  stacked checks drive error → 0 (→ `reliable`) — is never total (even formal proof only relocates the blind
  spot to the spec). Irreducible to #4 (marginal error) because it is the *joint* fact (correlated error). It
  bites only in the **autonomous multi-agent** pipeline: the human escape-hatch (§4/§5) is a partially-
  independent terminal, so **an autonomous loop cannot be its own ground truth** — forcing independence-
  seeking (external/human terminal · adversarial/independent review, the §6 `red-team` doing double duty
  with #8). *First **second-order** stone: a fact about the solver, not the task.*
- **Ceremony is proportional insurance — the inward base case (§10.7):** each beat is forced by a stone
  (§3); absent that stone it adds no information, so the inner loop **collapses toward bare `do`**
  (generalizing "degrades toward a single forward pass" from `reflect`/`observe` to all four beats). Run
  loop-ceremony ∝ residual risk `P(error)×cost(error)` — *tightest-sufficient* again (§10.2). The fractal
  bottoms out on **both** axes: outward at a checkable leaf (§10), inward at a stone-free node. **Overrides
  that forbid the collapse:** hard gates (§10.4) and non-convergence (§4) delete the *skip/accept* exit.
- **The change-axis machinery — regression & rollback (§10.8):** stone #5 forces two dual organs.
  **Regression** = the §10.5 reflect-artifact made *executable* — a fixed failure-class persisted as an
  auto-firing, monotonically-accumulating `verify` check (the ratchet that makes fixes stick: circle →
  spiral); *existence* is a **hard gate** (machinery-degrading), *coverage* is **graded** (T2). **Rollback ⟺
  irreversibility are dual:** the §10.4 irreversibility amplifier is *exactly the region beyond rollback's
  reach*, so rollback is a **graded** response and the **hard gate falls at its limit** (reversible ⇒
  graded/insured bet; irreversible seam ⇒ pre-execution gate). Keep *code reversible* (rollback), keep
  *lessons irreversible* (regression) — together they manufacture `resilient`'s **over-time** clause.
- **Observability's silent-failure gate & emission character (§10.9):** instrument-coverage is graded, but a
  seam is **hard-gated iff its *silent* (un-observed) failure is non-local** — the §10.4 test with "silent
  failure" for "violation": irreversible-seam · adversarial-seam (inherits §10.3 wholesale) · machinery-seam
  (blinds the loop to its own blindness). **Gate the per-seam binary signal; never the aggregate coverage %**
  (a Goodhartable proxy) — the concrete resolution of T2. And **emission character follows the fact's
  temporal type:** a *static point-fact* → **one-shot / single-locus** artifact (the ADR); a *dynamic
  envelope-fact*, regenerated every run and location-unknown a-priori → **continuous / every-seam** sensor
  (telemetry). So observe-coverage wears `secure`'s every-seam *form* but a *blind-sampler* (#5/#6) opponent
  — `resilient`-shaped and graded — tipping to `secure`'s wholesale wall only at security seams.
- **The lifecycle is a projection; `implement`/`release` are base act & seam (§10.10):** §7 is the §6
  elements projected onto wall-clock at product scale — a *view*, not new primitives (four node-kinds:
  control-element · base act · seam · phase-loop · Ouroboros). `implement` (the operand the loop controls)
  and `release` (the build→operate seam) are stone-free in their own right, so **exempt from the §3
  self-test** (one licensed exception, which makes the test *sound*).
- **A plan is a schedule bet (§10.10):** `scope`+`specify` projected onto the time axis — **an estimate is
  the stub of a task; critical-path feasibility is stub-composition on time**; premise A per-task
  (verify-like), premise B whole-future (observe-like → re-plan). So **`predictable` = cost (bounded, §4) +
  schedule (the bet)**, the schedule half a time-axis projection, *not* the point-property. The **forecast**
  is the bet's premise B; the **commitment** is its #7 artifact.
- **Every forced artifact is existence-hard, fidelity-graded (§10.5/§10.6/§10.8/§10.10):** across the ADR
  (`reliable`), telemetry (`observe`), the regression ratchet (`resilient`), and the plan (`predictable`),
  the *same* shape recurs — the intended-operand `analyze` compares against must **exist** (its absence is
  machinery-degrading, blinding the loop's own `analyze`/`check` → **hard gate**), but need only be **as
  accurate as the residual risk warrants** (its fidelity/coverage/content is a Goodhartable proxy →
  **graded**). **plan : predictable :: ADR : reliable :: regression : resilient :: telemetry : observe.** A
  convergent law found independently by tracks T3, T11, and T7/T8 (iteration 33).

## 13. Iteration log (compressed)

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
18. Wrote the per-beat artifacts up as **prose (§9)** with a dedicated `pipeline-graph`
    diagram — closing a gap where iteration 17's log had *claimed* the artifacts were captured
    as diagrams, but the file only actually held the loop + circuit. **Folded `decompose` into
    `design`** (vestigial: shared stone #3, owned no artifact, and its job is subsumed by
    design's output + the fractal + the shift-left re-target edge); `do` is now execution-only.
    **Promoted the fractal (§5) and process-flow (§7)** ASCII into interactive diagrams — the
    canvas now carries **5 live diagrams**.
19. Derived the **mechanism of Done** (new §10): a per-element target is *inherited by
    decomposition* (`Done(element) = Done(parent)` on the universal four-axis schema), rooted in
    `specify`-elicited intent and bottoming out in **binary leaf-checks** (deterministic or
    statistical). Each decomposition asserts a **composition hypothesis** `(∧Lᵢ) ⟹ P` — itself a
    *proxy* for the parent, judgment-laden where *P* is qualitative — and a green-leaves-yet-
    rejected composite **falsifies that hypothesis**, routing `analyze` → `decide` back to
    `design`; traceability forces the hypothesis to be a written artifact. Resolved the
    generalization question: **Done's form is universal (from the stones), its content
    contingent.** Added a 6th interactive diagram (**Done propagation**).
20. Independently triaged an external review of an older canvas version into *accept /
    partly-obsolete / contentious* and recorded it as the **Review backlog (R1–R7)** in §11. Key
    finding: **R2 (design needs a durable artifact) is now a live §9↔§10 contradiction** — §9 says
    design owns no artifact, §10 says its composition hypothesis *must* be written. R2 & R6 fold
    into the design-as-a-bet reframe (next).
21. **The design-as-a-bet reframe (new §10.1).** Established that `design`'s artifact is a **bet** —
    a decomposition + **interface contracts** + the composition hypothesis — that **stub-composition**
    falsifies **cheaply and one-sidedly** *before* the build (assume-guarantee reasoning; the design
    sub-loop's own `check`; shift-left on the hypothesis). It **discharges the wiring (⟹) and suspends
    the premises**, thereby **factoring** risk: after a green stub-check none remains in the wiring and
    all is relocated to **Premise A** (leaves are real → `verify` / deterministic leaf) and **Premise
    B** (the contract holds across its whole value-domain / "all permutations" → `observe` / statistical
    leaf). The **single reason** stub-composition reaches neither: it is **a-priori** and a **stub is a
    proxy for a not-yet-built real**, so both behavioral premises collapse into one a-posteriori
    stub↔real gap — §11's `define`-a-priori / `verify`·`observe`-a-posteriori seam and the proxy thread,
    reconfirmed from the interface side. **Closed R2** (design's durable artifact = the contracts +
    hypothesis, written executable-as-stubs); updated §9 note + table row. Added a 7th interactive
    diagram (**Stub-composition**). Next: the **premise-B lever** — can `design` shrink the
    a-posteriori residue by narrowing/totalizing contracts?
22. **The premise-B lever & design's two quality bars (new §10.2).** Resolved the lever: Premise B's
    *size* is something `design` **chooses** by how tight it draws each interface contract. Tightening
    **manufactures `predictable` at the seam** and dials premise B between the §10 leaf-kinds — loose →
    **statistical leaf** (sampled at `observe`, residue>0); tight → **deterministic leaf** (exhausted at
    `verify`, residue→0); type-encoded → **a-priori** (illegal values unrepresentable, never reaching
    run-time). But there is a **floor**: even with free prediction, tightening past the **required set of
    realities** (§4) rejects a valid input → breaks **`reliable`** (and **`resilient`** on the adverse
    slice). So the second quality bar is **tightest-sufficient contracts**, not *tightest* — and **all
    three §2 properties re-instantiate at every interface** (reliable + resilient = which realities must
    cross = the floor; predictable = how foreseeably = the tightening). Design's bet thus meets two bars:
    **fails cheap** (§10.1) + **tightest-sufficient contracts** (§10.2). Added an 8th interactive diagram
    (**premise-B lever / tightness dial**). Next: the long-open **map-onto-real-setup** step, now with a
    sharp lens (contract/stub tests = wiring bar; unit = premise A/deterministic; property+integration+
    e2e+telemetry = premise B/statistical; type-tightness = premise-B reduction; hard gates = R5).
23. **Admitted Stone #8 — adversarial actors — the first bedrock change since it was "complete at 7."**
    The governance audit (element-walk) reached `build`: `implement` is the *base act* (R1, defends no
    stone), so the audit target was the Hard Gates around it. Two catches — (a) `handle-all-errors` (the
    *total* premise-B lever) and `input-validation` (the *narrow* lever) are both §10.2 premise-B
    reductions; (b) the **security cluster** (SQLi · XSS · CSRF · credential theft) rested on **no
    stone** → by the §3 self-test's second direction, *a stone is missing*. Named it **#8: adversarial
    actors** — a **directed optimiser** over premise B, distinct from #6's random sampling and #4's
    accidental error, and *irreducible* (its defenses — authn/authz · sanitize · harden · threat-model
    — don't fall out of redundancy/degrade). Forces a cross-cutting **security repertoire** (§6). Closed
    **R4** (added #7 + #8 to the §8 ASCII line) and updated §3 (self-test now 1–8) + the circuit diagram
    + §12 + header. Opened: does #8 force a **4th property (secure)**? (test the §2 way).
24. **Admitted the 4th apex property — `secure` — as `resilient`'s *sibling* (§2).** Resolved
    iteration 23's open question. The context-hardness axis §2 gave `resilient` has **two sources of
    hardness**: *random* (#5 change / #6 uncertain — a blind **sampler** of the context-space) and
    *directed* (#8 adversarial — a **search** for the worst case). Resilience is the envelope against
    the random; **security is the envelope against the directed** — *same shape, different opponent* —
    so `secure` is a **fourth seat beside `resilient`, not under it** (statistical resilience machinery
    fails on, and can even feed, a directed foe — §12). Recast §2 from three properties to **four in
    two families** (point: reliable · predictable; envelope: resilient vs random · secure vs directed);
    added the `secure` row + the two-sources framing; synced header + §11. Opened the breakdown:
    secure's **loop-behaviour** (the empty §4/§8 seat — candidate: adversarial self-search / red-team),
    the **independence proof** (resilient-but-insecure / secure-but-fragile), and the ripple into §4 + §8.
25. **Filled `secure`'s behaviour cell + rippled the circuit.** Named the loop-behaviour that
    manufactures `secure`: **preempts** — the loop *proactively* red-teams its own inputs, searching
    permutations/combinations for any that drive an output **outside the allowed set** (leaked secret ·
    DoS · forged/intercepted message — the CIA triad, reproduced from scratch), then forecloses them. It
    must be *proactive* (unlike resilient's *reactive* nest-&-escalate) because a directed searcher (#8)
    hits the exact premise-B residue a random sampler (#6) would miss. Proved **secure ⊥ resilient** the
    §2 way (resilient-but-insecure vs secure-but-fragile). Rippled: §4 behaviour line; §8 prose + ASCII +
    the "complete circuit" pipeline-graph (added `secure`/`preempts` nodes + edges); the §2 secure row.
    Behaviour→property map now complete for all four. Opened iteration-25 frontier: does `secure`
    re-instantiate at every seam as a **forbidden-output wall** — the §10.2 dual (reliable/resilient =
    input *floor*; secure = output *ceiling*)?
26. **`secure` recurses at every seam — the forbidden-output wall (new §10.3).** Resolved iteration-25's
    frontier: `secure` re-instantiates at every interface *and* every element, exactly like the other
    three, along both the §5 element-fractal and the §10.2 seam (the decomposition tree's nodes *are* its
    seams). It is the **output-side dual** of the input-floor — floor = admit the required inputs
    (reliable/resilient), **wall = forbid the illegal outputs** (secure) — so every seam's Done is
    **four**-axed. Key catch (user's `.env` example): a design can be insecure **with every leaf green** —
    the flaw is the *decomposition* (a repo `.env` leaks when a full-disk backup syncs the working tree
    off-box, though the reader works and git excludes it) → the **security composition-hypothesis**
    falsified → re-target `design` (→ Keychain); MITM = same at the network-topology seam, SQLi = the
    leaf/build instance. Walked `secure` across all beats (specify abuse-cases → scope surface → design
    decomposition → implement injection-safe → verify red-team → observe IDS → reflect IR → evolve patch).
    **Why forced everywhere:** a directed optimiser enters at the **weakest link**, so one undefended seam
    = the whole envelope's hole (non-local, unlike a reliability leaf). Added §10.3 + a §12 law; synced
    §11 + header. Opened: does weakest-link / non-compensatory ⇒ `secure` is a **hard gate** (R5 / the
    governance Hard Gates), the first hit of the map-onto-real-setup step?
27. **Mapped the model onto the governance Hard Gates (new §10.4) — the map-onto-real-setup step, opened.**
    Derived *when* a leaf becomes a **hard gate**: iff a single violation is **non-local**
    (non-compensatory), via one of three amplifiers — **adversarial** (#8, guaranteed → `secure` hard
    *wholesale*), **irreversible** (escapes recover/rollback — a leaked secret can't be un-leaked), or
    **machinery-degrading** (a swallowed error / un-instrumented call / retrofitted test / mutation blinds
    or couples the loop). **Answered iteration-26's parked test:** `secure` is not the *only* non-gradable
    property, just the only one hard *wholesale*. Mapped every governance Hard Gate onto the three
    amplifiers and ran the §3 self-test → four findings: **G1** 80 % coverage is a proxy mis-gated
    (Goodhart); **G2** stone #7 / `reflect` **undefended** (no ADR/post-mortem — reconfirms the iter-22
    reflect-thin audit); **G3** stone #5 / change lightly gated (no regression/rollback gate); **G4**
    LLM-routing-via-proxy is really the observability sensor + concurrency cap, not "infra." Derived the
    predictive rule (violation non-local? → gate, else grade). **Closed R5.** Next: derive the missing
    `reflect` gate (mandated ADR + incident post-mortem), then finish the stack walk.
28. **Redirected to the ideal, consolidated the open tracks, re-opened on `reflect`.** Per the user: this
    canvas derives the **ideal MUST-HAVE** SDLC *only* — the current-setup mapping is **not** mixed in.
    Stripped §10.4's concrete governance-gate table and its G1–G4 current-setup findings, keeping the
    **ideal law** (hard gate = non-compensatory leaf; three amplifiers: adversarial · irreversible ·
    machinery-degrading) + the **predictive rule**; added a scope note. **Consolidated** every still-open
    thread from the last several sessions into one deduplicated **Open-tracks register** (§11): **T1**
    `reflect` (active) · **T2** proxy-graded-not-gated (ex-G1) · **T3** change-axis regression+rollback
    (ex-G3) · **T4** observability-as-sensor (ex-G4) · **T5** reflexivity / circular-verifier · **T6**
    bedrock pressure-test · **T7** R1 implement+lifecycle · **T8** R6 orphaned `plan` · **T9** R3
    resilience-formula · **T10** R7 artifacts-diagram; **descoped** map-onto-concrete-setup. Set the
    **active frontier to T1 — derive `reflect` as a MUST-HAVE** (hypothesis: its artifact is forced
    non-optional because *unwritten ⇒ machinery-degrading ⇒ untraceable*, §10.4; and `reflect` is the
    loop's only *learning* beat, feeding the Ouroboros evolve edge). Relabeled §1 + subtitle to four
    properties; updated HANDOFF.md.
29. **Closed T1 — `reflect` is the forced-MUST-HAVE beat (new §10.5).** Ran the artifact-*absence* trace in
    the two directions `reflect` feeds and found both fail as the **same** failure. *Within-loop* (the
    **agent** face): a green-leaves composite (§10) can't be root-caused once the composition hypothesis
    (§10.1) is unwritten — `analyze` is **starved** (intent-hidden #1, perished #7) → `reflect` collapses
    into `check`. *Next-loop* (the **time** face): with no post-mortem the Ouroboros **evolve** edge (§7/§8)
    is **unfed** → the failure-class recurs and the loop can't raise its floor. Both are **one transient
    reflect-output failure through the two faces of stone #7** (agent = **ADR**, time = **post-mortem**) —
    not a coincidence. **Backward-feed proof:** `reflect` is the only beat whose consumers are *all* across a
    #7 boundary, so its artifact is the **sole channel**, not insurance ⇒ **machinery-degrading (§10.4) ⇒
    forced hard gate** (confirming the iter-28 hypothesis). Folded out the **general boundary-distance law**
    (forced durability ∝ producer→consumer distance) into §9/§12 and **upgraded T10** from "redraw" to "a law
    to show." Edits: refined §9 (reflect-output = ADR + post-mortem, one category per boundary-face), added
    **§10.5**, two §12 laws, moved **T1 → Closed** in §11, synced header. Frontier: **between tracks** —
    user picks next (lean T4 observability, the other half of the machinery-degrading amplifier).
30. **Closed T4 — `observe` is the forced sensor (new §10.6); pressed the T1 coupling.** `analyze`
    (root-cause) is a *comparison* — **intended** (the ADR, §10.5) vs **actual** (run-time telemetry) — so
    telemetry is `analyze`'s missing second operand. The twist: telemetry does **two jobs** — `observe`'s
    **detector** (lets the run-time `check` fire → *THAT* it broke) *and* `analyze`'s **operand** (*WHY*) —
    so its absence blinds `observe` **and** starves `analyze`, **machinery-degrading (§10.4) one beat
    upstream** of the ADR. Absent it, detection is outsourced to the **end user** (silent churn ·
    non-diagnostic · no artifact — #7); *user-knows ≠ loop-knows.* Established **classify by the stone each
    defends, not where it runs** (verify/#4 ≠ observe/#6, non-substitutable), and the coupling **T1 =
    memory / T4 = senses** (sense ⊳ diagnose ⊳ remember; both forced by the irreducible a-posteriori
    residue that makes the loop a loop — closes the `observe`/#6 thin climax). Fork decided: `observe` is a
    **graded target with hard gates only at non-compensatory seams** (not wholesale like `secure`) — *the
    sensor's existence is forced, its coverage is graded* — deep-dive **deferred as T11** (cross-links T2).
    Edits: new **§10.6**, §9 check-row, three §12 laws, §11 (T4→Closed, T2 sharpened, **T11** added), header.
    Frontier: between tracks.
31. **Closed T5 — admitted a conditional second-order 9th stone: reflexivity (§3 #9).** Pressed the
    reflexivity angle against the T1/T4 coupling (the executor reading the loop's memory/senses shares their
    defect). Crux: `check` is only worth the **information** it adds beyond the doer's belief, so a checker
    whose errors are **correlated** with the doer's is an **echo-chamber** (zero bits; `verify` collapses
    into *declare*). The property at stake is **independence** — what lets stacked checks drive error → 0
    (→ `reliable`); reflexivity is the brute fact that it is **never total** (a common-mode floor; even
    formal proof only relocates the blind spot to the spec). **Irreducible to #4** (marginal error vs the
    *joint* correlated-error fact) → clears the §3 self-test. Flagged **second-order** (about the *solver*,
    not the task — the first of its kind) and **conditional**: it bites only in the **automated autonomous
    multi-agent** pipeline — with a human escape-hatch (§4/§5) it stays bounded; remove the human and
    terminal-independence → 0, so **an autonomous loop cannot be its own ground truth.** Forces
    independence-seeking (non-removable external/human terminal · adversarial review — §6 `red-team`, double
    duty with #8). Rippled: §3 (stone #9 + self-test), header, §2 caveat, §4/§5 escape-hatch, §6 red-team
    note, §8 (bedrock line + circuit-diagram node/edge), §12 law. **Partly closes T6** (the "is there a 9th?"
    sub-question). T5 → Closed. Frontier: between tracks.
32. **Backported design-doc Ch 6.4 → the inward base case / reducibility law (new §10.7).** The user
    directed the two-worked-example expansion of the fractal in the *design doc* (rate-limiting = graded ·
    password-reset = hard-gated); its §6.4 asked whether the full four-beat ceremony is always MUST-HAVE.
    Derived: **no** — a beat responds to a stone (§3), so where the stone is absent for a node the beat adds
    **zero information** and the inner loop **collapses toward bare `do`** (`implement`, the base act, T7).
    This **generalizes** the loop's known collapse ("single forward pass," §11/§12) from `reflect`/`observe`
    to **all four beats**, and pairs the **inward** base case with §10's **outward** termination (the fractal
    bottoms out on both axes). The collapse is itself a `decide` — ceremony = **insurance**, premium ∝
    `P(error)×cost(error)`, the *tightest-sufficient* move of §10.2. Two overrides delete `accept`: **hard
    gate** (§10.4 — non-local violation; the `observe`/`reflect`-artifact self-gates included) and
    **non-convergence** (§4 — a trivial-looking step that keeps failing reveals a hidden stone → re-expand).
    Gives **T2** its general frame (graded ⇒ collapsible · gated ⇒ non-waivable). Edits: new **§10.7**, §5
    base-case pointer, §11 (T2 advanced + active-frontier note), one §12 law, header sync. Frontier: between
    tracks (T2 advanced; next T3 · T6 · T11).
33. **Parallel sub-agent fold-in — closed T3, T11, T7/T8 (+ T9); surfaced the existence/fidelity law.** Ran
    four tracks concurrently (one sub-agent each; T6 held for the user). Folded in three: **T3** (new
    **§10.8**) — stone #5 has *two* time-faces forcing dual organs: **regression** = the §10.5 reflect-artifact
    made *executable* (the `reflect → verify` ratchet; *existence* hard/machinery-degrading, *coverage* graded),
    **rollback** = the reversibility net, *dual to* the §10.4 irreversibility amplifier (**irreversibility ≡
    beyond rollback's reach**) so rollback is graded and the hard gate falls at its *limit*. Corrected T3's own
    guess (the two halves gate by *different* amplifiers). Folded **T9** (repertoire compact form: escalate =
    up-exit · degrade/recover/roll back = in-place). **T11** (new **§10.9**) — the gate rule is §10.4 with
    "silent failure" for "violation" (irreversible/adversarial/machinery seams); telemetry is
    continuous/every-seam (a *dynamic envelope-fact*) vs the ADR's one-shot *point-fact*; gate the per-seam
    binary, grade the aggregate (resolves T2 for observability). **T7/T8** (new **§10.10**) — `implement` is the
    base act & `release` the base seam (exempt from the §3 self-test); §7 is a *projection* of §6 onto
    wall-clock; **a plan is a schedule bet** (`scope`+`specify` on the time axis — estimate = stub of a task,
    critical-path = stub-composition on time; existence-hard/content-graded). **Convergent law** (found by all
    three): *every forced artifact is existence-hard, fidelity-graded* — **plan : predictable :: ADR : reliable
    :: regression : resilient :: telemetry : observe**. Edits: **§10.8/§10.9/§10.10**, six §12 laws, §7 OPERATE
    +rollback & projection note, §3 base-act exception, §2 predictable caveat, §6 repertoire note, §11
    (T3/T7/T8/T9 → Closed, T11 → Closed w/ forks, T2 sharpened, frontier → **T6 held** + janitorial T10),
    header. Frontier: **T6 (bedrock pressure-test) — derived draft ready, awaiting the user's call.**

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
    {"id":"secure","label":"secure","group":"property","x":880,"y":100},
    {"id":"converges","label":"converges","group":"beat","x":100,"y":215},
    {"id":"bounded","label":"bounded","group":"beat","x":360,"y":215},
    {"id":"nests","label":"nests & escalate","group":"beat","x":620,"y":215},
    {"id":"preempts","label":"preempts","group":"beat","x":880,"y":215},
    {"id":"loop","label":"the loop","group":"beat","x":360,"y":320},
    {"id":"intent","label":"intent hidden","group":"stone","x":-40,"y":440},
    {"id":"finite","label":"finite","group":"stone","x":120,"y":440},
    {"id":"complex","label":"complex","group":"stone","x":270,"y":440},
    {"id":"err","label":"we err","group":"stone","x":420,"y":440},
    {"id":"change","label":"change","group":"stone","x":560,"y":440},
    {"id":"uncertain","label":"uncertain","group":"stone","x":710,"y":440},
    {"id":"distributed","label":"distributed & perishable","group":"stone","x":880,"y":440},
    {"id":"adversarial","label":"adversarial actors","group":"stone","x":1060,"y":440},
    {"id":"reflexivity","label":"reflexivity (#9 · 2nd-order · autonomous)","group":"stone","x":-180,"y":40}
  ],
  "edges": [
    {"source":"intent","target":"loop","member":true},
    {"source":"finite","target":"loop","member":true},
    {"source":"complex","target":"loop","member":true},
    {"source":"err","target":"loop","member":true},
    {"source":"change","target":"loop","member":true},
    {"source":"uncertain","target":"loop","member":true},
    {"source":"distributed","target":"loop","member":true},
    {"source":"adversarial","target":"loop","member":true},
    {"source":"loop","target":"converges"},
    {"source":"loop","target":"bounded"},
    {"source":"loop","target":"nests"},
    {"source":"loop","target":"preempts"},
    {"source":"converges","target":"reliable"},
    {"source":"bounded","target":"predictable"},
    {"source":"nests","target":"resilient"},
    {"source":"preempts","target":"secure"},
    {"source":"reliable","target":"evolve"},
    {"source":"predictable","target":"evolve"},
    {"source":"resilient","target":"evolve"},
    {"source":"secure","target":"evolve"},
    {"source":"evolve","target":"loop","dashed":true,"label":"re-target"},
    {"source":"reflexivity","target":"reliable","dashed":true,"label":"erodes if autonomous (#9)"}
  ]
}
```

**The fractal** — the same loop nested *up* across scope and *down* into each beat (§5).

```pipeline-graph
{
  "title": "The fractal — one loop, nested both ways",
  "nodes": [
    {"id":"s_action","label":"action","group":"element","x":0,"y":0},
    {"id":"s_feature","label":"feature","group":"element","x":150,"y":0},
    {"id":"s_stage","label":"stage","group":"element","x":300,"y":0},
    {"id":"s_release","label":"release","group":"element","x":450,"y":0},
    {"id":"s_product","label":"product","group":"element","x":600,"y":0},
    {"id":"b_define","label":"define","group":"beat","x":150,"y":130},
    {"id":"b_do","label":"do","group":"beat","x":330,"y":130},
    {"id":"b_check","label":"check","group":"beat","x":510,"y":130},
    {"id":"b_reflect","label":"reflect","group":"beat","x":690,"y":130},
    {"id":"human","label":"human (escape hatch)","group":"terminal","x":880,"y":130},
    {"id":"c_define","label":"define","group":"element","x":150,"y":280},
    {"id":"c_do","label":"do","group":"element","x":330,"y":280},
    {"id":"c_check","label":"check","group":"element","x":510,"y":280},
    {"id":"c_reflect","label":"reflect","group":"element","x":690,"y":280}
  ],
  "edges": [
    {"source":"s_action","target":"s_feature","member":true,"label":"⊂"},
    {"source":"s_feature","target":"s_stage","member":true,"label":"⊂"},
    {"source":"s_stage","target":"s_release","member":true,"label":"⊂"},
    {"source":"s_release","target":"s_product","member":true,"label":"⊂"},
    {"source":"s_feature","target":"b_define","member":true,"label":"any scope = a loop"},
    {"source":"b_define","target":"b_do"},
    {"source":"b_do","target":"b_check"},
    {"source":"b_check","target":"b_reflect"},
    {"source":"b_reflect","target":"b_define","dashed":true,"label":"re-target ↺"},
    {"source":"b_reflect","target":"human","dashed":true,"label":"escalate → human"},
    {"source":"b_define","target":"c_define","member":true,"label":"any beat = a loop (downward)"},
    {"source":"c_define","target":"c_do"},
    {"source":"c_do","target":"c_check"},
    {"source":"c_check","target":"c_reflect"},
    {"source":"c_reflect","target":"c_define","dashed":true,"label":"re-target ↺"},
    {"source":"c_reflect","target":"b_reflect","dashed":true,"label":"escalate ↑"}
  ]
}
```

**The process flow** — the lifecycle, with the build loop, the operate loop, and the Ouroboros (§7).

```pipeline-graph
{
  "title": "The process flow (lifecycle with nested loops)",
  "nodes": [
    {"id":"discover","label":"discover","group":"element","x":0,"y":0},
    {"id":"define","label":"define","group":"element","x":140,"y":0},
    {"id":"design","label":"design","group":"element","x":280,"y":0},
    {"id":"plan","label":"plan","group":"element","x":420,"y":0},
    {"id":"build","label":"BUILD","group":"beat","x":560,"y":0},
    {"id":"verify","label":"verify","group":"element","x":700,"y":0},
    {"id":"release","label":"release","group":"element","x":840,"y":0},
    {"id":"operate","label":"OPERATE","group":"beat","x":980,"y":0},
    {"id":"recover","label":"recover","group":"repertoire","x":840,"y":135},
    {"id":"degrade","label":"degrade","group":"repertoire","x":980,"y":135},
    {"id":"escalate","label":"escalate","group":"repertoire","x":1120,"y":135},
    {"id":"evolve","label":"evolve (Ouroboros)","group":"terminal","x":460,"y":165}
  ],
  "edges": [
    {"source":"discover","target":"define"},
    {"source":"define","target":"design"},
    {"source":"design","target":"plan"},
    {"source":"plan","target":"build"},
    {"source":"build","target":"verify"},
    {"source":"verify","target":"release"},
    {"source":"release","target":"operate"},
    {"source":"verify","target":"design","dashed":true,"label":"shift-left ↺"},
    {"source":"operate","target":"recover","dashed":true},
    {"source":"operate","target":"degrade","dashed":true},
    {"source":"operate","target":"escalate","dashed":true},
    {"source":"operate","target":"evolve","dashed":true,"label":"learn"},
    {"source":"evolve","target":"discover","dashed":true,"label":"evolve target ↺"}
  ]
}
```

**The artifacts** — stone #7's per-beat carriers, each crossing the *time* and *agent* boundaries (§9).

```pipeline-graph
{
  "title": "The artifacts — stone #7's per-beat carriers",
  "nodes": [
    {"id":"define","label":"define","group":"beat","x":0,"y":0},
    {"id":"do","label":"do","group":"beat","x":0,"y":90},
    {"id":"check","label":"check","group":"beat","x":0,"y":180},
    {"id":"reflect","label":"reflect","group":"beat","x":0,"y":270},
    {"id":"overtime","label":"repeat over time","group":"element","x":0,"y":360},
    {"id":"repertoire","label":"resilience repertoire","group":"repertoire","x":0,"y":450},
    {"id":"a_spec","label":"spec / target doc","group":"property","x":300,"y":0},
    {"id":"a_code","label":"code","group":"property","x":300,"y":90},
    {"id":"a_tests","label":"tests + telemetry","group":"property","x":300,"y":180},
    {"id":"a_post","label":"postmortem / ADR","group":"property","x":300,"y":270},
    {"id":"a_version","label":"version history","group":"property","x":300,"y":360},
    {"id":"a_runbook","label":"runbooks","group":"property","x":300,"y":450},
    {"id":"b_time","label":"TIME → persist","group":"stone","x":620,"y":135},
    {"id":"b_agent","label":"AGENT → make explicit","group":"stone","x":620,"y":315}
  ],
  "edges": [
    {"source":"define","target":"a_spec","label":"produces"},
    {"source":"do","target":"a_code","label":"produces"},
    {"source":"check","target":"a_tests","label":"produces"},
    {"source":"reflect","target":"a_post","label":"produces"},
    {"source":"overtime","target":"a_version","label":"produces"},
    {"source":"repertoire","target":"a_runbook","label":"produces"},
    {"source":"a_version","target":"b_time","dashed":true,"label":"crosses"},
    {"source":"a_spec","target":"b_agent","dashed":true,"label":"crosses"},
    {"source":"a_runbook","target":"b_time","dashed":true},
    {"source":"a_post","target":"b_agent","dashed":true}
  ]
}
```

**Done propagation** — the root Done is *elicited*, `design` *decomposes* it into sub-Dones (each edge a composition hypothesis), leaves bottom out in binary checks, and a rejected qualitative composite *falsifies the hypothesis* → back to `design` (§10).

```pipeline-graph
{
  "title": "Done propagation — elicit · decompose · bottom-out",
  "nodes": [
    {"id":"intent","label":"hidden intent","group":"stone","x":0,"y":0},
    {"id":"specify","label":"specify · elicit","group":"element","x":0,"y":95},
    {"id":"root","label":"root Done P","group":"beat","x":260,"y":95},
    {"id":"design","label":"design · decompose","group":"element","x":260,"y":195},
    {"id":"cA","label":"sub-Done A","group":"beat","x":110,"y":300},
    {"id":"cB","label":"sub-Done B · qualitative","group":"beat","x":440,"y":300},
    {"id":"accept","label":"human accept","group":"terminal","x":700,"y":300},
    {"id":"leaf1","label":"leaf · deterministic","group":"property","x":-20,"y":410},
    {"id":"leaf2","label":"leaf · deterministic","group":"property","x":200,"y":410},
    {"id":"leaf3","label":"leaf · statistical proxy","group":"property","x":440,"y":410}
  ],
  "edges": [
    {"source":"intent","target":"specify","member":true,"label":"elicit"},
    {"source":"specify","target":"root","label":"sets P"},
    {"source":"root","target":"design","label":"decompose"},
    {"source":"design","target":"cA","label":"hyp: (∧Lᵢ)⟹P"},
    {"source":"design","target":"cB","label":"hyp: (∧Lᵢ)⟹P"},
    {"source":"cA","target":"leaf1"},
    {"source":"cA","target":"leaf2"},
    {"source":"cB","target":"leaf3"},
    {"source":"cB","target":"accept","dashed":true,"label":"qualitative → human"},
    {"source":"accept","target":"design","dashed":true,"label":"falsified → re-decompose ↺"}
  ]
}
```

**Stub-composition** — `design` states a bet (contracts + composition hypothesis); a design-time **stub-composition** check *fails cheap* (→ re-decompose) or *survives*, discharging the **wiring (⟹)** and suspending **Premise A** (→ `verify` / deterministic leaf) and **Premise B** (→ `observe` / statistical leaf) (§10.1).

```pipeline-graph
{
  "title": "Stub-composition — the design bet, factored",
  "nodes": [
    {"id":"design","label":"design · state the bet","group":"element","x":0,"y":120},
    {"id":"contracts","label":"interface contracts","group":"property","x":250,"y":40},
    {"id":"hyp","label":"composition hyp (∧Lᵢ)⟹P","group":"beat","x":250,"y":200},
    {"id":"stub","label":"stub-composition (design-time check)","group":"element","x":540,"y":120},
    {"id":"fail","label":"fail → re-decompose","group":"terminal","x":540,"y":280},
    {"id":"survive","label":"survive (conditional)","group":"beat","x":830,"y":120},
    {"id":"wiring","label":"⟹ wiring · discharged","group":"property","x":1090,"y":20},
    {"id":"premA","label":"Premise A · leaves real","group":"beat","x":1090,"y":120},
    {"id":"premB","label":"Premise B · whole value-domain","group":"beat","x":1090,"y":230},
    {"id":"verify","label":"verify → deterministic leaf","group":"element","x":1400,"y":120},
    {"id":"observe","label":"observe → statistical leaf","group":"element","x":1400,"y":230}
  ],
  "edges": [
    {"source":"design","target":"contracts","member":true},
    {"source":"design","target":"hyp","member":true},
    {"source":"hyp","target":"stub","label":"stub it"},
    {"source":"stub","target":"fail","dashed":true,"label":"fails cheap ↺"},
    {"source":"fail","target":"design","dashed":true,"label":"re-decompose"},
    {"source":"stub","target":"survive","label":"green"},
    {"source":"survive","target":"wiring","label":"discharges ⟹"},
    {"source":"survive","target":"premA","dashed":true,"label":"suspends"},
    {"source":"survive","target":"premB","dashed":true,"label":"suspends"},
    {"source":"premA","target":"verify","label":"build-time"},
    {"source":"premB","target":"observe","label":"run-time"}
  ]
}
```

**Premise-B lever** — contract-tightness is a dial: it shrinks premise B (buys `predictable`, moving residue statistical → deterministic → a-priori), but the **floor** is the required set of realities (`reliable` + `resilient`) — so the bar is *tightest-sufficient*, not tightest (§10.2).

```pipeline-graph
{
  "title": "The premise-B lever — contract-tightness dial (floor = reliability)",
  "nodes": [
    {"id":"loose","label":"loose contract","group":"property","x":0,"y":0},
    {"id":"tsuff","label":"tightest-sufficient · THE BAR","group":"beat","x":330,"y":0},
    {"id":"over","label":"over-tight","group":"terminal","x":660,"y":0},
    {"id":"stat","label":"statistical leaf → observe (residue>0)","group":"element","x":0,"y":140},
    {"id":"det","label":"deterministic / a-priori leaf → verify · compile (residue→0)","group":"element","x":330,"y":140},
    {"id":"unrel","label":"rejects a required reality → UNRELIABLE","group":"stone","x":660,"y":140},
    {"id":"floor","label":"FLOOR = required set of realities (reliable + resilient)","group":"stone","x":330,"y":260},
    {"id":"pred","label":"tightening buys predictable · premise B ↓","group":"property","x":330,"y":-120}
  ],
  "edges": [
    {"source":"loose","target":"tsuff","member":true,"label":"tighten →"},
    {"source":"tsuff","target":"over","member":true,"dashed":true,"label":"one step too far"},
    {"source":"loose","target":"stat","label":"sampled"},
    {"source":"tsuff","target":"det","label":"exhausted / unrepresentable"},
    {"source":"over","target":"unrel","dashed":true},
    {"source":"tsuff","target":"pred","dashed":true,"label":"max predictability…"},
    {"source":"tsuff","target":"floor","member":true,"label":"…subject to the floor"},
    {"source":"over","target":"floor","dashed":true,"label":"breaches floor"}
  ]
}
```
