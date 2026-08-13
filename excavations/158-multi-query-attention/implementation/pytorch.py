"""Excavation 158: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

kv=torch.tensor([8,1])*100*64*2
assert kv[0]==8*kv[1]; print({"mha_values":kv[0].item(),"mqa_values":kv[1].item()})
