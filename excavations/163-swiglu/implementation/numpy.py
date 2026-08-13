"""Excavation 163: NumPy implementation of this chapter's repair."""
import numpy as np

gate=np.array([-10.,2.]); value=np.array([5.,5.]); silu=gate/(1+np.exp(-gate)); out=silu*value
assert out[0]<0 and out[1]>8
print({"gated":out})
