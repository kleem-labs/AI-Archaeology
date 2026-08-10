# Diagram — Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Question"] --> B["Try: Ask the language model to simulate every tool from memory."]
    A --> C["Observe: It invents live weather, makes arithmetic errors, and cannot know whether an external…"]
    B --> D["Repair: Let the model choose a permitted tool, provide structured arguments, observe the real…"]
    C --> D
```

```text
TRY     Ask the language model to simulate every tool from memory.
BREAK   It invents live weather, makes arithmetic errors, and cannot know whether an external…
REPAIR  Let the model choose a permitted tool, provide structured arguments, observe the real…
```
