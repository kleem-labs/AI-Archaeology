"""Excavation 155: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

angles=torch.tensor([.5,1.]); rotated=torch.stack([torch.cos(angles),torch.sin(angles)],dim=1); match=rotated[0]@rotated[1]
assert torch.allclose(match,torch.cos(torch.tensor(.5))); print({"relative_match":match.item()})
