"""Excavation 202: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

edges=torch.tensor([[0,0],[1,0]]); query=torch.tensor([0,0]); assert torch.any(torch.all(edges==query,dim=1)); print(edges)
