"""Excavation 162: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([2.,-1.],requires_grad=True); y=x+torch.zeros_like(x); y.sum().backward()
assert torch.equal(x.grad,torch.ones_like(x)); print({"identity_gradient":x.grad})
