# Diagram — Excavation 115 — Tree Search

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Expand every branch equally."]
    A --> C["Observe: Most computation is wasted on obviously poor branches."]
    B --> D["Repair: Balance exploring uncertain branches with deepening promising ones, then propagate outcomes…"]
    C --> D
```

```text
TRY     Expand every branch equally.
BREAK   Most computation is wasted on obviously poor branches.
REPAIR  Balance exploring uncertain branches with deepening promising ones, then propagate outcomes…
```
