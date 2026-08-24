"""Excavation 203: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

weights=np.array([220.,90.,12.]); indices={'tiger':0,'deer':1,'otter':2}; assert weights[indices['tiger']]==220; print(weights)
