# Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Nothing in the Archive Foundry yet bears today's mathematical name. There is only the archivist-engineer, the chain-of-custody ledger, and one plausible action: publish the final benchmark table and assume the configuration files explain the rest.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   publish the final benchmark table and… a score has no visible data lineage,…
            \        /
             \      /
              generate a training report from…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “publish the final benchmark table and assume the configuration files explain the rest.” It disappears into the observed failure: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. The darker trail carries one additional capacity—to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed training report mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Much later, people will call this territory **The Training Report**. Here the name is only a memory of the failure it can survive.

The chain-of-custody ledger has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and training report looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

## Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Training Report was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the chain-of-custody ledger

Rebuild the training report scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Tiny Pretraining Factory — Close the Accountable Training Loop](../200-tiny-pretraining-factory/README.md)
