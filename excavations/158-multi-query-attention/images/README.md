# Visual Brief — Multi-Query Attention — Why Cache Separate Copies for Every Head?

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** Why Cache Separate Copies for Every Head?
2. **Object:** the multi-query attention gear mounted on the brass reference machine
3. **Failure:** The gear follows the tempting path—preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections. Then the evidence answers: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.
4. **Transformation:** The enginewright changes one moving part. The gear can now keep many query heads but share one key head and one value head across them.
5. **Seal:** Multi-Query Attention keeps the missing power: keep many query heads but share one key head and one value head across them.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
