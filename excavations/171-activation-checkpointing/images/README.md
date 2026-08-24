# Visual Brief — Activation Checkpointing — Remember Less, Recompute Exactly

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we delete all activations after the forward pass?
2. **Object:** the activation checkpointing wheel mounted on the brass reference machine
3. **Failure:** The wheel follows the tempting path—delete all activations after the forward pass. Then the evidence answers: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.
4. **Transformation:** The enginewright changes one moving part. The wheel can now keep selected checkpoint activations and recompute the missing segments once when backward reaches them.
5. **Seal:** Activation Checkpointing keeps the missing power: keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
