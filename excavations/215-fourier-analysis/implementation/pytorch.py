"""Excavation 215: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

samples=torch.tensor([1.,0.,-1.,0.]); spectrum=torch.fft.fft(samples); assert torch.isclose(spectrum[1].real,torch.tensor(2.)); print(spectrum)
