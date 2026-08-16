"""Excavation 176: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

counts=torch.tensor([8412,12000]); assert counts.sum()==20412; print({"documents":counts})
