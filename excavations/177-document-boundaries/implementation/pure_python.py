"""Excavation 177: dependency-free evidence for this chapter.
"""

def boundary_mask(document_ids): return [[int(a==b) for b in document_ids] for a in document_ids]
def demo():
    mask=boundary_mask(["report-a","report-a","license-b"]); assert mask[0]==[1,1,0]
    return {"mask":mask}

if __name__ == "__main__":
    print(demo())
