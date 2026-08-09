# Diagram — Synthetic Data — Letting a Model Write Lessons

```mermaid
flowchart LR
    A["Observation"] --> B["Tempting shortcut"]
    B --> C["Counterexample"]
    C --> D["Required repair"]
    D --> E["Synthetic Data"]
```

```text
observation -> attempt -> failure -> requirement -> discovery
```
