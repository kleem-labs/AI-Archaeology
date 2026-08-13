"""Excavation 173: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([2.,3.]); W=torch.tensor([[1,0,2,0],[0,1,0,2]],dtype=torch.float32); blocks=torch.chunk(W,2,dim=1); joined=torch.cat([x@b for b in blocks])
assert torch.equal(joined,x@W); print({"joined":joined})
