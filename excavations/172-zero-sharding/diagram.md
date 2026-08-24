# Diagram — ZeRO — Stop Replicating the Same Training State

```mermaid
flowchart TB
    STATE["optimizer state: 12 chunks"] --> D0["device 0: chunks 0-2"]
    STATE --> D1["device 1: chunks 3-5"]
    STATE --> D2["device 2: chunks 6-8"]
    STATE --> D3["device 3: chunks 9-11"]
```

```text
replication: 12 + 12 + 12 + 12
sharding:     3 +  3 +  3 +  3
```

<!-- memory-film-v1:start -->
## Five-frame memory film

```text
QUESTION       What fails if we add devices and replicate the full training state on each one?
     ↓
OBJECT         the zero map mounted on the brass reference machine
     ↓
VISIBLE BREAK  The map follows the tempting path—add devices and replicate the full training state on each one. Then the evidence answers: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.
     ↓
TRANSFORMATION The enginewright changes one moving part. The map can now partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.
     ↓
MEMORY SEAL    ZeRO keeps the missing power: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.
```
<!-- memory-film-v1:end -->
