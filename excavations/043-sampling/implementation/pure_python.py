"""Stage 1 — Sampling — Choosing Without Always Taking the Maximum, with operations visible."""

import random
from math import exp
def sample(logits,temperature=1.0,seed=0):
 m=max(logits); e=[exp((x-m)/temperature) for x in logits]; total=sum(e); random.seed(seed); r=random.random()*total
 for i,w in enumerate(e):
  r-=w
  if r<=0:return i
 return len(e)-1
