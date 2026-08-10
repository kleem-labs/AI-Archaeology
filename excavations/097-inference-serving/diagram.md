# Diagram — Excavation 097 — Inference Serving

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Run one request at a time on one full model."] --> B["Reality: Hardware sits idle between small operations and traffic spikes create queues."]
    B -. "missing requirement" .-> C["Batch compatible requests, cache repeated state, schedule fairly, and enforce resource…"]
```

```text
TRY     Run one request at a time on one full model.
BREAK   Hardware sits idle between small operations and traffic spikes create queues.
REPAIR  Batch compatible requests, cache repeated state, schedule fairly, and enforce resource…
```
