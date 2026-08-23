# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

<!-- book-prose-v2 -->

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

A careful builder would first avoid adding machinery and give the agent a broad goal and let it continue until it believes the goal is complete.

The shortcut appears to retain everything bounded autonomy needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

The counterexample teaches bounded autonomy. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

Now—and not earlier—we may introduce **Bounded Autonomy**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to give the agent a broad goal and let it continue until it believes the goal is complete, and the case answers that a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. With the narrow repair—to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Bounded Autonomy returns to the same counterexample, replaces the attempt to give the agent a broad goal and let it continue until it believes the goal is complete with the responsibility to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path, and must succeed where the shortcut failed.

## Building an Agent That Can Be Trusted

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

Bounded Autonomy earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

A formula for bounded autonomy is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## Where bounded autonomy runs out

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

The boundary can be predicted from the construction itself. Bounded Autonomy performs the repair to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take bounded autonomy to the workbench

Move bounded autonomy from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running bounded autonomy, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the bounded autonomy result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Feedback Loops](../066-feedback-loops/README.md)
