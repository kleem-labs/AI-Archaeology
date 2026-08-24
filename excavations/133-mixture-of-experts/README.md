# Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Scientific self-improvement and oversight

Distillation transfers a teacher's pattern of belief into a smaller student. A dense student still spends every parameter on every token, even when different inputs need different expertise.

A new case arrives at the Academy of Trials, but the experimentalist first reaches for the familiar sealed evidence ledger. Its promise is simple: run every specialist for every token and average them.

The rule survives the easy cases. The next case leaves a crack through the middle of it: most computation is wasted on specialists irrelevant to the current token. More confidence cannot repair information that never entered the rule.

*The experimentalist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: run every specialist for every token…
                         │
                         └── mismatch: most computation is wasted on…

reference evidence ──▶ measured repair: learn a router that sends each token…
```

Two trails now cross the sealed evidence ledger. The pale trail bears the instruction “run every specialist for every token and average them.” It disappears into the observed failure: most computation is wasted on specialists irrelevant to the current token. The darker trail carries one additional capacity—to learn a router that sends each token to a small number of experts while balancing their workload. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed mixture of experts mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the sealed evidence ledger is altered in exactly one way: learn a router that sends each token to a small number of experts while balancing their workload. Much later, people will call this territory **Mixture of Experts**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the sealed evidence ledger. The failed path remains visible beneath the repair, because mixture of experts is easier to remember when its scar remains attached to it. The scar reads, ‘most computation is wasted on specialists irrelevant to the current token’; the new line exists only to keep that loss from happening again.

## Spending Computation Where It Helps

Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.

## Where mixture of experts runs out

Routers can collapse onto popular experts and leave others untrained.

The sealed evidence ledger answers today's question and falls silent at the next. That silence is precise: Mixture of Experts was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the sealed evidence ledger

Rebuild the mixture of experts scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Sparse Attention — Looking Without Comparing Everything](../134-sparse-attention/README.md)
