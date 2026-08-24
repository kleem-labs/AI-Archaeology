"""Excavation 222: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

P=torch.tensor([[0.,.7,.3],[.4,0.,.6],[.2,.3,.5]]); state=torch.tensor([1.,0.,0.]); tomorrow=state@P; assert torch.isclose(tomorrow.sum(),torch.tensor(1.)); print(tomorrow)
