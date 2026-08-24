# Excavation 025 — Gradient Descent — Teaching a Tiny Network

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Backpropagation can now return one local sensitivity to every adjustable weight. Sensitivity is advice, not learning: the network still needs a rule that turns millions of local directions into a new parameter state.

Morning reaches the Lantern Observatory before anyone has a name for today's difficulty. Beside the ring of glass lanterns, the keeper of uncertain stories tries the smallest continuation of what already works: jump directly opposite the gradient with no step control; the model may overshoot and diverge.

The rule survives the easy cases. The next case leaves a crack through the middle of it: take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another. More confidence cannot repair information that never entered the rule.

*The keeper of uncertain stories sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ jump directly opposite the gradient… ──▶ blurred: take microscopic steps; learning may…
      │
      └── new lens ──▶ move every parameter a controlled… ──▶ distinction survives
```

Two trails now cross the ring of glass lanterns. The pale trail bears the instruction “jump directly opposite the gradient with no step control; the model may overshoot and diverge.” It disappears into the observed failure: take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another. The darker trail carries one additional capacity—to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed gradient descent mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the ring of glass lanterns is altered in exactly one way: move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. Much later, people will call this territory **Gradient Descent**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the ring of glass lanterns. The failed path remains visible beneath the repair, because gradient descent is easier to remember when its scar remains attached to it. The scar reads, ‘take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another’; the new line exists only to keep that loss from happening again.

## The calculation hidden inside gradient descent

The keeper of uncertain stories carries the gradient descent scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

### Naming what is already on the table

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

### Why the melody needs these exact notes

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

The ring of glass lanterns answers today's question and falls silent at the next. That silence is precise: Gradient Descent was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the ring of glass lanterns

Rebuild the gradient descent scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
