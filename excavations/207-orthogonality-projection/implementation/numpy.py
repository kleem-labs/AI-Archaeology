"""Excavation 207: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

v=np.array([3.,2.]); u=np.array([1.,0.]); shadow=(v@u)/(u@u)*u; assert np.allclose(shadow,[3,0]); print(shadow)
