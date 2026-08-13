"""Excavation 168: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def memory_bytes(count,bits): return count*bits//8
def demo():
    assert memory_bytes(1_000_000,16)==2_000_000
    return {"fp32":memory_bytes(1_000_000,32),"fp16":memory_bytes(1_000_000,16)}

if __name__ == "__main__":
    print(demo())
