# Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

[Previous: Excavation 033](../033-validation/README.md)

Even a carefully validated model may meet a new hospital, dialect, season, or camera unlike anything in its files.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* State the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but no benchmark proves universal intelligence. Future distributions can change in ways neither data nor designers anticipated.

## Compress your discovery into mathematics


## Build each piece from what just happened

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

### Give Short Names Only After We Know the Pieces

- **θ** is one trained model and **f_θ(x)** its prediction for input x.
- **L(f_θ(x),y)** measures failure against outcome y.
- **P_future** names the deployment world we actually care about.
- Sampling (x,y) from that world prevents training data from silently defining success.
- The expectation averages loss over future cases; **R(θ)** names that future risk.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

## Carry the idea back into the world

A boat tested on one calm lake has not proved itself at sea. We must name the waters we expect it to cross.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 035](../035-tiny-neural-network/README.md)
