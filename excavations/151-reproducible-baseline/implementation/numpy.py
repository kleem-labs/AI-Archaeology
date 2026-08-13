"""Excavation 151: NumPy implementation of this chapter's repair."""
import numpy as np

baseline=np.array([2.4, 2.3, 2.35]); candidate=np.array([2.1, 2.2, 2.15])
change=candidate-baseline
assert np.all(change < 0)
print({"mean_change":float(change.mean())})
