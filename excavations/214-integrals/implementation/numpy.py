"""Excavation 214: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

t=np.linspace(0,1,10001); total=np.trapezoid(2*t,t); assert np.isclose(total,1); print(total)
