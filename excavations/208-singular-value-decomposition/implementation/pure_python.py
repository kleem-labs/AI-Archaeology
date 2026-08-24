"""Excavation 208: rebuild the chapter with no numerical library."""

def rank_one(matrix,steps=20):
    v=[1.0 for _ in matrix[0]]
    for _ in range(steps):
        u=[sum(row[j]*v[j] for j in range(len(v))) for row in matrix]; un=sum(x*x for x in u)**.5; u=[x/un for x in u]
        v=[sum(matrix[i][j]*u[i] for i in range(len(matrix))) for j in range(len(v))]; vn=sum(x*x for x in v)**.5; v=[x/vn for x in v]
    sigma=sum(u[i]*matrix[i][j]*v[j] for i in range(len(u)) for j in range(len(v))); return u,sigma,v
def demo():
    u,s,v=rank_one([[3.,0.],[0.,1.]]); assert abs(s-3)<1e-6; return {"singular_value":s}

if __name__ == "__main__":
    print(demo())
