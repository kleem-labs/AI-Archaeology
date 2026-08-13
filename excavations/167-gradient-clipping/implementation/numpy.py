"""Excavation 167: NumPy implementation of this chapter's repair."""
import numpy as np

g=np.array([12.,16.]); scale=min(1.,5./np.linalg.norm(g)); clipped=g*scale
assert np.allclose(clipped,[3.,4.])
print({"clipped":clipped})
