# Visual Brief — Loss Scaling — Rescue Gradients Too Small to Represent

Draw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.

<!-- memory-film-v1:start -->
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** What fails if we increase the learning rate so small updates become visible?
2. **Object:** the loss scaling vessel mounted on the brass reference machine
3. **Failure:** The vessel follows the tempting path—increase the learning rate so small updates become visible. Then the evidence answers: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.
4. **Transformation:** The enginewright changes one moving part. The vessel can now multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.
5. **Seal:** Loss Scaling keeps the missing power: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
<!-- memory-film-v1:end -->
