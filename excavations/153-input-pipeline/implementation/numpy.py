"""Excavation 153: NumPy implementation of this chapter's repair."""
import numpy as np

stages=np.array([35,45],dtype=float)
assert stages.sum()==80 and stages.max()==45
print({"serial_ms":stages.sum(),"overlapped_ms":stages.max()})
