# Excavation 089 — Q-Learning — Improving Values from Experience

<!-- book-prose-v2 -->

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

A careful builder would first avoid adding machinery and replace its value with the immediate reward.

The shortcut appears to retain everything q-learning needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: the update ignores the valuable state reached afterward.

The counterexample teaches q-learning. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: move the estimate toward reward plus the best discounted value available next.

Now—and not earlier—we may introduce **Q-Learning**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to replace its value with the immediate reward, and the case answers that the update ignores the valuable state reached afterward. With the narrow repair—to move the estimate toward reward plus the best discounted value available next—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Q-Learning returns to the same counterexample, replaces the attempt to replace its value with the immediate reward with the responsibility to move the estimate toward reward plus the best discounted value available next, and must succeed where the shortcut failed.

## Improving Values from Experience

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

A formula for q-learning is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside q-learning

Before Q-Learning receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

The immediate reward is what happened now.
The largest next-state Q value represents the best continuation currently known.
Discount γ reduces distant evidence and keeps unending sums bounded.
Adding immediate and discounted future reward creates the target the old estimate moves toward.

### Why no cheaper operation does the same job

[Addition](../../MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
[γ scales future value](../../MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
[Max](../../MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

Every symbol in Q-Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

## Where q-learning runs out

Maximization can overestimate noisy actions and offline data limits safe exploration.

The boundary can be predicted from the construction itself. Q-Learning performs the repair to move the estimate toward reward plus the best discounted value available next; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take q-learning to the workbench

Move q-learning from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running q-learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the q-learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 090](../090-policy-gradients/README.md)
