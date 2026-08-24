"""Excavation 218: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

x=np.array([0.,2.]); y=np.array([0.,2.]); assert np.isclose(x.var(),1) and np.isclose(np.cov(x,y,bias=True)[0,1],1); print({'mean':x.mean(),'variance':x.var(),'covariance':np.cov(x,y,bias=True)[0,1]})
