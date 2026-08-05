"""Stage 3: the same Probability — Counting What We Do Not Know idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
