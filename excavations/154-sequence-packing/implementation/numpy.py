"""Excavation 154: NumPy implementation of this chapter's repair."""
import numpy as np

lengths=np.array([6,5,3,2]); rows=np.array([[6,2],[5,3]])
efficiency=lengths.sum()/(rows.shape[0]*8)
assert efficiency==1
print({"packed_rows":rows,"efficiency":efficiency})
