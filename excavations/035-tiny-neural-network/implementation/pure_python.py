"""Stage 1 — A Tiny Neural Network — Assemble the Entire Learning Loop, with operations visible."""

from math import exp
def sigmoid(x): return 1/(1+exp(-x))
def train_one(x,target,w1,w2,rate=.1):
 hidden=sigmoid(w1*x); prediction=sigmoid(w2*hidden); d=(prediction-target)*prediction*(1-prediction); w2-=rate*d*hidden; w1-=rate*d*w2*hidden*(1-hidden)*x; return w1,w2,prediction
