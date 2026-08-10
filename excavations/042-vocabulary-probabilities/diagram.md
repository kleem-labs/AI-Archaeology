# Diagram — Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Divide each logit by their sum. Negative values break probability and shifting all scores…"] --> A["Reject: Divide each logit by their sum. Negative values break probability and shifting all scores…"]
    B --> C["Keep: Exponentiate relative scores, normalize them, then charge the negative log probability of…"]
```

```text
TRY     Divide each logit by their sum. Negative values break probability and shifting all scores…
BREAK   Divide each logit by their sum. Negative values break probability and shifting all scores…
REPAIR  Exponentiate relative scores, normalize them, then charge the negative log probability of…
```
