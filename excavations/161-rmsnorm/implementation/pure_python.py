"""Excavation 161: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def rmsnorm(values, eps=1e-8):
    rms=math.sqrt(sum(x*x for x in values)/len(values)+eps)
    return [x/rms for x in values]
def demo():
    a=rmsnorm([3,4]); b=rmsnorm([30,40])
    assert max(abs(x-y) for x,y in zip(a,b))<1e-8
    return {"small":a,"scaled":b}

if __name__ == "__main__":
    print(demo())
