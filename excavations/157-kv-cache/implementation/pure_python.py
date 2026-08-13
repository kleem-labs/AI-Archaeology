"""Excavation 157: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def append_cache(cache, new_value): return cache+[new_value]
def projection_counts(length): return {"without_cache":sum(range(1,length+1)),"with_cache":length}
def demo():
    counts=projection_counts(100); assert counts=={"without_cache":5050,"with_cache":100}
    return counts

if __name__ == "__main__":
    print(demo())
