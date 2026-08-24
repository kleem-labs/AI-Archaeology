"""Excavation 204: rebuild the chapter with no numerical library."""

def coordinates_in_diagonal_basis(vector):
    x,y=vector; return ((x+y)/2,(y-x)/2)
def rebuild(coefficients):
    first,second=coefficients; return (first-second,first+second)
def demo():
    c=coordinates_in_diagonal_basis((3,2)); assert rebuild(c)==(3,2); return c

if __name__ == "__main__":
    print(demo())
