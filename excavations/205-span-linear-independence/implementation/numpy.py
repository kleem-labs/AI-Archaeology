"""Excavation 205: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

directions=np.array([[1.,0.,1.],[0.,1.,1.]]); assert np.linalg.matrix_rank(directions)==2; print({'rank':np.linalg.matrix_rank(directions)})
