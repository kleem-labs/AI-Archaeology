"""Excavation 193: dependency-free evidence for this chapter.
"""

def worker_count(tensor,pipeline,data): return tensor*pipeline*data
def coordinates(tensor,pipeline,data): return [(t,p,d) for d in range(data) for p in range(pipeline) for t in range(tensor)]
def demo():
    ranks=coordinates(2,4,3); assert len(ranks)==worker_count(2,4,3)==24 and len(set(ranks))==24
    return {"workers":len(ranks),"first":ranks[0],"last":ranks[-1]}

if __name__ == "__main__":
    print(demo())
