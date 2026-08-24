# Visual brief — 054

Show the observation, the reader’s attempted mechanism, the counterexample, and the repaired information flow. The animation must pause before revealing the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we retrain the whole model whenever one document changes?
2. **Object:** the retrieval-augmented generation thread mounted on the listening table
3. **Failure:** The thread follows the tempting path—retrain the whole model whenever one document changes. Then the evidence answers: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.
4. **Transformation:** The public archivist changes one moving part. The thread can now search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.
5. **Seal:** Retrieval-Augmented Generation keeps the missing power: search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
