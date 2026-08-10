# Diagram — Excavation 033 — Validation — Testing Without Peeking at the Final Exam

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Use training loss for every choice; it rewards memorization. Check the test set repeatedly;…"] --> B["Reality: Use training loss for every choice; it rewards memorization. Check the test set repeatedly;…"]
    B -. "missing requirement" .-> C["Split data by role: training changes weights, validation changes design decisions, and test…"]
```

```text
TRY     Use training loss for every choice; it rewards memorization. Check the test set repeatedly;…
BREAK   Use training loss for every choice; it rewards memorization. Check the test set repeatedly;…
REPAIR  Split data by role: training changes weights, validation changes design decisions, and test…
```
