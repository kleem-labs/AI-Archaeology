"""Excavation 157: NumPy implementation of this chapter's repair."""
import numpy as np

cache=np.arange(6).reshape(3,2); new=np.array([[6,7]])
cache=np.concatenate([cache,new],axis=0)
assert cache.shape==(4,2) and np.array_equal(cache[-1],new[0])
print({"cache":cache})
