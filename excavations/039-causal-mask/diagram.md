# Diagram — Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Train each prefix in a separate forward pass."]
    A --> C["Observe: It prevents cheating but repeats nearly identical work."]
    B --> D["Repair: Process all positions together while blocking attention from position i to every later…"]
    C --> D
```

```text
TRY     Train each prefix in a separate forward pass.
BREAK   It prevents cheating but repeats nearly identical work.
REPAIR  Process all positions together while blocking attention from position i to every later…
```
