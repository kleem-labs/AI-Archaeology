# Diagrams — Feed-Forward Networks

```mermaid
flowchart LR
 X[Token vector] --> E[Expand with W₁]
 E --> A[Nonlinear activation]
 A --> P[Project with W₂]
 P --> Y[Transformed token]
```
