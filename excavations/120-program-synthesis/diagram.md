# Diagram — Excavation 120 — Program Synthesis

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Memorize the provided input-output pairs."] -->|"test"| B["A new input exposes the absence of an underlying algorithm."]
    B -->|"forces"| C["Search or generate candidate programs, execute them, and keep those satisfying examples and…"]
```

```text
TRY     Memorize the provided input-output pairs.
BREAK   A new input exposes the absence of an underlying algorithm.
REPAIR  Search or generate candidate programs, execute them, and keep those satisfying examples and…
```
