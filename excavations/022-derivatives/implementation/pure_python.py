"""Stage 1: visible lists, loops, and scalar operations."""

def derivative(function,x,epsilon=1e-5): return (function(x+epsilon)-function(x-epsilon))/(2*epsilon)
