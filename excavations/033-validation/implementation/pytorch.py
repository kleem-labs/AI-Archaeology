"""Stage 3 — Validation — Testing Without Peeking at the Final Exam, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
