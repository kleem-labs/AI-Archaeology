"""Excavation 224: rebuild the chapter with no numerical library."""

def convex_check(function,x,y,weight):
    left=function(weight*x+(1-weight)*y); right=weight*function(x)+(1-weight)*function(y); return left,right,left<=right
def demo():
    out=convex_check(lambda x:x*x,-2,2,.5); assert out==(0.,4.,True); return out

if __name__ == "__main__":
    print(demo())
