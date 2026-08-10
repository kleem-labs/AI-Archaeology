# Diagram — Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Assume all future observations come from exactly the same source as training. Or demand…"] --> A["Reject: Assume all future observations come from exactly the same source as training. Or demand…"]
    B --> C["Keep: State the deployment world, test meaningful shifts, and build representations around…"]
```

```text
TRY     Assume all future observations come from exactly the same source as training. Or demand…
BREAK   Assume all future observations come from exactly the same source as training. Or demand…
REPAIR  State the deployment world, test meaningful shifts, and build representations around…
```
