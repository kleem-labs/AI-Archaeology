# Excavation 122 — Differential Privacy

<!-- book-prose-v2 -->

Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.

Nothing yet appears to demand a new invention. We can remove names and assume records are anonymous.

There is a real principle behind this restraint: the complexity of differential privacy must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that the trouble appears immediately: rare combinations and model outputs can re-identify individuals.

That distinction is the hinge on which differential privacy turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.

We have earned the chapter's shorter name: **Differential Privacy**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that differential privacy is necessary rather than decorative. Delete its new responsibility and use the earlier plan to remove names and assume records are anonymous. Immediately, the trouble appears immediately: rare combinations and model outputs can re-identify individuals. Reintroduce the single job to limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise. Because the old plan to remove names and assume records are anonymous is the only displaced piece, the reader can locate exactly where differential privacy changes the outcome.

## Understanding differential privacy

Two datasets differing by one patient produce nearly indistinguishable released statistics.

The name differential privacy is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside differential privacy

Do not read the coming Differential Privacy line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A clinic wants to publish an average recovery time. Imagine two almost identical worlds: one dataset includes Maya's record and the other does not. If the published number changes dramatically, an observer can infer Maya's participation. The privacy mechanism limits how much the probability of any released result may differ between those worlds. Clipping limits one person's influence; calibrated randomness makes the two possible output distributions overlap.

D and D-prime are two datasets differing in one person.
The same possible released result S is considered under both.
Epsilon limits how much more likely that result may become because one person participated.
A smaller epsilon makes the two worlds harder to distinguish.

### Why no cheaper operation does the same job

[The two probabilities](../../MATHEMATICAL_MOVES.md#probability) ask how likely the same released event S is with or without one person's record.
[M(D) ∈ S](../../MATHEMATICAL_MOVES.md#membership) says the randomized mechanism's output landed in the set of outcomes being inspected.
[e^ε](../../MATHEMATICAL_MOVES.md#exponential) turns the privacy budget into a multiplicative allowance: ε=0 requires equal probabilities, while larger ε permits a bounded ratio.
[The ≤ sign](../../MATHEMATICAL_MOVES.md#inequalities) promises a ceiling rather than false equality; privacy needs the two distributions close, not identical for every dataset pair.

Every symbol in Differential Privacy can now be read back into an action already performed. The whole procedure fits in one line:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

## Where differential privacy runs out

Privacy consumes an accuracy budget and implementation mistakes break guarantees.

The weakness is not an accidental footnote. Every operation in differential privacy serves the narrower purpose to limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take differential privacy to the workbench

Understanding differential privacy now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running differential privacy, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the differential privacy result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 123](../123-federated-learning/README.md)
