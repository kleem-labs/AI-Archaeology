"""Excavation 187: NumPy form of the chapter experiment.
"""
import numpy as np

parameters=np.array([100e6,200e6]); tokens=np.array([2e9,1e9]); compute=6*parameters*tokens; assert compute[0]==compute[1]; print({"compute":compute})
