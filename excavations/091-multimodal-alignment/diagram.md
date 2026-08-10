# Diagram — Excavation 091 — Multimodal Alignment

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Compare raw pixels directly with token IDs."]
    A --> C["Observe: Their coordinates have unrelated meanings and shapes."]
    B --> D["Repair: Use separate encoders and train paired image-text examples to become nearby."]
    C --> D
```

```text
TRY     Compare raw pixels directly with token IDs.
BREAK   Their coordinates have unrelated meanings and shapes.
REPAIR  Use separate encoders and train paired image-text examples to become nearby.
```
