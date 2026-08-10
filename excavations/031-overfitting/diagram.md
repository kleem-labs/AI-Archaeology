# Diagram — Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Celebrate zero training error."]
    A --> C["Observe: The model may have memorized scratches and shadows. Make the model infinitely flexible; it…"]
    B --> D["Repair: Reserve unseen cases and compare training success with performance outside the training…"]
    C --> D
```

```text
TRY     Celebrate zero training error.
BREAK   The model may have memorized scratches and shadows. Make the model infinitely flexible; it…
REPAIR  Reserve unseen cases and compare training success with performance outside the training…
```
