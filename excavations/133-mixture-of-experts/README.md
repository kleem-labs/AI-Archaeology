# Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

Distillation transfers a teacher's pattern of belief into a smaller student. A dense student still spends every parameter on every token, even when different inputs need different expertise.

We first try to run every specialist for every token and average them.

That confidence lasts only until most computation is wasted on specialists irrelevant to the current token.

That failure tells us to learn a router that sends each token to a small number of experts while balancing their workload.

## Let the case decide

Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.

## The boundary of the discovery

Routers can collapse onto popular experts and leave others untrained.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Sparse Attention — Looking Without Comparing Everything](../134-sparse-attention/README.md)
