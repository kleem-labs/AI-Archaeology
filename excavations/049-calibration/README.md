# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

[Previous: Excavation 048](../048-hallucination/README.md)

A model labels many answers “80% confident.” Can a user interpret that number?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Treat the largest softmax probability as honest confidence.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

Only after that reasoning may we give your discovery its inherited name.

## Build each piece from what just happened

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Give Short Names Only After We Know the Pieces

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

Only now can we compress the exact procedure:

$$
\operatorname{ECE}=\sum_b\frac{|B_b|}{n}\left|\operatorname{accuracy}(B_b)-\operatorname{confidence}(B_b)\right|
$$

## Where your new idea still breaks

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 050](../050-data-quality/README.md)
