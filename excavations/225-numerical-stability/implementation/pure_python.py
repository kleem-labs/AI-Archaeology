"""Excavation 225: rebuild the chapter with no numerical library."""

import math
def logsumexp(scores):
    maximum=max(scores); return maximum+math.log(sum(math.exp(x-maximum) for x in scores))
def demo():
    value=logsumexp([1000,999,998]); assert math.isfinite(value) and 1000<value<1001; return value

if __name__ == "__main__":
    print(demo())
