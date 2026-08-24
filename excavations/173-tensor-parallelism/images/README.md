# Visual Brief — Tensor Parallelism — Split One Matrix That No Device Can Hold

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we assign whole layers to different devices and pass every activation through them sequentially?
2. **Object:** the tensor parallelism scale mounted on the brass reference machine
3. **Failure:** The scale follows the tempting path—assign whole layers to different devices and pass every activation through them sequentially. Then the evidence answers: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.
4. **Transformation:** The enginewright changes one moving part. The scale can now split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.
5. **Seal:** Tensor Parallelism keeps the missing power: split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
