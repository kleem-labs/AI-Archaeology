"""Excavation 165: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def adam_step(theta,g,m,v,t,lr=.1,b1=.9,b2=.999,eps=1e-8):
    m=b1*m+(1-b1)*g; v=b2*v+(1-b2)*g*g
    mh=m/(1-b1**t); vh=v/(1-b2**t)
    return theta-lr*mh/(math.sqrt(vh)+eps),m,v
def demo():
    theta,m,v=adam_step(1,2,0,0,1); assert theta<1
    return {"theta":theta,"m":m,"v":v}

if __name__ == "__main__":
    print(demo())
