# Diagram — Excavation 025 — Gradient Descent — Teaching a Tiny Network

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Jump directly opposite the gradient with no step control; the model may overshoot and…"] --> B["Reality: Gradient descent finds a reachable low region, not necessarily the unique best explanation.…"]
    B -. "missing requirement" .-> C["Move every parameter a controlled distance opposite its gradient, repeat on batches of…"]
```

```text
TRY     Jump directly opposite the gradient with no step control; the model may overshoot and…
BREAK   Gradient descent finds a reachable low region, not necessarily the unique best explanation.…
REPAIR  Move every parameter a controlled distance opposite its gradient, repeat on batches of…
```
