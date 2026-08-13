"""Excavation 160: NumPy implementation of this chapter's repair."""
import numpy as np

scores=np.array([1.,2.,3.,4.]); ordinary=np.exp(scores-scores.max()); ordinary/=ordinary.sum()
blocks=[]
for tile in np.array_split(scores,2): blocks.append(tile)
seen=np.concatenate(blocks); online=np.exp(seen-seen.max()); online/=online.sum()
assert np.allclose(ordinary,online)
print({"probabilities":online})
