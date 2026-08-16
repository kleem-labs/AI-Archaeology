"""Excavation 189: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

steps=torch.tensor([0.,50.,100.]); rates=.0001+(.001-.0001)/2*(1+torch.cos(torch.pi*steps/100)); assert torch.isclose(rates[1],torch.tensor(.00055)); print({"rates":rates})
