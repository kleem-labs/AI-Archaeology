"""Excavation 200: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

gates=torch.tensor([True,True,True,False,True,True]); release=torch.all(gates); assert not release; print({"release":release.item(),"failed_gate":torch.where(~gates)[0]})
