# Visual Brief — The Input Pipeline — Stop Making the Accelerator Wait

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we load a batch, wait until loading finishes, compute it, and only then begin loading the next one?
2. **Object:** the input pipeline vessel mounted on the brass reference machine
3. **Failure:** The vessel follows the tempting path—load a batch, wait until loading finishes, compute it, and only then begin loading the next one. Then the evidence answers: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.
4. **Transformation:** The enginewright changes one moving part. The vessel can now prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.
5. **Seal:** The Input Pipeline keeps the missing power: prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
