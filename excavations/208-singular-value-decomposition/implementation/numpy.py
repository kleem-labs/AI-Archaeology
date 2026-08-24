"""Excavation 208: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

A=np.diag([3.,1.]); u,s,vt=np.linalg.svd(A); recovered=(u*s)@vt; assert np.allclose(recovered,A); print(s)
