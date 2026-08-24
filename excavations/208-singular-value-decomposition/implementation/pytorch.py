"""Excavation 208: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

A=torch.diag(torch.tensor([3.,1.])); u,s,vh=torch.linalg.svd(A); assert torch.allclose((u*s)@vh,A); print(s)
