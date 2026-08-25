# Excavation 223 — Dynamic Programming — Remembering the Value of Futures Already Solved

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



A Markov state makes the next step depend on the present rather than the entire visible past. Planning remains expensive because every action opens more states, whose futures overlap and are recalculated along many paths.

Far below the Transformer, Dynamic Programming begins with an ordinary situation and a tool that almost—but not quite—solves it.

From forest, the ranger can walk toward river or village. Both routes may later reach the same bridge. Drawing every complete journey separately solves the bridge's remaining journey again each time it is encountered.

The chamber has reduced the abstraction to one physical thing: **a branching garden whose shared crossroads carry carved value stones**. The question carved beside it asks: *How can a future already solved stop being recomputed along every road?*

With no standard method to recite, the most economical proposal is to enumerate every possible full action sequence and total its reward independently.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. The number of paths grows exponentially with horizon, and shared suffixes are recomputed. A ten-step tree may contain many copies of the same state with the same remaining problem.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Dynamic Programming
```

The next idea is forced only because the evidence asks us to give each state one stored value equal to the best immediate reward plus the discounted expected value of its possible next states, then reuse that value wherever the state reappears.

The failure and repair now form one continuous argument for Dynamic Programming: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside dynamic programming

The symbols for dynamic programming will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Dynamic Programming against the named case

At the bridge, suppose crossing now gives 2 and leads to home worth 8 next step; waiting gives 1 and leaves a future worth 6. With discount 0.9, crossing is worth `2 + 0.9×8 = 9.2`; waiting is worth `1 + 0.9×6 = 6.4`. Record 9.2 once. Every route arriving at the bridge can now reuse it.

### Naming what is already on the table

**V(s)** is the best future value stored for state s. **a** is a candidate action. **r(s,a)** is immediate reward. **P(s′|s,a)** weighs possible next states. **γ** reduces the influence of distant reward. The maximum keeps the action with the best complete prospect.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) weights each future by both probability and discount. [Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive next-state possibilities; multiplying them would demand all next states occur together. [Maximum](../../MATHEMATICAL_MOVES.md#maximum) chooses among actions after each has been fully valued, while [addition](../../MATHEMATICAL_MOVES.md#addition) joins reward now with reward later.

Every operation required by dynamic programming now has a visible job in the named case, so the complete construction can be written compactly:

$$
V(s)=\max_a\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right]
$$

## A real-world echo

Instead of recounting every road to the sea, a cartographer writes the remaining distance on each crossroads. Every upstream route inherits the solved suffix.

## What this unlocks elsewhere

Bellman backups power value iteration, Q-learning, tree search, decoding variants, and many ways of turning a long decision into reusable local subproblems.

## Where the promise of dynamic programming breaks

Exact dynamic programming requires states and transitions that can be represented and revisited. Huge or continuous worlds need approximation, and a value function with arbitrary shape may still be difficult to optimize reliably.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Dynamic Programming tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 224: Convexity — A Landscape Without Hidden Valleys](../224-convexity/README.md)
