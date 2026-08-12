# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

An obvious shortcut is to give the agent a broad goal and let it continue until it believes the goal is complete.

But a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

That failure tells us to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

## Let the case decide

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The bounded agent can operate safely within one designed environment. The next arc must excavate learning from feedback, adaptation, and continuous improvement without silently changing its authority.

[Next: Feedback Loops](../066-feedback-loops/README.md)
