"""Excavation 153: PyTorch implementation of this chapter's repair."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

stages=torch.tensor([35.,45.]); print({"serial_ms":stages.sum().item(),"overlapped_ms":stages.max().item()})
