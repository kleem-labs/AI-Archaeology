"""Excavation 185: NumPy form of the chapter experiment.
"""
import numpy as np

rng=np.random.default_rng(7); draws=rng.choice(2,size=1000,p=[.8,.2]); counts=np.bincount(draws,minlength=2); assert counts.sum()==1000; print({"realized_counts":counts,"expected":np.array([800,200])})
