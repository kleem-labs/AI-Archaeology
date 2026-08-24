"""Excavation 203: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

weights=torch.tensor([220.,90.,12.]); assert weights[0]==220; print(weights)
