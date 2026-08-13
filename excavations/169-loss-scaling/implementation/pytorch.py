"""Excavation 169: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

x=torch.tensor([1e-3],requires_grad=True); scale=1000.; scaled=(x*x)*scale; scaled.backward(); recovered=x.grad/scale
assert torch.allclose(recovered,torch.tensor([2e-3])); print({"scaled_gradient":x.grad,"recovered":recovered})
