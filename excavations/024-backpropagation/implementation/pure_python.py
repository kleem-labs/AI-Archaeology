"""Stage 1: visible lists, loops, and scalar operations."""

def multiply(a,b): return a*b
def add(a,b): return a+b
def backward_multiply(a,b,upstream): return upstream*b,upstream*a
