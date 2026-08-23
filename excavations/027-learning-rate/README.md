# Excavation 027 — Learning Rate — How Large Should the Next Step Be?

<!-- book-prose-v2 -->

A mini-batch replaces one noisy witness with the average advice of a small council. The council can point downhill, but its vote still says nothing about how far the network should move.

The machinery already in our hands suggests that we always take a huge step: leap across the valley and oscillate.

This is how learning rate ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: always take a microscopic step: improve so slowly that the expedition ends first.

The wrong answer makes the need for learning rate inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

The usual name, **Learning Rate**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to always take a huge step: leap across the valley and oscillate. produces the observed failure: always take a microscopic step: improve so slowly that the expedition ends first. Starting with the repaired demand to we need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time preserves the information the shortcut lost. The subject of learning rate lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time instead of merely trying to always take a huge step: leap across the valley and oscillate.. That controlled contrast is what turns a plausible explanation of learning rate into an understandable derivation.

## The calculation hidden inside learning rate

Before Learning Rate receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

### Names for pieces we have already used

**g_t** is the downhill evidence measured at step t.
**η_t** converts direction into a chosen travel distance and may change with time.
The minus sign moves against increasing loss.
**θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.

### Why no cheaper operation does the same job

[gₜ](../../MATHEMATICAL_MOVES.md#gradient) gives direction but not distance.
[Multiplying by ηₜ](../../MATHEMATICAL_MOVES.md#multiplication) turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.
[Subtraction](../../MATHEMATICAL_MOVES.md#negative-sign) moves opposite the locally uphill gradient rather than making loss rise faster.

The notation is finally shorter than the story that created it:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

## Learning Rate beyond this one case

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

## Take learning rate to the workbench

The reader has reconstructed learning rate in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running learning rate, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the learning rate result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 028](../028-momentum/README.md)
