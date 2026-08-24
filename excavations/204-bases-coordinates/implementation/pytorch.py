"""Excavation 204: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

basis=torch.tensor([[1.,-1.],[1.,1.]]); v=torch.tensor([3.,2.]); c=torch.linalg.solve(basis,v); assert torch.allclose(basis@c,v); print(c)
