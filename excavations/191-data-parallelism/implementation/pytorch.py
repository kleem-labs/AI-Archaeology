"""Excavation 191: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

workers=torch.tensor([[2.,4.],[4.,2.],[3.,3.],[3.,3.]]); shared=workers.mean(0); assert torch.equal(shared,torch.tensor([3.,3.])); print({"shared_gradient":shared})
