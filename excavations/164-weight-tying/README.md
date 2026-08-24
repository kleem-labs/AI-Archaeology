# Excavation 164 — Weight Tying — Use One Word Geometry Twice

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to let both matrices learn independently because reading a token and predicting it are different jobs.

Reality answers without terminology: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   let both matrices learn independently… the model spends parameters learning…
            \        /
             \      /
              reuse the embedding table transposed…
```

The brass reference machine is divided down the middle. Left side: “let both matrices learn independently because reading a token and predicting it are different jobs.” Its final mark records the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. Right side: the same starting evidence, now allowed to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given weight tying a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. The name **Weight Tying** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to let both matrices learn independently because reading a token and predicting it are different jobs; on the other lies the observed fact that the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. The bridge called weight tying has exactly the planks needed to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

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
