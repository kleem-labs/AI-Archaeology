"""Excavation 158: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def cache_values(tokens, kv_heads, head_width): return tokens*kv_heads*head_width*2
def demo():
    mha=cache_values(100,8,64); mqa=cache_values(100,1,64)
    assert mha == 8*mqa
    return {"mha_values":mha,"mqa_values":mqa}

if __name__ == "__main__":
    print(demo())
