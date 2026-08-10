# Diagram — Excavation 098 — Red Teaming

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["Real users, attackers, and accidents find paths designers never listed."] --> A["Reject: Evaluate only expected well-formed requests."]
    B --> C["Keep: Actively search for failures, record reproducible cases, and turn discoveries into…"]
```

```text
TRY     Evaluate only expected well-formed requests.
BREAK   Real users, attackers, and accidents find paths designers never listed.
REPAIR  Actively search for failures, record reproducible cases, and turn discoveries into…
```
