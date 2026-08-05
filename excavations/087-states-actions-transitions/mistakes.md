# Mistakes — 087

## First idea

Store only action and final reward.

## Counterexample

The same action helps in one situation and harms in another.

## Repair

Record current state, chosen action, reward, and resulting state.
