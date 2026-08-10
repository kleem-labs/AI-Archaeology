# Diagram — Excavation 029 — Initialization — Where Should Learning Begin?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Set every weight to zero."] --> B["Reality: Neurons receive identical evidence and remain identical. Use arbitrarily huge random…"]
    B -. "missing requirement" .-> C["Draw small random weights whose scale depends on how many inputs feed the neuron."]
```

```text
TRY     Set every weight to zero.
BREAK   Neurons receive identical evidence and remain identical. Use arbitrarily huge random…
REPAIR  Draw small random weights whose scale depends on how many inputs feed the neuron.
```
