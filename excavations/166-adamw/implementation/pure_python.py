"""Excavation 166: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

import math
def adamw_step(theta,adam_update,lr=.1,decay=.01): return (1-lr*decay)*theta-lr*adam_update
def demo():
    out=adamw_step(2,.5); assert abs(out-1.948)<1e-12
    return {"old":2,"new":out}

if __name__ == "__main__":
    print(demo())
