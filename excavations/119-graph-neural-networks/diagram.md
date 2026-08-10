# Diagram — Excavation 119 — Graph Neural Networks

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Assign a fixed input slot to every possible neighbor."]
    A --> C["Observe: Graphs vary in size and neighbor order should not change meaning."]
    B --> D["Repair: Apply the same message rule to each edge and aggregate neighbor messages without depending…"]
    C --> D
```

```text
TRY     Assign a fixed input slot to every possible neighbor.
BREAK   Graphs vary in size and neighbor order should not change meaning.
REPAIR  Apply the same message rule to each edge and aggregate neighbor messages without depending…
```
