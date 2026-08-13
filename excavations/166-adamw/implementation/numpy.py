"""Excavation 166: NumPy implementation of this chapter's repair."""
import numpy as np

theta=np.array([2.,-1.]); adam_update=np.array([.5,-.25]); out=(1-.1*.01)*theta-.1*adam_update
assert np.all(np.abs(out)<np.abs(theta))
print({"decoupled_update":out})
