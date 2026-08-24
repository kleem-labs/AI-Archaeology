"""Excavation 221: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

d=torch.tensor([-1.6,2.4]).repeat(50); mean=d.mean(); se=d.std()/torch.sqrt(torch.tensor(float(len(d)))); interval=mean+torch.tensor([-1.,1.])*1.96*se; assert interval[0]<mean<interval[1]; print(mean,se,mean/se,interval)
