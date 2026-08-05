"""Stage 3 — Learning Rate — How Large Should the Next Step Be?, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
