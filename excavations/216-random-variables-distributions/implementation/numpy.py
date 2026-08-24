"""Excavation 216: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

values=np.array([0,0,1,2]); probability=np.array([.25]*4); masses=np.bincount(values,weights=probability); assert np.allclose(masses,[.5,.25,.25]); print(masses)
