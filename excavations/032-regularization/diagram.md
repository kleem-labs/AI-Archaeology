# Diagram — Excavation 032 — Regularization — Making Memorization More Expensive

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Forbid complexity by making the model too small; it may lose real structure too. Stop…"] -->|"test"| B["Forbid complexity by making the model too small; it may lose real structure too. Stop…"]
    B -->|"forces"| C["Add a cost for large weights, remove random paths during training, or stop when validation…"]
```

```text
TRY     Forbid complexity by making the model too small; it may lose real structure too. Stop…
BREAK   Forbid complexity by making the model too small; it may lose real structure too. Stop…
REPAIR  Add a cost for large weights, remove random paths during training, or stop when validation…
```
