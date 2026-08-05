"""A tiny two-head attention demonstration."""
from math import exp, sqrt

def softmax(xs):
    m=max(xs); es=[exp(x-m) for x in xs]; return [e/sum(es) for e in es]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def head(qs,ks,vs):
    out=[]
    for q in qs:
        w=softmax([dot(q,k)/sqrt(len(k)) for k in ks])
        out.append([sum(a*v[i] for a,v in zip(w,vs)) for i in range(len(vs[0]))])
    return out
if __name__ == "__main__":
    x=[[1,0],[0,1],[1,1]]
    h1=head(x,x,x); h2=head([[b,a] for a,b in x],x,x)
    print("concatenated:", [a+b for a,b in zip(h1,h2)])
