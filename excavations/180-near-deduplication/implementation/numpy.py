"""Excavation 180: NumPy form of the chapter experiment.
"""
import numpy as np

a=np.array([1,1,1,1,0,0],dtype=bool); b=np.array([1,1,1,0,1,0],dtype=bool); score=np.logical_and(a,b).sum()/np.logical_or(a,b).sum(); assert 0<score<1; print({"jaccard":score})
