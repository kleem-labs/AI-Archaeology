# Excavation 122 — Differential Privacy

Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.

One tempting answer is to remove names and assume records are anonymous.

The trouble appears immediately: rare combinations and model outputs can re-identify individuals.

So we limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.

## Let the case decide

Two datasets differing by one patient produce nearly indistinguishable released statistics.

## The arithmetic we have earned

A clinic wants to publish an average recovery time. Imagine two almost identical worlds: one dataset includes Maya's record and the other does not. If the published number changes dramatically, an observer can infer Maya's participation. The privacy mechanism limits how much the probability of any released result may differ between those worlds. Clipping limits one person's influence; calibrated randomness makes the two possible output distributions overlap.

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

### Why these operations are forced

- [The two probabilities](../../MATHEMATICAL_MOVES.md#probability) ask how likely the same released event S is with or without one person's record.
- [M(D) ∈ S](../../MATHEMATICAL_MOVES.md#membership) says the randomized mechanism's output landed in the set of outcomes being inspected.
- [e^ε](../../MATHEMATICAL_MOVES.md#exponential) turns the privacy budget into a multiplicative allowance: ε=0 requires equal probabilities, while larger ε permits a bounded ratio.
- [The ≤ sign](../../MATHEMATICAL_MOVES.md#inequalities) promises a ceiling rather than false equality; privacy needs the two distributions close, not identical for every dataset pair.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

## The boundary of the discovery

Privacy consumes an accuracy budget and implementation mistakes break guarantees.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 123](../123-federated-learning/README.md)
