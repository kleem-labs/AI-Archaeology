# Diagram — Excavation 059 — Memory — What Should Survive After the Context Ends?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Store every message forever and paste all history into every new prompt."]
    A --> C["Observe: Cost grows, irrelevant details drown current evidence, contradictions accumulate, and…"]
    B --> D["Repair: Separate short-term working context from durable memory. Store only useful facts with…"]
    C --> D
```

```text
TRY     Store every message forever and paste all history into every new prompt.
BREAK   Cost grows, irrelevant details drown current evidence, contradictions accumulate, and…
REPAIR  Separate short-term working context from durable memory. Store only useful facts with…
```
