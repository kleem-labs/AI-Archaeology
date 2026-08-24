# Excavation 038 — Position — Why Order Must Enter the Model

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Language models and useful answers

An embedding table gives every token a learned starting description. The sentences “dog bites man” and “man bites dog” still contain the same three descriptions, so the machine cannot tell who did what.

The doors of the Clockwork Scriptorium close against the wind. On the sentence-wheel, the mechanist writes the cheapest rule that might still be true: sort tokens by ID or trust their array slot without exposing it to the model.

Reality answers without terminology: the first invents arbitrary order; the second stores position outside the computation. The sentence-wheel now holds two situations the old rule cannot keep apart.

*The mechanist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: sort tokens by ID or trust their…
                         │
                         └── mismatch: the first invents arbitrary order;…

reference evidence ──▶ measured repair: add a position-specific vector to…
```

The sentence-wheel is divided down the middle. Left side: “sort tokens by ID or trust their array slot without exposing it to the model.” Its final mark records the first invents arbitrary order; the second stores position outside the computation. Right side: the same starting evidence, now allowed to add a position-specific vector to each token vector before attention. Content says what; position says where. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given position a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: add a position-specific vector to each token vector before attention. Content says what; position says where. The name **Position** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from position through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the first invents arbitrary order; the second stores position outside the computation. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

## The calculation hidden inside position

The mechanist carries the position scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

Compare “tiger chases deer” with “deer chases tiger.” The same three word cards appear, so content alone cannot distinguish hunter from hunted. Give the first slot one reusable position mark, the second another, and the third another. Adding the appropriate mark to each word leaves *tiger* recognizable while also telling later attention whether this occurrence came first or last.

### Naming what is already on the table

**token_i** is the vocabulary address appearing at sequence location i.
**E[token_i]** retrieves what that token currently represents.
**P_i** represents where the occurrence sits.
Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
**z_i** is the combined input at position i.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.
[The shared index i](../../MATHEMATICAL_MOVES.md#indices) forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.

The mandala has curved back upon itself. In this chamber we meet **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Nothing remains unnamed in the position case on the sentence-wheel. We can finally trade the long route for its compact map:

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

## Position beyond this one case

Seat numbers do not describe passengers, but they preserve who sat where.

## Return to the sentence-wheel

Rebuild the position scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 039](../039-causal-mask/README.md)
