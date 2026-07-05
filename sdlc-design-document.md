# The Ideal SDLC — A First-Principles Design

> **What this document is.** A clean, human-readable snapshot of the software-development
> lifecycle (SDLC) we have derived from first principles — *what an ideal SDLC must contain, and
> why every piece is logically forced into existence rather than adopted by convention.* It covers
> both the **human-run** lifecycle and the **autonomous / agentic** one (Chapter 12).
>
> This is the **design**, presented for comprehension. Its companion,
> [`sdlc-first-principles-canvas.md`](sdlc-first-principles-canvas.md), is the **working derivation**
> — the terse, evolving state file with the full audit trail of *how* we arrived here (the Socratic
> Q&A, the iteration log, the open research tracks). When the two disagree, the canvas is the source
> of truth for *reasoning*; this document is the source of truth for *understanding*.

---

## How to read this document

The document is a **zoom lens**. It starts at the widest possible view — the entire machine in one
picture — and then descends, chapter by chapter, into finer and finer detail. Each chapter answers
three questions in order:

1. **What is it?** — a plain description of the piece.
2. **Why does it exist?** — the brute fact about reality (a "stone") that *forces* it. Nothing here
   is a matter of taste; each element is a forced response to something reality makes unavoidable.
3. **How does it work?** — the mechanics, in ordinary language.

Wherever autonomy changes the picture, a callout marked **⟐ Under autonomy** flags it, and
**Chapter 12** gathers those threads into one place.

### The chart ladder

Every chapter carries at least one **interactive chart**. The charts are a single cohesive set,
ordered from the coarsest view to the finest, and cross-linked so you can *zoom out* to the parent
view or *zoom in* to the detail. In the accompanying viewer they render **inline**, exactly where
the prose discusses them, and a floating ladder on the right lets you jump between granularity
levels.

