# Mistakes — Excavation 197

## Tempting idea

Evaluate only the next training batch because it is already available.

## Evidence that breaks it

The same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.

## Requirement carried forward

Maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.

The wrong idea remains because its failure exposes information the successful design must preserve.
