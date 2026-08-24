"""Excavation 216: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

values=torch.tensor([0,0,1,2]); probability=torch.full((4,),.25); masses=torch.zeros(3).scatter_add_(0,values,probability); assert torch.allclose(masses,torch.tensor([.5,.25,.25])); print(masses)
