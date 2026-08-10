# Diagram — Excavation 030 — Activation Functions — Why a Network Must Bend

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Add more linear layers. Depth increases, but expressive power does not. Use a hard…"] --> A["Reject: Add more linear layers. Depth increases, but expressive power does not. Use a hard…"]
    B --> C["Keep: Place an activation after a linear transformation. ReLU opens positive paths; smoother…"]
```

```text
TRY     Add more linear layers. Depth increases, but expressive power does not. Use a hard…
BREAK   Add more linear layers. Depth increases, but expressive power does not. Use a hard…
REPAIR  Place an activation after a linear transformation. ReLU opens positive paths; smoother…
```
