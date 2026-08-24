# Diagram — Activation Checkpointing — Remember Less, Recompute Exactly

```mermaid
flowchart LR
    C0["keep layer 0"] --> R1["recompute 1,2"] --> C3["keep layer 3"]
    C3 --> R2["recompute 4,5"] --> C6["keep layer 6"]
    C6 --> R3["recompute 7,8"] --> L9["layer 9"]
```

```text
stored:      0       3       6
recomputed:    1 2     4 5     7 8
```

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we delete all activations after the forward pass?
     ↓
OBJECT         the activation checkpointing wheel mounted on the brass reference machine
     ↓
VISIBLE BREAK  The wheel follows the tempting path—delete all activations after the forward pass. Then the evidence answers: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.
     ↓
TRANSFORMATION The enginewright changes one moving part. The wheel can now keep selected checkpoint activations and recompute the missing segments once when backward reaches them.
     ↓
MEMORY SEAL    Activation Checkpointing keeps the missing power: keep selected checkpoint activations and recompute the missing segments once when backward reaches them.
```
<!-- memory-film-v1:end -->
