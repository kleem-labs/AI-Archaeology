import torch
from torch import nn
class TokenEmbedding(nn.Module):
 def __init__(self,vocabulary_size,width): super().__init__(); self.table=nn.Embedding(vocabulary_size,width)
 def forward(self,token_ids): return self.table(token_ids)
