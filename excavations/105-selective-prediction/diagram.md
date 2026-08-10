# Diagram — Excavation 105 — Selective Prediction

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Always return the highest-scoring answer."] --> B["Reality: A forced answer converts uncertainty into confident-looking error."]
    B -. "missing requirement" .-> C["Allow abstention and choose a coverage level whose retained answers meet a risk target."]
```

```text
TRY     Always return the highest-scoring answer.
BREAK   A forced answer converts uncertainty into confident-looking error.
REPAIR  Allow abstention and choose a coverage level whose retained answers meet a risk target.
```
