"""Excavation 184: dependency-free evidence for this chapter.
"""

def validate(weights,tolerance=1e-12): return all(x>=0 for x in weights.values()) and abs(sum(weights.values())-1)<tolerance
def demo():
    mix={"web":.5,"science":.2,"code":.15,"books":.1,"field":.05}; assert validate(mix)
    return {"mixture":mix,"total":sum(mix.values())}

if __name__ == "__main__":
    print(demo())
