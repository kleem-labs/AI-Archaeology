"""Excavation 224: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

f=lambda z:z*z; x=torch.tensor(-2.); y=torch.tensor(2.); weight=.5; left=f(weight*x+(1-weight)*y); right=weight*f(x)+(1-weight)*f(y); assert left<=right; print(left,right)
