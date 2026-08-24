"""Excavation 210: rebuild the chapter with no numerical library."""

def loss(tiger_weight,deer_weight): return (tiger_weight-220)**2+(deer_weight-90)**2
def finite_gradient(point,step=1e-5):
    out=[]
    for i in range(2):
        left=list(point); right=list(point); left[i]-=step; right[i]+=step
        out.append((loss(*right)-loss(*left))/(2*step))
    return out
def demo():
    g=finite_gradient((218.,94.)); assert abs(g[0]+4)<1e-4 and abs(g[1]-8)<1e-4; return g

if __name__ == "__main__":
    print(demo())
