"""Excavation 174: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

target=torch.tensor([.4,.8]); draft=torch.tensor([.8,.4]); acceptance=torch.minimum(torch.ones(2),target/draft)
assert torch.allclose(acceptance,torch.tensor([.5,1.])); print({"acceptance":acceptance})
