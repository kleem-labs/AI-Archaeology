"""Excavation 217: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

prior=np.array([.1,.9]); likelihood=np.array([.8,.1]); posterior=prior*likelihood/(prior@likelihood); assert np.isclose(posterior[0],8/17); print(posterior)
