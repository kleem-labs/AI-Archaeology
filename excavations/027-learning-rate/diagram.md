# Diagram — Excavation 027 — Learning Rate — How Large Should the Next Step Be?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Always take a huge step: leap across the valley and oscillate."]
    A --> C["Observe: Always take a microscopic step: improve so slowly that the expedition ends first."]
    B --> D["Repair: Multiply the gradient by a learning rate, observe whether loss descends, and adjust the…"]
    C --> D
```

```text
TRY     Always take a huge step: leap across the valley and oscillate.
BREAK   Always take a microscopic step: improve so slowly that the expedition ends first.
REPAIR  Multiply the gradient by a learning rate, observe whether loss descends, and adjust the…
```
