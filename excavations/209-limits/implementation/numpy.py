"""Excavation 209: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

n=np.arange(1,1001); values=1/n; assert values[-1]<.002; print(values[-5:])
