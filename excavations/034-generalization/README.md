# Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

[Previous: Excavation 033](../033-validation/README.md)

Even a carefully validated model may meet a new hospital, dialect, season, or camera unlike anything in its files.

Our first construction is deliberately modest: Assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

It works—right up to this boundary: Assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

Crossing that boundary requires one additional idea: State the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts.

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
