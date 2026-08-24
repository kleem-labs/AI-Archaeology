# Visual Brief — AdamW — Keep Shrinkage Separate from Adaptation

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we treat penalty gradients and data gradients identically because both appear in one total loss?
2. **Object:** the adamw thread mounted on the brass reference machine
3. **Failure:** The thread follows the tempting path—treat penalty gradients and data gradients identically because both appear in one total loss. Then the evidence answers: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.
4. **Transformation:** The enginewright changes one moving part. The thread can now apply Adam's adaptive data update and parameter decay as separate operations.
5. **Seal:** AdamW keeps the missing power: apply Adam's adaptive data update and parameter decay as separate operations.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
