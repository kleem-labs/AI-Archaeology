"""Excavation 212: rebuild the chapter with no numerical library."""

def bowl(x,y): return x*x+3*y*y+x*y
def hessian(): return [[2,1],[1,6]]
def demo():
    H=hessian(); assert H[0][1]==H[1][0] and H[1][1]>H[0][0]; return H

if __name__ == "__main__":
    print(demo())
