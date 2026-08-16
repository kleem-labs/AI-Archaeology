"""Excavation 196: NumPy form of the chapter experiment.
"""
import numpy as np

history=np.array([2.0,2.1,1.9,2.0]); current=2.6; z=(current-history.mean())/(history.std() or 1); assert z>3; print({"z_score":z})
