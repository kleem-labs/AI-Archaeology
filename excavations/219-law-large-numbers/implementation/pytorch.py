"""Excavation 219: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

values=torch.tensor([1.,0.]).repeat(500); means=torch.cumsum(values,0)/torch.arange(1,len(values)+1); assert means[-1]==.5; print(means[-5:])
