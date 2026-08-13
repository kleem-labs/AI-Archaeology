"""Excavation 162: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def pre_norm_block(x, branch): return [a+b for a,b in zip(x,branch)]
def demo():
    x=[2.0,-1.0]; y=pre_norm_block(x,[0.0,0.0]); assert y==x
    return {"input":x,"zero_branch_output":y}

if __name__ == "__main__":
    print(demo())
