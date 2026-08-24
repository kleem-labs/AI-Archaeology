"""Excavation 219: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

values=np.tile([1.,0.],500); means=np.cumsum(values)/np.arange(1,len(values)+1); assert means[-1]==.5; print(means[-5:])
