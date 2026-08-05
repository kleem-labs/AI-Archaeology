# Diagrams — Softmax

```mermaid
flowchart LR
    S[Raw scores] --> M[Subtract maximum]
    M --> E[Exponentiate]
    E --> N[Divide by total]
    N --> P[Positive weights summing to 1]
```
