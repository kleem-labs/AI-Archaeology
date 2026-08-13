"""Excavation 168: NumPy implementation of this chapter's repair."""
import numpy as np

a=np.ones(1_000_000,dtype=np.float32); b=a.astype(np.float16)
assert b.nbytes==a.nbytes//2
print({"fp32_bytes":a.nbytes,"fp16_bytes":b.nbytes})
