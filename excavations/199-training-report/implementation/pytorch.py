"""Excavation 199: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

metrics=torch.tensor([8_192_000.,49_152_000.,2.1,.3]); assert torch.isfinite(metrics).all(); print({"tokens_compute_loss_exposure":metrics})
