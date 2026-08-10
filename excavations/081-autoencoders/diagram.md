# Diagram — Excavation 081 — Autoencoders — Compressing and Rebuilding

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Copy the input through an unrestricted hidden layer."] --> B["Reality: A wide hidden layer learns identity without compression."]
    B -. "missing requirement" .-> C["Force information through a bottleneck and train reconstruction."]
```

```text
TRY     Copy the input through an unrestricted hidden layer.
BREAK   A wide hidden layer learns identity without compression.
REPAIR  Force information through a bottleneck and train reconstruction.
```
