"""Excavation 165: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

theta=torch.nn.Parameter(torch.tensor([1.])); opt=torch.optim.Adam([theta],lr=.1); (theta**2).backward(); opt.step()
assert theta.item()<1; print({"theta":theta.item()})
