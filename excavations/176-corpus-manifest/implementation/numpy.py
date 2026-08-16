"""Excavation 176: NumPy form of the chapter experiment.
"""
import numpy as np

sources=np.array(["field-v3","science-v2"]); counts=np.array([8412,12000]); assert counts.sum()==20412; print({"sources":sources,"documents":counts})
