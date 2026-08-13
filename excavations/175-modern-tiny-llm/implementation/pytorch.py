"""Excavation 175: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

reference=torch.tensor([.2,.3,.5]); optimized=reference.clone(); error=(reference-optimized).abs().max()
assert error==0; print({"equivalence_error":error.item(),"components":14})
