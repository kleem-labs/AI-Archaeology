# Diagram — Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Memory explodes and tiny shifts move evidence to neighboring cells."] --> A["Reject: Keep every activation at full resolution through every layer."]
    B --> C["Keep: Summarize small neighborhoods while retaining the strongest or average evidence."]
```

```text
TRY     Keep every activation at full resolution through every layer.
BREAK   Memory explodes and tiny shifts move evidence to neighboring cells.
REPAIR  Summarize small neighborhoods while retaining the strongest or average evidence.
```
