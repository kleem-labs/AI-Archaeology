"""Excavation 179: NumPy form of the chapter experiment.
"""
import numpy as np

fingerprints=np.array([12,12,91,37,91]); unique,counts=np.unique(fingerprints,return_counts=True); assert counts.max()==2; print({"unique":unique,"duplicate_counts":counts})
