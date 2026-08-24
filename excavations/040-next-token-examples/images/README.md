# Visual brief — 040

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we treat an entire sentence as one training example with one answer?
2. **Object:** the next-token examples bell mounted on the sentence-wheel
3. **Failure:** The bell follows the tempting path—treat an entire sentence as one training example with one answer. Then the evidence answers: most of its transitions provide no learning signal.
4. **Transformation:** The mechanist changes one moving part. The bell can now shift the sequence by one position so every visible prefix predicts the token immediately following it.
5. **Seal:** Next-Token Examples keeps the missing power: shift the sequence by one position so every visible prefix predicts the token immediately following it.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
