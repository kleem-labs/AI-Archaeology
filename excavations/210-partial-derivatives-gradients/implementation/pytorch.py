"""Excavation 210: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

point=torch.tensor([218.,94.],requires_grad=True); loss=((point-torch.tensor([220.,90.]))**2).sum(); loss.backward(); assert torch.allclose(point.grad,torch.tensor([-4.,8.])); print(point.grad)
