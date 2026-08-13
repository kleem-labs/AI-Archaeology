"""Excavation 152: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def profile(parts):
    total = sum(parts.values())
    return total, {k: v / total for k, v in parts.items()}
def demo():
    total, shares = profile({"data":35,"compute":45,"communication":10,"idle":10})
    assert total == 100 and max(shares, key=shares.get) == "compute"
    return {"total_ms": total, "shares": shares}

if __name__ == "__main__":
    print(demo())
