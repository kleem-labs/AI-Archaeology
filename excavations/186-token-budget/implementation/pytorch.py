"""Excavation 186: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

tokens=torch.tensor(2000,dtype=torch.int64)*32*128; assert tokens==8_192_000; print({"tokens":tokens.item()})
