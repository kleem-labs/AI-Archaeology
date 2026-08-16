"""Excavation 180: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

a=torch.tensor([1,1,1,1,0,0],dtype=torch.bool); b=torch.tensor([1,1,1,0,1,0],dtype=torch.bool); score=(a&b).sum().float()/(a|b).sum(); assert 0<score<1; print({"jaccard":score})
