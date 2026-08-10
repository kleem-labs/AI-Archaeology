# Diagram — Excavation 023 — The Chain Rule — Following One Change Through Many Machines

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Measure only the first effect or only the final effect."]
    A --> C["Observe: Either breaks the causal path. Recompute the whole network separately for every weight;…"]
    B --> D["Repair: Multiply local sensitivities along the causal path. Each stage tells how strongly it passes…"]
    C --> D
```

```text
TRY     Measure only the first effect or only the final effect.
BREAK   Either breaks the causal path. Recompute the whole network separately for every weight;…
REPAIR  Multiply local sensitivities along the causal path. Each stage tells how strongly it passes…
```
