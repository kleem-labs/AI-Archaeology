"""Excavation 169: NumPy implementation of this chapter's repair."""
import numpy as np

loss=np.float16(1e-6); scale=np.float16(1000); visible=np.float16(loss*scale); recovered=np.float32(visible)/np.float32(scale)
assert visible>loss
print({"scaled":visible,"recovered":recovered})
