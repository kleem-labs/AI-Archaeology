"""Stage 3 — Causal Masking — Preventing the Future from Leaking Backward."""
import torch

def mask(length): return torch.triu(torch.full((length,length),float("-inf")),diagonal=1)
