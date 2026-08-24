# Excavation 163 — SwiGLU — Let One Learned Path Gate Another

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

The rule survives the easy cases. The next case leaves a crack through the middle of it: width adds capacity but still asks one projection both to create content and decide when that content matters. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[make the hidden layer merely wider…]
    │
    ╳  width adds capacity but still asks…
    │
    ▼
[create one content projection and one…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “make the hidden layer merely wider and trust more coordinates to express every conditional interaction.” It disappears into the observed failure: width adds capacity but still asks one projection both to create content and decide when that content matters. The darker trail carries one additional capacity—to create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed swiglu mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Much later, people will call this territory **SwiGLU**. Here the name is only a memory of the failure it can survive.

The brass reference machine has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and swiglu looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## Let One Learned Path Gate Another

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

## The calculation hidden inside swiglu

The enginewright carries the swiglu scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The enginewright reads the journey of swiglu once more across the brass reference machine, then lets the words contract without losing their order:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

## Where swiglu runs out

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: SwiGLU was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the brass reference machine

Rebuild the swiglu scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Weight Tying — Use One Word Geometry Twice](../164-weight-tying/README.md)
