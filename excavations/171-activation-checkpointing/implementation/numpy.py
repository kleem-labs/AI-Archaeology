"""Excavation 171: NumPy implementation of this chapter's repair."""
import numpy as np

layers=np.arange(9); kept=layers[::3]; recomputed=np.setdiff1d(layers,kept)
assert np.array_equal(kept,[0,3,6])
print({"kept":kept,"recomputed":recomputed})
