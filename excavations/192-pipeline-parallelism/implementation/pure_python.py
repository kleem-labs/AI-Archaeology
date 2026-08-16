"""Excavation 192: dependency-free evidence for this chapter.
"""

def utilization(microbatches,stages): return microbatches/(microbatches+stages-1)
def timeline(microbatches,stages): return [[m+s for m in range(microbatches)] for s in range(stages)]
def demo():
    assert utilization(8,4)==8/11
    return {"utilization":utilization(8,4),"clock_slots":timeline(8,4)}

if __name__ == "__main__":
    print(demo())
