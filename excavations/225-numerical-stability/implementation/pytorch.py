"""Excavation 225: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([1000.,999.,998.]); value=torch.logsumexp(x,dim=0); assert torch.isfinite(value); print(value)
