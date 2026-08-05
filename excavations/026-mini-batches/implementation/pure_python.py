"""Stage 1 — Mini-Batches — Learning from More Than One Example, with operations visible."""

def batch_gradient(gradients):
 width=len(gradients[0]); return [sum(g[j] for g in gradients)/len(gradients) for j in range(width)]
