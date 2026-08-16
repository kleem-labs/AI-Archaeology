"""Excavation 190: NumPy form of the chapter experiment.
"""
import numpy as np

g=np.array([[2.,1.],[2.1,.9],[1.9,1.1]]); mean=g.mean(0); covariance=np.cov(g,rowvar=False,bias=True); scale=np.trace(covariance)/(mean@mean); assert scale<.01; print({"noise_scale":scale,"covariance":covariance})
