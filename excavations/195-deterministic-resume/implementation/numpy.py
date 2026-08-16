"""Excavation 195: NumPy form of the chapter experiment.
"""
import numpy as np

state=np.array([1.0,.2,200,800,7]); restored=state.copy(); assert np.array_equal(state,restored); print({"restored_state":restored})
