"""Excavation 163: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def silu(x): return x/(1+math.exp(-x))
def swiglu(gate, value): return [silu(g)*v for g,v in zip(gate,value)]
def demo():
    out=swiglu([-10,2],[5,5]); assert out[0]<0 and out[1]>8
    return {"gated":out}

if __name__ == "__main__":
    print(demo())
