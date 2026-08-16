"""Excavation 191: NumPy form of the chapter experiment.
"""
import numpy as np

workers=np.array([[2.,4.],[4.,2.],[3.,3.],[3.,3.]]); shared=workers.mean(0); assert np.array_equal(shared,[3,3]); print({"shared_gradient":shared})
