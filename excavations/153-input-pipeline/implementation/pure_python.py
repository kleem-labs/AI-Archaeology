"""Excavation 153: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def serial(data_ms, compute_ms): return data_ms + compute_ms
def overlapped(data_ms, compute_ms): return max(data_ms, compute_ms)
def demo():
    assert serial(35,45) == 80 and overlapped(35,45) == 45
    return {"serial_ms":80,"overlapped_ms":45}

if __name__ == "__main__":
    print(demo())
