# Diagram — Excavation 029 — Initialization — Where Should Learning Begin?

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Set every weight to zero. Neurons receive identical evidence and remain identical. Use…"] --> B["Reality: Set every weight to zero. Neurons receive identical evidence and remain identical. Use…"]
    B -. "missing requirement" .-> C["Draw small random weights whose scale depends on how many inputs feed the neuron."]
```

```text
TRY     Set every weight to zero. Neurons receive identical evidence and remain identical. Use…
BREAK   Set every weight to zero. Neurons receive identical evidence and remain identical. Use…
REPAIR  Draw small random weights whose scale depends on how many inputs feed the neuron.
```
