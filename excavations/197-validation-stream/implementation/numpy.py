"""Excavation 197: NumPy form of the chapter experiment.
"""
import numpy as np

p=np.array([[.7,.6],[.8,.9]]); losses=-np.log(p).mean(1); assert losses[0]>losses[1]; print({"field_loss":losses[0],"web_loss":losses[1]})
