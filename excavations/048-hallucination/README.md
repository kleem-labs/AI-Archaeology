# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

At the Hall of Voices, the public archivist returns to the listening table. Yesterday's instrument still lies open, so the first move asks for no new magic: trust fluent language because uncertainty should sound hesitant.

For a moment the mark looks complete. Then the evidence refuses to fit: training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The public archivist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: trust fluent language because…
possible road B ─┘              └── loses: training rewards plausible…

same roads ──▶ repaired map ──▶ separate linguistic plausibility from…
```

The public archivist lays two translucent sheets over the listening table. The first is inscribed, “trust fluent language because uncertainty should sound hesitant.” Its path ends where training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. The second receives the same evidence but is allowed to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. Held to the light, the sheets separate at exactly one decision.

No one reaches for a hallucination formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The public archivist changes only that one responsibility: separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. When the ink dries, the name **Hallucination** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The listening table keeps both histories. Its older mark still says, ‘trust fluent language because uncertainty should sound hesitant’; beside it, the newer mark says, ‘separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.’ The distance between those sentences is the exact shape of hallucination: no larger than the failure required, and no smaller than reality permits.

## When Fluent Prediction Outruns Evidence

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

## Where hallucination runs out

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

At the Hall of Voices, the public archivist leaves a blank beneath the new mark. Hallucination has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the listening table

Rebuild the hallucination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 049](../049-calibration/README.md)
