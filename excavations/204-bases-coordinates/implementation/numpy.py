"""Excavation 204: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

basis=np.array([[1.,-1.],[1.,1.]]); v=np.array([3.,2.]); c=np.linalg.solve(basis,v); assert np.allclose(basis@c,v); print(c)
