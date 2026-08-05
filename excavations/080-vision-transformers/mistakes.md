# Mistakes — 080

## First idea

Treat every pixel as a token.

## Counterexample

The sequence becomes enormous and individual pixels carry little stable structure.

## Repair

Group pixels into patches, embed them as tokens, add position, and apply attention.
