"""Stage 3 — A Tiny Neural Network — Assemble the Entire Learning Loop, using differentiable tensors."""
import torch

def run(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)

class TinyNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__(); self.layers=torch.nn.Sequential(torch.nn.Linear(1,4),torch.nn.Sigmoid(),torch.nn.Linear(4,1),torch.nn.Sigmoid())
    def forward(self,x): return self.layers(x)
