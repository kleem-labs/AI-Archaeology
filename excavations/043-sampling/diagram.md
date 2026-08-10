# Diagram — Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Always use argmax."]
    A --> C["Observe: The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality…"]
    B --> D["Repair: Control the distribution with temperature and optionally restrict it to a credible top set…"]
    C --> D
```

```text
TRY     Always use argmax.
BREAK   The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality…
REPAIR  Control the distribution with temperature and optionally restrict it to a credible top set…
```
