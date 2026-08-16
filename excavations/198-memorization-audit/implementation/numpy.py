"""Excavation 198: NumPy form of the chapter experiment.
"""
import numpy as np

ranks=np.array([100000,10]); exposure=np.log2(1_000_000)-np.log2(ranks); assert exposure[1]>exposure[0]; print({"exposure":exposure})
