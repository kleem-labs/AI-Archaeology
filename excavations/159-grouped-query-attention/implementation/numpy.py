"""Excavation 159: NumPy implementation of this chapter's repair."""
import numpy as np

heads=np.arange(8); groups=np.floor(heads*2/8).astype(int)
assert np.array_equal(groups,[0,0,0,0,1,1,1,1])
print({"groups":groups})
