# Diagram — Excavation 044 — Context Windows — How Much Past Can the Model Carry?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Attend to the entire history forever."] -->|"test"| B["Computation and memory grow, and the model eventually exceeds positions it was trained to…"]
    B -->|"forces"| C["Choose a maximum context, train within it, and reuse cached keys and values during…"]
```

```text
TRY     Attend to the entire history forever.
BREAK   Computation and memory grow, and the model eventually exceeds positions it was trained to…
REPAIR  Choose a maximum context, train within it, and reuse cached keys and values during…
```
