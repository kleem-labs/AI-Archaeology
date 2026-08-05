"""Stage 3: the same Likelihood — Which Hidden Story Produced This Evidence? idea with differentiable tensors."""
import torch

def inspect(values):
    return torch.tensor(values,dtype=torch.float32,requires_grad=True)
