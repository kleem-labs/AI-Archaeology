"""Excavation 189: NumPy form of the chapter experiment.
"""
import numpy as np

steps=np.array([0,50,100]); rates=.0001+(.001-.0001)/2*(1+np.cos(np.pi*steps/100)); assert np.isclose(rates[1],.00055); print({"rates":rates})
