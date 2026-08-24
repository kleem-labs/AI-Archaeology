"""Excavation 205: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

directions=torch.tensor([[1.,0.,1.],[0.,1.,1.]]); rank=torch.linalg.matrix_rank(directions); assert rank==2; print(rank)
