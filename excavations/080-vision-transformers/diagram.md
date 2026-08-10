# Diagram — Excavation 080 — Vision Transformers

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Treat every pixel as a token."] -->|"test"| B["The sequence becomes enormous and individual pixels carry little stable structure."]
    B -->|"forces"| C["Group pixels into patches, embed them as tokens, add position, and apply attention."]
```

```text
TRY     Treat every pixel as a token.
BREAK   The sequence becomes enormous and individual pixels carry little stable structure.
REPAIR  Group pixels into patches, embed them as tokens, add position, and apply attention.
```
