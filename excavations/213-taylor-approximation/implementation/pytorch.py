"""Excavation 213: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

h=torch.tensor(.1); powers=torch.arange(5); factorial=torch.tensor([math.factorial(n) for n in range(5)]); estimate=(h**powers/factorial).sum(); assert torch.isclose(estimate,torch.exp(h),atol=1e-5); print(estimate)
