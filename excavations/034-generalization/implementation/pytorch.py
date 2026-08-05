"""Stage 3 — Generalization — What Should Survive Beyond the Dataset?, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
