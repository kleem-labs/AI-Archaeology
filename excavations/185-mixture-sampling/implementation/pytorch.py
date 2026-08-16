"""Excavation 185: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

generator=torch.Generator().manual_seed(7); weights=torch.tensor([.8,.2]); draws=torch.multinomial(weights,1000,replacement=True,generator=generator); counts=torch.bincount(draws,minlength=2); assert counts.sum()==1000; print({"counts":counts})
