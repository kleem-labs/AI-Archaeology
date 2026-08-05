# Mistakes — 026

## Wrong Idea #1

Use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

## Why it fails

A single example is too noisy; the entire archive is too expensive.

## Correct idea

Average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.
