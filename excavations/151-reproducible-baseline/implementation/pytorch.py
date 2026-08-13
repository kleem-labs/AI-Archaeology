"""Excavation 151: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

baseline=torch.tensor([2.4,2.3,2.35]); candidate=torch.tensor([2.1,2.2,2.15]); change=candidate-baseline
assert torch.all(change<0); print({"mean_change":change.mean().item()})
