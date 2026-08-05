"""Stage 3 — Momentum — Remembering Which Way Downhill Persists, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
