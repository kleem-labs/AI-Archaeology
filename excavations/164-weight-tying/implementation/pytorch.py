"""Excavation 164: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

E=torch.tensor([[1.,0.],[0.,1.]],requires_grad=True); hidden=torch.tensor([.8,.2]); logits=hidden@E.T; logits.sum().backward()
assert E.grad is not None; print({"logits":logits,"shared_table_gradient":E.grad})
