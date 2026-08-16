"""Excavation 200: NumPy form of the chapter experiment.
"""
import numpy as np

gates=np.array([True,True,True,False,True,True]); assert not gates.all(); print({"release":gates.all(),"failed_gate":np.where(~gates)[0]})
