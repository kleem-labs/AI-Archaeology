# Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

<!-- book-prose-v2 -->

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

At this point the shortest path seems to be to use the same raw gradient step scale for every parameter.

This is how adam ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

The wrong answer makes the need for adam inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

The usual name, **Adam**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to use the same raw gradient step scale for every parameter produces the observed failure: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. Starting with the repaired demand to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude preserves the information the shortcut lost. The subject of adam lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude instead of merely trying to use the same raw gradient step scale for every parameter. That controlled contrast is what turns a plausible explanation of adam into an understandable derivation.

## Give Each Parameter Its Own Step Scale

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

There are now two histories of this adam case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside adam

Before Adam receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Every symbol in Adam can now be read back into an action already performed. The whole procedure fits in one line:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## Where adam runs out

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

Look back at what adam actually preserves: it can keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take adam to the workbench

The reader has reconstructed adam in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running adam, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the adam result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: AdamW — Keep Shrinkage Separate from Adaptation](../166-adamw/README.md)
