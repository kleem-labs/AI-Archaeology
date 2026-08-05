"""Stage 3 — Initialization — Where Should Learning Begin?, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
