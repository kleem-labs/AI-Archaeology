"""Excavation 202: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

relation=np.array([['tiger','river'],['otter','river']]); assert np.any(np.all(relation==['tiger','river'],axis=1)); print(relation)
