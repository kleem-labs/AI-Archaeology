# Diagram — Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Keep the best checkpoint and report its score."] -->|"test"| B["Changing only the random seed makes the gain disappear."]
    B -->|"forces"| C["Record code, data, configuration, environment, seeds, and variation across repeated runs."]
```

```text
TRY     Keep the best checkpoint and report its score.
BREAK   Changing only the random seed makes the gain disappear.
REPAIR  Record code, data, configuration, environment, seeds, and variation across repeated runs.
```

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we keep the best checkpoint and report its score?
     ↓
OBJECT         the reproducibility seal mounted on the sealed evidence ledger
     ↓
VISIBLE BREAK  The seal follows the tempting path—keep the best checkpoint and report its score. Then the evidence answers: changing only the random seed makes the gain disappear.
     ↓
TRANSFORMATION The experimentalist changes one moving part. The seal can now record code, data, configuration, environment, seeds, and variation across repeated runs.
     ↓
MEMORY SEAL    Reproducibility keeps the missing power: record code, data, configuration, environment, seeds, and variation across repeated runs.
```
<!-- memory-film-v1:end -->
