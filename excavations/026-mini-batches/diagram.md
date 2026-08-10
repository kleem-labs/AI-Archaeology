# Diagram — Excavation 026 — Mini-Batches — Learning from More Than One Example

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    B["It is fast, but noisy accidents dominate. Use every observation before each update. It is…"] --> A["Reject: Use one example per update."]
    B --> C["Keep: Average the evidence from a small group. Each batch is large enough to soften accidents and…"]
```

```text
TRY     Use one example per update.
BREAK   It is fast, but noisy accidents dominate. Use every observation before each update. It is…
REPAIR  Average the evidence from a small group. Each batch is large enough to soften accidents and…
```
