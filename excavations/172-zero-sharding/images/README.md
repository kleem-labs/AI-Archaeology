# Visual Brief — ZeRO — Stop Replicating the Same Training State

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we add devices and replicate the full training state on each one?
2. **Object:** the zero map mounted on the brass reference machine
3. **Failure:** The map follows the tempting path—add devices and replicate the full training state on each one. Then the evidence answers: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.
4. **Transformation:** The enginewright changes one moving part. The map can now partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.
5. **Seal:** ZeRO keeps the missing power: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
