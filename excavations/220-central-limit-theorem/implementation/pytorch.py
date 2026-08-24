"""Excavation 220: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

values=torch.full((100,),10.2); z=(values.mean()-10)/(2/torch.sqrt(torch.tensor(100.))); assert torch.isclose(z,torch.tensor(1.),atol=1e-5); print(z)
