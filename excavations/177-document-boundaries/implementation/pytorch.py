"""Excavation 177: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

ids=torch.tensor([0,0,1]); mask=(ids[:,None]==ids[None,:]).int(); assert torch.equal(mask[0],torch.tensor([1,1,0])); print({"mask":mask})
