# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

[Previous: Excavation 064](../064-observability/README.md)

We can now plan, remember, call tools, verify, and retry. Combining all powers without boundaries creates a system capable of compounding mistakes.

The first solution that suggests itself is this: Give the agent a broad goal and let it continue until it believes the goal is complete.

The idea survives only until we test it against reality: A mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. Name the missing guarantee before continuing.

The failure gives us a precise requirement: Create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

## Now work a case you can see

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

The boundary follows from the mechanism itself. We designed it to Create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

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
