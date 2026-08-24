"""Excavation 209: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

n=torch.arange(1,1001,dtype=torch.float32); values=1/n; assert values[-1]<.002; print(values[-5:])
