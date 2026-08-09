# Diagram — Pre-Deployment Evaluations — Fail Before the World Pays

```mermaid
flowchart LR
    A["Observation"] --> B["Tempting shortcut"]
    B --> C["Counterexample"]
    C --> D["Required repair"]
    D --> E["Pre-Deployment Evaluations"]
```

```text
observation -> attempt -> failure -> requirement -> discovery
```
