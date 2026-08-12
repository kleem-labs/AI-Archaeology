# Excavation 072 — Linear Probes

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

Perhaps we train a powerful classifier on hidden states and call any success evidence.

The trouble appears immediately: the probe learns the task itself even if the representation did not make it simple.

Now we can see what is missing: we must use a deliberately limited probe and compare layers, controls, and baselines.

## Let the case decide

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

## The boundary of the discovery

Decodable information is not proof the model uses it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 073](../073-attribution/README.md)
