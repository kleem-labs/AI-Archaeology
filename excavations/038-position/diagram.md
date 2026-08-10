# Diagram — Excavation 038 — Position — Why Order Must Enter the Model

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["The first invents arbitrary order; the second stores position outside the computation."] --> A["Reject: Sort tokens by ID or trust their array slot without exposing it to the model."]
    B --> C["Keep: Add a position-specific vector to each token vector before attention. Content says what;…"]
```

```text
TRY     Sort tokens by ID or trust their array slot without exposing it to the model.
BREAK   The first invents arbitrary order; the second stores position outside the computation.
REPAIR  Add a position-specific vector to each token vector before attention. Content says what;…
```
