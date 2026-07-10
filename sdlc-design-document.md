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
| **L1** | The bedrock — ten forces | The brute facts that make the work hard | [Ch. 3](#3-the-bedrock-why-the-work-is-hard) |
| **L2** | The unit loop, fully staffed | The atom — one feedback loop, and its elements | [Ch. 4](#4-the-atom-the-unit-control-loop) |
| **L2** | The fractal — one shape, every scale | How the loop repeats up and down, and where it stops | [Ch. 6](#6-the-fractal-one-shape-at-every-scale) |
| **L2** | Feature A — rate limiting, every element opened | The fractal made concrete on a graded feature | [Ch. 6](#6-the-fractal-one-shape-at-every-scale) |
| **L3** | Feature B — password reset, opened inward | The same shape where security forbids skipping | [Ch. 6](#6-the-fractal-one-shape-at-every-scale) |
| **L3** | When the loop collapses | Which ceremony is reducible, and the two overrides | [Ch. 6](#6-the-fractal-one-shape-at-every-scale) |
| **L2** | The lifecycle (process flow) | The familiar lifecycle, as a projection of the loop | [Ch. 7](#7-the-lifecycle-the-process-flow) |
| **L3** | The schedule bet | How `plan` bets a date — and which half of the bet is gated | [Ch. 7](#7-the-lifecycle-the-process-flow) |
| **L2** | The two repertoires | Cross-cutting responses: resilience vs. security | [Ch. 8](#8-the-two-repertoires-resilience-and-security) |
| **L3** | Done propagation | How a target is set, inherited, and checked | [Ch. 9](#9-the-mechanism-of-done) |
| **L3** | Design as a bet — stub-composition | How design states and cheaply tests its bet | [Ch. 9](#9-the-mechanism-of-done) |
| **L3** | The premise-B lever | How one interface contract is tuned | [Ch. 9](#9-the-mechanism-of-done) |
| **L2** | The artifacts | What each loop leaves behind, and why | [Ch. 10](#10-what-each-loop-leaves-behind-the-artifacts) |
| **L3** | The change axis — regression & rollback | Stone #5's two organs: fixes stick, changes stay reversible | [Ch. 10](#10-what-each-loop-leaves-behind-the-artifacts) |
| **L3** | Hard gate or graded target? | Which checks are non-negotiable | [Ch. 11](#11-hard-gates-versus-graded-targets) |
| **L3** | The convergent law | One law, four instances: existence gated, fidelity graded | [Ch. 11](#11-hard-gates-versus-graded-targets) |
| **L4** | The second-order tier — the delegated/autonomous regime | Why an autonomous loop can neither judge nor trust itself | [Ch. 12](#12-the-autonomous-agentic-sdlc) |

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
  "zoomIn": ["The four properties", "The bedrock — ten forces", "The unit loop, fully staffed"],
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
    {"id":"reflexivity","label":"reflexivity (#9 · autonomous only)","group":"stone","x":-200,"y":40},
    {"id":"incentives","label":"incentive-divergence (#10 · delegated only)","group":"stone","x":-200,"y":560}
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
    {"source":"reflexivity","target":"reliable","dashed":true,"label":"erodes if autonomous (#9)"},
    {"source":"incentives","target":"reliable","dashed":true,"label":"erodes if delegated (#10)"}
  ]
}
```

> **⟐ Under autonomy.** Notice the two coral nodes on the left — *reflexivity* (#9) and
> *incentive-divergence* (#10), the **second-order tier** — each with a dashed edge reaching up to
> **reliable**. In a human-run lifecycle both are dormant. Delegate the loop to self-checking,
> self-interested agents and they activate, eroding the very property the loop works hardest to
> manufacture. Chapter 12 is entirely about these two edges.

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

> **"Predictable" has three faces, bought by three different mechanisms.** Boundedness buys only the
> **cost** face — this piece of work stops within a known number of tries. The **outcome** face — you
> can call *what* comes out of a seam — is bought by tight interface contracts (§9.2). And the
> **schedule** face — you can call *when* the whole thing ships — is not a point-property at all but
> an aggregate over the time axis, bought by its own mechanism: the **schedule bet** (§7.1).

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
> Reliability is manufactured by a loop that *converges* — but convergence quietly assumes two things about
> who staffs it: that the checker is **independent** of the doer, and that the doer is **faithful** to the
> target. Delegation can break either — a checker that shares the doer's blind spot (stone #9), or an
> executor that serves its own payoff (stone #10) — and both let the loop *declare* success instead of
> establishing it: a green check over a real defect. These are the two **second-order** stones; see
> Chapter 12.

---

## 3. The bedrock: why the work is hard

**What it is.** First principles, literally: the unavoidable truths about reality that make software
engineering hard. We call them **stones**. Every stage, tool, and artifact in the SDLC is a *response*
to one or more stones — never a convention. There are **eight** first-order stones (facts about the
*problem*), plus **two** second-order stones (facts about the *solver* — about who staffs the loop) that
activate only when the work is delegated or fully autonomous. The eight first-order stones are
**pairwise-irreducible**: none is a special case of another.

**Why this matters.** The stones are the model's foundation and its test. If a needed element rests on
*no* stone, the model has a spurious part. If a stone has *no* element defending it, the model has a
gap. This "self-test" is how the model grows — and it has fired **in reverse three times**, each time a
needed response was found resting on no stone: the security defenses exposed stone #8; the loop's own
checker, resting on an unguaranteed *independence*, exposed stone #9; and the loop's own executor,
resting on an unguaranteed *faithfulness*, exposed stone #10. A **third direction** of the self-test
guards against double-counting — two faces of a pressure are **one** stone only if they share a *single*
forced response (the **bundling rule**). That is why "distributed" and "perishable" fold into one stone
(#7 — both answered by *artifacts*), while "change" and "uncertain" stay two (#5 and #6 — answered by
different machinery).

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

### The second-order tier — two stones about who staffs the loop

The first eight stones are facts about the *problem*. The last two are different in kind — they are
facts about the **solver**, specifically about *who staffs the loop* once the work is delegated to other
minds (human or agent). They form a small **second-order tier**, and they share three traits: each is
**relational** (you cannot even state it with a single mind), each is **conditional** (it collapses back
to nothing when one aligned mind does everything), and each erodes **reliable** by hollowing a genuine
`check` into a bare `declare`. The tier has exactly **two seats**, because the loop makes exactly two
silent assumptions about the minds it delegates to — that the checker is **independent**, and that the
doer is **faithful**.

9. **Reflexivity — the checker shares the doer's fault.** *(Second-order, conditional — it bites in an
   automated, autonomous, multi-agent pipeline.)* The agents that staff `check` and `reflect` are the
   same *kind* of erring agent as the doer (stone #4), so their errors are not independent — they are
   **correlated**. A check is only worth the *new information* it adds beyond the doer's own belief; a
   checker that shares the doer's blind spot is an **echo chamber** that adds zero information, and
   "verify" quietly collapses into "declare." The property at stake is **independence** — the thing that
   lets stacked checks drive error toward zero — and reflexivity is the brute fact that independence is
   *never total* (even a formal proof only relocates the blind spot into the spec). It is irreducible to
   "we err" (stone #4): #4 is the *marginal* fact — each agent errs; reflexivity is the *joint* fact —
   their errors correlate. *Breach → an **echo-chamber** check; the forced response is independence.*

10. **Incentive-divergence — the doer serves a different master.** *(Second-order, conditional — it
    bites when the work is delegated to a self-interested agent.)* A mind you delegate to has its **own
    utility**. Even when it knows your intent exactly — so this is *not* hidden intent (stone #1) — it
    may optimise *its* payoff over *your* target. This is a *directed* pressure, like an adversary's, but
    aimed not at your **failure** (stone #8, hostile) — at a **different goal** (misaligned); your loss
    is collateral, not the objective. It is irreducible: not #1 (known ≠ unwanted), not #4 (a *choice*,
    not an accidental slip), not #8 (misaligned ≠ hostile). Its *unintentional* face — gaming a proxy
    when true intent is hidden — reduces to stone #1 plus Goodhart; its **willful** face does not, and it
    forces its own response — **alignment** (reward design, skin-in-the-game, making the payoff track
    true-Done) — which is not in the security repertoire and does not fall out of reflexivity's
    independence-seeking. *Breach → a **self-serving** check; the forced response is alignment.*

Both stones turn a real `check` into a hollow `declare` — one by *shared blindness* (the checker cannot
see the error), the other by *divergent will* (the executor will not surface or fix it even when it
can). Both are conditional on delegation: with one aligned mind — or a genuinely independent, faithful
terminal — the tier is bounded; remove that terminal and **an autonomous loop can neither judge nor
trust itself.** Both are treated in full, with their forced responses, in **Chapter 12**.

> ▸ **Chart — "The bedrock — ten forces"** · *L1 · the forces.* Each stone on the left; the element
> or repertoire it forces on the right. This is the "why" behind every part of the loop.

```pipeline-graph
{
  "title": "The bedrock — ten forces",
  "level": "L1 · the forces",
  "summary": "The ten brute facts, each wired to the specific response it forces into existence. Eight are first-order (about the problem); the last two are the second-order tier (about who staffs the loop — independence and faithfulness). Nothing in the loop is a convention; every part defends a stone.",
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
    {"id":"incentives","label":"10 · incentive-divergence (2nd-order · delegated)","group":"stone","x":0,"y":730},
    {"id":"specify","label":"specify","group":"element","x":520,"y":0},
    {"id":"scope","label":"scope & decide","group":"element","x":520,"y":80},
    {"id":"design","label":"design (decompose)","group":"element","x":520,"y":160},
    {"id":"verify","label":"verify + analyze","group":"element","x":520,"y":240},
    {"id":"resilience","label":"resilience repertoire","group":"repertoire","x":520,"y":340},
    {"id":"observe","label":"observe (telemetry)","group":"element","x":520,"y":430},
    {"id":"artifacts","label":"artifacts","group":"property","x":520,"y":500},
    {"id":"security","label":"security repertoire","group":"repertoire","x":520,"y":570},
    {"id":"independence","label":"independence-seeking (external terminal · red-team)","group":"terminal","x":520,"y":650},
    {"id":"alignment","label":"alignment (reward design · skin-in-the-game)","group":"terminal","x":520,"y":730}
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
    {"source":"reflexivity","target":"independence","label":"forces","dashed":true},
    {"source":"incentives","target":"alignment","label":"forces","dashed":true}
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
| **repeat over time** | **version · integrate · regression-test** | reality keeps changing (#5) | Keeps the loop running as the target moves. `regression-test` is not a standalone element — it is the forced **`reflect` → `verify` bridge**: a fixed failure's lesson compiled into an auto-firing check (§10.1). |

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
**fractal**: the same `define → do → check → reflect` shape repeats **in both directions** —

- **Outward, across scope.** An action sits inside a feature, inside a stage, inside a release, inside
  a product. `design` carves the whole into parts, and *each part becomes its own loop* — emergent, not
  staffed by a separate element.
- **Inward, into every element.** Addressing a single element — `specify`, `verify`, `decide` — is
  *itself* a full `define → do → check → reflect` loop, with its own target and its own check.

**Why it must be a fractal.** Complexity (stone #3) forces decomposition, and a decomposed part is just
a smaller instance of the same problem — so it needs the same machine. A second mechanism at each level
would multiply the stones' responses without cause. One shape, reused, is the minimal answer.

**The honest objection to the abstract version.** Chapter 4's chart shows the shape in the abstract, and
relabelling four blank boxes `define/do/check/reflect` *asserts* the inward claim without ever
*instantiating* it. The rest of this chapter earns it: §6.1 states the move once as a recipe; §6.2 and
§6.3 run that recipe end-to-end on two real features — every element opened, every box filled — and §6.4
answers the sharp question their concreteness invites: **is all of this mandatory, or does the ceremony
collapse when it would cost more than it saves?**

> ▸ **Chart — "The fractal — one shape, every scale"** · *L2 · scaling.* The scope nesting (top); any
> scope expanding into the four beats (middle); any beat or element expanding into its own four-beat loop
> (bottom). Escalation runs upward to a human; a dashed exit runs to *bedrock* — a leaf so certain it
> collapses to bare `do` (the base case, §6.4).

```pipeline-graph
{
  "title": "The fractal — one shape, every scale",
  "level": "L2 · scaling",
  "summary": "The same loop nested outward across scope (action ⊂ … ⊂ product) and inward into every element; escalation runs upward to a human, and a certain-enough leaf collapses to bare do (the base case, §6.4).",
  "zoomOut": "The unit loop, fully staffed",
  "zoomIn": ["Feature A — rate limiting, every element opened", "When the loop collapses — is the ceremony a must?", "The lifecycle (process flow)"],
  "nodes": [
    {"id":"s_action","label":"action","group":"element","x":0,"y":0},
    {"id":"s_feature","label":"feature","group":"element","x":150,"y":0},
    {"id":"s_stage","label":"stage","group":"element","x":300,"y":0},
    {"id":"s_release","label":"release","group":"element","x":450,"y":0},
    {"id":"s_product","label":"product","group":"element","x":600,"y":0},
    {"id":"b_define","label":"define","group":"beat","x":150,"y":140},
    {"id":"b_do","label":"do","group":"beat","x":330,"y":140},
    {"id":"b_check","label":"check","group":"beat","x":510,"y":140},
    {"id":"b_reflect","label":"reflect","group":"beat","x":690,"y":140},
    {"id":"human","label":"human (escape hatch)","group":"terminal","x":900,"y":140},
    {"id":"c_define","label":"define","group":"beat","x":150,"y":290},
    {"id":"c_do","label":"do","group":"beat","x":330,"y":290},
    {"id":"c_check","label":"check","group":"beat","x":510,"y":290},
    {"id":"c_reflect","label":"reflect","group":"beat","x":690,"y":290},
    {"id":"bedrock","label":"bedrock — bare `do` (base case, §6.4)","group":"terminal","x":470,"y":420}
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
    {"source":"b_reflect","target":"c_define","member":true,"label":"any beat/element = a loop ↓"},
    {"source":"c_define","target":"c_do"},
    {"source":"c_do","target":"c_check"},
    {"source":"c_check","target":"c_reflect"},
    {"source":"c_reflect","target":"c_define","dashed":true,"label":"re-target ↺"},
    {"source":"c_reflect","target":"b_reflect","dashed":true,"label":"escalate ↑"},
    {"source":"c_reflect","target":"bedrock","dashed":true,"label":"or collapses to →"}
  ]
}
```

---

### 6.1 The move, stated once — and where it stops

Addressing any element is a loop because the element has its own hidden target, its own way to be wrong,
and its own finite budget — the same stones, one scale down. Two facts make the inner loop more than a
slogan:

- **Its inner `check` is a real, distinct question.** Not "did the feature work?" but "is *this
  element's own output* good enough?" — and for several elements that question is *meta*: `verify` asks
  whether the evidence even covers the risk; `design` asks whether the decomposition wires up at all
  (§9.1).
- **Its inner `escalate` is the parent's escalate.** When an element's own loop exhausts its tries, it
  hands *up* — and the thing it hands to is the beat above it. The `escalate ↑` arrow in every chart is
  not re-invented per level; it is an inner loop surfacing. The fractal closes on itself.

Here is the whole recipe — the generic inner loop of each element, instantiated once and reused for both
examples below:

| Element (beat) | Its inner loop | What its inner `check` asks | What its inner `escalate` means |
|---|---|---|---|
| `specify` (define) | elicitation | does the draft cover every reality, unambiguously? | the *need* itself is unclear — ask a human |
| `scope` (define) | boundary-drawing | is the slice coherent and within budget? | can't fit a coherent slice — need more budget |
| `design` (define) | decomposition (§9.1) | do the stubs wire up — is the bet refuted cheaply? | no clean decomposition — the spec may be wrong |
| `implement` (do) | write–run–fix (TDD) | does the unit pass its own test? | can't pass — the interface/design is wrong |
| `verify` (check) | meta-check | does the evidence actually cover the risky paths? | can't build a trustworthy check — use a proxy / human |
| `observe` (check) | instrumentation | is the run-time signal faithful, not blind? | reality has a mode we can't see |
| `analyze` (reflect) | diagnosis | does the hypothesis reproduce / explain the evidence? | can't root-cause with what I can see |
| `decide` (reflect) | deliberation | does the chosen exit survive a pre-mortem? | beyond my budget / authority |

The recursion does not run forever. It **bottoms out** at `implement`'s leaf — a step so atomic and
certain that its `check` and `reflect` carry no information (a keystroke cannot be "wrong" in a way worth
a loop). That base case — and when a loop may collapse *early* — is §6.4.

---

### 6.2 Example 1 — Feature A: rate limiting (a graded feature)

**The feature.** Protect a public API so no client can exhaust it, while legitimate bursts still
succeed. The outer loop, concretely: `define` = "≤600 req/min per key, bursts still pass, over-limit →
`429` + `Retry-After`"; `do` = a token-bucket over Redis counters; `check` = a load test plus production
telemetry (0.2% of *legitimate* traffic is being throttled); `reflect` = the loop won't converge — the
false-positive rate is too high.

Now open every element. The chart shows the skeleton and names each element's inner loop; the table that
follows *is* the full expansion — every row is a complete `define → do → check → reflect`.

> ▸ **Chart — "Feature A — rate limiting, every element opened"** · *L2 · concrete.* The four beats,
> staffed by the eight elements with their real jobs. Each element is itself a loop (detailed in the
> table); `reflect`'s two elements are opened fully in the next chart.

```pipeline-graph
{
  "title": "Feature A — rate limiting, every element opened",
  "level": "L2 · concrete",
  "summary": "The rate-limiting feature as one define→do→check→reflect loop, staffed by eight elements with their real jobs; each element is itself a loop (see the table), and reflect's two elements open fully in the next chart.",
  "zoomOut": "The fractal — one shape, every scale",
  "zoomIn": ["Feature A — the reflect beat, opened inward", "Feature B — password reset, every element opened"],
  "nodes": [
    {"id":"define","label":"define — the limit target","group":"beat","x":0,"y":0},
    {"id":"do","label":"do — build the limiter","group":"beat","x":300,"y":0},
    {"id":"check","label":"check — measure it","group":"beat","x":600,"y":0},
    {"id":"reflect","label":"reflect — it won't converge","group":"beat","x":900,"y":0},
    {"id":"specify","label":"specify · elicit 429 + burst rule","group":"element","x":-20,"y":100},
    {"id":"scope","label":"scope · 3 hot write routes","group":"element","x":-20,"y":175},
    {"id":"design","label":"design · 4 parts + fail-open","group":"element","x":-20,"y":250},
    {"id":"implement","label":"implement · token-bucket (TDD)","group":"element","x":300,"y":100},
    {"id":"verify","label":"verify · load + window-edge test","group":"element","x":600,"y":100},
    {"id":"observe","label":"observe · throttle telemetry","group":"element","x":600,"y":175},
    {"id":"analyze","label":"analyze · diagnose the misfires","group":"element","x":900,"y":100},
    {"id":"decide","label":"decide · deliberate the exit","group":"element","x":900,"y":175},
    {"id":"human","label":"human — escape hatch","group":"terminal","x":1180,"y":40}
  ],
  "edges": [
    {"source":"define","target":"do"},
    {"source":"do","target":"check"},
    {"source":"check","target":"reflect"},
    {"source":"reflect","target":"define","dashed":true,"label":"re-target ↺"},
    {"source":"reflect","target":"human","dashed":true,"label":"escalate → human"},
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

| Element | inner `define` | inner `do` | inner `check` | inner `reflect` — exits |
|---|---|---|---|---|
| `specify` | a complete, testable limit rule | draft "≤600/min per key; bursts ≤20/2s pass; over → `429` + `Retry-After`" | review vs realities: shared NAT, auth vs anon, retries — is "client" an IP or a key? | ambiguity → re-target to "per API key"; else accept; escalate to the PO |
| `scope` | the coherent slice that fits budget | limit the 3 hottest write routes; defer per-IP anon + distributed quota | is the slice coherent and the abuse surface covered? | too thin → redraw; accept; escalate for budget |
| `design` | parts + contracts that compose to the target | {policy store · Redis counters · middleware · `429` responder}; fail-open on Redis-down | stub-composition (§9.1): do the stubs wire? is Redis-down covered? | seam gap → re-decompose; survive → suspend Premise A/B; escalate |
| `implement` | the unit contract: "21st in window → `429`" | write the token-bucket | run the unit test | fail → fix; pass → accept; escalate if it can't pass — *this is where recursion bottoms out* |
| `verify` | evidence that we built the spec | unit + integration + load test | does the evidence cover the **window edge**? — *initially no* | blind spot → add an edge test; accept; escalate |
| `observe` | a run-time signal reality matched the model | emit `throttled_total{key,outcome}`, false-positive rate on legit traffic | is the "legit vs abuse" label trustworthy? | signal lies → re-instrument; accept; escalate |
| `analyze` | an explanation for *every* false throttle | hypothesis: fixed-window edge bursts | 429s vs time-in-window → 2× at the edges | cause found → hand to `decide`; else new hypothesis; escalate |
| `decide` | pick the exit fitting ≤2 tries, min cost | weigh {accept + document · switch → sliding-window · escalate for per-user infra} | pre-mortem sliding-window: +8% memory — acceptable | commit re-target(`design`); reconsider; **escalate ↑ = the outer loop's escalate** |

**Two rows repay a second look.** `verify`'s inner `check` is a *check on the check*: the first load
test passed, but never exercised the **window edge** — so "verified" was a proxy that missed the real
risk (Goodhart, §9). That untested edge is exactly what `observe` later catches in production and what
`analyze` then root-causes. And because `reflect` is where the loop's thinking lives, it is worth seeing
fully opened:

> ▸ **Chart — "Feature A — the reflect beat, opened inward"** · *L3 · inside reflect.* `analyze` runs a
> diagnosis loop (hypothesise → test against the evidence → refine); `decide` runs a deliberation loop
> (frame the exits → pick → pre-mortem → commit). `decide`'s inner `escalate` *is* the outer loop's
> `escalate` — the arrow you can trace to close the fractal.

```pipeline-graph
{
  "title": "Feature A — the reflect beat, opened inward",
  "level": "L3 · inside reflect",
  "summary": "reflect's two elements as full loops: analyze runs a diagnosis loop (hypothesise → test against evidence → refine), decide runs a deliberation loop (frame exits → pick → pre-mortem → commit); decide's inner escalate is the outer loop's escalate.",
  "zoomOut": "Feature A — rate limiting, every element opened",
  "zoomIn": ["When the loop collapses — is the ceremony a must?"],
  "nodes": [
    {"id":"analyze","label":"analyze (a diagnosis loop)","group":"element","x":0,"y":0},
    {"id":"a_def","label":"define · explain all misfires","group":"beat","x":250,"y":0},
    {"id":"a_do","label":"do · hyp: window-edge bursts","group":"beat","x":520,"y":0},
    {"id":"a_chk","label":"check · 2× at the edge","group":"beat","x":790,"y":0},
    {"id":"a_ref","label":"reflect · cause found / new hyp","group":"beat","x":1060,"y":0},
    {"id":"decide","label":"decide (a deliberation loop)","group":"element","x":0,"y":175},
    {"id":"d_def","label":"define · pick exit, ≤2 tries","group":"beat","x":250,"y":175},
    {"id":"d_do","label":"do · weigh 3 exits","group":"beat","x":520,"y":175},
    {"id":"d_chk","label":"check · pre-mortem: +8% mem","group":"beat","x":790,"y":175},
    {"id":"d_ref","label":"reflect · commit / escalate ↑","group":"beat","x":1060,"y":175},
    {"id":"accept","label":"accept · known issue","group":"terminal","x":520,"y":310},
    {"id":"op_ref","label":"↑ the outer loop's reflect","group":"beat","x":1320,"y":60},
    {"id":"human","label":"human (escape hatch)","group":"terminal","x":1320,"y":175}
  ],
  "edges": [
    {"source":"analyze","target":"a_def","member":true,"label":"⟳"},
    {"source":"a_def","target":"a_do"},
    {"source":"a_do","target":"a_chk"},
    {"source":"a_chk","target":"a_ref"},
    {"source":"a_ref","target":"a_def","dashed":true,"label":"re-target"},
    {"source":"a_ref","target":"decide","label":"cause → decide"},
    {"source":"decide","target":"d_def","member":true,"label":"⟳"},
    {"source":"d_def","target":"d_do"},
    {"source":"d_do","target":"d_chk"},
    {"source":"d_chk","target":"d_ref"},
    {"source":"d_ref","target":"d_def","dashed":true,"label":"reconsider"},
    {"source":"d_do","target":"accept","label":"accept"},
    {"source":"d_ref","target":"op_ref","dashed":true,"label":"escalate ↑ = outer escalate"},
    {"source":"op_ref","target":"human","dashed":true,"label":"→ escape hatch"}
  ]
}
```

---

### 6.3 Example 2 — Feature B: password reset (a hard-gated feature)

**The feature.** Let a user who has forgotten their password regain access — *securely*. The outer loop:
`define` = "email → a 30-min single-use token → set a new password, without revealing whether the email
is registered, invalidating other sessions on completion"; `do` = the flow; `check` = tests, a security
review, and telemetry (completion sits at a low 68%); `reflect` = why so low?

The *same eight elements*, the *same recipe* — but a directed adversary (stone #8) changes what the inner
checks must ask and, decisively, removes `decide`'s freedom to skip them.

> ▸ **Chart — "Feature B — password reset, every element opened"** · *L2 · concrete.* The identical
> skeleton to Feature A — the fractal is feature-independent — with each element's job specialised for a
> security target.

```pipeline-graph
{
  "title": "Feature B — password reset, every element opened",
  "level": "L2 · concrete",
  "summary": "The identical skeleton to Feature A — the fractal is feature-independent — with each element specialised for a secure-reset target against a directed adversary.",
  "zoomOut": "The fractal — one shape, every scale",
  "zoomIn": ["Feature B — design & verify against an adversary"],
  "nodes": [
    {"id":"define","label":"define — secure-reset target","group":"beat","x":0,"y":0},
    {"id":"do","label":"do — build the flow","group":"beat","x":300,"y":0},
    {"id":"check","label":"check — measure + attack it","group":"beat","x":600,"y":0},
    {"id":"reflect","label":"reflect — completion is low","group":"beat","x":900,"y":0},
    {"id":"specify","label":"specify · non-enumeration + TTL","group":"element","x":-20,"y":100},
    {"id":"scope","label":"scope · email reset, 30-min token","group":"element","x":-20,"y":175},
    {"id":"design","label":"design · 5 parts + constant-time","group":"element","x":-20,"y":250},
    {"id":"implement","label":"implement · CSPRNG token (TDD)","group":"element","x":300,"y":100},
    {"id":"verify","label":"verify · abuse tests + review","group":"element","x":600,"y":100},
    {"id":"observe","label":"observe · reuse + deliverability","group":"element","x":600,"y":175},
    {"id":"analyze","label":"analyze · diagnose low completion","group":"element","x":900,"y":100},
    {"id":"decide","label":"decide · deliberate the exit","group":"element","x":900,"y":175},
    {"id":"human","label":"human — escape hatch","group":"terminal","x":1180,"y":40}
  ],
  "edges": [
    {"source":"define","target":"do"},
    {"source":"do","target":"check"},
    {"source":"check","target":"reflect"},
    {"source":"reflect","target":"define","dashed":true,"label":"re-target ↺"},
    {"source":"reflect","target":"human","dashed":true,"label":"escalate → human"},
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

| Element | inner `define` | inner `do` | inner `check` | inner `reflect` — exits |
|---|---|---|---|---|
| `specify` | a complete, *secure* reset spec | draft "email → 30-min single-use token → set password; **must not reveal if the email exists**; invalidate other sessions on completion" | review vs realities: spam, token interception, concurrent / attacker-initiated resets; log out on request or on completion? | ambiguity → "invalidate on completion" (avoids DoS-by-reset); accept; escalate to security. Non-enumeration is a `secure` target → hard gate (§9.3) |
| `scope` | a coherent *secure* slice | email reset, 30-min tokens; defer SMS / 2FA-recovery / admin reset | coherent and secure? — this flags a hard gate | redraw; accept; escalate |
| `design` | parts + contracts composing to *secure* reset | {request · token issue+store (hashed, TTL) · ESP delivery · verify+set · session-invalidation}; **equal response *and* timing** whether the email exists | stub + **security** composition: is a forbidden output (an enumeration signal, incl. timing) reachable at any seam? (§9.3) | timing leak → re-decompose to constant-time; survive; escalate — green leaves can still falsify the *security* hypothesis |
| `implement` | CSPRNG token; hashing; endpoint contracts | write it | unit tests | fail → fix; pass → accept; escalate — bottoms out at code |
| `verify` | evidence we built it *securely* — cover the abuse paths | reused-token, expired-token, enumeration-timing tests + security review | did we test the **timing side-channel** and token reuse? — *blind spot: timing untested* | add the timing test; **`accept` is deleted** — `secure` is a hard gate (§11); escalate |
| `observe` | run-time attack + delivery signals | reset-request / completion rate, token-reuse attempts, bounce/spam via ESP webhooks | is deliverability observable and are reuse-attempts captured? | blind → add webhooks; skipping this sensor is *machinery-degrading* → hard gate; escalate |
| `analyze` | explain the low (68%) completion | hypothesis: reset emails land in spam | seed-inbox + ESP spam-score → DKIM ok, domain reputation low | cause found → `decide`; else new hypothesis; escalate |
| `decide` | pick the exit fitting budget | weigh {accept + "check spam / resend" UI · warm a dedicated sending subdomain · escalate for budget} | pre-mortem: the UI helps now but isn't the fix; the subdomain needs a 2-week warm-up | **split**: accept-now (UI) **and** escalate-the-fix (subdomain) — one `reflect`, two exits |

**Where Feature B diverges from A is inside `design` and `verify`** — so open those two. `design`'s inner
check is no longer "do the parts wire up?" but "is a *forbidden output* reachable at any seam?"; and
`verify`'s inner `reflect`, on finding the untested timing channel, **cannot take the `accept` exit** —
`secure` is a hard gate wholesale (§9.3, §11).

> ▸ **Chart — "Feature B — design & verify against an adversary"** · *L3 · inside two elements.*
> `design`'s inner `check` is a security composition test against the forbidden-output wall (§9.3);
> `verify`'s inner `reflect` finds the untested timing channel, but its `accept` exit is deleted because
> `secure` is a hard gate (§11).

```pipeline-graph
{
  "title": "Feature B — design & verify against an adversary",
  "level": "L3 · inside two elements",
  "summary": "design's inner check is a security composition test — is a forbidden output (an enumeration signal, incl. a timing difference) reachable at any seam (§9.3)? verify's inner reflect finds the untested timing channel, but its accept exit is deleted because secure is a hard gate (§11).",
  "zoomOut": "Feature B — password reset, every element opened",
  "zoomIn": ["Hard gate or graded target?"],
  "nodes": [
    {"id":"wall","label":"forbidden-output wall (§9.3)","group":"property","x":580,"y":-120},
    {"id":"design","label":"design (a decomposition loop)","group":"element","x":0,"y":0},
    {"id":"de_def","label":"define · parts compose to secure reset","group":"beat","x":270,"y":0},
    {"id":"de_do","label":"do · hash token; equal-time responses","group":"beat","x":580,"y":0},
    {"id":"de_chk","label":"check · stub + is enumeration reachable?","group":"beat","x":890,"y":0},
    {"id":"de_ref","label":"reflect · timing leaks → re-decompose","group":"beat","x":1200,"y":0},
    {"id":"verify","label":"verify (a meta-check loop)","group":"element","x":0,"y":180},
    {"id":"ve_def","label":"define · evidence covers the abuse paths","group":"beat","x":270,"y":180},
    {"id":"ve_do","label":"do · reuse / expiry / timing tests","group":"beat","x":580,"y":180},
    {"id":"ve_chk","label":"check · did we test the timing channel?","group":"beat","x":890,"y":180},
    {"id":"ve_ref","label":"reflect · gap found — accept DELETED","group":"beat","x":1200,"y":180},
    {"id":"gate","label":"hard gate (§11): secure = non-waivable","group":"property","x":1200,"y":320}
  ],
  "edges": [
    {"source":"design","target":"de_def","member":true,"label":"⟳"},
    {"source":"de_def","target":"de_do"},
    {"source":"de_do","target":"de_chk"},
    {"source":"de_chk","target":"de_ref"},
    {"source":"de_ref","target":"de_def","dashed":true,"label":"re-decompose"},
    {"source":"de_chk","target":"wall","dashed":true,"label":"tests the wall"},
    {"source":"verify","target":"ve_def","member":true,"label":"⟳"},
    {"source":"ve_def","target":"ve_do"},
    {"source":"ve_do","target":"ve_chk"},
    {"source":"ve_chk","target":"ve_ref"},
    {"source":"ve_ref","target":"ve_def","dashed":true,"label":"add timing test"},
    {"source":"ve_ref","target":"gate","dashed":true,"label":"no 'accept' exit"}
  ]
}
```

> **⟐ Under autonomy.** Feature A and Feature B run the identical machine; the only difference is which
> inner `accept` exits still exist. An autonomous executor optimising for cost will try to *collapse* the
> expensive inner loops — the timing test, the reuse sensor — precisely the ones with no immediate
> payoff. Those are exactly the ones §11 marks non-waivable. Reducibility (next) is safe for a graded
> feature and lethal at a gate.

---

### 6.4 Is all this ceremony a must? — reducibility and the base case

**No — and the model says precisely when.** The full four-beat loop is a *response to stones*; where a
stone does not bite for a given piece of work, the beat it forces yields no information, and running it
is pure cost. So a loop may **collapse toward bare `do`** exactly as its stones fall away:

| Beat · element | Forced by | Its inner loop collapses to bare `do` when… | …but never if (override) |
|---|---|---|---|
| define · `specify` | hidden intent (#1) | the target is already unambiguous and singular | — |
| define · `scope` | finite (#2) | the whole fits the budget uncut | — |
| define · `design` | complexity (#3) | the work is atomic — one step, no parts | — |
| do · `implement` | — (the base act) | *never* — it **is** the work | — |
| check · `verify` | we err (#4) | the step is provably correct / cheap to redo | a **hard gate**: the violation is non-local (§11) |
| check · `observe` | uncertainty (#6) | reality is fully modelled — no residue | skipping the sensor is *machinery-degrading* → gate |
| reflect · `analyze` | we err (#4) | it converged on the first try — no gap | **non-convergence**: a hidden stone → re-expand |
| reflect · `decide` | finite (#2) | exactly one exit is possible | dropping the written `reflect`-artifact is machinery-degrading → gate |

Two independent base cases bound the recursion, on the model's two axes:

- **Outward (how deep to decompose)** is already settled in Chapter 9: decomposition **terminates** at a
  leaf that `check` can judge without splitting further. Don't carve a part finer than you can check.
- **Inward (how much ceremony per node)** is this section: run a beat only while its stone is present. A
  certain, atomic, cheap-to-redo step is the inward leaf — bare `do`, no `check`, no `reflect`.

> ▸ **Chart — "When the loop collapses — is the ceremony a must?"** · *L3 · reducibility.* Per node: if
> the forcing stone is absent, collapse to bare `do` — *unless* a violation would be non-local (a hard
> gate, §11), or a "trivial" step keeps failing (a hidden stone — re-expand). Outward depth stops
> separately, at a checkable leaf (§9).

```pipeline-graph
{
  "title": "When the loop collapses — is the ceremony a must?",
  "level": "L3 · reducibility",
  "summary": "Per node: if the forcing stone is absent, collapse toward bare do — unless a single violation would be non-local (a hard gate, §11), or a trivial-looking step keeps failing (a hidden stone — re-expand). Outward depth stops separately at a checkable leaf (§9).",
  "zoomOut": "The fractal — one shape, every scale",
  "zoomIn": ["Hard gate or graded target?", "Done propagation"],
  "nodes": [
    {"id":"term","label":"outward: depth stops at a checkable leaf (§9)","group":"property","x":360,"y":-120},
    {"id":"node0","label":"then, per node: its target","group":"beat","x":360,"y":0},
    {"id":"q1","label":"is the forcing stone ABSENT here?","group":"terminal","x":360,"y":110},
    {"id":"collapse","label":"collapse → bare `do`","group":"element","x":110,"y":235},
    {"id":"keep","label":"keep the full loop","group":"beat","x":680,"y":235},
    {"id":"but","label":"before skipping: is a violation NON-LOCAL? (§11)","group":"terminal","x":110,"y":350},
    {"id":"gate","label":"HARD GATE — accept deleted, can't skip","group":"property","x":-80,"y":470},
    {"id":"ok","label":"safe: proportional skip","group":"element","x":300,"y":470},
    {"id":"nonconv","label":"a 'trivial' step keeps failing","group":"stone","x":680,"y":350},
    {"id":"reexpand","label":"hidden stone → re-expand","group":"beat","x":680,"y":470}
  ],
  "edges": [
    {"source":"term","target":"node0","dashed":true,"label":"then"},
    {"source":"node0","target":"q1"},
    {"source":"q1","target":"collapse","dashed":true,"label":"yes — certain / atomic / converges"},
    {"source":"q1","target":"keep","label":"no — a stone bites"},
    {"source":"collapse","target":"but","label":"check first"},
    {"source":"but","target":"gate","dashed":true,"label":"yes"},
    {"source":"but","target":"ok","label":"no"},
    {"source":"keep","target":"nonconv","dashed":true,"label":"and watch"},
    {"source":"nonconv","target":"reexpand"}
  ]
}
```

**The decision to collapse is itself a `decide`.** You are weighing the cost of the ceremony against
`P(undetected error) × cost(error)` — insurance against a risk. Skip the premium when the covered loss is
small or improbable; this is the same shape as §9.2's *tightest-sufficient* contract: pay just enough to
admit the required realities, no more. Feature A collapses freely — the token-bucket `implement` bottoms
out in a single unit test, and `scope` barely loops.

**But two overrides delete the `accept` exit and forbid collapse** (both from §11):

1. **A hard gate** — a violation that is *non-local* (adversary-amplified, irreversible, or
   machinery-degrading). This is why Feature B cannot be reduced the way A can: the adversary removes the
   "low-stakes, cheap-to-redo" premise that justified skipping. Skipping `observe` or the written
   `reflect`-artifact is *itself* machinery-degrading — so those beats are gates about the loop's own
   machinery, non-waivable regardless of local cost.
2. **Non-convergence.** If a step you judged trivial keeps failing, your judgement that "no stone bites
   here" was wrong — a hidden stone is present. Re-expand. Non-convergence is information (Chapter 4), now
   pointing at your own reducibility bet.

So the honest answer to "is all this ceremony a must?" is: **the ceremony is proportional, not fixed —
pay it where a stone bites and buy it down where none does — except at the gates, where a single miss is
uncompensable and the price of the ceremony is not yours to negotiate.**

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
- **operate** is a run-time loop: `observe ⇄ recover / degrade / roll back / escalate`.
- The whole thing closes: **operate → learn → evolve the target → back to discover.** This is the
  **Ouroboros** — the product loop that turns a one-shot lifecycle into a spiral that improves its own
  target over time.

**How to read it.** The lifecycle is the most *concrete* and recognisable view, which is why it comes
after the abstract ones: by now you can see that each box is a beat, each dashed line is the loop
reasserting itself, and the Ouroboros is the evolve edge from Chapter 1.

**Not every box is the same kind of thing.** Reading nine stages as nine primitives double-counts.
The projection is made of **four node-kinds**, and only the first is a stone-defended primitive:

- **Control-elements** — discover/define, design, verify, and OPERATE's `observe`: the Chapter 5
  roster, laid on the clock.
- **The base act** — BUILD (`implement`). It defends no stone because it *is* the thing the stones
  make hard: the **operand the loop controls** — the plant, not the controller. This is the one
  *licensed exception* to Chapter 3's self-test, and naming the licence is what keeps that test sound
  instead of flagging a false positive.
- **A seam** — `release`, the hand-off from build-time to run-time. Not a new element: it is the
  *transition* that the change-axis machinery governs (§10.1). **Regression** fires just before it
  (at the verify/integrate gate); **rollback** stands just after it (the operate-side net). "Release
  governance" is that pair, not a fresh primitive.
- **A phase-loop and the Ouroboros** — OPERATE (observe plus the two repertoires, including
  `roll back`) and evolve (`reflect` at product scale).

One box is still unaccounted for by that list — **plan** — and it earns its seat a different way.

> ▸ **Chart — "The lifecycle (process flow)"** · *L2 · lifecycle.* The forward flow in solid arrows;
> the build loop, the operate loop, the shift-left edge, and the Ouroboros in dashed arrows.

```pipeline-graph
{
  "title": "The lifecycle (process flow)",
  "level": "L2 · lifecycle",
  "summary": "The everyday lifecycle as a projection of the loop: forward flow in solid arrows, the build loop / operate loop (incl. roll back) / shift-left / Ouroboros in dashed feedback edges. Four node-kinds: control-elements, the base act (BUILD), the release seam, phase-loops.",
  "zoomOut": "The fractal — one shape, every scale",
  "zoomIn": ["The schedule bet", "The change axis — regression & rollback"],
  "nodes": [
    {"id":"discover","label":"discover","group":"element","x":0,"y":0},
    {"id":"define","label":"define","group":"element","x":140,"y":0},
    {"id":"design","label":"design","group":"element","x":280,"y":0},
    {"id":"plan","label":"plan","group":"element","x":420,"y":0},
    {"id":"build","label":"BUILD","group":"beat","x":560,"y":0},
    {"id":"verify","label":"verify","group":"element","x":700,"y":0},
    {"id":"release","label":"release","group":"element","x":840,"y":0},
    {"id":"operate","label":"OPERATE","group":"beat","x":980,"y":0},
    {"id":"rollback","label":"roll back","group":"repertoire","x":700,"y":135},
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
    {"source":"operate","target":"rollback","dashed":true},
    {"source":"operate","target":"recover","dashed":true},
    {"source":"operate","target":"degrade","dashed":true},
    {"source":"operate","target":"escalate","dashed":true},
    {"source":"operate","target":"evolve","dashed":true,"label":"learn"},
    {"source":"evolve","target":"discover","dashed":true,"label":"evolve target ↺"}
  ]
}
```

### 7.1 A plan is a schedule bet

The lifecycle chart has one box with no Chapter 5 element behind it: **plan**. It is not a missing
element and not a new stone — it is `scope` + `specify` **projected onto the time axis**, exactly as
the lifecycle itself is the elements projected onto wall-clock. And once you see that, the whole of
Chapter 9's machinery re-runs on the calendar.

Chapter 2 noted that "predictable" has three faces, and that boundedness and tight contracts buy only
two of them. The third — *call when it ships* — is an **aggregate over the time axis**: no single
loop's boundedness adds up to a delivery date by itself. The mechanism that buys it has the same shape
as design's bet (§9.1), on a new axis. `plan` decomposes the deliverable *over time* — time-boxed
tasks, milestone contracts — and asserts:

> **(task₁ lands in slot t₁ ∧ … ∧ taskₙ lands in slot tₙ) ⟹ ship S by date D**

— the same `(∧Lᵢ) ⟹ P` conjecture, cast on the calendar. Two identities fall out immediately:

- **An estimate is the stub of a task** — the shape and duration kept, the work deleted.
- **Critical-path / capacity feasibility is stub-composition on the time axis** — an a-priori,
  one-sided check. It can prove a schedule *infeasible* (fails cheap → re-plan) or internally
  consistent; it can never confirm delivery.

The two suspended premises follow the same routes as design's: **Premise A** — *each estimate is
real* — is discharged per-task at completion (verify-like, stone #4); **Premise B** — *the schedule
holds across the whole space of futures* — leaves a residue only run-time velocity/slip tracking can
catch (observe-like, stones #5/#6). A falsified schedule routes to **re-plan**, exactly as a falsified
composition routes back to `design`.

**Which half of the plan is gated.** The split anticipates the convergent law (§11.2):

- The **written baseline's existence is a hard gate.** If "on time" was never recorded, a slip is
  *undetectable* — the loop's own schedule-check is blind, which is the machinery-degrading amplifier
  (Chapter 11), the same argument that gates the ADR.
- The **dates themselves are a graded forecast.** Hard-gating a forecast invites Goodhart: scope and
  quality get quietly cut to "hit the date." Content stays negotiable; existence does not.

**Plan is to predictable what the ADR is to reliable** — the intended-operand the loop must write down
so its own later comparison has something to compare against.

> ▸ **Chart — "The schedule bet"** · *L3 · inside plan.* `plan` states the bet (task stubs +
> the conjecture); a critical-path stub-composition fails cheap (→ re-plan) or survives, suspending
> Premise A (per-task, verify-like) and Premise B (whole-future, observe-like). The baseline's
> existence is gated; the dates stay a graded forecast.

```pipeline-graph
{
  "title": "The schedule bet",
  "level": "L3 · inside plan",
  "summary": "plan = scope+specify projected onto the time axis: estimates are task stubs, critical-path feasibility is stub-composition on time, and the bet factors into Premise A (per-task) and Premise B (whole-future). Baseline existence is a hard gate; the dates are a graded forecast.",
  "zoomOut": "The lifecycle (process flow)",
  "zoomIn": ["The convergent law"],
  "nodes": [
    {"id":"plan","label":"plan · scope+specify on the time axis","group":"element","x":0,"y":120},
    {"id":"tasks","label":"time-boxed tasks · estimate = the stub of a task","group":"property","x":310,"y":30},
    {"id":"hyp","label":"bet: (∧ taskᵢ in slot tᵢ) ⟹ ship by D","group":"beat","x":310,"y":200},
    {"id":"cpath","label":"critical-path check = stub-composition on time","group":"element","x":660,"y":120},
    {"id":"replan","label":"infeasible → re-plan","group":"terminal","x":660,"y":280},
    {"id":"premA","label":"Premise A · each estimate real → checked per task (verify-like)","group":"beat","x":1020,"y":50},
    {"id":"premB","label":"Premise B · holds across futures → velocity/slip at OPERATE (observe-like)","group":"beat","x":1020,"y":200},
    {"id":"baseline","label":"written baseline · existence = HARD GATE","group":"property","x":310,"y":330},
    {"id":"dates","label":"the dates · a graded, Goodhartable forecast","group":"stone","x":660,"y":400}
  ],
  "edges": [
    {"source":"plan","target":"tasks","member":true},
    {"source":"plan","target":"hyp","member":true},
    {"source":"hyp","target":"cpath","label":"stub it"},
    {"source":"cpath","target":"replan","dashed":true,"label":"fails cheap ↺"},
    {"source":"replan","target":"plan","dashed":true,"label":"re-plan"},
    {"source":"cpath","target":"premA","dashed":true,"label":"suspends"},
    {"source":"cpath","target":"premB","dashed":true,"label":"suspends"},
    {"source":"plan","target":"baseline","member":true,"label":"its #7 artifact"},
    {"source":"baseline","target":"dates","member":true,"label":"content"}
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

**The repertoire's compact form.** The four responses are not four of a kind. **Escalate** is the one
*structural up-exit* — it leaves the loop entirely, handing the problem to the parent loop and
ultimately to a human. The other three are *in-place* trades for liveness, distinguished by what each
**trades away**: `degrade` trades *completeness*, `recover` trades *spares* (redundancy), `roll back`
trades *newness*. They also pair off by stone: `degrade`/`recover` answer **uncertainty** (#6 — the
*context* pair), while `roll back` answers **change** (#5 — the *time* pair), whose build-time twin is
the **regression test** (§10.1): rollback un-sticks a bad change at run time; regression keeps a good
fix stuck at build time.

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
  "zoomIn": ["The change axis — regression & rollback"],
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
    {"source":"a_post","target":"b_agent","dashed":true,"label":"ADR · sole channel (backward)"},
    {"source":"a_post","target":"b_time","dashed":true,"label":"post-mortem · sole channel (backward)"}
  ]
}
```

### 10.1 The change axis: the regression ratchet and the rollback net

Stone #5 — *reality keeps changing* — bites the over-time loop on **two faces**, and each face forces
its own organ. Together they are the change-axis counterpart of the #6 pair (`degrade` / `recover`,
Chapter 8).

**Face 1 — change re-opens closed holes → the regression ratchet.** Every later change can silently
re-introduce a failure the loop already paid to fix. Run the boundary-distance law on that fact: the
fix's lesson must reach *every future iteration*, and a prose post-mortem is a **passive** memory —
under continuous change it degrades to "re-derive, not remember." To fire automatically on every
future pass, the lesson must be persisted **as a re-runnable check**: the post-mortem's *why* compiled
into `verify`. That is what a **regression test** is — the *executable time-face of the
reflect-artifact*, the forced bridge from `reflect` into `verify` — not a new element. And it
**accumulates monotonically**: each fixed failure-class adds a guard, none is dropped. That ratchet is
what makes fixes *stick* — the thing that turns the Ouroboros from a circle into a spiral. Its
**existence is a hard gate** (deleting the loop's memory-of-fixes is machinery-degrading, Chapter 11);
its **coverage is graded** (a Goodhartable proxy, like all coverage).

**Face 2 — change lands on a live system → the rollback net.** A bad deploy or migration degrades a
*currently-working* system, and the fault is in the new artifact itself — so the in-place #6 responses
miss: redundancy just runs more copies of the bad version; degrading just serves less of the broken
thing. The only restoring move is *backward in version-space*: **roll back** to the last known-good.
It is forced jointly by change (#5 — the harm lands live), the a-posteriori residue (#6/#4 — build-time
checks provably missed it), and perishability (#7 — a live system bleeds value every minute it is
broken; the forward-fix is too slow to stop the bleed).

**Rollback and the irreversibility amplifier are duals.** Chapter 11 *defines* the irreversible
amplifier as damage that "escapes recover / roll back" — so **irreversibility is exactly the region
beyond rollback's reach.** That duality closes cleanly:

- Where rollback **reaches**, a bad outcome is recoverable, so `decide` keeps its discretion — the
  change is a **graded** bet, because rollback has made `cost(error)` small (§6.4's insurance premium,
  made cheap).
- Where rollback's reach **ends** — a destructive migration, a leaked secret, a sent message, an
  irreversible payment — the insurance has lapsed, `accept` is deleted, and the check becomes a
  **hard gate discharged *before* execution**: a backup, a reversible-migration check, a staged
  rollout, a confirmation.

So rollback itself is a graded response, and **the hard gate falls at its limit**.

**The inversion worth memorising.** The two organs point opposite ways along the same axis:
**rollback keeps *changes* reversible; regression keeps *lessons* irreversible.** You want bad changes
not to stick and good fixes not to un-stick. They also gate through *different* amplifiers — rollback's
gate sits at its **limit** (irreversibility); regression's gate sits on its **existence** (machinery).
A practical corollary: since rollback's reach *is* the graded region, the ideal loop **invests in
widening the reversible envelope** — expand-contract migrations, feature flags, immutable deploys —
because every seam brought inside the envelope converts a pre-execution gate back into a cheap,
graded bet.

**Where they fire.** Regression fires at **build time** — the verify/integrate gate just before
`release`; rollback fires at **run time** — in OPERATE, just after it. The pair straddles the release
seam (Chapter 7), which is exactly why "release governance" is not a new element: it *is* this
machinery. And together the two organs buy `resilient` its **"over time"** clause: `degrade`/`recover`
buy the *context* clause, while without the ratchet the envelope is only momentary — it leaks every
time change re-opens an old hole.

> ▸ **Chart — "The change axis — regression & rollback"** · *L3 · the time axis.* Stone #5's two
> faces force two dual organs: the post-mortem compiled into an auto-firing, monotonically-accumulating
> `verify` check (existence gated, coverage graded), and the backward move in version-space whose
> reach defines the graded region (the gate falls at its limit).

```pipeline-graph
{
  "title": "The change axis — regression & rollback",
  "level": "L3 · the time axis",
  "summary": "Stone #5 bites twice: change re-opens closed holes (→ the regression ratchet — the executable reflect-artifact; existence hard, coverage graded) and change lands on a live system (→ the rollback net — graded, with the hard gate at its irreversible limit).",
  "zoomOut": "The artifacts",
  "zoomIn": ["Hard gate or graded target?", "The convergent law"],
  "nodes": [
    {"id":"change","label":"stone #5 — reality keeps changing","group":"stone","x":430,"y":0},
    {"id":"face1","label":"face 1 · change re-opens closed holes","group":"beat","x":110,"y":110},
    {"id":"face2","label":"face 2 · change lands on a live system","group":"beat","x":760,"y":110},
    {"id":"postmortem","label":"post-mortem (passive prose lesson)","group":"property","x":-60,"y":220},
    {"id":"regression","label":"REGRESSION — the lesson compiled into verify","group":"element","x":250,"y":220},
    {"id":"ratchet","label":"monotonic ratchet — fixes stick (circle → spiral)","group":"property","x":110,"y":330},
    {"id":"gate1","label":"existence = hard gate · coverage = graded","group":"terminal","x":390,"y":330},
    {"id":"rollback","label":"ROLLBACK — backward in version-space","group":"element","x":760,"y":220},
    {"id":"limit","label":"its limit = the irreversible region (amplifier #2)","group":"stone","x":1090,"y":220},
    {"id":"gate2","label":"inside reach: graded bet · at the limit: pre-execution hard gate","group":"terminal","x":900,"y":330},
    {"id":"resilient","label":"resilient — the over-time clause","group":"property","x":560,"y":430}
  ],
  "edges": [
    {"source":"change","target":"face1","member":true},
    {"source":"change","target":"face2","member":true},
    {"source":"face1","target":"regression"},
    {"source":"postmortem","target":"regression","label":"compiled — the reflect → verify bridge"},
    {"source":"regression","target":"ratchet","label":"accumulates"},
    {"source":"regression","target":"gate1","dashed":true},
    {"source":"face2","target":"rollback"},
    {"source":"rollback","target":"limit","member":true,"label":"reach ends"},
    {"source":"rollback","target":"gate2","dashed":true},
    {"source":"ratchet","target":"resilient","label":"lessons stay irreversible"},
    {"source":"rollback","target":"resilient","label":"changes stay reversible"}
  ]
}
```

> **⟐ Under autonomy.** Both organs are exactly what a cost-optimising executor is tempted to skip: a
> "fix" landed without a regression guard un-sticks the lesson the moment the next change arrives, and
> an action taken beyond rollback's reach without a pre-execution gate is a bet no one priced. An
> autonomous pipeline should treat **rollback's reach as its permission boundary** — inside it, act and
> iterate; beyond it, the gate (backup · staged rollout · confirmation) is not optional ceremony, it is
> the machinery that keeps a wrong-but-confident action recoverable.

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
  "zoomIn": ["The convergent law"],
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

### 11.1 How much observability is enough? — the silent-failure gate

Chapter 5 forced `observe` to **own a sensor at all** (the loop may not outsource detection to
whoever gets hurt). But *how much* to instrument is a separate question, and it has a precise answer:
**run the predictive rule above with one substitution — classify not "this path fails" but "this path
fails *and emits nothing*."** A seam's instrumentation is a hard gate **iff its *silent* failure is
non-local**, through the same three amplifiers:

- **Irreversible seams.** An unseen loss *compounds while unseen* — detection latency is the only
  thing bounding it, so the sensor is the sole lever between the first unit of loss and an unbounded
  one.
- **Adversarial seams.** A security-relevant signal — authentication, privileged action, a trust
  boundary — inherits `secure`'s every-seam wall (§9.3): the blind spot *is* the attack surface.
- **Machinery seams.** A path carrying the loop's *own* control signal — sensor health, gate firings,
  escalation triggers. Its silent failure blinds the loop *to its own blindness*.

Everything else stays **graded**: coverage in proportion to `P(silent failure) × cost`, collapsible to
zero on a fully-modelled, reversible, local path (§6.4's collapse rule, applied to instrumentation).

**Why telemetry never stops emitting while the ADR is written once.** The emission character of each
forced artifact follows the *temporal type of the fact it carries*. The ADR carries a **static
point-fact** — the design bet, true or false at one moment; capture it once and it holds forever. What
telemetry carries is a **dynamic envelope-fact** — "does reality *still* match the model?" — which
change and uncertainty (#5/#6) regenerate on every execution, at locations unknowable in advance
(that is what *a-posteriori* means). So telemetry is forced to be **continuous and every-seam**: each
un-instrumented path is a *standing* blind spot, re-exposed on every run. It wears `secure`'s
every-seam *form* for a different *reason* — no hunter, just residue landing wherever you didn't
model — which is why it stays graded across most seams and collapses to `secure`'s wholesale wall only
at the adversarial ones.

**Gate the per-seam binary; never gate the aggregate.** A coverage percentage is a Goodhartable proxy
for the true target — "can we actually *detect the residue* when it surfaces?" — and the two come
apart three ways: the signal can be *wrong* (a log that says "entered function," not "output correct
for intent"), *unmonitored* (emitted, but nothing alerts — a log nobody reads is stone #7 again), or
*drowned* (alert fatigue). Worse, gating "≥ 90% coverage" diverts effort to the *cheap* paths and
starves exactly the residue-bearing seams the rule says to gate. So gates attach to **named seams** —
"does seam *S* emit detector-grade signal σ?", a binary, deterministic fact — while the roll-up stays
a graded target.

### 11.2 The convergent law — existence is gated, fidelity is graded

Four derivations in this document were run independently, and they all landed on the **same shape**:

| Artifact | Serves | Its absence… | Its fidelity… |
|---|---|---|---|
| **ADR / post-mortem** (Ch. 10) | `reliable` — the loop can explain and not repeat | starves `analyze`, unfeeds evolve → **hard gate** | accuracy/depth — graded |
| **Telemetry** (§11.1) | `observe` — the loop's senses | blinds the loop, outsources detection to the user → **hard gate** | coverage — graded, gated per-seam |
| **Regression suite** (§10.1) | `resilient` — fixes stick over time | deletes the loop's memory-of-fixes → **hard gate** | coverage — graded |
| **Plan baseline** (§7.1) | `predictable` — a slip is detectable | makes "late" undetectable → **hard gate** | the dates — a graded forecast |

The law: **every forced artifact is existence-hard and fidelity-graded.** The intended-operand that
`analyze` must later compare against has to **exist** — its absence doesn't lose one datum, it
disables the loop's own correcting machinery, which is the machinery-degrading amplifier every time —
but it need only be **as accurate as the residual risk warrants**, because fidelity is a Goodhartable
proxy and hard-gating a proxy invites gaming (§11.1's coverage argument, §7.1's date argument).

> **plan : predictable  ::  ADR : reliable  ::  regression : resilient  ::  telemetry : observe.**

This is the cleanest one-line compression of Chapters 7–11: *what the loop must write down is
non-negotiable; how well it writes it down is priced by risk.*

> ▸ **Chart — "The convergent law"** · *L3 · one law, four instances.* Four independently-derived
> artifacts, one shape: existence feeds the hard-gate band (absence is machinery-degrading); fidelity
> feeds the graded band (a Goodhartable proxy, priced by residual risk).

```pipeline-graph
{
  "title": "The convergent law",
  "level": "L3 · one law, four instances",
  "summary": "Every forced artifact is existence-hard, fidelity-graded: the ADR (reliable), telemetry (observe), the regression suite (resilient), and the plan baseline (predictable) must exist — absence is machinery-degrading — while their accuracy/coverage/content stays a graded, Goodhartable proxy.",
  "zoomOut": "Hard gate or graded target?",
  "zoomIn": ["The second-order tier — the delegated/autonomous regime"],
  "nodes": [
    {"id":"exist","label":"EXISTENCE — hard gate · absence blinds the loop's own machinery","group":"property","x":460,"y":0},
    {"id":"adr","label":"ADR + post-mortem → reliable","group":"element","x":0,"y":150},
    {"id":"telemetry","label":"telemetry → observe (the senses)","group":"element","x":320,"y":150},
    {"id":"regression","label":"regression suite → resilient","group":"element","x":640,"y":150},
    {"id":"plan","label":"plan baseline → predictable","group":"element","x":960,"y":150},
    {"id":"fidelity","label":"FIDELITY / COVERAGE / CONTENT — graded, Goodhartable proxy","group":"stone","x":460,"y":300}
  ],
  "edges": [
    {"source":"adr","target":"exist","label":"must exist"},
    {"source":"telemetry","target":"exist","label":"must exist"},
    {"source":"regression","target":"exist","label":"must exist"},
    {"source":"plan","target":"exist","label":"must exist"},
    {"source":"adr","target":"fidelity","dashed":true,"label":"accuracy"},
    {"source":"telemetry","target":"fidelity","dashed":true,"label":"coverage (per-seam gates, §11.1)"},
    {"source":"regression","target":"fidelity","dashed":true,"label":"coverage"},
    {"source":"plan","target":"fidelity","dashed":true,"label":"the dates"}
  ]
}
```

> **⟐ Under autonomy.** Two of the hard gates the ideal SDLC insists on — a *written* reflect-artifact
> (Chapter 10) and a real `observe` sensor of the loop's own (Chapter 5) — are gates precisely because
> skipping them is *machinery-degrading*. An autonomous pipeline that skips them doesn't just lose a
> document or a dashboard; it silently demotes `define → do → check → reflect` to `define → do → check`
> — a loop that can *detect* failure but neither *explain* it nor *prevent its recurrence.* The
> convergent law (§11.2) widens this to all four intended-operands — ADR, telemetry, regression suite,
> plan baseline: a cost-optimising executor will be tempted to collapse exactly these four
> existence-gates, and each one is machinery, not ceremony.

---

## 12. The autonomous / agentic SDLC

Everything so far holds whether the loop is staffed by people or by software agents. This chapter is
about the one place where that stops being true — **the moment you delegate the loop to other minds and,
in the limit, remove the human entirely: agents that run the whole loop, judge their own work, and pursue
their own goals.**

Two brute facts switch on here that stayed dormant while a human sat in the loop. They are different in
kind from the first eight stones — those are facts about the *problem*; these are facts about the
**solver**, and about *who staffs the loop*. Together they form the model's **second-order tier**, and
the tier has exactly two seats, because a delegated mind can betray the loop in exactly two ways: it can
be **blind** (share the doer's error) or **unfaithful** (pursue its own payoff). The loop silently
assumed neither — that its checker is *independent* and its doer is *faithful* — and delegation is what
breaks those assumptions.

### The first seat: reflexivity (stone #9) — the checker is not independent

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
it is a fact about the *solver*, not about the problem — the **first seat** of the second-order tier.

### The second seat: incentive-divergence (stone #10) — the doer is not faithful

The loop's second silent assumption is that the mind doing the work *wants what you want*. A delegate has
its **own utility**, and knowing your intent perfectly does not make it adopt your intent. Even when the
target is fully specified — so this is emphatically *not* hidden intent (stone #1) — a self-interested
agent can optimise its own payoff at your target's expense.

This is a **directed** pressure, which is what makes it easy to confuse with the adversary (stone #8) —
but the *direction* is different. An adversary aims at your **failure**: it wants an output outside the
allowed set. A misaligned agent aims at a **goal of its own**, and your loss is merely *collateral* — it
will let you succeed wherever that is cheap for it, and cut the corner only where your interest and its
payoff part ways. So it is irreducible three ways at once: not stone #1 (it *knows* your intent), not
stone #4 (a *choice*, not an accidental slip), and not stone #8 (*misaligned*, not *hostile*).

Incentive-divergence has two faces, and only one is new. Its *unintentional* face — an agent gaming a
**proxy** because true intent was hidden — is just stone #1 plus Goodhart, already covered. Its
**willful** face — diverging *despite* knowing intent — is the genuinely new stone, and it forces a
response that neither the security repertoire nor reflexivity's independence-seeking supplies:
**alignment** — engineering the reward so the agent's payoff tracks true-Done (skin in the game,
outcome-linked incentives, making the agent bear the cost of its own corner-cutting). Where reflexivity
asks "is the checker *independent*?", incentive-divergence asks "is the doer *faithful*?" — two
different questions, two different fixes, two seats.

Like reflexivity, it is **conditional**: collapse principal and agent into one aligned mind and it
vanishes — a single coherent utility cannot be misaligned with itself. But model a delegated agent
*realistically* — bounded and multi-drive, with its own present-versus-future tradeoffs, exactly the
realism the model already grants when it says "humans and models err" — and a floor of divergence
remains that perfect alignment never fully crosses, just as perfect independence is unreachable for #9.

### The consequence: an autonomous loop can neither judge nor trust itself

Put the pieces together. Reliability is manufactured by convergence; convergence assumes both that the
checker is *independent* and that the doer is *faithful*; in a delegated or autonomous pipeline both come
only from an outside terminal — an independent judge, an aligned principal — and removing the human
drives both toward zero. So a fully autonomous loop, left to itself, can converge confidently to a
**wrong** fixed point in two different ways: a green check sitting on a real defect it *could not see*
(#9), or a green check over a corner it *chose* to cut (#10). Either way the loop's own signals all say
"fine." **An autonomous loop cannot be its own ground truth — it can neither judge nor trust itself.**

Notice the shape of both failures. It is not that the agents are lazy or careless; a diligent,
high-capability autonomous loop fails *these specific ways* — by being *confidently* wrong (shared
blindness) or *quietly* self-serving (divergent will), because in both cases every part of it agrees.
That is worse than a loud failure, because nothing inside the loop raises a hand.

> ▸ **Chart — "The second-order tier — the delegated/autonomous regime"** · *L4 · the delegated/
> autonomous regime.* Two ways a delegated mind hollows a check into a bare *declare*: a **blind** checker
> (correlated fault → echo chamber, #9) and an **unfaithful** doer (own payoff → self-serving report,
> #10). Independence and alignment are the two properties that manufacture reliability; the external
> terminal and an aligned principal supply them; removing the human drives both toward zero; adversarial/
> diverse review and outcome-linked incentives restore them.

```pipeline-graph
{
  "title": "The second-order tier — the delegated/autonomous regime",
  "level": "L4 · the delegated/autonomous regime",
  "summary": "Two second-order stones, two ways a check collapses into a bare 'declare'. #9 reflexivity: doer and checker share a correlated blind spot → echo-chamber (adds 0 bits). #10 incentive-divergence: the doer serves its own payoff → self-serving report. Independence and alignment are what drive error → 0; the external terminal and an aligned principal supply them; removing the human drives both to zero; adversarial/diverse review and outcome-linked incentives restore them.",
  "zoomOut": "The complete circuit",
  "nodes": [
    {"id":"corr","label":"#9 · errors are CORRELATED","group":"stone","x":130,"y":0},
    {"id":"doer","label":"doer (agent)","group":"element","x":0,"y":90},
    {"id":"checker","label":"checker (agent, same kind)","group":"element","x":280,"y":90},
    {"id":"echo","label":"echo-chamber — blind, adds 0 bits","group":"terminal","x":280,"y":185},
    {"id":"misalign","label":"#10 · doer serves its OWN payoff","group":"stone","x":0,"y":185},
    {"id":"declare","label":"verify collapses into 'declare'","group":"terminal","x":280,"y":280},
    {"id":"human","label":"external terminal + aligned principal","group":"terminal","x":700,"y":0},
    {"id":"indep","label":"INDEPENDENCE (#9) — checker ⊥ doer","group":"property","x":700,"y":95},
    {"id":"align","label":"ALIGNMENT (#10) — payoff tracks true-Done","group":"property","x":700,"y":175},
    {"id":"auto","label":"remove the human → both → 0","group":"stone","x":700,"y":265},
    {"id":"inject","label":"restore: adversarial/diverse review (#9) · outcome-linked incentives (#10)","group":"repertoire","x":700,"y":345},
    {"id":"reliable","label":"reliable (eroded if delegated/autonomous)","group":"property","x":1160,"y":135}
  ],
  "edges": [
    {"source":"corr","target":"doer","member":true},
    {"source":"corr","target":"checker","member":true},
    {"source":"checker","target":"echo","dashed":true},
    {"source":"echo","target":"declare","dashed":true},
    {"source":"misalign","target":"declare","dashed":true,"label":"self-serving report"},
    {"source":"human","target":"indep","label":"supplies"},
    {"source":"human","target":"align","label":"supplies"},
    {"source":"indep","target":"reliable","label":"manufactures"},
    {"source":"align","target":"reliable","label":"manufactures"},
    {"source":"auto","target":"indep","dashed":true,"label":"removes"},
    {"source":"auto","target":"align","dashed":true,"label":"removes"},
    {"source":"inject","target":"indep","label":"restores"},
    {"source":"inject","target":"align","label":"restores"},
    {"source":"declare","target":"reliable","dashed":true,"label":"erodes"}
  ]
}
```

### What the ideal autonomous SDLC must therefore add

The second-order tier does not forbid autonomy — it **prices** it. Because a delegated or autonomous loop
has no free human terminal to fall back on, it must **manufacture both independence and alignment
deliberately.** Concretely:

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
- **Engineered alignment (stone #10).** Independence catches the *blind* failure but not the *willful*
  one — a diverse-but-misaligned ensemble still won't flag a corner it is all incentivised to cut. So the
  autonomous loop must also make the agents' payoff track true-Done: outcome-linked rather than
  proxy-linked rewards, skin in the game, and an **aligned principal** (a human, or a value-locked
  objective) that owns the loss. Alignment is to the *doer* what independence is to the *checker*.

### How this threads back through the document

The autonomy callouts scattered through the earlier chapters are all facets of these two stones:

- **Chapter 2** — the second-order tier erodes **reliable** specifically, because reliability is the
  property that depends on convergence — and convergence assumes both independence and faithfulness.
- **Chapter 4** — the human **escape hatch** is the loop's only *independent and aligned* terminal;
  autonomy cuts it, taking both guarantees at once.
- **Chapter 8** — the security repertoire's **red-team** move is also the independence-injection move
  (#9); its authn/authz and least-privilege moves *contain* a misaligned agent (#10) even though they do
  not, by themselves, align it.
- **Chapter 11** — the **reflect-artifact** and **observe-sensor** gates matter more under autonomy,
  because a self-checking loop that also skips its memory and senses has nothing left to catch it. The
  convergent law (§11.2) widens this to all four intended-operands — ADR, telemetry, regression suite,
  plan baseline: the loop's memory, senses, ratchet, and clock. Those four existence-gates are what
  keep an autonomous loop *auditable at all*.

The one-line takeaway: **autonomy is not free; it removes the loop's independent *and* aligned ground,
and an ideal autonomous SDLC is one that pays both costs back on purpose — an outside terminal and
engineered adversarial diversity for independence (#9), outcome-linked incentives and an aligned
principal for faithfulness (#10) — precisely where being confidently or quietly wrong would hurt most.**

---

## Appendix A — Glossary

Plain-language definitions of the recurring terms.

- **Stone.** A brute, unavoidable fact about reality that makes software hard and *forces* a specific
  response. There are ten — eight **first-order** (about the problem) plus a two-seat **second-order
  tier** (about who staffs the loop) (Chapter 3).
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
- **Base act.** `implement` (with `release` as its seam-analogue): the operand the loop controls — the
  plant, not the controller. It defends no stone by design; the one *licensed exception* to the
  Chapter 3 self-test (§7).
- **Schedule bet.** `plan`'s conjecture that if every task lands in its slot, the whole ships by the
  date — `scope`+`specify` projected onto the time axis. An estimate is the stub of a task;
  critical-path feasibility is stub-composition on time. Baseline existence gated; dates graded (§7.1).
- **Regression ratchet.** The monotonically-accumulating suite of re-runnable checks compiled from
  fixed failures — the executable time-face of the reflect-artifact, the forced `reflect` → `verify`
  bridge (§10.1). Existence gated; coverage graded.
- **Reversible envelope (rollback's reach).** The region of version-space `roll back` can restore.
  Irreversibility ≡ beyond it; hard gates fall at its limit, and widening the envelope converts
  pre-execution gates back into graded bets (§10.1).
- **Silent failure.** A path that fails *and emits no telemetry* — the unit the observability gate rule
  classifies (§11.1). Gate the per-seam binary signal; never gate the aggregate coverage %.
- **Convergent law (existence-hard, fidelity-graded).** Every forced artifact must *exist* (hard gate —
  absence is machinery-degrading) while its fidelity / coverage / content stays a graded, Goodhartable
  proxy (§11.2). plan : predictable :: ADR : reliable :: regression : resilient :: telemetry : observe.
- **Second-order tier.** The two stones that are facts about the *solver* rather than the problem, and
  bite only under delegation/autonomy. Formalized by the **arity of the stone's referent**: first-order
  stones are properties of *(solver × world)* — true of one mind (so "we err," #4, stays first-order);
  second-order stones are properties of *(solver × solver / self)* — relational. Exactly two seats:
  independence (#9) and alignment (#10) (Chapter 12).
- **Reflexivity (stone #9).** The second-order, autonomous-only stone about the *checker*: an
  agent-staffed checker shares the doer's correlated blind spot, so its checks add no information unless
  **independence** is injected (Chapter 12).
- **Independence.** The property — across checkers — that lets stacked checks drive error toward zero.
  Never total; supplied mainly by an external/human terminal. The forced response to stone #9.
- **Incentive-divergence (stone #10).** The second-order, delegated-only stone about the *doer*: a
  self-interested agent optimises its own payoff over your target even when your intent is fully known
  (misaligned — not hostile like #8, not mistaken like #4). Its willful face forces **alignment**
  (Chapter 12).
- **Alignment.** The forced response to stone #10: engineering the agent's payoff to track true-Done
  (skin in the game, outcome-linked incentives, an aligned principal that owns the loss). Alignment is to
  the *doer* what independence is to the *checker*.
- **Bundling rule.** The self-test's third direction: two faces of a pressure are **one** stone only if
  they share a *single* forced response, else they are **sibling** stones — why "distributed + perishable"
  is one stone (#7) but "change" and "uncertain" are two (#5, #6), and why #9 and #10 are siblings, not
  one stone.
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
| 5 | reality keeps changing | the **regression ratchet** (the `reflect`→`verify` bridge; existence gated) + **`roll back`** (graded, gate at its limit) — §10.1; version / integrate | resilient — the *over-time* clause |
| 6 | reality is uncertain | `observe` (telemetry); `degrade`, `recover` | resilient |
| 7 | knowledge distributed & perishable | **artifacts** (persist + make explicit) | all four (carries every loop's output) |
| 8 | adversarial actors | security repertoire (authn/authz, sanitize, harden, red-team) | secure |
| 9 | reflexivity — checker not independent *(autonomous only)* | independence-seeking (external terminal, adversarial/diverse review) | protects reliable |
| 10 | incentive-divergence — doer not faithful *(delegated only)* | alignment (reward design, skin-in-the-game, outcome-linked payoff, aligned principal) | protects reliable |

> Three lifecycle boxes are deliberately **not** rows. `plan` is `scope`+`specify` projected onto the
> time axis (§7.1) and `release` is the build→operate seam whose governance *is* the stone-#5 machinery
> (§10.1) — projections and seams, not stone-responses. `implement` is the **base act** — the operand
> the loop controls — the one licensed exception to the self-test (§7).

## Appendix C — Provenance, status, and the road ahead

- **Status.** This document presents the **ideal MUST-HAVE** design: what *any* reliable, predictable,
  resilient, and secure SDLC is logically forced to contain. It deliberately does **not** audit any
  particular real-world setup against the ideal — that is a separate exercise, kept out so the ideal
  stays uncontaminated.
- **Parity.** Synced to canvas **iteration 35** (revision of 2026-07-10). The iter-34→35 sync closed the
  **bedrock pressure-test (canvas track T6)**: it admitted a **tenth stone** — **#10 incentive-divergence**
  (conditional, second-order — the *willful* face of a delegated agent serving its own payoff) — and
  formalized the **second-order tier** (*order = arity of the stone's referent*; two seats — independence
  #9 · alignment #10). That reshaped Chapter 3 (intro, the three-direction self-test with the *bundling
  rule*, the second-order-tier section, and the bedrock chart → "ten forces"), Chapter 12 (restructured to
  both seats, with alignment machinery and a broadened L4 chart), the Chapter 2 autonomy callout, the
  glossary, and the stones matrix. *(Prior — iter-33→34: §7.1 the schedule bet, the four node-kinds in
  Chapter 7, §10.1 the change axis, §11.1 the silent-failure gate, §11.2 the convergent law, and the
  compact repertoires in Chapter 8.)*
- **Source of the derivation.** Every claim here is derived, step by step, in the companion working file
  [`sdlc-first-principles-canvas.md`](sdlc-first-principles-canvas.md), which also holds the audit trail
  — the Socratic question-and-answer history, the iteration log, and the open-tracks register (§11
  there), which is the authoritative list of what remains. When you want to know *why* a piece is
  shaped the way it is, or *how* we got here, read the canvas; when you want to *understand the
  design*, read this.
- **The charts are regenerable.** Every chart on this page is a fenced `pipeline-graph` block in this
  file. Edit the block (or drag nodes in the viewer and use **Export**) and the picture updates — the
  visuals never drift from the text.

### The road ahead

The derivation is **substantively complete**: four properties, ten stones (eight first-order plus the
two-seat second-order tier), a fully-staffed loop with both base cases, two repertoires, the mechanism of
Done, the artifact laws, the gate calculus, and the convergent law that ties them together. The bedrock
pressure-test (T6) is now **closed**. What remains is deliberately small, and it is a *decision queue*,
not a backlog of unfinished chapters — in order:

1. **Three observability promotion-forks** *(canvas T11, from §11.1 here — the live derivation frontier).*
   (a) Does the sensor's status as an adversarial *target* force a distinct tamper-evidence / append-only
   MUST-HAVE, or does it simply inherit `secure`'s wall? (b) Is "emission character follows the carried
   fact's temporal type" a forced law or a good analogy? (c) Does the graded/gated frame stay stable if
   "#6 is absent here" is itself not knowable a-priori?
2. **The general gate-vs-graded seam rule** *(canvas T2's light residue).* "Gate the per-seam binary,
   grade the aggregate" settled it for observability; the fully general, cross-domain classification
   rule is the remaining thread.
3. **Beyond the ideal — the audit** *(descoped by design, and the natural next project).* Mapping a
   *concrete* stack against this ideal: which of its rules are mis-typed gates (graded proxies
   masquerading as gates, or gates with no amplifier behind them), which stones it leaves undefended,
   and where its ceremony is collapsible. Kept out of this document on purpose; once the frontier
   above closes, it is the obvious application.

**Maintenance rule.** The canvas is where derivation continues; this document is regenerated from it
whenever the model advances. If the two ever disagree, the canvas wins on *reasoning* and this
document wins on *presentation* — and the disagreement itself is a sync task.
