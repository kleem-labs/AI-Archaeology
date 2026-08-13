"""Excavation 173: NumPy implementation of this chapter's repair."""
import numpy as np

x=np.array([2.,3.]); W=np.array([[1,0,2,0],[0,1,0,2]],dtype=float); blocks=np.hsplit(W,2); joined=np.concatenate([x@b for b in blocks])
assert np.allclose(joined,x@W)
print({"joined":joined})
