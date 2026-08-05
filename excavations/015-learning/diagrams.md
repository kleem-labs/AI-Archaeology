# Diagrams — Learning

```mermaid
flowchart LR
 D[Training example] --> P[Prediction]
 P --> L[Loss]
 L --> G[Backpropagated gradients]
 G --> U[Parameter update]
 U --> P
```
