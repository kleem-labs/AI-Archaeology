# Excavation 026 — Mini-Batches — Learning from More Than One Example

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: use one example per update.

Reality answers without terminology: it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: use one example per update
possible road B ─┘              └── loses: it is fast, but noisy accidents…

same roads ──▶ repaired map ──▶ average the evidence from a small…
```

The ring of glass lanterns is divided down the middle. Left side: “use one example per update.” Its final mark records it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. Right side: the same starting evidence, now allowed to average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given mini-batches a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. The name **Mini-Batches** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from mini-batches through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we use one example per update?

## When the chamber changes

Keep the formal name Mini-Batches covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The gate follows the tempting path—use one example per update. Then the evidence answers: it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The gate can now average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

The object that should remain after the terminology disappears is **the mini-batches gate mounted on the ring of glass lanterns**.

> **Memory seal — Mini-Batches**
>
> Mini-Batches keeps the missing power: average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

Give the idea a bodily path: Touch the mini-batches gate in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

## The calculation hidden inside mini-batches

The keeper of uncertain stories carries the mini-batches scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

### Naming what is already on the table

**B** is the selected mini-batch and **|B|** its number of examples.
**Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
Summing combines the witnesses.
Dividing by batch size prevents merely using more examples from making the step proportionally larger.
**g_B** is the batch's less noisy gradient estimate.

### Why the melody needs these exact notes

[The sum](../../MATHEMATICAL_MOVES.md#summation) lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.
[Dividing by |B|](../../MATHEMATICAL_MOVES.md#division) asks for advice per example, so merely inviting twice as many witnesses does not double the update.
[i ∈ B](../../MATHEMATICAL_MOVES.md#membership) restricts the sum to examples actually selected for this mini-batch; [|B|](../../MATHEMATICAL_MOVES.md#cardinality) means the number of those examples.

Three old motions cast new shadows here: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Nothing remains unnamed in the mini-batches case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

## Mini-Batches beyond this one case

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

## Return to the ring of glass lanterns

Rebuild the mini-batches scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 027](../027-learning-rate/README.md)
