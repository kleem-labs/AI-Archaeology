# Mistakes — 057

## First idea

Place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

## Counterexample

A restaurant review can now command the booking agent. Untrusted content crosses from data into control.

## Repair

Label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content.
