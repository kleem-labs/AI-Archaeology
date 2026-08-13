"""Excavation 170: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

micro=torch.tensor([[2.,4.],[4.,2.],[3.,3.]]); effective=micro.mean(0)
assert torch.equal(effective,torch.tensor([3.,3.])); print({"effective_gradient":effective})
