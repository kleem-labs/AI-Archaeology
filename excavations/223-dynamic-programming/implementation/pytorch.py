"""Excavation 223: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

reward=torch.tensor([2.,1.]); future=torch.tensor([8.,6.]); values=reward+.9*future; assert values.argmax()==0; print(values)
