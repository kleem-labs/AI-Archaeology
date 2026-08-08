# Excavation 122 — Differential Privacy

[Previous: Excavation 121](../121-formal-verification/README.md)

Can aggregate learning reveal whether one person’s record was included?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Remove names and assume records are anonymous.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Rare combinations and model outputs can re-identify individuals.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Two datasets differing by one patient produce nearly indistinguishable released statistics.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build each piece from what just happened

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

## Where your new idea still breaks

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
