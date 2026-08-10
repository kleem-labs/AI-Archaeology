# Diagram — Excavation 083 — Autoregressive Generation Beyond Text

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Predict all pixels independently."]
    A --> C["Observe: Independent pixels produce noise because neighboring colors and shapes constrain one…"]
    B --> D["Repair: Choose an order and predict each piece from previously generated pieces."]
    C --> D
```

```text
TRY     Predict all pixels independently.
BREAK   Independent pixels produce noise because neighboring colors and shapes constrain one…
REPAIR  Choose an order and predict each piece from previously generated pieces.
```
