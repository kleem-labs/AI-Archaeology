"""Stage 1: visible lists, loops, and scalar operations."""

def chain(local_derivatives):
    result=1.0
    for derivative in local_derivatives: result*=derivative
    return result
