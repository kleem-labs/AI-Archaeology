"""Excavation 178: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

scores=torch.tensor([.93,.05,.02]); winner=scores.argmax(); assert winner.item()==0 and scores.max()>=.8; print({"winner_index":winner.item(),"confidence":scores.max().item()})
