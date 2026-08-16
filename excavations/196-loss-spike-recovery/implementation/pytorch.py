"""Excavation 196: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

history=torch.tensor([2.,2.1,1.9,2.]); current=torch.tensor(2.6); z=(current-history.mean())/history.std(correction=0); assert z>3; print({"z_score":z})
