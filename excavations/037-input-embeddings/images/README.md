# Visual brief

Show an arbitrary token ID failing as a measurement, an enormous sparse one-hot vector, and a hand selecting one dense row from a trainable table. An animation should show prediction gradients moving only the rows used by a sentence.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we feed token IDs directly into the network?
2. **Object:** the input embeddings bridge mounted on the sentence-wheel
3. **Failure:** The bridge follows the tempting path—feed token IDs directly into the network. Then the evidence answers: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one.
4. **Transformation:** The mechanist changes one moving part. The bridge can now give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.
5. **Seal:** Input Embeddings keeps the missing power: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
