# Visual brief — 041

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we choose the nearest input embedding directly?
2. **Object:** the logits vessel mounted on the sentence-wheel
3. **Failure:** The vessel follows the tempting path—choose the nearest input embedding directly. Then the evidence answers: that restricts the scoring rule and hides how every vocabulary candidate should compete.
4. **Transformation:** The mechanist changes one moving part. The vessel can now use a learned linear map to produce one raw score for every vocabulary item.
5. **Seal:** Logits keeps the missing power: use a learned linear map to produce one raw score for every vocabulary item.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
