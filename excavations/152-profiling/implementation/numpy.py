"""Excavation 152: NumPy implementation of this chapter's repair."""
import numpy as np

parts=np.array([35,45,10,10],dtype=float)
shares=parts/parts.sum()
assert parts.sum()==100 and shares.argmax()==1
print({"total_ms":parts.sum(),"shares":shares})
