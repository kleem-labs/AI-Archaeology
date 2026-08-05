# Diagrams — Residual Connections

```mermaid
flowchart LR
 X[x] --> F[Transformation F]
 X --> A[Add]
 F --> A
 A --> Y[x + F(x)]
```
