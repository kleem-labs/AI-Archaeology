"""Excavation 221: array form of the same named experiment."""
import math
from pathlib import Path
import sys

_here = Path(__file__).resolve().parent
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]
import numpy as np

d=np.tile([-1.6,2.4],50); mean=d.mean(); se=d.std(ddof=1)/np.sqrt(len(d)); interval=mean+np.array([-1,1])*1.96*se; assert interval[0]<mean<interval[1]; print({'mean':mean,'se':se,'z':mean/se,'interval':interval})
