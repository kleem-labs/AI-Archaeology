"""Stage 3 — A Tiny GPT — Close the Prediction Loop."""
import torch

class TinyGPT(torch.nn.Module):
 def __init__(self,vocab,width):
  super().__init__(); self.token=torch.nn.Embedding(vocab,width); self.position=torch.nn.Embedding(128,width); self.head=torch.nn.Linear(width,vocab)
 def forward(self,ids):
  positions=torch.arange(ids.shape[1],device=ids.device); return self.head(self.token(ids)+self.position(positions))
