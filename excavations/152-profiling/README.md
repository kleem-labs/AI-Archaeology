# Excavation 152 — Profiling — Measure Where the Time Went

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: optimize the largest-looking matrix because attention is famous for being expensive.

Reality answers without terminology: the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   optimize the largest-looking matrix… the device spends much of the run…
            \        /
             \      /
              measure data loading, computation,…
```

The brass reference machine is divided down the middle. Left side: “optimize the largest-looking matrix because attention is famous for being expensive.” Its final mark records the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. Right side: the same starting evidence, now allowed to measure data loading, computation, communication, and idle time separately before choosing a repair. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given profiling a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: measure data loading, computation, communication, and idle time separately before choosing a repair. The name **Profiling** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to optimize the largest-looking matrix because attention is famous for being expensive; on the other lies the observed fact that the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. The bridge called profiling has exactly the planks needed to measure data loading, computation, communication, and idle time separately before choosing a repair.

## Measure Where the Time Went

A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.

## The calculation hidden inside profiling

The enginewright carries the profiling scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.

Each T names elapsed time assigned to one non-overlapping stage of the same training step.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.

Listen beneath profiling: **the joining river**—separate contributions meet without losing where they came from. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Nothing remains unnamed in the profiling case on the brass reference machine. We can finally trade the long route for its compact map:

$$
T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}
$$

## Where profiling runs out

A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.

A final test reaches beyond the new instrument. It does not refute Profiling; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

## Return to the brass reference machine

Rebuild the profiling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Input Pipeline — Stop Making the Accelerator Wait](../153-input-pipeline/README.md)
