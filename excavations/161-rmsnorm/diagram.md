# Diagram — RMSNorm — Do We Need to Subtract the Centre?

```mermaid
flowchart LR
    X["features: 3, 4"] --> S["squares: 9, 16"]
    S --> A["mean square: 12.5"]
    A --> R["root: 3.54"]
    R --> N["divide features by 3.54"]
```

```text
[3,4] and [30,40] -> same normalized direction
```
