"""Stage 3 — Activation Functions — Why a Network Must Bend, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
