"""Excavation 184: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

weights=torch.tensor([.5,.2,.15,.1,.05]); assert torch.all(weights>=0) and torch.isclose(weights.sum(),torch.tensor(1.)); print({"weights":weights})
