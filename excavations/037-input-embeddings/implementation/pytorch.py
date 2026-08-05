"""The industry form: a trainable embedding module."""
import torch
from torch import nn

class InputEmbedding(nn.Module):
 def __init__(self,vocabulary_size,width):
  super().__init__(); self.table=nn.Embedding(vocabulary_size,width)
 def forward(self,token_ids):
  return self.table(token_ids)

if __name__=="__main__":
 model=InputEmbedding(100,16)
 ids=torch.tensor([[4,8,2],[7,3,0]])
 print(model(ids).shape)
