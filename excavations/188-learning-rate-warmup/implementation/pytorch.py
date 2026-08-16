"""Excavation 188: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

steps=torch.tensor([0.,25.,50.,100.]); rates=.001*torch.minimum(torch.ones_like(steps),steps/100); assert torch.allclose(rates,torch.tensor([0.,.00025,.0005,.001])); print({"rates":rates})
