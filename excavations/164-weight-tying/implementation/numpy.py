"""Excavation 164: NumPy implementation of this chapter's repair."""
import numpy as np

E=np.array([[1.,0.],[0.,1.]]); hidden=np.array([.8,.2]); logits=hidden@E.T
assert np.allclose(logits,[.8,.2])
print({"logits_from_tied_table":logits})
