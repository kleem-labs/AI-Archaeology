"""Excavation 166: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

theta=torch.nn.Parameter(torch.tensor([2.])); opt=torch.optim.AdamW([theta],lr=.1,weight_decay=.01); (theta*.5).backward(); opt.step()
assert theta.item()<2; print({"theta":theta.item()})
