"""Excavation 213: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

h=.1; powers=np.arange(5); estimate=np.sum(h**powers/np.array([math.factorial(int(n)) for n in powers])); assert np.isclose(estimate,np.exp(h),atol=1e-5); print(estimate)
