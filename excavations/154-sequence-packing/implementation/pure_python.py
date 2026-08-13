"""Excavation 154: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def efficiency(lengths, rows, width): return sum(lengths)/(rows*width)
def first_fit(lengths, width):
    bins=[]
    for length in sorted(lengths, reverse=True):
        for i, used in enumerate(bins):
            if used+length <= width: bins[i]+=length; break
        else: bins.append(length)
    return bins
def demo():
    bins=first_fit([6,5,3,2],8)
    assert bins == [8,8]
    return {"bins":bins,"efficiency":efficiency([6,5,3,2],len(bins),8)}

if __name__ == "__main__":
    print(demo())
