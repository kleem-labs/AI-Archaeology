"""Excavation 182: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

stage_ids=torch.tensor([0,1,2,3]); assert torch.equal(stage_ids[1:],stage_ids[:-1]+1); print({"lineage_stage_ids":stage_ids})
