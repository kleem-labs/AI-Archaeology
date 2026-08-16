"""Excavation 194: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

expected=torch.tensor([11,22,33,44]); present=torch.tensor([11,22,33,44]); assert torch.equal(torch.sort(expected).values,torch.sort(present).values); print({"complete":True})
