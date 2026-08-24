"""Excavation 207: rebuild the chapter with no numerical library."""

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def project(vector,direction):
    scale=dot(vector,direction)/dot(direction,direction); return [scale*x for x in direction]
def demo():
    shadow=project((3,2),(1,0)); assert shadow==[3,0]; return shadow

if __name__ == "__main__":
    print(demo())
