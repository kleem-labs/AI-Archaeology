"""Excavation 192: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

m,p=8,4; clocks=torch.arange(p)[:,None]+torch.arange(m)[None,:]; utilization=m/(m+p-1); assert clocks.shape==(4,8); print({"utilization":utilization,"clock_slots":clocks})
