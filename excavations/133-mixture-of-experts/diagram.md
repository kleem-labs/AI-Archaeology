# Diagram — Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Run every specialist for every token and average them."] --> B["Reality: Most computation is wasted on specialists irrelevant to the current token."]
    B -. "missing requirement" .-> C["Learn a router that sends each token to a small number of experts while balancing their…"]
```

```text
TRY     Run every specialist for every token and average them.
BREAK   Most computation is wasted on specialists irrelevant to the current token.
REPAIR  Learn a router that sends each token to a small number of experts while balancing their…
```
