"""Excavation 183: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

risk=torch.tensor([0.,1.,0.,1.,0.,0.]); redacted=risk.bool(); assert redacted.sum()==2; print({"redacted_positions":torch.where(redacted)[0]})
