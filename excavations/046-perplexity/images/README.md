# Visual brief — 046

Show the observation, the reader’s attempted mechanism, the counterexample, and the repaired information flow. The animation must pause before revealing the repair.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** How Surprised Is the Model?
2. **Object:** the perplexity gear mounted on the listening table
3. **Failure:** The gear follows the tempting path—count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree. Then the evidence answers: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.
4. **Transformation:** The public archivist changes one moving part. The gear can now score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.
5. **Seal:** Perplexity keeps the missing power: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
