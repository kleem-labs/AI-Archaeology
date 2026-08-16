"""Excavation 181: NumPy form of the chapter experiment.
"""
import numpy as np

signals=np.array([[.8,0],[.0,2]],dtype=float); retained=signals[:,0]<.5; assert np.array_equal(retained,[False,True]); print({"signals":signals,"retained":retained})
