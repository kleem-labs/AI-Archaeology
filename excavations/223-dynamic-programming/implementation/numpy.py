"""Excavation 223: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

reward=np.array([2.,1.]); future=np.array([8.,6.]); values=reward+.9*future; assert values.argmax()==0; print(values)
