# Visual Brief — The KV Cache — Stop Re-reading the Entire Past

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we at step t, recompute keys and values for positions 1 through t because the prefix is presented again?
2. **Object:** the kv cache scale mounted on the brass reference machine
3. **Failure:** The scale follows the tempting path—at step t, recompute keys and values for positions 1 through t because the prefix is presented again. Then the evidence answers: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.
4. **Transformation:** The enginewright changes one moving part. The scale can now store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.
5. **Seal:** The KV Cache keeps the missing power: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
