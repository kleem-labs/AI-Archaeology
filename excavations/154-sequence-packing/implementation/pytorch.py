"""Excavation 154: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

lengths=torch.tensor([6.,5.,3.,2.]); efficiency=lengths.sum()/(2*8)
assert efficiency==1; print({"efficiency":efficiency.item()})
