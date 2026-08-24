# Excavation 122 — Differential Privacy

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.

The table of mirrored maps at the Hall of Possible Worlds still carries the marks of the previous discovery. The keeper of unfinished questions follows them as far as they seem willing to go: remove names and assume records are anonymous.

Reality answers without terminology: the trouble appears immediately: rare combinations and model outputs can re-identify individuals. The table of mirrored maps now holds two situations the old rule cannot keep apart.

*The keeper of unfinished questions sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: remove names and assume records are…
                         │
                         └── mismatch: the trouble appears immediately: rare…

reference evidence ──▶ measured repair: limit how much any one record can…
```

The table of mirrored maps is divided down the middle. Left side: “remove names and assume records are anonymous.” Its final mark records the trouble appears immediately: rare combinations and model outputs can re-identify individuals. Right side: the same starting evidence, now allowed to limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given differential privacy a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise. The name **Differential Privacy** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from differential privacy through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the trouble appears immediately: rare combinations and model outputs can re-identify individuals. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

## Understanding differential privacy

Two datasets differing by one patient produce nearly indistinguishable released statistics.

## The calculation hidden inside differential privacy

The keeper of unfinished questions carries the differential privacy scene to the table of mirrored maps. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A clinic wants to publish an average recovery time. Imagine two almost identical worlds: one dataset includes Maya's record and the other does not. If the published number changes dramatically, an observer can infer Maya's participation. The privacy mechanism limits how much the probability of any released result may differ between those worlds. Clipping limits one person's influence; calibrated randomness makes the two possible output distributions overlap.

D and D-prime are two datasets differing in one person.
The same possible released result S is considered under both.
Epsilon limits how much more likely that result may become because one person participated.
A smaller epsilon makes the two worlds harder to distinguish.

### Why the melody needs these exact notes

[The two probabilities](../../MATHEMATICAL_MOVES.md#probability) ask how likely the same released event S is with or without one person's record.
[M(D) ∈ S](../../MATHEMATICAL_MOVES.md#membership) says the randomized mechanism's output landed in the set of outcomes being inspected.
[e^ε](../../MATHEMATICAL_MOVES.md#exponential) turns the privacy budget into a multiplicative allowance: ε=0 requires equal probabilities, while larger ε permits a bounded ratio.
[The ≤ sign](../../MATHEMATICAL_MOVES.md#inequalities) promises a ceiling rather than false equality; privacy needs the two distributions close, not identical for every dataset pair.

Three old motions cast new shadows here: **the rising flame**—a small score difference becomes positive relative evidence. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Nothing remains unnamed in the differential privacy case on the table of mirrored maps. We can finally trade the long route for its compact map:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

## Where differential privacy runs out

Privacy consumes an accuracy budget and implementation mistakes break guarantees.

A final test reaches beyond the new instrument. It does not refute Differential Privacy; it reveals the edge of what was constructed. The keeper of unfinished questions carries that edge into the following room.

## Return to the table of mirrored maps

Rebuild the differential privacy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 123](../123-federated-learning/README.md)
