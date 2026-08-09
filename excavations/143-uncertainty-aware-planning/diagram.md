# Diagram — Uncertainty-Aware Planning — Choosing While Admitting Ignorance

```mermaid
flowchart LR
    A["Observation"] --> B["Tempting shortcut"]
    B --> C["Counterexample"]
    C --> D["Required repair"]
    D --> E["Uncertainty-Aware Planning"]
```

```text
observation -> attempt -> failure -> requirement -> discovery
```
