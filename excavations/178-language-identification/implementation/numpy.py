"""Excavation 178: NumPy form of the chapter experiment.
"""
import numpy as np

scores=np.array([.93,.05,.02]); labels=np.array(["en","es","unknown"]); winner=labels[scores.argmax()] if scores.max()>=.8 else "unknown"; assert winner=="en"; print({"winner":winner,"confidence":scores.max()})
