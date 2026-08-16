"""Excavation 191: dependency-free evidence for this chapter.
"""

def average_worker_gradients(workers): return [sum(values)/len(workers) for values in zip(*workers)]
def demo():
    g=average_worker_gradients([[2,4],[4,2],[3,3],[3,3]]); assert g==[3,3]
    return {"shared_gradient":g,"workers":4}

if __name__ == "__main__":
    print(demo())
