# Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

Perhaps we begin immediately at the peak learning rate chosen for the stable middle of training.

But the run answers back. The first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

The failure leaves one precise requirement. Increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

## Let one run decide

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

## The arithmetic we have earned

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Only now can we compress the procedure:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

## What this repair cannot do

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Cosine Decay — Make Late Corrections Smaller Without a Cliff](../189-cosine-decay/README.md)
