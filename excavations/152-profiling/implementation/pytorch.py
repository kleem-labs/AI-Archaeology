"""Excavation 152: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

parts=torch.tensor([35.,45.,10.,10.]); shares=parts/parts.sum()
assert parts.sum()==100 and shares.argmax()==1; print({"total_ms":parts.sum().item(),"shares":shares})
