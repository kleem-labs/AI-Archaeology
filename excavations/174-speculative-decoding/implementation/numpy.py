"""Excavation 174: NumPy implementation of this chapter's repair."""
import numpy as np

target=np.array([.4,.8]); draft=np.array([.8,.4]); acceptance=np.minimum(1.,target/draft)
assert np.allclose(acceptance,[.5,1.])
print({"acceptance":acceptance})
