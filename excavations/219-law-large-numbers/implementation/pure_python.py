"""Excavation 219: rebuild the chapter with no numerical library."""

def running_means(values):
    total=0.; out=[]
    for count,value in enumerate(values,1): total+=value; out.append(total/count)
    return out
def demo():
    means=running_means([1,0]*500); assert means[-1]==.5; return means[-5:]

if __name__ == "__main__":
    print(demo())
