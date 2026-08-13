"""Excavation 160: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def online_softmax(scores, block=2):
    maximum=float("-inf"); denominator=0.0; weighted=0.0
    for start in range(0,len(scores),block):
        tile=scores[start:start+block]; new_max=max(maximum,max(tile))
        scale=0.0 if maximum==float("-inf") else math.exp(maximum-new_max)
        denominator*=scale; weighted*=scale
        for i,s in enumerate(tile,start):
            w=math.exp(s-new_max); denominator+=w; weighted+=w*i
        maximum=new_max
    return weighted/denominator
def demo():
    answer=online_softmax([1,2,3,4]); assert 2.49<answer<2.51
    return {"weighted_index":answer}

if __name__ == "__main__":
    print(demo())
