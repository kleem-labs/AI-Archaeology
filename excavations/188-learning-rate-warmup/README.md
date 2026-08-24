# Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to begin immediately at the peak learning rate chosen for the stable middle of training.

Reality answers without terminology: the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ begin immediately at the peak… ──▶ the first noisy batches can make…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ increase the learning rate gradually… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “begin immediately at the peak learning rate chosen for the stable middle of training.” Its final mark records the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. Right side: the same starting evidence, now allowed to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given learning-rate warmup a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. The name **Learning-Rate Warmup** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to begin immediately at the peak learning rate chosen for the stable middle of training; on the other lies the observed fact that the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. The bridge called learning-rate warmup has exactly the planks needed to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

## Let Adam Learn the Terrain Before Running

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

## The calculation hidden inside learning-rate warmup

The archivist-engineer carries the learning-rate warmup scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

### Why the melody needs these exact notes

[Division](../../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Inside learning-rate warmup, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the lock and key**—one influence matters through another, and either missing factor can close the path. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the learning-rate warmup case on the chain-of-custody ledger. We can finally trade the long route for its compact map:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

## Where learning-rate warmup runs out

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

A final test reaches beyond the new instrument. It does not refute Learning-Rate Warmup; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## Return to the chain-of-custody ledger

Rebuild the learning-rate warmup scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Cosine Decay — Make Late Corrections Smaller Without a Cliff](../189-cosine-decay/README.md)
