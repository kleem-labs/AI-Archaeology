# Diagram — Excavation 116 — Reasoning and Verification

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Judge only the final answer."] -->|"test"| B["A lucky answer hides invalid reasoning; one arithmetic slip ruins an otherwise sound plan."]
    B -->|"forces"| C["Represent intermediate claims and verify each with an appropriate checker or evidence…"]
```

```text
TRY     Judge only the final answer.
BREAK   A lucky answer hides invalid reasoning; one arithmetic slip ruins an otherwise sound plan.
REPAIR  Represent intermediate claims and verify each with an appropriate checker or evidence…
```
