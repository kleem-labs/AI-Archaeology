# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

Inside the Clockwork Scriptorium, every old tool is given one honest chance. The mechanist sets the sentence-wheel between the evidence and the desired answer, then tries to attend to the entire history forever.

Reality answers without terminology: computation and memory grow, and the model eventually exceeds positions it was trained to handle. The sentence-wheel now holds two situations the old rule cannot keep apart.

*The mechanist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: attend to the entire history forever
                         │
                         └── mismatch: computation and memory grow, and the…

reference evidence ──▶ measured repair: choose a maximum context, train…
```

The sentence-wheel is divided down the middle. Left side: “attend to the entire history forever.” Its final mark records computation and memory grow, and the model eventually exceeds positions it was trained to handle. Right side: the same starting evidence, now allowed to choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given context windows a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. The name **Context Windows** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to attend to the entire history forever; on the other lies the observed fact that computation and memory grow, and the model eventually exceeds positions it was trained to handle. The bridge called context windows has exactly the planks needed to choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

## The calculation hidden inside context windows

The mechanist carries the context windows scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

### Naming what is already on the table

**n** is the number of tokens inside the active context.
Each of n queries can compare with n keys, creating roughly n×n score pairs.
That repeated pairwise work is why cost grows proportionally to n² rather than n.
The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

### Why the melody needs these exact notes

[Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
[The square](../../MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

Inside context windows, familiar operations return with stricter duties: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the context windows case on the sentence-wheel. We can finally trade the long route for its compact map:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

## Context Windows beyond this one case

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

## Return to the sentence-wheel

Rebuild the context windows scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 045](../045-tiny-gpt/README.md)
