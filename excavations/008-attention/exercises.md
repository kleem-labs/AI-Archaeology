# Exercises — Attention

## Trace Context

1. In “Sam put the book on the table because it was sturdy,” what should *it* retrieve?
2. Rewrite the ending so *it* refers to the book instead. Which routing weights should change?
3. Find a sentence whose important dependency crosses at least ten words.

## Calculate

4. Compute the weighted sum of `[1, 0]` and `[0, 2]` with weights `0.75` and `0.25`.
5. Use the chapter's three value vectors and weights `[0.05, 0.80, 0.15]`.
6. Prove coordinate by coordinate that a weighted mixture has the same dimension as each value.

## Experiment

7. Run `implementation.py` and make the output move toward each source in turn.
8. Supply weights that do not sum to one. Explain why the program refuses them.
9. Give every token equal weight. Describe precisely what information is lost.

## Reconstruct

10. Design an attention-style retrieval system for choosing evidence from five notes when answering a question. Separate routing from contributed content.
