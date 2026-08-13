"""Excavation 172: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def shard(items,workers): return [items[i::workers] for i in range(workers)]
def demo():
    parts=shard(list(range(12)),4); assert all(len(p)==3 for p in parts)
    return {"shards":parts}

if __name__ == "__main__":
    print(demo())
