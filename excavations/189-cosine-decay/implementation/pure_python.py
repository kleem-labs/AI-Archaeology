"""Excavation 189: dependency-free evidence for this chapter.
"""

import math
def cosine_rate(step,horizon,maximum,minimum=0): return minimum+(maximum-minimum)/2*(1+math.cos(math.pi*step/horizon))
def demo():
    rates=[cosine_rate(t,100,.001,.0001) for t in (0,50,100)]; assert abs(rates[1]-.00055)<1e-12
    return {"start_middle_end":rates}

if __name__ == "__main__":
    print(demo())
