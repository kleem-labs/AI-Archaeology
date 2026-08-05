"""Stage 3 — Mini-Batches — Learning from More Than One Example, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
