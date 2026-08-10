# Diagram — Excavation 010 — Query, Key, and Value

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Similarity is not directional relevance."] --> A["Reject: Use Euclidean distance"]
    B --> C["Keep: Match queries to keys and mix values. The chapter derives why this repair exists before…"]
```

```text
TRY     Use Euclidean distance
BREAK   Similarity is not directional relevance.
REPAIR  Match queries to keys and mix values. The chapter derives why this repair exists before…
```
