"""Excavation 161: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([[3.,4.],[30.,40.]]); y=x*torch.rsqrt((x*x).mean(-1,keepdim=True)+1e-8)
assert torch.allclose(y[0],y[1]); print({"normalized":y})
