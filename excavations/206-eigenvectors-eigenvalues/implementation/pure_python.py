"""Excavation 206: rebuild the chapter with no numerical library."""

def transform(matrix,vector): return [sum(a*b for a,b in zip(row,vector)) for row in matrix]
def demo():
    matrix=((2,0),(0,1)); east=(1,0); image=transform(matrix,east); assert image==[2,0]; return {"direction":east,"scale":2}

if __name__ == "__main__":
    print(demo())
