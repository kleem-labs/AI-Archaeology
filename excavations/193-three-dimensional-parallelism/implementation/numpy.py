"""Excavation 193: NumPy form of the chapter experiment.
"""
import numpy as np

shape=np.array([2,4,3]); workers=shape.prod(); coords=np.stack(np.unravel_index(np.arange(workers),shape),axis=1); assert len(coords)==24; print({"worker_grid":shape,"workers":workers})
