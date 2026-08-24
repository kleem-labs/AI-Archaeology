"""Excavation 206: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

A=torch.diag(torch.tensor([2.,1.])); values,vectors=torch.linalg.eig(A); assert torch.allclose((A@vectors.real),vectors.real@torch.diag(values.real)); print(values)
