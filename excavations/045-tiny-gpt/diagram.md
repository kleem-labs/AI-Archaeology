# Diagram — Excavation 045 — A Tiny GPT — Close the Prediction Loop

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Call a framework Transformer and hide the causal chain. Or connect the parts without…"] --> B["Reality: Call a framework Transformer and hide the causal chain. Or connect the parts without…"]
    B -. "missing requirement" .-> C["Assemble token and position embeddings, masked Transformer blocks, vocabulary logits,…"]
```

```text
TRY     Call a framework Transformer and hide the causal chain. Or connect the parts without…
BREAK   Call a framework Transformer and hide the causal chain. Or connect the parts without…
REPAIR  Assemble token and position embeddings, masked Transformer blocks, vocabulary logits,…
```
