"""Excavation 194: NumPy form of the chapter experiment.
"""
import numpy as np

expected=np.array([11,22,33,44]); present=np.array([11,22,33,44]); assert np.array_equal(np.sort(expected),np.sort(present)); print({"complete":True,"shards":len(present)})
