"""Stage 3 — Overfitting — When Perfect Memory Pretends to Be Intelligence, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
