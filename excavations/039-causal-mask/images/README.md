# Visual brief — 039

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we train each prefix in a separate forward pass?
2. **Object:** the causal masking mirror mounted on the sentence-wheel
3. **Failure:** The mirror follows the tempting path—train each prefix in a separate forward pass. Then the evidence answers: it prevents cheating but repeats nearly identical work.
4. **Transformation:** The mechanist changes one moving part. The mirror can now process all positions together while blocking attention from position i to every later position j.
5. **Seal:** Causal Masking keeps the missing power: process all positions together while blocking attention from position i to every later position j.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
