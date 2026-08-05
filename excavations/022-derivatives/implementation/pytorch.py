"""Stage 3: the same Derivatives — Asking One Weight What It Changed idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
