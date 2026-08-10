# Diagram — Excavation 143 — Uncertainty-Aware Planning — Choosing While Admitting Ignorance

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Plan using only the single most likely world."]
    A --> C["Observe: A small chance of bridge failure dominates the consequence but disappears from the chosen…"]
    B --> D["Repair: Carry multiple plausible worlds, weight their consequences, and seek information when…"]
    C --> D
```

```text
TRY     Plan using only the single most likely world.
BREAK   A small chance of bridge failure dominates the consequence but disappears from the chosen…
REPAIR  Carry multiple plausible worlds, weight their consequences, and seek information when…
```
