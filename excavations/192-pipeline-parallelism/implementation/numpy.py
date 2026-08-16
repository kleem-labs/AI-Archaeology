"""Excavation 192: NumPy form of the chapter experiment.
"""
import numpy as np

m,p=8,4; utilization=m/(m+p-1); clocks=np.add.outer(np.arange(p),np.arange(m)); assert np.isclose(utilization,8/11); print({"utilization":utilization,"clock_slots":clocks})
