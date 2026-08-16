# Mistakes — Excavation 183

## Tempting idea

Remove any entire document containing a sequence that resembles personal information.

## Evidence that breaks it

One phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

## Requirement carried forward

Detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.

The wrong idea remains because its failure exposes information the successful design must preserve.
