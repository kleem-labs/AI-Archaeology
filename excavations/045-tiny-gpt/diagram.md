# Diagram — Excavation 045 — A Tiny GPT — Close the Prediction Loop

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Call a framework Transformer and hide the causal chain."] --> B["Reality: Or connect the parts without checking shapes, leakage, and target alignment."]
    B -. "missing requirement" .-> C["Assemble token and position embeddings, masked Transformer blocks, vocabulary logits,…"]
```

```text
TRY     Call a framework Transformer and hide the causal chain.
BREAK   Or connect the parts without checking shapes, leakage, and target alignment.
REPAIR  Assemble token and position embeddings, masked Transformer blocks, vocabulary logits,…
```
