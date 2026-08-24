"""Excavation 222: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

P=np.array([[0.,.7,.3],[.4,0.,.6],[.2,.3,.5]]); state=np.array([1.,0.,0.]); tomorrow=state@P; assert np.isclose(tomorrow.sum(),1); print(tomorrow)
