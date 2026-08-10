# Diagram — Excavation 014 — Layer Normalization

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Each token can drift differently."] --> A["Reject: Use one global scale"]
    B --> C["Keep: Normalize each token across its features. The chapter derives why this repair exists before…"]
```

```text
TRY     Use one global scale
BREAK   Each token can drift differently.
REPAIR  Normalize each token across its features. The chapter derives why this repair exists before…
```
