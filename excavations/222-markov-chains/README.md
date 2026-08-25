# Excavation 222 — Markov Chains — When the Present Carries the Relevant Past

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

### Realm 5 — The Garden of Futures

A final door opens outdoors beneath a night sky. Paths branch through a garden of possible futures, cross a single bowl-shaped valley, and end at a small machine whose range is finite.

Listen for footsteps at crossroads, a taut string, and a machine breathing safely. The questions in this realm travel as one chain:

```text
sufficient present → remembered futures → trustworthy landscape → safe computation
```



Statistical tests judge evidence gathered from repeated trials. Many intelligent systems instead inhabit a sequence: the next room, token, or state depends on what has already happened, and carrying the entire history soon becomes impossible.

The vault of Markov Chains opens onto a problem a ranger, builder, or machine could encounter without knowing any modern terminology.

A ranger moves among forest, river, and village. Tomorrow's location depends strongly on today's location. The station has years of paths, but planning one step ahead should not require rereading every footprint since the expedition began.

The chamber has reduced the abstraction to one physical thing: **a traveler's satchel beside an impossibly long scroll of footprints**. The question carved beside it asks: *When can the present safely replace the entire remembered past?*

The old machinery invites a plausible shortcut: assign one fixed next-location distribution regardless of the current location.

The stone does not object with terminology; it objects with a result we already know cannot be right. The river makes village likely while deep forest makes river likely. Erasing the present state destroys exactly the information that changes the next step.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Markov Chains
```

We do not leap to a famous formula. We carry one missing responsibility forward: choose a state description rich enough that, once the present state is known, earlier history adds no further information about the next-state distribution.

The failure and repair now form one continuous argument for Markov Chains: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside markov chains

The symbols for markov chains will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Markov Chains against the named case

Suppose that from forest the ranger moves to river with probability 0.7 and village with 0.3; from river the probabilities differ. If today's state is forest, the forest row supplies tomorrow's distribution. Yesterday may have been cave or village, but under this model it has already influenced the prediction by determining today's forest state.

### Naming what is already on the table

**Xₜ** names the state at time t. The left side conditions tomorrow on the complete recorded history. The right side conditions only on today. Equality is the modelling promise that the chosen present state contains every historical detail relevant to one-step prediction.

### Why the melody needs these exact notes

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) holds known history fixed while asking about the next state. [Equality](../../MATHEMATICAL_MOVES.md#equals) claims that discarding older conditions changes no next-step probability. Multiplying every transition probability here would answer the probability of a complete path, not the one-step memory question.

Every operation required by markov chains now has a visible job in the named case, so the complete construction can be written compactly:

$$
P(X_{t+1}\mid X_t,X_{t-1},\ldots,X_0)=P(X_{t+1}\mid X_t)
$$

## A real-world echo

A good travel diary can be compressed into your present location only when that location carries everything the next turn needs. If hunger or weather also matters, they must enter the state.

## What this unlocks elsewhere

Autoregressive generation, hidden-state models, reinforcement learning, diffusion steps, and queueing systems all choose states intended to make the future conditionally manageable.

## Where the promise of markov chains breaks

The Markov property does not say the physical world has no memory; it says our state representation has captured the relevant memory. Even with that representation, choosing actions for long-term reward still requires comparing branching futures.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Markov Chains tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 223: Dynamic Programming — Remembering the Value of Futures Already Solved](../223-dynamic-programming/README.md)
