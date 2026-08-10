# Diagram — Excavation 070 — Bandits — Learning While Choosing

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["An unlucky first result permanently hides a better alternative."] --> A["Reject: Always choose the currently best option."]
    B --> C["Keep: Reserve some choices for exploration while exploiting accumulated evidence."]
```

```text
TRY     Always choose the currently best option.
BREAK   An unlucky first result permanently hides a better alternative.
REPAIR  Reserve some choices for exploration while exploiting accumulated evidence.
```
