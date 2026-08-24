"""Excavation 211: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

point=torch.tensor([2.,3.]); fn=lambda p:torch.stack((p[0]+p[1],p[0]*p[1])); J=torch.autograd.functional.jacobian(fn,point); assert torch.allclose(J,torch.tensor([[1.,1.],[3.,2.]])); print(J)
