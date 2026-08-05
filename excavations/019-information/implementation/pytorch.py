"""Stage 3: the same Information — Why Surprise Needs a Number idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
