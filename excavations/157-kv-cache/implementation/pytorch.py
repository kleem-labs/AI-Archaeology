"""Excavation 157: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

cache=torch.arange(6).reshape(3,2); new=torch.tensor([[6,7]]); cache=torch.cat([cache,new])
assert cache.shape==(4,2); print({"cache":cache})
