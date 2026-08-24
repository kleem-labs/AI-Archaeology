"""Excavation 212: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

H=np.array([[2.,1.],[1.,6.]]); values=np.linalg.eigvalsh(H); assert np.all(values>0); print(values)
