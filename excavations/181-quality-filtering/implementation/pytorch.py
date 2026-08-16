"""Excavation 181: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

signals=torch.tensor([[.8,0.],[0.,2.]]); retained=signals[:,0]<.5; assert torch.equal(retained,torch.tensor([False,True])); print({"retained":retained})
