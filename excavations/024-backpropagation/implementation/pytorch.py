"""Stage 3: the same Backpropagation — Reusing Blame Instead of Recomputing It idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
