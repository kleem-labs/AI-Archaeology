"""Stage 3 — Regularization — Making Memorization More Expensive, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
