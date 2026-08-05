# Mistakes — 052

## First idea

Prompt more forcefully and hope next-token prediction infers the desired interaction.

## Counterexample

Given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

## Repair

Show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.
