# Diagram — Excavation 144 — Impact Measures — Notice What Changed Besides the Goal

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Score only the requested final condition."] -->|"test"| B["Unnecessary irreversible changes remain invisible to the goal score."]
    B -->|"forces"| C["Compare the resulting world with a reasonable baseline and penalize avoidable side effects."]
```

```text
TRY     Score only the requested final condition.
BREAK   Unnecessary irreversible changes remain invisible to the goal score.
REPAIR  Compare the resulting world with a reasonable baseline and penalize avoidable side effects.
```
