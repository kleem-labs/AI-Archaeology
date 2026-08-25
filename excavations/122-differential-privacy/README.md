# Excavation 122 — Differential Privacy

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to remove names and assume records are anonymous.

This is precisely the kind of shortcut a careful builder should try first. The instruction to remove names and assume records are anonymous preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the trouble appears immediately: rare combinations and model outputs can re-identify individuals.

The counterexample separates two questions that the attempt to remove names and assume records are anonymous had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Differential Privacy**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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
