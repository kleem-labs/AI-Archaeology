"""Excavation 171: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

from torch.utils.checkpoint import checkpoint
x=torch.tensor([2.],requires_grad=True)
def block(v): return v*v+1
y=checkpoint(block,x,use_reentrant=False); y.backward(); assert x.grad.item()==4; print({"output":y.item(),"recomputed_gradient":x.grad.item()})
