# Mistakes — Excavation 180

## Tempting idea

Lowercase both documents and demand that every remaining word match.

## Evidence that breaks it

One inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

## Requirement carried forward

Represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.

The wrong idea remains because its failure exposes information the successful design must preserve.
