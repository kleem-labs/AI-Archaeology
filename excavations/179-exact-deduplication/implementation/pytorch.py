"""Excavation 179: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

fingerprints=torch.tensor([12,12,91,37,91]); unique,counts=torch.unique(fingerprints,return_counts=True); assert counts.max()==2; print({"unique":unique,"counts":counts})
