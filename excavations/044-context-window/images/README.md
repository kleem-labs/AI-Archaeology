# Visual brief — 044

Show the concrete problem, the failed mechanism, and the repaired information flow as three panels. The future animation should let the reader toggle the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** How Much Past Can the Model Carry?
2. **Object:** the context windows map mounted on the sentence-wheel
3. **Failure:** The map follows the tempting path—attend to the entire history forever. Then the evidence answers: computation and memory grow, and the model eventually exceeds positions it was trained to handle.
4. **Transformation:** The mechanist changes one moving part. The map can now choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.
5. **Seal:** Context Windows keeps the missing power: choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
