"""Excavation 211: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

J=np.array([[1.,1.],[3.,2.]]); change=np.array([.1,-.2]); print({'jacobian':J,'output_change':J@change})
