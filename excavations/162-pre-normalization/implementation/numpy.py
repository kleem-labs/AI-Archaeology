"""Excavation 162: NumPy implementation of this chapter's repair."""
import numpy as np

x=np.array([2.,-1.]); branch=np.zeros_like(x); y=x+branch
assert np.array_equal(x,y)
print({"identity_path":y})
