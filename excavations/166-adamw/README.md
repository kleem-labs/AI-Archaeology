# Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

The doors of the Engine Cavern close against the wind. On the brass reference machine, the enginewright writes the cheapest rule that might still be true: treat penalty gradients and data gradients identically because both appear in one total loss.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ treat penalty gradients and data… ──▶ blurred: coordinates with different gradient…
      │
      └── new lens ──▶ apply Adam's adaptive data update and… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “treat penalty gradients and data gradients identically because both appear in one total loss”; the other knows how to apply Adam's adaptive data update and parameter decay as separate operations. When the failure—coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to adamw. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: apply Adam's adaptive data update and parameter decay as separate operations. This problem and its repair will travel under the name **AdamW**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—treat penalty gradients and data gradients identically because both appear in one total loss? The answer remains coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

## Keep Shrinkage Separate from Adaptation

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

## The calculation hidden inside adamw

The enginewright carries the adamw scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chisel**—what is shared is removed so the remaining change can be seen. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about adamw and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## Where adamw runs out

Decoupled decay still requires choosing which parameters to decay and how strongly.

The adamw repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the brass reference machine

Rebuild the adamw scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Clipping — Stop One Shock from Becoming a Catastrophe](../167-gradient-clipping/README.md)
