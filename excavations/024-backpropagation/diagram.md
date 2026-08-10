# Diagram — Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Perturb each weight and rerun the model."] -->|"test"| B["This needs at least one extra forward pass per weight. Or trace paths independently and…"]
    B -->|"forces"| C["Compute the prediction once, remember intermediate values, then move backward. At each…"]
```

```text
TRY     Perturb each weight and rerun the model.
BREAK   This needs at least one extra forward pass per weight. Or trace paths independently and…
REPAIR  Compute the prediction once, remember intermediate values, then move backward. At each…
```
