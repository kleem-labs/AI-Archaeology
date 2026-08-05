"""Stage 1 — Regularization — Making Memorization More Expensive, with operations visible."""

def l2_loss(data_loss,weights,strength): return data_loss+strength*sum(w*w for w in weights)
