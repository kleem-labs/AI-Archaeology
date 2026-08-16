"""Excavation 186: NumPy form of the chapter experiment.
"""
import numpy as np

steps=np.int64(2000); batch=np.int64(32*128); tokens=steps*batch; assert tokens==8_192_000; print({"tokens":tokens})
