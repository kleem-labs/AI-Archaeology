"""Excavation 156: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def biased(score, query_pos, key_pos, slope): return score-slope*abs(query_pos-key_pos)
def demo():
    assert biased(3,20,18,.1)==2.8 and biased(3,20,0,.1)==1
    return {"near":2.8,"far":1.0}

if __name__ == "__main__":
    print(demo())
