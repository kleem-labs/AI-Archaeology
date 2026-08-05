"""Stage 2 — A Tiny Neural Network — Assemble the Entire Learning Loop, using array operations."""
import numpy as np

def run(values):
    array=np.asarray(values,dtype=float)
    return array

def forward(x,w1,w2):
    hidden=1/(1+np.exp(-(x@w1)))
    return 1/(1+np.exp(-(hidden@w2)))
