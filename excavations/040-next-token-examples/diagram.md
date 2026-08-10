# Diagram — Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart LR
    A["Treat an entire sentence as one training example with one answer. Most of its transitions…"] -->|"test"| B["Treat an entire sentence as one training example with one answer. Most of its transitions…"]
    B -->|"forces"| C["Shift the sequence by one position so every visible prefix predicts the token immediately…"]
```

```text
TRY     Treat an entire sentence as one training example with one answer. Most of its transitions…
BREAK   Treat an entire sentence as one training example with one answer. Most of its transitions…
REPAIR  Shift the sequence by one position so every visible prefix predicts the token immediately…
```
