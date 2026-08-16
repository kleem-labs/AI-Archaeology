"""Excavation 197: dependency-free evidence for this chapter.
"""

import math
def mean_nll(probabilities): return -sum(math.log(p) for p in probabilities)/len(probabilities)
def demo():
    domains={"field":[.7,.6],"web":[.8,.9]}; losses={name:mean_nll(p) for name,p in domains.items()}; assert losses["field"]>losses["web"]
    return {"per_domain_loss":losses}

if __name__ == "__main__":
    print(demo())
