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

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we let a cheap draft model emit several tokens and return them directly?
     ↓
OBJECT         the speculative decoding gear mounted on the brass reference machine
     ↓
VISIBLE BREAK  The gear follows the tempting path—let a cheap draft model emit several tokens and return them directly. Then the evidence answers: speed improves by silently replacing the trusted target distribution with a weaker model's distribution.
     ↓
TRANSFORMATION The enginewright changes one moving part. The gear can now let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.
     ↓
MEMORY SEAL    Speculative Decoding keeps the missing power: let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.
```
<!-- memory-film-v1:end -->
