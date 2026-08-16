"""Excavation 198: dependency-free evidence for this chapter.
"""

import math
def exposure(search_space,rank): return math.log2(search_space)-math.log2(rank)
def demo():
    once=exposure(1_000_000,100_000); repeated=exposure(1_000_000,10); assert repeated>once
    return {"single_exposure":once,"repeated_exposure":repeated}

if __name__ == "__main__":
    print(demo())
