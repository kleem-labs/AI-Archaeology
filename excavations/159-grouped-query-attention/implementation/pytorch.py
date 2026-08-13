"""Excavation 159: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

heads=torch.arange(8); groups=torch.floor(heads*2/8).long()
assert torch.equal(groups,torch.tensor([0,0,0,0,1,1,1,1])); print({"groups":groups})
