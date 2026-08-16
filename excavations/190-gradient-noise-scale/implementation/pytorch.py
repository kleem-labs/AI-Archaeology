"""Excavation 190: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

g=torch.tensor([[2.,1.],[2.1,.9],[1.9,1.1]]); mean=g.mean(0); centered=g-mean; covariance=centered.T@centered/len(g); scale=torch.trace(covariance)/(mean@mean); assert scale<.01; print({"noise_scale":scale})
