# Visual brief — 042

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we divide each logit by their sum?
2. **Object:** the vocabulary probabilities gate mounted on the sentence-wheel
3. **Failure:** The gate follows the tempting path—divide each logit by their sum. Then the evidence answers: negative values break probability and shifting all scores changes the result.
4. **Transformation:** The mechanist changes one moving part. The gate can now exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.
5. **Seal:** Vocabulary Probabilities keeps the missing power: exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
