"""Excavation 220: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

values=np.full(100,10.2); z=(values.mean()-10)/(2/np.sqrt(len(values))); assert np.isclose(z,1); print(z)
