# Excavation 056 — Authority — What Is the Agent Allowed to Do?

> **PART VI — TRUSTING AN ACTING MACHINE**
>
> The model no longer merely answers. Its words can cause actions, and every action creates questions of authority and proof.


[Previous: Excavation 055](../055-tool-using-agents/README.md)

A travel agent can read calendars, send email, and purchase tickets. A useful request to “plan my trip” does not automatically authorize spending money.

A reasonable place to begin is: Give every available tool to the model and treat user intent as unlimited permission.

Now place that proposal under pressure: Ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not. Name the missing guarantee before continuing.

What broke tells us what the replacement must preserve: Separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.

## Now work a case you can see

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 057](../057-prompt-injection/README.md)
