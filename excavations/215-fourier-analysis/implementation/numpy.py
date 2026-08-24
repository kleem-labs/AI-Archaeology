"""Excavation 215: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

samples=np.array([1.,0.,-1.,0.]); spectrum=np.fft.fft(samples); assert np.isclose(spectrum[1],2); print(spectrum)
