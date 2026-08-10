# Diagram — Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Negative values break probability and shifting all scores changes the result."] --> A["Reject: Divide each logit by their sum."]
    B --> C["Keep: Exponentiate relative scores, normalize them, then charge the negative log probability of…"]
```

```text
TRY     Divide each logit by their sum.
BREAK   Negative values break probability and shifting all scores changes the result.
REPAIR  Exponentiate relative scores, normalize them, then charge the negative log probability of…
```
