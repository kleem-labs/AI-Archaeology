"""Excavation 172: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

state=torch.arange(12); shards=torch.chunk(state,4)
assert all(s.numel()==3 for s in shards); print({"shards":shards})
