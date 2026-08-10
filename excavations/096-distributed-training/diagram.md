# Diagram — Excavation 096 — Distributed Training

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Let many machines train independent copies and combine them occasionally."] -->|"test"| B["Their parameters drift and duplicated work wastes computation."]
    B -->|"forces"| C["Partition data or model work, synchronize required results, and preserve one coherent…"]
```

```text
TRY     Let many machines train independent copies and combine them occasionally.
BREAK   Their parameters drift and duplicated work wastes computation.
REPAIR  Partition data or model work, synchronize required results, and preserve one coherent…
```
