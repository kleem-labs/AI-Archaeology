"""Excavation 212: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

point=torch.tensor([0.,0.]); fn=lambda p:p[0]**2+3*p[1]**2+p[0]*p[1]; H=torch.autograd.functional.hessian(fn,point); assert torch.allclose(H,torch.tensor([[2.,1.],[1.,6.]])); print(H)
