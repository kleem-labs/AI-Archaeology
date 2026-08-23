# Excavation 029 — Initialization — Where Should Learning Begin?

<!-- book-prose-v2 -->

Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.

A careful builder would first avoid adding machinery and set every weight to zero.

The shortcut appears to retain everything initialization needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

The counterexample teaches initialization. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: draw small random weights whose scale depends on how many inputs feed the neuron.

Now—and not earlier—we may introduce **Initialization**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to set every weight to zero., and the case answers that neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate. With the narrow repair—to draw small random weights whose scale depends on how many inputs feed the neuron—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Initialization returns to the same counterexample, replaces the attempt to set every weight to zero. with the responsibility to draw small random weights whose scale depends on how many inputs feed the neuron, and must succeed where the shortcut failed.

## The calculation hidden inside initialization

Before Initialization receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

### Names for pieces we have already used

**w** is one newly initialized weight.
**Var(w)** measures the typical squared spread of starting weights, not their meaning.
**n_in** counts signals entering the neuron.
Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
“Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

### Why no cheaper operation does the same job

[Variance](../../MATHEMATICAL_MOVES.md#variance) describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.
[Dividing by the number of incoming signals](../../MATHEMATICAL_MOVES.md#division) makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.
[The approximately sign](../../MATHEMATICAL_MOVES.md#approximation) admits a design target rather than claiming every finite random sample has exactly this variance; see [equality](../../MATHEMATICAL_MOVES.md#equals) for the stronger claim it avoids.

The notation is finally shorter than the story that created it:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

## Initialization beyond this one case

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

## Take initialization to the workbench

Move initialization from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running initialization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the initialization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 030](../030-activation-functions/README.md)
