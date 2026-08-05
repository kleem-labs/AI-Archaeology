# Excavation 056 — Authority — What Is the Agent Allowed to Do?

[Previous: Excavation 055](../055-tool-using-agents/README.md)

## Take the First Step Yourself

> **Your problem:** A travel agent can read calendars, send email, and purchase tickets. A useful request to “plan my trip” does not automatically authorize spending money.

> **Try your first idea:** Give every available tool to the model and treat user intent as unlimited permission.

> **Now try to break your idea:** Ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

A travel agent can read calendars, send email, and purchase tickets. A useful request to “plan my trip” does not automatically authorize spending money.

## Your First Attempt

Give every available tool to the model and treat user intent as unlimited permission.

## Break Your First Attempt

Ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

Name the missing guarantee before continuing.

## Repair Your Attempt

Separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.

## What You Have Just Invented

**Separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.**

## Rebuild the Discovery with a Concrete Case

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 057](../057-prompt-injection/README.md)
