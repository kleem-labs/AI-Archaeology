"""Excavation 193: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

shape=torch.tensor([2,4,3]); workers=shape.prod(); assert workers==24; print({"parallel_shape":shape,"workers":workers.item()})
