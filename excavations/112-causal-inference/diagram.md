# Diagram — Excavation 112 — Causal Inference

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Treat every correlation as a controllable cause."] -->|"test"| B["Hot weather raises both; changing one does not necessarily change the other."]
    B -->|"forces"| C["Represent plausible causal structure and distinguish observing a variable from intervening…"]
```

```text
TRY     Treat every correlation as a controllable cause.
BREAK   Hot weather raises both; changing one does not necessarily change the other.
REPAIR  Represent plausible causal structure and distinguish observing a variable from intervening…
```
