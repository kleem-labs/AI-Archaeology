# Visual brief — 024

Create a three-panel illustration: the real problem, the failed attempt, and the discovery. Preserve the chapter example and avoid unexplained symbols.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we perturb each weight and rerun the model?
2. **Object:** the backpropagation bell mounted on the ring of glass lanterns
3. **Failure:** The bell follows the tempting path—perturb each weight and rerun the model. Then the evidence answers: this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.
4. **Transformation:** The keeper of uncertain stories changes one moving part. The bell can now compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.
5. **Seal:** Backpropagation keeps the missing power: compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
