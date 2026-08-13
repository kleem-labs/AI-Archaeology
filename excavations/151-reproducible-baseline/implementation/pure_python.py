"""Excavation 151: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def compare(baseline, candidate): return candidate - baseline
def demo():
    assert compare(2.4, 2.1) == -0.2999999999999998
    return {"baseline": 2.4, "candidate": 2.1, "change": compare(2.4, 2.1)}

if __name__ == "__main__":
    print(demo())
