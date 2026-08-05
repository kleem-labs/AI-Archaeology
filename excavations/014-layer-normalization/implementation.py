"""Layer normalization for one token vector."""
from math import sqrt
def layer_norm(x,gamma=None,beta=None,epsilon=1e-5):
    mean=sum(x)/len(x); var=sum((v-mean)**2 for v in x)/len(x)
    gamma=gamma or [1.0]*len(x); beta=beta or [0.0]*len(x)
    return [g*(v-mean)/sqrt(var+epsilon)+b for v,g,b in zip(x,gamma,beta)]
if __name__ == "__main__":
    for x in ([1,2,3],[10,20,30],[5,5,5]): print(x,"->",[round(v,3) for v in layer_norm(x)])
