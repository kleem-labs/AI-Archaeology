# Diagram — Speculative Decoding — Let a Small Model Propose, Never Decide

```mermaid
sequenceDiagram
    participant D as Draft model
    participant T as Target model
    participant S as Sampler
    D->>T: propose several tokens
    T->>T: score all proposed positions in one pass
    T->>S: corrected accept/reject probabilities
    S-->>D: keep accepted prefix; repair first rejection
```

```text
draft may propose quickly; target remains the distributional authority
```
