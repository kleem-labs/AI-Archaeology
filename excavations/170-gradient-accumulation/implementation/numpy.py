"""Excavation 170: NumPy implementation of this chapter's repair."""
import numpy as np

micro=np.array([[2.,4.],[4.,2.],[3.,3.]])
effective=micro.mean(axis=0)
assert np.allclose(effective,[3.,3.])
print({"effective_gradient":effective})
