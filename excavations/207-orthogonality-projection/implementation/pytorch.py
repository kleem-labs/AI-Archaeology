"""Excavation 207: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

v=torch.tensor([3.,2.]); u=torch.tensor([1.,0.]); shadow=(v@u)/(u@u)*u; assert torch.allclose(shadow,torch.tensor([3.,0.])); print(shadow)
