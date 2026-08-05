# Mistakes — 056

## First idea

Give every available tool to the model and treat user intent as unlimited permission.

## Counterexample

Ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

## Repair

Separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.
