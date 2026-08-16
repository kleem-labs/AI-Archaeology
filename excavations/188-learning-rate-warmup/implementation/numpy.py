"""Excavation 188: NumPy form of the chapter experiment.
"""
import numpy as np

steps=np.array([0,25,50,100]); rates=.001*np.minimum(1,steps/100); assert np.allclose(rates,[0,.00025,.0005,.001]); print({"rates":rates})
