# Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning from uncertainty and error

Validation lets us choose among models without opening the sealed test set. Even an honest test can come from yesterday's hospital, dialect, season, or camera while tomorrow arrives from somewhere else.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: assume all future observations come from exactly the same source as training.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: or demand good performance on every imaginable world, which no finite evidence can guarantee. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[assume all future observations come…]
    │
    ╳  or demand good performance on every…
    │
    ▼
[state the deployment world, test…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “assume all future observations come from exactly the same source as training”; the other knows how to state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts. When the failure—or demand good performance on every imaginable world, which no finite evidence can guarantee—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to generalization. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts. This problem and its repair will travel under the name **Generalization**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—assume all future observations come from exactly the same source as training? The answer remains or demand good performance on every imaginable world, which no finite evidence can guarantee. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

## The calculation hidden inside generalization

The keeper of uncertain stories carries the generalization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but no benchmark proves universal intelligence. Future distributions can change in ways neither data nor designers anticipated.

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

### Naming what is already on the table

**θ** is one trained model and **f_θ(x)** its prediction for input x.
**L(f_θ(x),y)** measures failure against outcome y.
**P_future** names the deployment world we actually care about.
Sampling (x,y) from that world prevents training data from silently defining success.
The expectation averages loss over future cases; **R(θ)** names that future risk.

### Why the melody needs these exact notes

[Expectation](../../MATHEMATICAL_MOVES.md#expectation) weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.
[fθ(x)](../../MATHEMATICAL_MOVES.md#function-application) feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.
The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.

Three old motions cast new shadows here: **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Cover the prose about generalization and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

## Generalization beyond this one case

A boat tested on one calm lake has not proved itself at sea. We must name the waters we expect it to cross.

## Return to the ring of glass lanterns

Rebuild the generalization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 035](../035-tiny-neural-network/README.md)
