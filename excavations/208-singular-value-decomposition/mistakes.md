# Mistakes Worth Preserving — Excavation 208

## The tempting idea

We tried to keep the largest individual matrix entries and set the rest to zero.

## The evidence that refused it

a useful direction may be distributed across many modest entries, while one large entry may contribute little to the matrix's coordinated behavior. Entry size ignores how rows and columns act together.

## What the wreckage taught us

The next construction had to rotate the input into orthogonal right-singular directions, scale each by a nonnegative singular value, and rotate into orthogonal output directions; keep the strongest channels for a principled low-rank approximation.

Keep this wrong idea. It is the negative space around Singular Value Decomposition: it records why the accepted method has exactly the responsibilities it does.
