"""Excavation 174: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def acceptance(target,draft): return min(1.0,target/draft)
def demo():
    assert acceptance(.4,.8)==.5 and acceptance(.8,.4)==1
    return {"overproduced":.5,"underproduced":1.0}

if __name__ == "__main__":
    print(demo())
