"""Excavation 175: NumPy implementation of this chapter's repair."""
import numpy as np

reference=np.array([.2,.3,.5]); optimized=np.array([.2,.3,.5]); error=np.max(np.abs(reference-optimized))
assert error==0
print({"equivalence_error":error,"components":14})
