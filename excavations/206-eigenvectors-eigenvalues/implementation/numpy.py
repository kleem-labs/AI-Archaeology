"""Excavation 206: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

A=np.diag([2.,1.]); values,vectors=np.linalg.eig(A); assert np.allclose(A@vectors,vectors@np.diag(values)); print(values)
