# Excavation 164 — Weight Tying — Use One Word Geometry Twice

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: let both matrices learn independently because reading a token and predicting it are different jobs.

The attraction of this attempt is easy to see. To let both matrices learn independently because reading a token and predicting it are different jobs reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

The contradiction matters because it identifies a structural loss in the instruction to let both matrices learn independently because reading a token and predicting it are different jobs, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Weight Tying**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Use One Word Geometry Twice

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

## The calculation hidden inside weight tying

The enginewright carries the weight tying scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

### Why the melody needs these exact notes

[Equality](../../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Nothing remains unnamed in the weight tying case on the brass reference machine. We can finally trade the long route for its compact map:

$$
W_{\text{out}}=E^{\mathsf T}
$$

## Where weight tying runs out

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

A final test reaches beyond the new instrument. It does not refute Weight Tying; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

## Return to the brass reference machine

Rebuild the weight tying scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Adam — Give Each Parameter Its Own Step Scale](../165-adam/README.md)
