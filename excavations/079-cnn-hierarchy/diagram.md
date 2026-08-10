# Diagram — Excavation 079 — CNN Hierarchies

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Classify directly from isolated edge responses."]
    A --> C["Observe: One edge has no object-level meaning."]
    B --> D["Repair: Stack local detectors so later layers combine earlier patterns over wider regions."]
    C --> D
```

```text
TRY     Classify directly from isolated edge responses.
BREAK   One edge has no object-level meaning.
REPAIR  Stack local detectors so later layers combine earlier patterns over wider regions.
```
