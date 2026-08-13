"""Excavation 172: NumPy implementation of this chapter's repair."""
import numpy as np

state=np.arange(12); shards=np.array_split(state,4)
assert all(len(s)==3 for s in shards)
print({"shards":shards})