| Level | Chart | Shows | Chapter |
|---|---|---|---|
| **L0** | The complete circuit | The whole machine: forces → loop → behaviours → properties | [Ch. 1](#1-the-system-at-a-glance) |
| **L1** | The four properties | The destination — what a good SDLC produces | [Ch. 2](#2-the-destination-four-properties) |
| **L1** | The bedrock — nine forces | The brute facts that make the work hard | [Ch. 3](#3-the-bedrock-why-the-work-is-hard) |
| **L2** | The unit loop, fully staffed | The atom — one feedback loop, and its elements | [Ch. 4](#4-the-atom-the-unit-control-loop) |
| **L2** | The fractal — one shape, every scale | How the loop repeats up and down | [Ch. 6](#6-the-fractal-one-shape-at-every-scale) |
| **L2** | The lifecycle (process flow) | The familiar lifecycle, as a projection of the loop | [Ch. 7](#7-the-lifecycle-the-process-flow) |
| **L2** | The two repertoires | Cross-cutting responses: resilience vs. security | [Ch. 8](#8-the-two-repertoires-resilience-and-security) |
| **L3** | Done propagation | How a target is set, inherited, and checked | [Ch. 9](#9-the-mechanism-of-done) |
| **L3** | Design as a bet — stub-composition | How design states and cheaply tests its bet | [Ch. 9](#9-the-mechanism-of-done) |
| **L3** | The premise-B lever | How one interface contract is tuned | [Ch. 9](#9-the-mechanism-of-done) |
| **L2** | The artifacts | What each loop leaves behind, and why | [Ch. 10](#10-what-each-loop-leaves-behind-the-artifacts) |
| **L3** | Hard gate or graded target? | Which checks are non-negotiable | [Ch. 11](#11-hard-gates-versus-graded-targets) |
| **L4** | Reflexivity — the autonomous regime | Why an autonomous loop cannot judge itself | [Ch. 12](#12-the-autonomous-agentic-sdlc) |

> **The one-sentence thesis.** A reliable, predictable, resilient, and secure SDLC is not a
> checklist of practices — it is the **emergent behaviour of a single bounded feedback loop**, forced
> into a specific shape by a handful of unavoidable facts about reality, and repeated at every scale.

---

## 1. The system at a glance

**What it is.** The entire SDLC, compressed into one causal chain. Read it bottom-to-top:

> **brute facts about reality** &nbsp;→&nbsp; **one control loop** &nbsp;→&nbsp; **four loop behaviours**
> &nbsp;→&nbsp; **four emergent properties** &nbsp;→&nbsp; **an evolve feedback that re-aims the whole thing.**

**Why it exists — the key insight.** The four things we actually want from software — that it is
**reliable, predictable, resilient, and secure** — cannot be *installed*. There is no "reliability
module." They are **emergent**: they appear only as the *behaviour* of a system of feedback loops
that is itself built from parts, each of which is a forced response to a brute fact. Change the
brute facts and the whole machine would be different; because the brute facts are unavoidable, the
machine's shape is forced.

**How it works.** The chain has four links, each detailed in a later chapter:

1. **The bedrock** (Chapter 3) — nine brute facts ("stones") about reality that make software hard:
   intent is hidden, resources are finite, systems exceed one mind, we make mistakes, reality
   changes, reality is uncertain, knowledge is scattered and perishable, adversaries hunt weakness,
   and — in the autonomous case — a checker can share the doer's blind spot.
2. **The loop** (Chapter 4) — those facts force exactly one atom: `define → do → check → reflect`,
   repeated until good enough, then stopped.
3. **The behaviours** (Chapter 2) — the way the loop runs produces four behaviours: it **converges**,
   it stays **bounded**, it **nests and escalates**, and it **preempts** (searches its own inputs for
   trouble before trouble finds them).
4. **The properties** (Chapter 2) — those four behaviours *are* what we experience as reliable,
   predictable, resilient, and secure. A final **evolve** edge feeds what we learn back into the
   target, turning the loop into a spiral — the "Ouroboros."

> ▸ **Chart — "The complete circuit"** · *L0 · the whole system.* The master synthesis: every later
> chart is a zoom into one region of this one. Start here, then zoom in.

```pipeline-graph
{
  "title": "The complete circuit",
  "level": "L0 · the whole system",
  "summary": "The entire machine in one frame: brute facts force one loop, whose behaviours manufacture four emergent properties, which feed an evolve edge.",
  "zoomIn": ["The four properties", "The bedrock — nine forces", "The unit loop, fully staffed"],
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
    {"id":"loop","label":"the loop (define → do → check → reflect ↺)","group":"beat","x":360,"y":320},
    {"id":"intent","label":"intent hidden","group":"stone","x":-40,"y":440},
    {"id":"finite","label":"finite","group":"stone","x":120,"y":440},
    {"id":"complex","label":"complex","group":"stone","x":270,"y":440},
    {"id":"err","label":"we err","group":"stone","x":420,"y":440},
    {"id":"change","label":"change","group":"stone","x":560,"y":440},
    {"id":"uncertain","label":"uncertain","group":"stone","x":710,"y":440},
    {"id":"distributed","label":"distributed & perishable","group":"stone","x":880,"y":440},
    {"id":"adversarial","label":"adversarial actors","group":"stone","x":1060,"y":440},
    {"id":"reflexivity","label":"reflexivity (#9 · autonomous only)","group":"stone","x":-200,"y":40}
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

> **⟐ Under autonomy.** Notice the lone coral node on the left, *reflexivity*, with a dashed edge
> reaching up to **reliable**. In a human-run lifecycle it is dormant. Remove the human and it
> activates, eroding the very property the loop works hardest to manufacture. Chapter 12 is entirely
> about this edge.

---

## 2. The destination: four properties

Before building anything, name what "good" means — because you cannot check work against nothing.
A good SDLC produces **four distinct properties**, in **two families**. They are distinct because
each guards against a *different* way the work can fail, and you can have any one without the others.

### The two families

**Point-properties** are measured at a *single* point — one task, in one context.

- **Reliable** — *faithful to intent.* The output is correct: nothing missing, nothing invented. It
  guards against "it gave me the wrong thing." Produced by a loop that **converges** — iterates until
  the result actually matches the need.
- **Predictable** — *foreseeable.* Low variance; you can call the output and the timing in advance
  and plan around them. It guards against "I couldn't foresee it / couldn't plan around it." Produced
  by a loop that is **bounded** — it takes a knowable number of tries and then stops.

**Envelope-properties** are measured along a third axis — **how hard the context is × time.** They
are the envelope that keeps the point-properties alive across the *whole range* of contexts, not just
the easy one. The range has two very different sources of hardness, and each forces its own envelope:

- **Resilient** — *withstands and recovers from **random** hardship.* Reality changes and reality is
  uncertain; together they *sample* the space of contexts blindly and will eventually hand you a hard
  one. Resilience is the envelope against that blind sampler. It guards against "it collapsed on a
  hard context and couldn't recover." Produced by a loop that **nests and escalates** — smaller loops
  hand up to larger ones, and a repertoire of responses (retry, fail over, degrade, roll back) keeps
  the function alive.
- **Secure** — *withstands a **directed** adversary hunting the worst case.* An attacker is not blind
  variance; it is a *directed optimiser* that deliberately searches for the one input that breaks you.
  Security is the envelope against that searcher. It guards against "an attacker drove it to do
  something outside its allowed set" — leak a secret, cause downtime, forge or intercept a message.
  Produced by a loop that **preempts** — it red-teams its *own* inputs for forbidden outputs and
  forecloses them before the adversary arrives.

### Why security is a fourth seat, not a corner of resilience

It is tempting to file security under "resilience on the hardest context." That is wrong, and the
distinction is load-bearing. The machinery that manufactures resilience — redundancy, retries,
graceful degradation — is *statistical*: it assumes hardship arrives at random and rare events are
rare. Against a directed opponent that machinery can *backfire*: a retry loop is a gift to a
denial-of-service attack, because the attacker aims straight at the expensive path. Resilience
answers a blind sampler; security answers a hunter. Same *shape* (an envelope over context-hardness),
different *opponent* — so security takes a fourth seat beside resilience, with its own repertoire
(Chapter 8).

### They are genuinely independent

Each property is independent of its family sibling — you can hold one and fail the other:

- **Reliable ⟂ Predictable.** *Correct-but-unforeseeable*: a system that always eventually returns
  the right answer but at wildly varying, un-callable times (reliable, not predictable).
  *Foreseeable-but-wrong*: a system that returns a confidently wrong answer at a perfectly
  predictable moment (predictable, not reliable).
- **Secure ⟂ Resilient.** *Resilient-but-insecure*: auto-failover and self-healing under random load,
  sitting behind an open authentication bypass. *Secure-but-fragile*: hardened and authorised on every
  request, but with no redundancy, so a single random outage kills it.

Because each combination exists, none of the four reduces to another. All four must be produced on
purpose.

> ▸ **Chart — "The four properties"** · *L1 · the destination.* A zoom into the top band of the
> complete circuit: the two families, the behaviour that produces each property, and the two
> independence relations (⟂).

```pipeline-graph
{
  "title": "The four properties",
  "level": "L1 · the destination",
  "summary": "Two point-properties (measured at one task) and two envelope-properties (measured across contexts × time); each is produced by a distinct loop behaviour and is independent of its sibling.",
  "zoomOut": "The complete circuit",
  "zoomIn": ["The unit loop, fully staffed"],
  "nodes": [
    {"id":"point","label":"POINT — one task, one context","group":"terminal","x":120,"y":0},
    {"id":"envelope","label":"ENVELOPE — across contexts × time","group":"terminal","x":700,"y":0},
    {"id":"reliable","label":"reliable — faithful to intent","group":"property","x":0,"y":110},
    {"id":"predictable","label":"predictable — foreseeable, low variance","group":"property","x":300,"y":110},
    {"id":"resilient","label":"resilient — survives RANDOM hardness","group":"property","x":600,"y":110},
    {"id":"secure","label":"secure — survives a DIRECTED adversary","group":"property","x":920,"y":110},
    {"id":"converges","label":"loop converges","group":"beat","x":0,"y":235},
    {"id":"bounded","label":"loop is bounded","group":"beat","x":300,"y":235},
    {"id":"nests","label":"loop nests & escalates","group":"beat","x":600,"y":235},
    {"id":"preempts","label":"loop preempts (self red-teams)","group":"beat","x":920,"y":235}
  ],
  "edges": [
    {"source":"point","target":"reliable","member":true},
    {"source":"point","target":"predictable","member":true},
    {"source":"envelope","target":"resilient","member":true},
    {"source":"envelope","target":"secure","member":true},
    {"source":"converges","target":"reliable","label":"produces"},
    {"source":"bounded","target":"predictable","label":"produces"},
    {"source":"nests","target":"resilient","label":"produces"},
    {"source":"preempts","target":"secure","label":"produces"},
    {"source":"reliable","target":"predictable","dashed":true,"label":"⟂ independent"},
    {"source":"resilient","target":"secure","dashed":true,"label":"⟂ independent"}
  ]
}
```

> **⟐ Under autonomy.** Of the four, **reliable** is the one autonomy most directly threatens.
> Reliability is manufactured by a loop that *converges* — but convergence quietly assumes the checker
> is independent of the doer. When the same kind of agent both builds and checks, the loop can
> converge to a *confident wrong answer* (a green check over a real defect). See Chapter 12.

---

## 3. The bedrock: why the work is hard

**What it is.** First principles, literally: the unavoidable truths about reality that make software
engineering hard. We call them **stones**. Every stage, tool, and artifact in the SDLC is a *response*
to one or more stones — never a convention. There are **eight** first-order stones (facts about the
*problem*), plus a **ninth**, second-order stone (a fact about the *solver*) that activates only in the
autonomous case.

**Why this matters.** The stones are the model's foundation and its test. If a needed element rests on
*no* stone, the model has a spurious part. If a stone has *no* element defending it, the model has a
gap. This "self-test" is how the model grows: it fired in reverse twice — the security defenses rested
on no stone, which exposed stone #8; and the loop's own checker rested on an unguaranteed assumption,
which exposed stone #9.

### The eight first-order stones

| # | Stone (brute fact) | What it forces |
|---|---|---|
| 1 | **Intent is hidden.** The real need isn't given; what's asked ≠ what's needed. | `specify` — draw the true target out of a hidden head. |
| 2 | **Unbounded vs. finite.** Infinite possible scope against finite resources. | `scope` (bound before) and `decide` (bound after). |
| 3 | **Complexity exceeds one step.** Systems exceed any single mind or single step. | `design` — carve the whole into parts that fit a mind. |
| 4 | **Humans and models err.** Translating intent into an artifact is lossy and mistake-prone. | `verify` (catch the error) and `analyze` (root-cause it). |
| 5 | **Reality keeps changing.** The target moves over *time*. | the over-time machinery (versioning, integration, regression) and the resilience response *roll back*. |
| 6 | **Reality is uncertain.** You can't know which reality will materialise at any moment. | `observe` (run-time sensing) and the resilience responses *degrade* / *recover*. |
| 7 | **Knowledge is distributed and perishable.** It lives in separate private heads and decays over time. | **artifacts** — persistent, explicit carriers (Chapter 10). |
| 8 | **Adversarial actors.** Reality contains agents who actively hunt and exploit weakness. | the **security repertoire** — authn/authz, sanitize, harden, red-team (Chapter 8). |

Two clarifications that keep the stones distinct:

- **Stone #6 (uncertain) vs. stone #8 (adversarial).** Uncertainty *samples* the space of possible
  inputs at random; an adversary *searches* it for the worst case. A defense that beats random
  sampling (make the rare case survivable) can be defeated by a searcher (who makes the rare case
  common). Different opponents, different responses.
- **Facts are not one-to-one with stages.** One stone forces several responses (finiteness forces both
  `scope` and `decide`; "we err" forces both `verify` and `analyze`), and several stones can converge
  on one response.

### The ninth stone — reflexivity (conditional, second-order)

9. **Reflexivity — the checker shares the doer's fault.** *(Second-order and conditional — it bites
   only in an automated, autonomous, multi-agent pipeline.)*

The agents that staff `check` and `reflect` are the same *kind* of erring agent as the doer (stone #4).
So their errors are not independent — they are **correlated**. A check is only worth the *new
information* it adds beyond the doer's own belief; a checker that shares the doer's blind spot is an
**echo chamber** that adds zero information, and "verify" quietly collapses into "declare." The property
at stake is **independence** — the thing that lets stacked checks drive error toward zero (and thereby
manufacture reliability). Reflexivity is the brute fact that independence is *never total*: a
common-mode floor always remains (even a formal proof only relocates the blind spot into the spec).

This stone is different in kind from the first eight — they are facts about the *problem*; this is a
fact about the *solver*. And it is conditional: with a human in the loop, the human is a
partially-independent terminal and reflexivity stays bounded; remove the human and independence at the
terminal collapses to zero — so **an autonomous loop cannot be its own ground truth.** It is treated in
full in Chapter 12.

> ▸ **Chart — "The bedrock — nine forces"** · *L1 · the forces.* Each stone on the left; the element
> or repertoire it forces on the right. This is the "why" behind every part of the loop.

```pipeline-graph
{
  "title": "The bedrock — nine forces",
  "level": "L1 · the forces",
  "summary": "The nine brute facts, each wired to the specific response it forces into existence. Nothing in the loop is a convention; every part defends a stone.",
  "zoomOut": "The complete circuit",
  "zoomIn": ["The unit loop, fully staffed"],
  "nodes": [
    {"id":"intent","label":"1 · intent is hidden","group":"stone","x":0,"y":0},
    {"id":"finite","label":"2 · unbounded vs finite","group":"stone","x":0,"y":80},
    {"id":"complex","label":"3 · complexity > one step","group":"stone","x":0,"y":160},
    {"id":"err","label":"4 · humans & models err","group":"stone","x":0,"y":240},
    {"id":"change","label":"5 · reality keeps changing","group":"stone","x":0,"y":320},
    {"id":"uncertain","label":"6 · reality is uncertain","group":"stone","x":0,"y":400},
    {"id":"distributed","label":"7 · knowledge distributed & perishable","group":"stone","x":0,"y":480},
    {"id":"adversarial","label":"8 · adversarial actors","group":"stone","x":0,"y":560},
    {"id":"reflexivity","label":"9 · reflexivity (2nd-order · autonomous)","group":"stone","x":0,"y":650},
    {"id":"specify","label":"specify","group":"element","x":520,"y":0},
    {"id":"scope","label":"scope & decide","group":"element","x":520,"y":80},
    {"id":"design","label":"design (decompose)","group":"element","x":520,"y":160},
    {"id":"verify","label":"verify + analyze","group":"element","x":520,"y":240},
    {"id":"resilience","label":"resilience repertoire","group":"repertoire","x":520,"y":340},
    {"id":"observe","label":"observe (telemetry)","group":"element","x":520,"y":430},
    {"id":"artifacts","label":"artifacts","group":"property","x":520,"y":500},
    {"id":"security","label":"security repertoire","group":"repertoire","x":520,"y":570},
    {"id":"independence","label":"independence-seeking (external terminal · red-team)","group":"terminal","x":520,"y":650}
  ],
  "edges": [
    {"source":"intent","target":"specify","label":"forces"},
    {"source":"finite","target":"scope","label":"forces"},
    {"source":"complex","target":"design","label":"forces"},
    {"source":"err","target":"verify","label":"forces"},
    {"source":"change","target":"resilience","label":"forces"},
    {"source":"change","target":"observe","dashed":true},
    {"source":"uncertain","target":"observe","label":"forces"},
    {"source":"uncertain","target":"resilience","dashed":true},
    {"source":"distributed","target":"artifacts","label":"forces"},
    {"source":"adversarial","target":"security","label":"forces"},
    {"source":"reflexivity","target":"independence","label":"forces","dashed":true}
  ]
}
```

---

## 4. The atom: the unit control loop

**What it is.** Everything in the SDLC reduces to a single feedback loop, repeated:

> **`set a target → do the work → check the result → reflect → (re-aim and repeat)`**

**Why it exists.** It is the minimal machine that answers the stones together. Because intent is
hidden and we err (stones #1, #4), you cannot get it right in one shot — you need a *check* and a way
to *try again*. Because resources are finite (stone #2), you cannot try forever — the loop must be
*bounded*. Because reality changes and is uncertain (stones #5, #6), the loop must keep running after
you ship. The loop is not one choice among many; it is what these facts jointly force.

**How it works — the four beats.**

- **Define (set the target).** State what "done" means for this piece of work. This is not a yes/no
  flag — it is a **threshold on a quality range** (see Chapter 9). Defining is itself composite: `scope`
  sets the boundary (how much / which items), and `specify` sets correctness (what's right), across the
  whole set of realities the work must serve.
- **Do (build).** Execute — produce the artifact the target described. This beat is pure construction;
  all the judgement lives in the beats around it.
- **Check (measure).** Compare the result against the target. `check` is **graded, not binary**: it
  measures *how well* on a quality range — using a real metric where one exists, or a **proxy** (a
  stand-in measurement, like test coverage for "well-tested") where the true quality can't be measured
  directly — and asks whether the measurement clears the threshold. It happens at **build time**
  (`verify`) and at **run time** (`observe`), and those two are not interchangeable (Chapter 5).
- **Reflect (close the loop).** The thinking beat. It **analyzes** — frames the problem ("the loop
  can't converge") and root-causes it — and then **decides** among three exits:
  - **accept** the gap as a known issue (stop here — the bounded, predictable exit);
  - **re-target** — redefine the target and iterate (the converging, reliable exit);
  - **escalate** — hand the problem up when bounded tries are exhausted (the nesting, resilient exit).

**Two properties of the loop that carry a lot of weight:**

- **Non-convergence is information, not just failure.** If honest tries keep missing, suspect the
  *target* (the spec), not only the build. A loop that won't converge is often pointing at a wrong
  definition of done — so `reflect` escalates *up*, toward re-defining, rather than grinding *down* on
  the build.
- **The loop is bounded, and boundedness is where predictability comes from.** "A few tries, then
  stop" is what makes cost and timing foreseeable. `decide`'s *accept* exit is the stop.

**The escape hatch.** Escalation ultimately ends at a **human** — the loop's one *independent*
terminal, the place where a genuinely outside judgement can enter. This is normally a convenience. It
becomes structurally load-bearing under autonomy (Chapter 12): remove the human and the loop loses its
only independent ground.

> ▸ **Chart — "The unit loop, fully staffed"** · *L2 · the atom.* The four beats across the top; the
> elements that staff each beat below them; the cross-cutting repertoire along the bottom; the dashed
> `re-target` edge closing the loop. Chapter 5 walks the elements one by one.

```pipeline-graph
{
  "title": "The unit loop, fully staffed",
  "level": "L2 · the atom",
  "summary": "One feedback loop — define, do, check, reflect — with the elements that staff each beat, the three exits of decide, and the cross-cutting repertoire.",
  "zoomOut": "The complete circuit",
  "zoomIn": ["The fractal — one shape, every scale", "Done propagation", "The two repertoires", "The artifacts"],
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

> **⟐ Under autonomy.** The dashed line from `reflect` to the human escape hatch (implicit here,
> explicit in the fractal chart) is the loop's independent terminal. An autonomous pipeline that lets
> an executor staff `escalate`/`decide` too has *cut that line* — and with it the loop's only outside
> check. This is the single most important structural change autonomy makes.

---

## 5. The loop, fully staffed: the elements

**What it is.** The **elements** are the concrete jobs that staff the loop's beats in the *outermost*
SDLC loop. They are not a checklist bolted on by habit; they are the **anatomy of the loop**, each one
forced by a specific stone. Every element is a *verb*, because each names an action.

**Why there are exactly these.** Run the self-test from Chapter 3: each element defends a stone, and
each stone that needs an element has one. Take one away and a stone goes undefended; add one that
defends nothing and the model flags it as ceremony.

| Beat | Element | Forced by | What it does |
|---|---|---|---|
| **define** | **specify** | intent is hidden (#1) | Draws the real target out of a hidden need — the one *elicited* input the model has. |
| **define** | **scope** | unbounded vs. finite (#2) | Sets the boundary: how much, which items, in this pass. |
| **define** | **design** | complexity > one step (#3) | Carves the whole into parts and states how they compose — the decomposition *is* design's output. |
| **do** | **implement** | (the build itself) | Executes. The base act; it defends no stone of its own — it is simply the work. |
| **check** | **verify** | humans & models err (#4) | Build-time check: did we build what we specified? |
| **check** | **observe** | reality is uncertain (#6) | Run-time check: did reality match what we modelled? The loop's own sensor (telemetry). |
| **reflect** | **analyze** | humans & models err (#4) | Frames and root-causes the gap. |
| **reflect** | **decide** | unbounded vs. finite (#2) | Chooses: accept a known issue, or re-target. |
| **repeat over time** | **version · integrate · regression-test** | reality keeps changing (#5) | Keeps the loop running as the target moves. |

### Two planes: beats vs. elements

There is a subtle but important distinction. The **beats** (`define → do → check → reflect`) are
*scale-invariant* — the same four recur at every level of the system. The **elements** (specify … decide)
are the *outermost* loop's particular staffing of those beats. `analyze` and `decide`, for instance,
are how the `reflect` beat is staffed at the top level; deeper down, `reflect` is staffed by finer
activities. Keep the two planes separate and the fractal (Chapter 6) makes sense; conflate them and it
looks like a contradiction.

### Why there is no separate "decompose"

An earlier version of the model had a distinct `decompose` element. It was removed because it did no
work `design` wasn't already doing: `design`'s output *is* the decomposition, the loop re-applies
itself to each part that design carves, and the feedback edge (`reflect → re-target(design)`) already
carries any "this decomposition was wrong" signal back. A `decompose` element defended the same stone
as `design` (#3) and owned no artifact of its own — so it was vestigial, and folding it away left `do`
as pure execution. This is the self-test doing maintenance: *two elements on one stone, one of them
derivable, is a smell.*

*(This chapter reuses the **"The unit loop, fully staffed"** chart from Chapter 4 — the middle band is
the element roster.)*

---

## 6. The fractal: one shape at every scale

**What it is.** The loop is not a top-level ceremony with different machinery underneath. It is a
**fractal**: the same `define → do → check → reflect` shape repeats **in both directions**.

- **Outward, across scope.** An action sits inside a feature, inside a stage, inside a release, inside
  a product. `design` carves the whole into parts, and *each part becomes its own loop*. The nesting is
  not staffed by a separate element — it is **emergent**: decompose, and the sub-loops appear.
- **Inward, into every element.** Addressing a single element — `specify`, say — is *itself* a full
  `define → do → check → reflect` loop, with its own graded target and its own metric or proxy.

**Why it must be a fractal.** Complexity (stone #3) forces decomposition, and a decomposed part is
just a smaller instance of the same problem — so it needs the same machine. The alternative (a
different mechanism at each level) would multiply the stones' responses without cause. One shape,
reused, is the minimal answer.

**How it behaves.** A stuck inner loop **escalates** to the loop above it. The outermost loop's escape
hatch is a human. Two planes, again: the *beats* are the same at every level; the *elements* get finer
as you descend.

> ▸ **Chart — "The fractal — one shape, every scale"** · *L2 · scaling.* The top row is the scope
> nesting (action ⊂ feature ⊂ … ⊂ product). Any scope expands into the four beats (middle). Any beat
> expands, in turn, into its own four-beat loop (bottom). Escalation runs upward; a human sits at the
> top.

```pipeline-graph
{
  "title": "The fractal — one shape, every scale",
  "level": "L2 · scaling",
  "summary": "The same loop nested up across scope (action ⊂ feature ⊂ … ⊂ product) and down into every beat; escalation runs upward to a human terminal.",
  "zoomOut": "The unit loop, fully staffed",
  "zoomIn": ["The lifecycle (process flow)"],
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

---

## 7. The lifecycle: the process flow

**What it is.** The familiar left-to-right lifecycle — discover, define, design, plan, build, verify,
release, operate — is not a separate model. It is the **projection** of the loop onto the timeline of a
single release: the beats laid out in order, with the feedback edges drawn back in.

**Why it looks like a pipeline but behaves like a loop.** The solid arrows are the *forward flow* — the
lifecycle as usually drawn. The dashed arrows are the *loops and feedback*, present at every scale:

- The **build** step is itself a loop: `do ⇄ check against a graded 'done' → reflect → re-target`.
- **verify** feeds back to **design** — the *shift-left* edge: catching a defect late is exponentially
  more expensive than catching it early, so verification is a cross-cutting layer, not a step bolted on
  after build.
- **operate** is a run-time loop: `observe ⇄ recover / degrade / escalate`.
- The whole thing closes: **operate → learn → evolve the target → back to discover.** This is the
  **Ouroboros** — the product loop that turns a one-shot lifecycle into a spiral that improves its own
  target over time.

**How to read it.** The lifecycle is the most *concrete* and recognisable view, which is why it comes
after the abstract ones: by now you can see that each box is a beat, each dashed line is the loop
reasserting itself, and the Ouroboros is the evolve edge from Chapter 1.

> ▸ **Chart — "The lifecycle (process flow)"** · *L2 · lifecycle.* The forward flow in solid arrows;
> the build loop, the operate loop, the shift-left edge, and the Ouroboros in dashed arrows.

```pipeline-graph
{
  "title": "The lifecycle (process flow)",
  "level": "L2 · lifecycle",
  "summary": "The everyday lifecycle as a projection of the loop: forward flow in solid arrows, the build loop / operate loop / shift-left / Ouroboros in dashed feedback edges.",
  "zoomOut": "The fractal — one shape, every scale",
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

---

## 8. The two repertoires: resilience and security

**What it is.** Some responses are not beats in the forward flow — they are a **repertoire** of moves
the loop can invoke from `reflect`, at *any* element and *any* scale, mostly at run time. There are two
repertoires, one per source of hardness, and together they manufacture the two envelope-properties.

**Why two, not one.** Chapter 2 showed that context-hardness has two sources: *random* (a blind
sampler — stones #5, #6) and *directed* (a worst-case searcher — stone #8). Each needs its own kit,
because the statistical moves that beat randomness can be turned *against* you by a searcher.

### The resilience repertoire — against random hardship (→ resilient)

| Response | What it does | Example |
|---|---|---|
| **escalate** | Hand up when bounded tries are exhausted; ends at a human. | Retries for one email domain keep failing → page the on-call. |
| **degrade** | Fail partial, not total (graceful degradation). | Email provider down → queue the request and say "arriving shortly" instead of returning a 500. |
| **recover** | Spares, replicas, retries so the function survives a failure (redundancy). | A second email provider takes over when the primary fails. |
| **roll back** | Revert to the last known-good state. | A new template spikes bounce rates → redeploy the previous one. |

### The security repertoire — against a directed adversary (→ secure)

| Response | What it does | Example |
|---|---|---|
| **authenticate / authorize** | Prove identity, then gate every action by least privilege. | Signed-in ≠ allowed; check the permission on each request. |
| **sanitize / validate** | Narrow every boundary contract; never trust external data. | Parameterised queries (SQL injection), output-encoding (XSS), CSRF tokens. |
| **minimise surface / harden** | Least exposure; secrets in a vault; no information leaked in errors. | Secrets from the keychain; generic error messages. |
| **threat-model / red-team** | Search for your *own* worst case before the adversary does. | Penetration test; abuse-case review at design time. |

**A seam worth noticing.** `sanitize / validate` is exactly the "narrow the contract" lever from
Chapter 9 — but here its floor is set by an *attacker*, not by natural variance. That is precisely why
"never trust external data" is a **hard gate** (Chapter 11) and not merely good advice: the downside is
non-local.

> ▸ **Chart — "The two repertoires"** · *L2 · cross-cutting.* Left: random hardness → resilient →
> four resilience moves. Right: a directed adversary → secure → four security moves. Same shape,
> different opponent.

```pipeline-graph
{
  "title": "The two repertoires",
  "level": "L2 · cross-cutting",
  "summary": "Two families of cross-cutting responses invoked from reflect: resilience against blind/random hardship, security against a directed adversary. Statistical moves that beat randomness can backfire against a searcher.",
  "zoomOut": "The unit loop, fully staffed",
  "nodes": [
    {"id":"random","label":"RANDOM hardness (#5 change · #6 uncertain) — a blind sampler","group":"stone","x":0,"y":0},
    {"id":"directed","label":"DIRECTED hardness (#8 adversary) — a worst-case searcher","group":"stone","x":640,"y":0},
    {"id":"resilient","label":"→ resilient","group":"property","x":160,"y":110},
    {"id":"secure","label":"→ secure","group":"property","x":800,"y":110},
    {"id":"escalate","label":"escalate","group":"repertoire","x":-40,"y":220},
    {"id":"degrade","label":"degrade","group":"repertoire","x":110,"y":220},
    {"id":"recover","label":"recover","group":"repertoire","x":260,"y":220},
    {"id":"rollback","label":"roll back","group":"repertoire","x":410,"y":220},
    {"id":"authz","label":"authenticate / authorize","group":"repertoire","x":600,"y":220},
    {"id":"sanitize","label":"sanitize / validate","group":"repertoire","x":820,"y":220},
    {"id":"harden","label":"minimise surface / harden","group":"repertoire","x":600,"y":300},
    {"id":"redteam","label":"threat-model / red-team","group":"repertoire","x":820,"y":300}
  ],
  "edges": [
    {"source":"random","target":"resilient","label":"envelope"},
    {"source":"directed","target":"secure","label":"envelope"},
    {"source":"resilient","target":"escalate","member":true},
    {"source":"resilient","target":"degrade","member":true},
    {"source":"resilient","target":"recover","member":true},
    {"source":"resilient","target":"rollback","member":true},
    {"source":"secure","target":"authz","member":true},
    {"source":"secure","target":"sanitize","member":true},
    {"source":"secure","target":"harden","member":true},
    {"source":"secure","target":"redteam","member":true}
  ]
}
```

> **⟐ Under autonomy.** `threat-model / red-team` does double duty. It is the response to the external
> adversary (stone #8) *and* the response to the internal shared blind spot (stone #9): an
> *independent, adversarial* checker who deliberately does not share the builder's assumptions is
> exactly what breaks the doer-checker correlation. An autonomous pipeline has no free human
> escape-hatch to fall back on, so it must inject this independence deliberately.

---

## 9. The mechanism of Done

This is the first deep zoom — *inside a single beat.* Chapter 4 said a "done" is a graded threshold,
not a yes/no; Chapter 6 said every element carries its own target. This chapter shows **how that target
is actually set, inherited, and checked** — and why the mechanism is the same regardless of what
software you are building.

### Origination → propagation → termination

- **Origination (the root).** The top-level "done" has no parent to inherit from. It is **elicited from
  hidden intent by `specify`** (stone #1). This is the one *contingent seed* of the whole tree — it
  cannot be derived, only drawn out.
- **Propagation (internal nodes).** `design` decomposes a parent target *P* into child targets
  {L₁ … Lₙ}, one per part, each cast on the same **four-axis schema** — *scope · reliable · resilient ·
  predictable* — that the top-level target used. The schema is scale-invariant, so every node's target
  has the same shape. In short: `Done(part) = Done(parent), projected onto this part's slice.`
- **Termination (the leaf).** Decomposition stops where a target can be checked *without further
  decomposition* — where `check` yields a genuine yes/no. There are two kinds of leaf:
  - a **deterministic** leaf (logic → an assertion or unit test — passes or fails), and
  - a **statistical** leaf (an irreducible proxy → a threshold on a sampled value: "done with
    confidence ≥ c"). The statistical leaf is where uncertainty and change (stones #5, #6) keep the
    check from ever being perfectly deterministic.

### Decomposition is a bet — the composition hypothesis

To split *P* into parts {Lᵢ} is to *assert* a conjecture:

> **(L₁ ∧ L₂ ∧ … ∧ Lₙ) ⟹ P** — "if every part is done, the whole is done."

This is **not a deduction**; it is a **hypothesis** that `design` makes. Where *P* is qualitative
("feels trustworthy," "is intuitive"), the hypothesis rests on human judgement. So decomposition and
proxy-construction are the *same act*: the conjunction of leaf-targets is a **constructed proxy** for
the parent target, and it inherits every proxy pathology — it can be gamed (Goodhart's law: "all units
pass" is a proxy for "the feature works," and the gap between them is where the bug lives).

**Failure routing.** A composite is done only if (a) its leaves pass *and* (b) the composition
hypothesis holds. If a composite **fails acceptance while all its leaves are green**, the parts kept
their promises but the whole did not — so the **composition hypothesis is falsified**. `analyze`
root-causes to *that hypothesis*, and `decide` **re-targets `design`** to re-decompose — *not* the
leaves. This is "non-convergence points at the target" (Chapter 4), now localised precisely to the
decomposition. To trace such a failure back, the hypothesis must be *written down* — which is why the
design artifact exists (Chapter 10).

**Universal form, contingent content.** The *form* — the four-axis schema, elicit-root → decompose →
bottom-out, the composition-hypothesis structure, the failure-routing rule — is universal, forced by
the stones. The *content* — the specific thresholds, which proxies, which decomposition to bet on — is
contingent. Only the root is elicited; every internal target is derived. This is why "done" generalises
across any software.

> ▸ **Chart — "Done propagation"** · *L3 · inside a beat.* Intent is elicited into a root target;
> `design` decomposes it (each edge a composition hypothesis); leaves bottom out into deterministic or
> statistical checks; a rejected qualitative composite falsifies the hypothesis and routes back to
> `design`.

```pipeline-graph
{
  "title": "Done propagation",
  "level": "L3 · inside a beat",
  "summary": "The root target is elicited from intent; design decomposes it into sub-targets (each edge a composition hypothesis); leaves bottom out into binary checks; a green-leaves-but-rejected composite falsifies the hypothesis and re-targets design.",
  "zoomOut": "The unit loop, fully staffed",
  "zoomIn": ["Design as a bet — stub-composition"],
  "nodes": [
    {"id":"intent","label":"hidden intent","group":"stone","x":0,"y":0},
    {"id":"specify","label":"specify · elicit","group":"element","x":0,"y":95},
    {"id":"root","label":"root target P","group":"beat","x":260,"y":95},
    {"id":"design","label":"design · decompose","group":"element","x":260,"y":195},
    {"id":"cA","label":"sub-target A","group":"beat","x":110,"y":300},
    {"id":"cB","label":"sub-target B · qualitative","group":"beat","x":440,"y":300},
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

### 9.1 Design as a bet — stub-composition

If the composition hypothesis is design's central artifact, then **design is not "draw the structure"
— it is "state and defend a bet"**: a decomposition into components, the **interface contracts** between
them, and the conjecture that they compose to *P*. The valuable property of a bet is that it can be
**refuted cheaply, before the build.**

- **Stub-composition** is how. Replace each component with a **stub** — its interface contract with the
  behaviour deleted (right shape, computes nothing) — and check that the stubs *wire together*. This is
  the `check` beat of the design sub-loop (the fractal again), executed at design time. It is the
  earliest, cheapest place to test the bet.
- **It discharges the arrow, suspends the premises.** A green stub-composition proves only the **⟹** —
  that the contracts are mutually coherent (what A emits is what B accepts, across the graph). It is
  one-sided: it can **fail cheap** (kill a bad decomposition) or **survive**, but it never *confirms*.
- **It factors risk; it does not remove it.** After a green stub-check, provably *zero* design risk
  lives in the wiring, and all of it has been relocated into two named, attackable premises:
  - **Premise A — the leaves are real** (each stub behaves like the real component). Discharged at
    **build time** by `verify` (a unit test on the real leaf) → the *deterministic* leaf.
  - **Premise B — the contract holds across its *whole* range of inputs.** Only *sampled* at build
    (property tests); the residue is caught at **run time** by `observe` (telemetry) → the *statistical*
    leaf.
- **Why it reaches neither premise.** A stub is a proxy for a component that does not exist yet, and
  both premises are claims about *behaviour* — the one thing a stub deletes. So neither becomes a fact
  until the real thing is built and run. That is the single reason design-time checking cannot close
  them; it can only *name* and *route* them.

> ▸ **Chart — "Design as a bet — stub-composition"** · *L3 · inside design.* Design states the bet; a
> design-time stub-composition either fails cheap (→ re-decompose) or survives — discharging the wiring
> and suspending Premise A (→ verify) and Premise B (→ observe).

```pipeline-graph
{
  "title": "Design as a bet — stub-composition",
  "level": "L3 · inside design",
  "summary": "Design states a bet (contracts + composition hypothesis); a cheap design-time stub-composition discharges the wiring and factors the remaining risk into Premise A (leaves real → verify) and Premise B (whole input range → observe).",
  "zoomOut": "Done propagation",
  "zoomIn": ["The premise-B lever"],
  "nodes": [
    {"id":"design","label":"design · state the bet","group":"element","x":0,"y":120},
    {"id":"contracts","label":"interface contracts","group":"property","x":250,"y":40},
    {"id":"hyp","label":"composition hyp (∧Lᵢ)⟹P","group":"beat","x":250,"y":200},
    {"id":"stub","label":"stub-composition (design-time check)","group":"element","x":540,"y":120},
    {"id":"fail","label":"fail → re-decompose","group":"terminal","x":540,"y":280},
    {"id":"survive","label":"survive (conditional)","group":"beat","x":830,"y":120},
    {"id":"wiring","label":"⟹ wiring · discharged","group":"property","x":1090,"y":20},
    {"id":"premA","label":"Premise A · leaves real","group":"beat","x":1090,"y":120},
    {"id":"premB","label":"Premise B · whole input range","group":"beat","x":1090,"y":230},
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

### 9.2 The premise-B lever — the two quality bars of a good bet

Premise B — "the contract holds across its whole range of inputs" — is **not a fixed cost.** Its *size*
is something `design` **chooses**, by how tightly it draws each interface contract. This is the second
quality bar.

- **A tight contract manufactures `predictable` at the seam.** Premise B's residue *is* the
  unpredictability at an interface (the unforeseen input combinations). Tightening dials that residue
  down through the leaf-kinds: **loose** → a range too big to exhaust (a *statistical* leaf, sampled at
  `observe`, residue > 0); **tight** → a range small enough to exhaust (a *deterministic* leaf at
  `verify`, residue → 0); **type-encoded** → illegal values can't even be *constructed* (discharged at
  compile time, never reaching run time).
- **The contract governs the *what*, not the *how*.** It constrains a part's observable inputs and
  outputs while leaving its interior free — which is exactly why a stub can stand in for it, and why
  Premises A and B were separable in the first place. This is encapsulation, derived from first
  principles.
- **There is a floor — so the bar is *tightest-sufficient*, not *tightest*.** Tighten past the **set of
  realities the part must actually serve** and the contract rejects a *valid* input the real need
  sends → the part returns the wrong thing (or nothing) on a legitimate case → **`reliable` breaks**
  (and on the adverse-but-valid cases, `resilient` breaks). The contract's range must equal the
  required set of realities — no wider (needless residue), no narrower (excluded reality).

**So all three point/envelope input-properties re-appear at every seam.** The contract's *floor* (which
realities must cross) is `reliable` (expected) + `resilient` (adverse); the *downward pressure* (how
foreseeably they cross) is `predictable`. The optimum contract is **maximum predictability, subject to
admitting the whole required set of realities.** A good design bet therefore meets two bars: (1) it
**fails cheap** (§9.1), and (2) it carries **tightest-sufficient contracts** (§9.2).

> ▸ **Chart — "The premise-B lever"** · *L3 · inside a contract.* Contract-tightness is a dial:
> tightening buys `predictable` and moves residue from statistical → deterministic → compile-time, but
> the floor is the required set of realities (`reliable` + `resilient`). One step past the floor and
> the contract rejects a valid input.

```pipeline-graph
{
  "title": "The premise-B lever",
  "level": "L3 · inside a contract",
  "summary": "Contract-tightness is a dial that shrinks Premise B (buying predictability, moving residue statistical → deterministic → compile-time), but the floor is the required set of realities. The bar is tightest-sufficient, not tightest.",
  "zoomOut": "Design as a bet — stub-composition",
  "nodes": [
    {"id":"loose","label":"loose contract","group":"property","x":0,"y":0},
    {"id":"tsuff","label":"tightest-sufficient · THE BAR","group":"beat","x":330,"y":0},
    {"id":"over","label":"over-tight","group":"terminal","x":660,"y":0},
    {"id":"stat","label":"statistical leaf → observe (residue > 0)","group":"element","x":0,"y":140},
    {"id":"det","label":"deterministic / compile-time leaf → verify (residue → 0)","group":"element","x":330,"y":140},
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

### 9.3 Security recurses at every seam — the forbidden-output wall

The three input-properties re-appear at every seam as a **floor** (which realities *must* cross).
`secure` re-appears too, as the **complement on the output side**: not "admit the whole required input
set" but "**forbid the whole illegal output set**" — a wall, dual to the floor. So every seam's target
is **four**-axed.

The consequence is sharp: a design can be insecure *no matter how correctly each leaf is built.* The
classic example: store a credential in a repository's `.env` file and add it to `.gitignore`. Every
leaf is green — the reader works, and git really does exclude the file — yet the whole leaks the instant
an un-modelled exit opens (a full-disk backup syncing the working tree to the cloud). The forbidden
output (a secret readable at rest, off-box) is *reachable*, so the security composition hypothesis is
falsified **with green leaves** → root-cause to the *decomposition* → re-target `design` (move the
secret to the keychain).

**Why security is forced at every seam, harder than the other three.** A directed adversary enters at
the *least-defended* seam, so the security of the whole is the **weakest link**, not the average. One
undefended stage is not a local weakness — it is the whole envelope's hole, because the attacker *finds*
it and pivots. So `secure` cannot be defended "mostly": it holds at every seam or it does not hold. This
is why `secure` is a **hard gate wholesale** (Chapter 11).

---

## 10. What each loop leaves behind: the artifacts

**What it is.** An **artifact** is the persistent, explicit carrier of a loop's target, result, or
lesson. Specs, code, tests, telemetry, decision records, post-mortems, version history, runbooks — each
is the durable residue of a beat.

**Why they exist.** Stone #7 (knowledge is distributed and perishable) forces every loop to hand its
information across **two boundaries**: *time* (the knowledge perishes — defeated by **persistence**) and
*agent* (the knowledge is trapped in one head — defeated by an **explicit, external form**). An artifact
is exactly the thing that crosses both. Shared understanding is the *output*; distribution is the
*fact*; the artifact manufactures the shared, durable copy that a head cannot. Artifacts are not process
hygiene — they are *logically forced* the moment a loop's information must cross a boundary it cannot
cross in a head.

**One artifact per beat**, plus two for the cross-cutting machinery:

| Beat / cross-cut | Artifact | Crosses *time* (persist) | Crosses *agent* (make explicit) |
|---|---|---|---|
| **define** (specify · scope · design) | **spec / target doc** — including design's interface contracts + composition hypothesis, written to be executable as stubs | outlives the moment it was framed | a different builder can build from it |
| **do** (implement) | **code** | persists as the running system | a different maintainer can read it |
| **check** (verify · observe) | **tests + telemetry** — tests are `verify`'s build-time carrier; telemetry is `observe`'s run-time sensor | a repeatable, re-runnable check | someone else can run and interpret it |
| **reflect** (analyze · decide) | **decision record (ADR) + post-mortem** | the post-mortem carries the lesson to the *next* iteration | the ADR carries the *why* to a *later* root-causer |
| **repeat over time** | **version history** | *is itself* the durable time-axis | bisect / blame across contributors |
| **resilience repertoire** | **runbooks** | know-how outlives the on-call who learned it | whoever is paged next, not just the first responder |

### The boundary-distance law

How *durable* an artifact is *forced* to be scales with the **distance between its producer and its
consumer**:

- **Forward beats hand off *live*.** A spec is consumed by the code in the same iteration; the code by
  the test right after. Producer and consumer are adjacent, so the written artifact merely **insures**
  the output against boundaries it *might* cross later. Skip it and a future re-reader is inconvenienced.
- **`reflect` feeds *backward*, so its artifact is the *sole channel*.** Its only consumers are a
  *later* agent doing root-cause (the **ADR** — the agent boundary) and a *future* iteration's `define`
  (the **post-mortem** — the time boundary). Both are across a stone-#7 boundary *by construction*. Skip
  it and the output reaches **no one**: the composite failure becomes untraceable (`analyze` is starved,
  so `reflect` collapses into "we know it broke, not why"), and the same failure class recurs forever
  (the Ouroboros evolve edge is unfed, so the loop cannot raise its own floor). This is why the
  reflect-artifact is a **hard gate** (Chapter 11), not documentation hygiene: it is the only *backward*
  channel the loop has, and it is what makes `reflect` the loop's one *learning* beat.

> ▸ **Chart — "The artifacts"** · *L2 · persistence overlay.* Each beat produces its carrier (left →
> middle); each carrier crosses the *time* and/or *agent* boundary (middle → right).

```pipeline-graph
{
  "title": "The artifacts",
  "level": "L2 · persistence overlay",
  "summary": "Stone #7's per-beat carriers. Every loop's information must cross the time boundary (perishable → persist) and the agent boundary (distributed → make explicit); an artifact is the thing that crosses both.",
  "zoomOut": "The unit loop, fully staffed",
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
    {"id":"a_post","label":"ADR + post-mortem","group":"property","x":300,"y":270},
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
    {"source":"a_post","target":"b_agent","dashed":true},
    {"source":"a_post","target":"b_time","dashed":true,"label":"sole channel (backward)"}
  ]
}
```

---

## 11. Hard gates versus graded targets

**What it is.** Most targets are **graded**: `check` measures how well the work did on a quality range,
and `decide` retains discretion — it can *accept* a known gap. A **hard gate** is a leaf where the
*accept* exit is **deleted**: a single violation blocks, full stop, no amount of quality elsewhere buys
it back.

**Why some checks earn a gate and most don't.** The rule is precise: a leaf becomes a hard gate **iff a
single violation is *non-local*** — no amount of green elsewhere can compensate. Three amplifiers make a
violation non-local:

1. **Adversarial (stone #8).** A directed optimiser turns *any* hole into a whole compromise. This
   amplification is *guaranteed*, which is why **all of `secure` is hard, wholesale** (§9.3).
2. **Irreversible.** The damage escapes `recover` and `roll back` — data loss; a *leaked* secret cannot
   be un-leaked. The run-time repertoire can't undo it after the fact.
3. **Machinery-degrading.** The violation blinds the loop's own `check`/`observe`, or couples parts so
   one corrupts another: a swallowed error (no signal), an un-instrumented call (no telemetry), a test
   retrofitted after the code (can't actually falsify), a mutation that couples shared state. This is
   non-local *by construction* — it disables the very thing that would have caught it.

**The predictive rule.** To classify *any* candidate constraint, ask one question: **"Is a single
violation non-local — adversary-amplified, irreversible, or does it blind the loop?"** *Yes* → hard gate
(delete `accept`). *No* → graded target (keep `decide`'s discretion). Two corollaries fall out: a
*graded proxy* wrongly declared a gate (say, an 80%-coverage bar — a statistical-leaf proxy) invites
gaming; and a hard gate with *no* amplifier behind it is mis-typed. Non-compensability — not
"importance" — is what makes a rule a gate.

> ▸ **Chart — "Hard gate or graded target?"** · *L3 · gating overlay.* One decision node: is a single
> violation non-local? Three amplifiers route to *hard gate*; their absence routes to *graded target*.

```pipeline-graph
{
  "title": "Hard gate or graded target?",
  "level": "L3 · gating overlay",
  "summary": "A leaf becomes a non-waivable hard gate iff a single violation is non-local — via one of three amplifiers (adversarial, irreversible, machinery-degrading). Otherwise it stays a graded target.",
  "zoomOut": "The unit loop, fully staffed",
  "nodes": [
    {"id":"leaf","label":"a candidate constraint (leaf check)","group":"beat","x":320,"y":0},
    {"id":"q","label":"is a single violation NON-LOCAL?","group":"terminal","x":320,"y":100},
    {"id":"adv","label":"adversary-amplified (#8)","group":"stone","x":0,"y":220},
    {"id":"irr","label":"irreversible (escapes recover/rollback)","group":"stone","x":300,"y":220},
    {"id":"mach","label":"machinery-degrading (blinds check/observe)","group":"stone","x":640,"y":220},
    {"id":"gate","label":"HARD GATE — delete 'accept'","group":"property","x":180,"y":340},
    {"id":"grade","label":"GRADED TARGET — keep discretion","group":"element","x":560,"y":340}
  ],
  "edges": [
    {"source":"leaf","target":"q"},
    {"source":"q","target":"adv","dashed":true,"label":"yes, via"},
    {"source":"q","target":"irr","dashed":true,"label":"yes, via"},
    {"source":"q","target":"mach","dashed":true,"label":"yes, via"},
    {"source":"adv","target":"gate"},
    {"source":"irr","target":"gate"},
    {"source":"mach","target":"gate"},
    {"source":"q","target":"grade","label":"no amplifier"}
  ]
}
```

> **⟐ Under autonomy.** Two of the hard gates the ideal SDLC insists on — a *written* reflect-artifact
> (Chapter 10) and a real `observe` sensor of the loop's own (Chapter 5) — are gates precisely because
> skipping them is *machinery-degrading*. An autonomous pipeline that skips them doesn't just lose a
> document or a dashboard; it silently demotes `define → do → check → reflect` to `define → do → check`
> — a loop that can *detect* failure but neither *explain* it nor *prevent its recurrence.*

---

## 12. The autonomous / agentic SDLC

Everything so far holds whether the loop is staffed by people or by software agents. This chapter is
about the one place where that stops being true — **the moment you remove the human and let agents run
the whole loop, including judging their own work.**

### The extra stone: reflexivity (stone #9)

In a human-run lifecycle the loop has a quiet luxury: when it checks its own work, the checker is at
least *somewhat* independent of the doer — a different person, a different perspective, and ultimately a
human escape hatch that can say "no, this is wrong" from outside the system. Independence is what lets
you *stack* checks and drive error toward zero. That is the hidden assumption behind the word
"converges," and behind the property **reliable**.

Reflexivity is the brute fact that in an autonomous, multi-agent pipeline **that independence is not
there.** The agents that staff `check` and `reflect` are the same *kind* of erring agent as the doer
(stone #4). Their errors are **correlated**, not independent. And a check is only worth the *new
information* it adds beyond the doer's own belief:

- A checker that shares the doer's blind spot is an **echo chamber**. It agrees for the same wrong
  reasons. It adds **zero bits** of information. "Verify" silently collapses into "declare" — the system
  announces it is correct instead of establishing that it is.
- Stacking more such checkers does not help: correlated checks don't multiply into confidence. There is
  a **common-mode floor** of shared error that no amount of iteration crosses. Even a formal proof
  doesn't escape it — it only *relocates* the blind spot from the code into the spec.

This is why reflexivity is a genuinely *new* stone and not just a restatement of "we err" (stone #4).
Stone #4 is the *marginal* fact — each agent errs. Reflexivity is the *joint* fact — their errors are
correlated. You can grant that every agent is individually excellent and reflexivity still bites,
because it is a statement about the *relationship between* the checkers, not about any one of them. And
it is a fact about the *solver*, not about the problem — which makes it the model's first
**second-order** stone.

### The consequence: an autonomous loop cannot be its own ground truth

Put the pieces together. Reliability is manufactured by convergence; convergence assumes independence;
independence in an autonomous pipeline comes only from the terminal (the outside judge); remove the human
and the terminal's independence goes to zero. Therefore a fully autonomous loop, left to itself, can
converge confidently to a **wrong** fixed point — a green check sitting on top of a real defect — and
have no way to know. **An autonomous loop cannot be its own ground truth.**

Notice the shape of the failure. It is not that the agents are lazy or careless; a diligent,
high-quality autonomous loop fails *this specific way* — by being *confidently* wrong, because every part
of it agrees. That is worse than a loud failure, because the loop's own signals all say "fine."

> ▸ **Chart — "Reflexivity — the autonomous regime"** · *L4 · the autonomous regime.* The doer and
> checker share a correlated fault, so the check becomes an echo chamber and "verify" collapses into
> "declare." Independence is what manufactures reliability; the human/external terminal supplies it;
> removing it drives independence to zero; deliberate adversarial review restores some of it.

```pipeline-graph
{
  "title": "Reflexivity — the autonomous regime",
  "level": "L4 · the autonomous regime",
  "summary": "When the checker shares the doer's blind spot, the check adds zero information and 'verify' collapses into 'declare'. Independence is what drives error → 0; removing the human terminal drives it to zero; adversarial/diverse review must be injected to restore it.",
  "zoomOut": "The complete circuit",
  "nodes": [
    {"id":"corr","label":"errors are CORRELATED (#9)","group":"stone","x":130,"y":0},
    {"id":"doer","label":"doer (agent)","group":"element","x":0,"y":90},
    {"id":"checker","label":"checker (agent, same kind)","group":"element","x":280,"y":90},
    {"id":"echo","label":"echo-chamber — check adds 0 bits","group":"terminal","x":280,"y":185},
    {"id":"declare","label":"verify collapses into 'declare'","group":"terminal","x":280,"y":265},
    {"id":"human","label":"human / external terminal (partial independence)","group":"terminal","x":650,"y":0},
    {"id":"indep","label":"INDEPENDENCE — what drives error → 0","group":"property","x":650,"y":95},
    {"id":"auto","label":"remove the human → independence at terminal → 0","group":"stone","x":650,"y":185},
    {"id":"redteam","label":"inject independence: adversarial / diverse review · red-team","group":"repertoire","x":650,"y":265},
    {"id":"reliable","label":"reliable (eroded if autonomous)","group":"property","x":1010,"y":95}
  ],
  "edges": [
    {"source":"corr","target":"doer","member":true},
    {"source":"corr","target":"checker","member":true},
    {"source":"checker","target":"echo","dashed":true},
    {"source":"echo","target":"declare","dashed":true},
    {"source":"human","target":"indep","label":"supplies"},
    {"source":"indep","target":"reliable","label":"manufactures"},
    {"source":"auto","target":"indep","dashed":true,"label":"removes"},
    {"source":"redteam","target":"indep","label":"restores"},
    {"source":"declare","target":"reliable","dashed":true,"label":"erodes"}
  ]
}
```

### What the ideal autonomous SDLC must therefore add

Reflexivity does not forbid autonomy — it **prices** it. Because an autonomous loop has no free human
terminal to fall back on, it must **manufacture independence deliberately.** Concretely:

- **A non-removable external / human terminal.** Keep at least one genuinely independent judge in the
  escalation path — a human, or a check whose errors are demonstrably *uncorrelated* with the doer's
  (different model family, different training, different method). The point is not "a human because
  humans are better"; it is "a terminal whose blind spots differ from the doer's."
- **Deliberate adversarial and diverse review.** `threat-model / red-team` (Chapter 8) does double duty
  here: a reviewer instructed to *disagree*, seeded with different assumptions, breaks the doer-checker
  correlation. Diversity of method is the mechanism; adversariality is how you force it.
- **Independence budgeting.** Treat independence as a resource to be spent where a wrong-but-confident
  convergence would be most costly — exactly the non-compensatory seams that earn hard gates
  (Chapter 11). You cannot make every check independent; you *can* make the load-bearing ones
  independent.

### How this threads back through the document

The autonomy callouts scattered through the earlier chapters are all facets of this one stone:

- **Chapter 2** — reflexivity erodes **reliable** specifically, because reliability is the property that
  depends on convergence-under-independence.
- **Chapter 4** — the human **escape hatch** is the loop's only independent terminal; autonomy cuts it.
- **Chapter 8** — the security repertoire's **red-team** move is also the independence-injection move.
- **Chapter 11** — the **reflect-artifact** and **observe-sensor** gates matter more under autonomy,
  because a self-checking loop that also skips its memory and senses has nothing left to catch it.

The one-line takeaway: **autonomy is not free; it removes the loop's independent ground, and an ideal
autonomous SDLC is one that pays that cost back on purpose — with an outside terminal and engineered
adversarial diversity — precisely where being confidently wrong would hurt most.**

---

## Appendix A — Glossary

Plain-language definitions of the recurring terms.

- **Stone.** A brute, unavoidable fact about reality that makes software hard and *forces* a specific
  response. There are nine (Chapter 3).
- **The loop / the atom.** The single feedback cycle `define → do → check → reflect ↺` that everything
  reduces to (Chapter 4).
- **Beat.** One of the four scale-invariant phases of the loop (define, do, check, reflect).
- **Element.** The outermost loop's concrete staffing of a beat (specify, scope, design, implement,
  verify, observe, analyze, decide).
- **Fractal.** The property that the loop repeats, unchanged in shape, both up across scope and down
  into each element (Chapter 6).
- **Point-property.** A property measured at a single task in a single context: *reliable*, *predictable*.
- **Envelope-property.** A property measured across the range of contexts over time: *resilient* (vs.
  random hardship), *secure* (vs. a directed adversary).
- **Graded target.** A "done" expressed as a threshold on a quality range, checked by measurement — as
  opposed to a yes/no.
- **Proxy.** A measurable stand-in for a quality you can't measure directly (coverage for "well-tested,"
  latency for "feels fast"). Proxies can be gamed — the gap between proxy and intent is where defects
  hide.
- **Composition hypothesis.** The bet `design` makes that "if every part is done, the whole is done"
  — `(∧Lᵢ) ⟹ P`. Falsifiable; when a composite fails with green leaves, this hypothesis is what broke.
- **Stub-composition.** Wiring together behaviour-less stubs of each component at design time, to cheaply
  refute a bad decomposition before building.
- **Premise A / Premise B.** After stub-composition, the two remaining risks: A = "the leaves are real"
  (checked at build by `verify`); B = "the contract holds across its whole input range" (sampled at
  build, residue caught at run time by `observe`).
- **Leaf.** A target checkable without further decomposition — *deterministic* (an assertion) or
  *statistical* (a threshold on a sampled value).
- **Repertoire.** A set of cross-cutting responses invoked from `reflect`: the *resilience* repertoire
  (escalate, degrade, recover, roll back) and the *security* repertoire (authn/authz, sanitize, harden,
  red-team).
- **Hard gate.** A leaf whose *accept* exit is deleted — non-waivable — because a single violation is
  non-local (Chapter 11).
- **Amplifier.** One of the three things that make a violation non-local: adversarial, irreversible,
  machinery-degrading.
- **Artifact.** The persistent, explicit carrier of a loop's target / result / lesson across the *time*
  and *agent* boundaries (Chapter 10).
- **Boundary-distance law.** The forced durability of an artifact scales with the distance between its
  producer and its consumer; `reflect`'s backward-feeding artifact is the extreme case (the sole
  channel).
- **Reflexivity.** The second-order, autonomous-only stone: an agent-staffed checker shares the doer's
  correlated blind spot, so its checks add no information unless independence is injected (Chapter 12).
- **Independence.** The property — across checkers — that lets stacked checks drive error toward zero.
  Never total; supplied mainly by an external/human terminal.
- **Ouroboros / evolve.** The product-level feedback edge that feeds run-time learning back into the
  target, turning the loop into an improving spiral.

## Appendix B — The stones-to-responses matrix

One table, the whole causal skeleton.

| Stone | Fact | Forced response(s) | Property served |
|---|---|---|---|
| 1 | intent is hidden | `specify` (elicit the root target) | reliable |
| 2 | unbounded vs. finite | `scope`, `decide` | predictable |
| 3 | complexity > one step | `design` (decompose + composition hypothesis) | all four, at every seam |
| 4 | humans & models err | `verify`, `analyze` | reliable |
| 5 | reality keeps changing | version / integrate / regression; `roll back` | resilient |
| 6 | reality is uncertain | `observe` (telemetry); `degrade`, `recover` | resilient |
| 7 | knowledge distributed & perishable | **artifacts** (persist + make explicit) | all four (carries every loop's output) |
| 8 | adversarial actors | security repertoire (authn/authz, sanitize, harden, red-team) | secure |
| 9 | reflexivity *(autonomous only)* | independence-seeking (external terminal, adversarial/diverse review) | protects reliable |

## Appendix C — Provenance and status

- **Status.** This document presents the **ideal MUST-HAVE** design: what *any* reliable, predictable,
  resilient, and secure SDLC is logically forced to contain. It deliberately does **not** audit any
  particular real-world setup against the ideal — that is a separate exercise, kept out so the ideal
  stays uncontaminated.
- **Source of the derivation.** Every claim here is derived, step by step, in the companion working file
  [`sdlc-first-principles-canvas.md`](sdlc-first-principles-canvas.md), which also holds the audit trail
  — the Socratic question-and-answer history, the iteration log, and the still-open research tracks
  (for example: the precise boundary between a graded proxy and a hard gate; the regression/rollback
  machinery for the change axis; whether "second-order" is a distinct *class* of stone worth
  formalising). When you want to know *why* a piece is shaped the way it is, or *how* we got here, read
  the canvas; when you want to *understand the design*, read this.
- **The charts are regenerable.** Every chart on this page is a fenced `pipeline-graph` block in this
  file. Edit the block (or drag nodes in the viewer and use **Export**) and the picture updates — the
  visuals never drift from the text.
