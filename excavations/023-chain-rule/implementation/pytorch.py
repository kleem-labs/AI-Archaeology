"""Stage 3: the same The Chain Rule — Following One Change Through Many Machines idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
