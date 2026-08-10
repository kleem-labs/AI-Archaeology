# Diagram — Excavation 110 — Self-Supervised Learning

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Labels are expensive and discard most structure already inside observations."] --> A["Reject: Wait for humans to label every example."]
    B --> C["Keep: Hide or transform part of an observation and train the model to recover the missing…"]
```

```text
TRY     Wait for humans to label every example.
BREAK   Labels are expensive and discard most structure already inside observations.
REPAIR  Hide or transform part of an observation and train the model to recover the missing…
```
