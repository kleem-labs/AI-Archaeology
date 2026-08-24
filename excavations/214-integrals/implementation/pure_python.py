"""Excavation 214: rebuild the chapter with no numerical library."""

def integrate(rate,start,end,slices):
    width=(end-start)/slices; return sum(rate(start+i*width)*width for i in range(slices))
def demo():
    total=integrate(lambda t:2*t,0,1,10000); assert abs(total-1)<.001; return total

if __name__ == "__main__":
    print(demo())
