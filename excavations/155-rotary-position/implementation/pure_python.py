"""Excavation 155: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def rotate(pair, angle):
    x,y=pair; c,s=math.cos(angle),math.sin(angle)
    return [c*x-s*y,s*x+c*y]
def demo():
    a=rotate([1,0],0.5); b=rotate([1,0],1.0)
    dot=sum(x*y for x,y in zip(a,b))
    assert abs(dot-math.cos(0.5))<1e-9
    return {"relative_match":dot}

if __name__ == "__main__":
    print(demo())
