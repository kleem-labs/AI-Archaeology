"""Excavation 210: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

point=np.array([218.,94.]); gradient=2*(point-np.array([220.,90.])); assert np.allclose(gradient,[-4,8]); print(gradient)
