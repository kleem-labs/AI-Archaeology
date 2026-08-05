from math import exp,log
def perplexity(probabilities): return exp(-sum(log(p) for p in probabilities)/len(probabilities))
