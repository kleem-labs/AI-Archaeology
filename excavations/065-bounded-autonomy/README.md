# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

[Previous: Excavation 064](../064-observability/README.md)

## Take the First Step Yourself

> **Your problem:** We can now plan, remember, call tools, verify, and retry. Combining all powers without boundaries creates a system capable of compounding mistakes.

> **Try your first idea:** Give the agent a broad goal and let it continue until it believes the goal is complete.

> **Now try to break your idea:** A mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

We can now plan, remember, call tools, verify, and retry. Combining all powers without boundaries creates a system capable of compounding mistakes.

## Your First Attempt

Give the agent a broad goal and let it continue until it believes the goal is complete.

## Break Your First Attempt

A mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

Name the missing guarantee before continuing.

## Repair Your Attempt

Create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

## What You Have Just Invented

**Create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.**

## Rebuild the Discovery with a Concrete Case

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The bounded agent can operate safely within one designed environment. The next arc must excavate learning from feedback, adaptation, and continuous improvement without silently changing its authority.

[Next: Feedback Loops](../066-feedback-loops/README.md)
