"""Excavation 225: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

x=np.array([1000.,999.,998.]); maximum=x.max(); value=maximum+np.log(np.exp(x-maximum).sum()); assert np.isfinite(value); print(value)
