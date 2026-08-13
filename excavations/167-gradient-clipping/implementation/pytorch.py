"""Excavation 167: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

p=torch.nn.Parameter(torch.zeros(2)); p.grad=torch.tensor([12.,16.]); before=p.grad.norm(); torch.nn.utils.clip_grad_norm_([p],5.); after=p.grad.norm()
assert torch.allclose(after,torch.tensor(5.)); print({"before":before.item(),"after":after.item()})
