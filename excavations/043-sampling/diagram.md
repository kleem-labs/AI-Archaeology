# Diagram — Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities…"]
    A --> C["Observe: Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities…"]
    B --> D["Repair: Control the distribution with temperature and optionally restrict it to a credible top set…"]
    C --> D
```

```text
TRY     Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities…
BREAK   Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities…
REPAIR  Control the distribution with temperature and optionally restrict it to a credible top set…
```
