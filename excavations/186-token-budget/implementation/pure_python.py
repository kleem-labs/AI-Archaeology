"""Excavation 186: dependency-free evidence for this chapter.
"""

def token_budget(steps,sequences,width): return steps*sequences*width
def demo():
    total=token_budget(2000,32,128); assert total==8_192_000
    return {"tokens":total}

if __name__ == "__main__":
    print(demo())
