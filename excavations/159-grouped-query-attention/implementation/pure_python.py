"""Excavation 159: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def group(head, query_heads, kv_heads): return (head*kv_heads)//query_heads
def demo():
    groups=[group(h,8,2) for h in range(8)]
    assert groups==[0,0,0,0,1,1,1,1]
    return {"groups":groups}

if __name__ == "__main__":
    print(demo())
