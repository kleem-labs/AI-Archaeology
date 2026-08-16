"""Excavation 198: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

ranks=torch.tensor([100000.,10.]); exposure=torch.log2(torch.tensor(1_000_000.))-torch.log2(ranks); assert exposure[1]>exposure[0]; print({"exposure":exposure})
