"""Excavation 171: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def checkpoint_plan(layers,segment): return list(range(0,layers,segment))
def demo():
    kept=checkpoint_plan(9,3); assert kept==[0,3,6]
    return {"layers":9,"kept":kept,"recomputed_per_segment":3}

if __name__ == "__main__":
    print(demo())
