"""A compact Transformer block after its components have earned their names."""

from __future__ import annotations

try:
    import torch
    from torch import nn
except ImportError as error:
    raise SystemExit("Install PyTorch to run this optional implementation stage") from error


class CausalSelfAttention(nn.Module):
    def __init__(self, width: int, heads: int) -> None:
        super().__init__()
        if width % heads:
            raise ValueError("model width must divide evenly across attention heads")
        self.heads = heads
        self.head_width = width // heads
        self.qkv = nn.Linear(width, 3 * width)
        self.combine = nn.Linear(width, width)

    def forward(self, tokens: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        batch, length, width = tokens.shape
        qkv = self.qkv(tokens).view(batch, length, 3, self.heads, self.head_width)
        query, key, value = qkv.unbind(dim=2)
        query, key, value = [part.transpose(1, 2) for part in (query, key, value)]
        scores = query @ key.transpose(-2, -1) / (self.head_width ** 0.5)
        future = torch.triu(torch.ones(length, length, device=tokens.device, dtype=torch.bool), 1)
        scores = scores.masked_fill(future, float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        context = weights @ value
        context = context.transpose(1, 2).contiguous().view(batch, length, width)
        return self.combine(context), weights


class TransformerBlock(nn.Module):
    """Communication, private processing, safe correction, stable scale."""

    def __init__(self, width: int = 32, heads: int = 4, expansion: int = 4) -> None:
        super().__init__()
        self.attention_norm = nn.LayerNorm(width)
        self.attention = CausalSelfAttention(width, heads)
        self.ffn_norm = nn.LayerNorm(width)
        self.ffn = nn.Sequential(
            nn.Linear(width, expansion * width),
            nn.GELU(),
            nn.Linear(expansion * width, width),
        )

    def forward(self, tokens: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        proposal, weights = self.attention(self.attention_norm(tokens))
        tokens = tokens + proposal
        tokens = tokens + self.ffn(self.ffn_norm(tokens))
        return tokens, weights


if __name__ == "__main__":
    torch.manual_seed(7)
    block = TransformerBlock()
    sample = torch.randn(2, 6, 32)
    output, attention_weights = block(sample)
    print("token shape:", tuple(output.shape))
    print("attention shape:", tuple(attention_weights.shape))
