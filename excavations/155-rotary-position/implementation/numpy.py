"""Excavation 155: NumPy implementation of this chapter's repair."""
import numpy as np

angles=np.array([.5,1.0]); c=np.cos(angles); s=np.sin(angles)
rotated=np.stack([c,s],axis=1)
match=rotated[0]@rotated[1]
assert np.allclose(match,np.cos(.5))
print({"relative_match":match})
