"""Excavation 217: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

prior=torch.tensor([.1,.9]); likelihood=torch.tensor([.8,.1]); posterior=prior*likelihood/(prior@likelihood); assert torch.isclose(posterior[0],torch.tensor(8/17)); print(posterior)
