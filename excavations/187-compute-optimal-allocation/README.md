# Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: spend nearly the entire budget on parameter count because a larger model can store more patterns.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   spend nearly the entire budget on… the large model is stopped after too…
            \        /
             \      /
              estimate candidate…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “spend nearly the entire budget on parameter count because a larger model can store more patterns.” It disappears into the observed failure: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. The darker trail carries one additional capacity—to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed compute-optimal allocation mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Much later, people will call this territory **Compute-Optimal Allocation**. Here the name is only a memory of the failure it can survive.

The chain-of-custody ledger has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and compute-optimal allocation looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## Buy a Larger Memory or More Experience

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

## The calculation hidden inside compute-optimal allocation

The archivist-engineer carries the compute-optimal allocation scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The archivist-engineer reads the journey of compute-optimal allocation once more across the chain-of-custody ledger, then lets the words contract without losing their order:

$$
C\approx 6PD
$$

## Where compute-optimal allocation runs out

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Compute-Optimal Allocation was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the chain-of-custody ledger

Rebuild the compute-optimal allocation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Learning-Rate Warmup — Let Adam Learn the Terrain Before Running](../188-learning-rate-warmup/README.md)
