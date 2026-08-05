# Mistakes — 028

## Wrong Idea #1

Obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

## Why it fails

Useful direction persists across batches while much of the noise changes sign.

## Correct idea

Keep a fading memory of past gradients and combine it with the new one.
