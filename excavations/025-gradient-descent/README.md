# Excavation 025 — Gradient Descent — Teaching a Tiny Network

<!-- book-prose-v2 -->

Backpropagation can now return one local sensitivity to every adjustable weight. Sensitivity is advice, not learning: the network still needs a rule that turns millions of local directions into a new parameter state.

For a moment, remain loyal to the simplest proposal: jump directly opposite the gradient with no step control; the model may overshoot and diverge.

Its appeal is not ignorance but economy. Gradient Descent should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

Notice what the counterexample has accomplished for gradient descent. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.

Humanity eventually gathered this problem and its repairs under the name **Gradient Descent**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace gradient descent with the old instruction to jump directly opposite the gradient with no step control; the model may overshoot and diverge.. The result is again that take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another. Put back only the requirement to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when gradient descent is introduced. The same evidence that defeated the attempt to jump directly opposite the gradient with no step control; the model may overshoot and diverge. is presented again. Only the ability to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress changes, so the repaired conclusion cannot be credited to a conveniently different example.

## The calculation hidden inside gradient descent

Before Gradient Descent receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

### Names for pieces we have already used

**θ_t** packages the current weights; our tiny example has only 8.
**L** is the mistake measure; here it is (weight − 3)².
**∇_θL** packages local sensitivities; our example has only 10.
The minus sign reverses the uphill direction.
**η** is the chosen fraction of the correction; here it is 0.1.
**t** means before this correction; **t+1** means after it.

Substitute real values before compact symbols:

~~~text
next weight = current weight - learning rate × uphill sensitivity
            = 8              - 0.1           × 10
            = 7
~~~

### Why no cheaper operation does the same job

[The time indices](../../MATHEMATICAL_MOVES.md#indices) distinguish the parameter state before update t from the state after it.
[The gradient](../../MATHEMATICAL_MOVES.md#gradient) supplies one local uphill sensitivity for each parameter; [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) reverses that direction toward lower loss.
[Multiplying by η](../../MATHEMATICAL_MOVES.md#multiplication) supplies the missing travel distance. A direction alone does not say whether to move one millimetre or one kilometre.

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$

## Gradient Descent beyond this one case

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

## Where gradient descent runs out

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

Why does that boundary remain? Gradient Descent was built for one responsibility: move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take gradient descent to the workbench

The argument for gradient descent is still provisional until a runnable case can make it fail. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). The [Gradient Step-Size Field Lab](../../labs/04_gradient_lab.py) lets you watch a cautious step learn, a useful step learn faster, and an oversized step bounce forever. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient descent, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient descent result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
