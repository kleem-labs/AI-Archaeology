"""Excavation 215: rebuild the chapter with no numerical library."""

import cmath
def dft(samples):
    N=len(samples); return [sum(x*cmath.exp(-2j*cmath.pi*k*n/N) for n,x in enumerate(samples)) for k in range(N)]
def demo():
    spectrum=dft([1,0,-1,0]); assert abs(spectrum[1]-2)<1e-9; return spectrum

if __name__ == "__main__":
    print(demo())
