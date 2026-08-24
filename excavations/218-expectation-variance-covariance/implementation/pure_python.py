"""Excavation 218: rebuild the chapter with no numerical library."""

def summaries(xs,ys):
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys); variance=sum((x-mx)**2 for x in xs)/len(xs); covariance=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/len(xs); return mx,variance,covariance
def demo():
    out=summaries([0,2],[0,2]); assert out==(1,1,1); return out

if __name__ == "__main__":
    print(demo())
