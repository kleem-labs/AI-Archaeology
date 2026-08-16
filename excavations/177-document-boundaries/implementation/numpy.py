"""Excavation 177: NumPy form of the chapter experiment.
"""
import numpy as np

ids=np.array([0,0,1]); mask=(ids[:,None]==ids[None,:]).astype(int); assert np.array_equal(mask[0],[1,1,0]); print({"mask":mask})
