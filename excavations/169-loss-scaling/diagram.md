# Diagram — Loss Scaling — Rescue Gradients Too Small to Represent

```mermaid
flowchart LR
    L["tiny loss signal"] --> S["× scale before backward"] --> B["representable gradient"]
    B --> U["÷ same scale"] --> G["original gradient"]
```

```text
0.000001 -> ×1000 -> 0.001 -> survive -> ÷1000 -> 0.000001
```
