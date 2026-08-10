# Diagram — Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Create many agents for every problem and let them freely edit shared state."]
    A --> C["Observe: They duplicate searches, contradict one another, overwrite files, and consume more time…"]
    B --> D["Repair: Delegate only separable work with explicit ownership, inputs, outputs, and merge rules.…"]
    C --> D
```

```text
TRY     Create many agents for every problem and let them freely edit shared state.
BREAK   They duplicate searches, contradict one another, overwrite files, and consume more time…
REPAIR  Delegate only separable work with explicit ownership, inputs, outputs, and merge rules.…
```
