"""Excavation 170: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def accumulate(gradients): return [sum(col)/len(gradients) for col in zip(*gradients)]
def demo():
    out=accumulate([[2,4],[4,2],[3,3]]); assert out==[3,3]
    return {"effective_gradient":out}

if __name__ == "__main__":
    print(demo())
