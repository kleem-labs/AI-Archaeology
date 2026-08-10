# Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

[Previous excavation](../132-knowledge-distillation/README.md)

Making every layer wider improves capacity but charges every token the full cost.

At first, the simplest answer is tempting: Run every specialist for every token and average them.

But the simplicity has discarded something important: Most computation is wasted on specialists irrelevant to the current token.

The missing information determines the next move: Learn a router that sends each token to a small number of experts while balancing their workload.

Only here do we name the idea: **Mixture of Experts**.

## Follow one case all the way through

Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Routers can collapse onto popular experts and leave others untrained.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Sparse Attention — Looking Without Comparing Everything](../134-sparse-attention/README.md)
