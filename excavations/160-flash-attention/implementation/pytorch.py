"""Excavation 160: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

scores=torch.tensor([1.,2.,3.,4.]); reference=torch.softmax(scores,0); tiles=torch.chunk(scores,2); rebuilt=torch.softmax(torch.cat(tiles),0)
assert torch.allclose(reference,rebuilt); print({"probabilities":rebuilt})
