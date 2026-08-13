"""Excavation 173: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def matmul(x,w): return [sum(a*b for a,b in zip(x,col)) for col in zip(*w)]
def split_columns(w,parts):
    width=len(w[0]); step=width//parts
    return [[row[i:i+step] for row in w] for i in range(0,width,step)]
def demo():
    x=[2,3]; w=[[1,0,2,0],[0,1,0,2]]
    joined=sum((matmul(x,p) for p in split_columns(w,2)),[])
    assert joined==matmul(x,w)
    return {"joined":joined}

if __name__ == "__main__":
    print(demo())
