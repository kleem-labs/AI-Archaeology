"""Excavation 185: dependency-free evidence for this chapter.
"""

import random
def schedule(weights,draws,seed):
    names=list(weights); rng=random.Random(seed); return rng.choices(names,weights=[weights[n] for n in names],k=draws)
def demo():
    weights={"web":.8,"field":.2}; a=schedule(weights,1000,7); b=schedule(weights,1000,7); assert a==b
    return {"field_draws":a.count("field"),"reproducible":True}

if __name__ == "__main__":
    print(demo())
