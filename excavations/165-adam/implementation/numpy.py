"""Excavation 165: NumPy implementation of this chapter's repair."""
import numpy as np

g=np.array([2.,.2]); m=.1*g; v=.001*g*g; mh=m/(1-.9); vh=v/(1-.999); step=mh/(np.sqrt(vh)+1e-8)
assert np.allclose(step,[1.,1.],atol=1e-6)
print({"raw_gradient":g,"adapted_step":step})
