"""Excavation 163: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

gate=torch.tensor([-10.,2.]); value=torch.tensor([5.,5.]); out=torch.nn.functional.silu(gate)*value
assert out[0]<0 and out[1]>8; print({"gated":out})
