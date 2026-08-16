"""Excavation 197: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

p=torch.tensor([[.7,.6],[.8,.9]]); losses=-torch.log(p).mean(1); assert losses[0]>losses[1]; print({"domain_losses":losses})
