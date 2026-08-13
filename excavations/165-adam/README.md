# Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

Perhaps we use the same raw gradient step scale for every parameter.

It survives until the measured run answers back. A rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

Now the missing requirement is concrete. Keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

## Let one run decide

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Only now can we compress the procedure:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## What this repair cannot do

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: AdamW — Keep Shrinkage Separate from Adaptation](../166-adamw/README.md)
