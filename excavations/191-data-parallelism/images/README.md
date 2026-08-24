# Visual Brief — Data Parallelism — Let Several Workers Observe Different Evidence

Illustrate the same ranger-station corpus and training run in two states. The first must make the lost provenance, false boundary, duplicated evidence, wasted compute, disagreement, or unrecoverable state visible. Reveal the repair only in the second state. Do not substitute generic neural-network boxes for the concrete documents, workers, shards, or measurements in this excavation.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we send the same mini-batch to every worker and average their gradients?
2. **Object:** the data parallelism prism mounted on the chain-of-custody ledger
3. **Failure:** The prism follows the tempting path—send the same mini-batch to every worker and average their gradients. Then the evidence answers: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.
4. **Transformation:** The archivist-engineer changes one moving part. The prism can now replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.
5. **Seal:** Data Parallelism keeps the missing power: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
