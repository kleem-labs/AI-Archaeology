# Excavation 122 — Differential Privacy

[Previous: Excavation 121](../121-formal-verification/README.md)

## Take the First Step Yourself

> **Your problem:** Can aggregate learning reveal whether one person’s record was included?

> **Try your first idea:** Remove names and assume records are anonymous.

> **Now try to break your idea:** Rare combinations and model outputs can re-identify individuals.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Can aggregate learning reveal whether one person’s record was included?

## Your First Attempt

Remove names and assume records are anonymous.

## Break Your First Attempt

Rare combinations and model outputs can re-identify individuals.

## Repair Your Attempt

Limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.

## What You Have Just Invented

**Limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.**

## Rebuild the Discovery with a Concrete Case

Two datasets differing by one patient produce nearly indistinguishable released statistics.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build Every Piece from the Concrete Example

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

## Real-World Limit

Privacy consumes an accuracy budget and implementation mistakes break guarantees.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 123](../123-federated-learning/README.md)
