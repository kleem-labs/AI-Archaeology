"""Excavation 211: rebuild the chapter with no numerical library."""

def machine(height,weight): return (height+weight, height*weight)
def jacobian(height,weight): return [[1,1],[weight,height]]
def demo():
    J=jacobian(2,3); assert J==[[1,1],[3,2]]; return J

if __name__ == "__main__":
    print(demo())
