# Diagram — Excavation 101 — Two Kinds of Uncertainty

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Represent every uncertainty with one low confidence number."] --> B["Reality: A clearer image can repair blur, but not missing knowledge; more training data can repair…"]
    B -. "missing requirement" .-> C["Separate uncertainty in the observation from uncertainty in the model’s knowledge."]
```

```text
TRY     Represent every uncertainty with one low confidence number.
BREAK   A clearer image can repair blur, but not missing knowledge; more training data can repair…
REPAIR  Separate uncertainty in the observation from uncertainty in the model’s knowledge.
```
