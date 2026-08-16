"""Excavation 184: NumPy form of the chapter experiment.
"""
import numpy as np

weights=np.array([.5,.2,.15,.1,.05]); assert np.all(weights>=0) and np.isclose(weights.sum(),1); print({"weights":weights})
