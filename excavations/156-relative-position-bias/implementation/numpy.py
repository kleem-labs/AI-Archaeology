"""Excavation 156: NumPy implementation of this chapter's repair."""
import numpy as np

scores=np.array([3.,3.]); distances=np.array([2.,20.])
adjusted=scores-.1*distances
assert np.allclose(adjusted,[2.8,1.])
print({"adjusted_scores":adjusted})
