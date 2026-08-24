"""Excavation 218: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([0.,2.]); y=torch.tensor([0.,2.]); covariance=((x-x.mean())*(y-y.mean())).mean(); assert x.var(correction=0)==1 and covariance==1; print(x.mean(),x.var(correction=0),covariance)
