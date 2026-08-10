# Diagram — Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Feed token IDs directly into the network."] --> B["Reality: Since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance…"]
    B -. "missing requirement" .-> C["Give every vocabulary item a one-hot vector: one coordinate is one and all others are zero.…"]
```

```text
TRY     Feed token IDs directly into the network.
BREAK   Since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance…
REPAIR  Give every vocabulary item a one-hot vector: one coordinate is one and all others are zero.…
```
