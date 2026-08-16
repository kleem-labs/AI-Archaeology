"""Excavation 187: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

parameters=torch.tensor([100e6,200e6]); tokens=torch.tensor([2e9,1e9]); compute=6*parameters*tokens; assert compute[0]==compute[1]; print({"compute":compute})
