# Diagram — Excavation 114 — Model-Based Planning

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["One forecast may exploit model error or miss better branches."] --> A["Reject: Commit to the first sequence imagined."]
    B --> C["Keep: Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and…"]
```

```text
TRY     Commit to the first sequence imagined.
BREAK   One forecast may exploit model error or miss better branches.
REPAIR  Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and…
```
