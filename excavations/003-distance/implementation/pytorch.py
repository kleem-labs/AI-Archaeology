"""Stage 3 — Euclidean distance, using trainable tensor machinery."""
try:
 import torch
except ImportError as e:
 raise SystemExit("Install torch for Stage 3") from e

# This tensor remains inspectable and can participate in automatic differentiation.
def inspect(values):
 return torch.tensor(values,dtype=torch.float32,requires_grad=True)
