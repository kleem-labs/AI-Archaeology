"""Excavation 156: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

scores=torch.tensor([3.,3.]); distances=torch.tensor([2.,20.]); adjusted=scores-.1*distances
assert torch.allclose(adjusted,torch.tensor([2.8,1.])); print({"adjusted_scores":adjusted})
