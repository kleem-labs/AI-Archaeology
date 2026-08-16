"""Excavation 195: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

state={"weights":torch.tensor([1.]),"moments":torch.tensor([.2]),"step":torch.tensor(200),"cursor":torch.tensor(800),"rng":torch.tensor(7)}; restored={k:v.clone() for k,v in state.items()}; assert all(torch.equal(state[k],restored[k]) for k in state); print(restored)
