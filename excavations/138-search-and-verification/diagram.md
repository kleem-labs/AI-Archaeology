# Diagram — Search and Verification — Separate Proposing from Checking

```mermaid
flowchart LR
    A["Observation"] --> B["Tempting shortcut"]
    B --> C["Counterexample"]
    C --> D["Required repair"]
    D --> E["Search and Verification"]
```

```text
observation -> attempt -> failure -> requirement -> discovery
```
