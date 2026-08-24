"""Excavation 214: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

t=torch.linspace(0,1,10001); total=torch.trapezoid(2*t,t); assert torch.isclose(total,torch.tensor(1.)); print(total)
