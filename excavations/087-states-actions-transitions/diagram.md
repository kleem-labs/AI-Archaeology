# Diagram — Excavation 087 — States, Actions, and Transitions

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Store only action and final reward."]
    A --> C["Observe: The same action helps in one situation and harms in another."]
    B --> D["Repair: Record current state, chosen action, reward, and resulting state."]
    C --> D
```

```text
TRY     Store only action and final reward.
BREAK   The same action helps in one situation and harms in another.
REPAIR  Record current state, chosen action, reward, and resulting state.
```
