# Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

Validation lets us choose among models without opening the sealed test set. Even an honest test can come from yesterday's hospital, dialect, season, or camera while tomorrow arrives from somewhere else.

Using what we have, we assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

So we state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts.

## From procedure to notation

The repair solves the immediate failure, but no benchmark proves universal intelligence. Future distributions can change in ways neither data nor designers anticipated.

## The arithmetic we have earned

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

### Only now do the symbols earn names

- **θ** is one trained model and **f_θ(x)** its prediction for input x.
- **L(f_θ(x),y)** measures failure against outcome y.
- **P_future** names the deployment world we actually care about.
- Sampling (x,y) from that world prevents training data from silently defining success.
- The expectation averages loss over future cases; **R(θ)** names that future risk.

### Why these operations are forced

- [Expectation](../../MATHEMATICAL_MOVES.md#expectation) weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.
- [fθ(x)](../../MATHEMATICAL_MOVES.md#function-application) feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.
- The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.

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
