# Diagram — Excavation 085 — Denoising — Predicting What the Noise Hid

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Ask it to recreate the entire clean image directly from every noise level."] --> B["Reality: The task changes dramatically across noise strengths."]
    B -. "missing requirement" .-> C["Tell the model the noise level and predict the added noise or equivalent clean direction."]
```

```text
TRY     Ask it to recreate the entire clean image directly from every noise level.
BREAK   The task changes dramatically across noise strengths.
REPAIR  Tell the model the noise level and predict the added noise or equivalent clean direction.
```
