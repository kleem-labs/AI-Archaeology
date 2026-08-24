"""Excavation 220: rebuild the chapter with no numerical library."""

def standardized_mean(values,mean,deviation):
    sample=sum(values)/len(values); return (sample-mean)/(deviation/(len(values)**.5))
def demo():
    z=standardized_mean([10.2]*100,10,2); assert abs(z-1)<1e-12; return z

if __name__ == "__main__":
    print(demo())
