# Excavation 125 — An Open-Ended Research System

[Previous: Excavation 124](../124-adversarial-robustness/README.md)

## Take the First Step Yourself

> **Your problem:** How can a system keep discovering without silently rewriting its goals or safety boundaries?

> **Try your first idea:** Let it generate experiments, change itself, and deploy improvements automatically.

> **Now try to break your idea:** A flawed metric or experiment compounds through self-modification before external review.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can a system keep discovering without silently rewriting its goals or safety boundaries?

## Your First Attempt

Let it generate experiments, change itself, and deploy improvements automatically.

## Break Your First Attempt

A flawed metric or experiment compounds through self-modification before external review.

## Repair Your Attempt

Separate hypothesis generation, sandboxed experiment, independent evaluation, authority, reproducibility, and approved deployment.

## What You Have Just Invented

**Separate hypothesis generation, sandboxed experiment, independent evaluation, authority, reproducibility, and approved deployment.**

## Rebuild the Discovery with a Concrete Case

The system proposes a tokenizer change, tests it in isolation, reproduces gains, checks regressions, and submits evidence for human approval.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Open-ended discovery remains bounded by chosen objectives, measurements, and human institutions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The system can conduct bounded research. The next excavation must be forced by the new observations that research creates.
