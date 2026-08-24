"""Excavation 201: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

a=np.array(['tiger','deer','otter']); b=np.array(['tiger','otter','frog']); out=np.intersect1d(a,b); assert set(out)=={'tiger','otter'}; print(out)
