"""Excavation 161: NumPy implementation of this chapter's repair."""
import numpy as np

x=np.array([[3.,4.],[30.,40.]])
y=x/np.sqrt(np.mean(x*x,axis=1,keepdims=True)+1e-8)
assert np.allclose(y[0],y[1])
print({"normalized":y})
