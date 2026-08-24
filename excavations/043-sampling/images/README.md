# Visual brief — 043

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we always use argmax?
2. **Object:** the sampling wheel mounted on the sentence-wheel
3. **Failure:** The wheel follows the tempting path—always use argmax. Then the evidence answers: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.
4. **Transformation:** The mechanist changes one moving part. The wheel can now control the distribution with temperature and optionally restrict it to a credible top set before sampling.
5. **Seal:** Sampling keeps the missing power: control the distribution with temperature and optionally restrict it to a credible top set before sampling.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
