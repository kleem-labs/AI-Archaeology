"""Excavation 201: tensor form of the same named experiment."""
import math
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

a={'tiger','deer','otter'}; b={'tiger','otter','frog'}; out=a&b; assert out=={'tiger','otter'}; print(out)
