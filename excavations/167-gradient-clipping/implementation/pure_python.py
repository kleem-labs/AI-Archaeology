"""Excavation 167: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def clip(values,ceiling):
    norm=math.sqrt(sum(x*x for x in values)); scale=min(1,ceiling/(norm or 1))
    return [x*scale for x in values]
def demo():
    out=clip([12,16],5); assert out==[3.0,4.0]
    return {"clipped":out}

if __name__ == "__main__":
    print(demo())
