# Diagram — Excavation 086 — Rewards — Learning Without Correct Answers

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["For exploration or games, nobody knows every correct intermediate move."] --> A["Reject: Label the correct action at every moment."]
    B --> C["Keep: Provide outcome feedback and let experience connect actions with later consequences."]
```

```text
TRY     Label the correct action at every moment.
BREAK   For exploration or games, nobody knows every correct intermediate move.
REPAIR  Provide outcome feedback and let experience connect actions with later consequences.
```
