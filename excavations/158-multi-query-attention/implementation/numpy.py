"""Excavation 158: NumPy implementation of this chapter's repair."""
import numpy as np

tokens,head_width=100,64
kv=np.array([8,1])*tokens*head_width*2
assert kv[0]==8*kv[1]
print({"mha_values":kv[0],"mqa_values":kv[1]})
