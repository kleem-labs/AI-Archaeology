# Diagram — Excavation 092 — Contrastive Learning

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Pull every observed pair together without negatives."] -->|"test"| B["All representations can collapse to one point."]
    B -->|"forces"| C["Compare each true pair against mismatched alternatives in the same batch."]
```

```text
TRY     Pull every observed pair together without negatives.
BREAK   All representations can collapse to one point.
REPAIR  Compare each true pair against mismatched alternatives in the same batch.
```
