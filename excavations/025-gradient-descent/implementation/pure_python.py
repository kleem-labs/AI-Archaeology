"""Stage 1: visible lists, loops, and scalar operations."""

def train(weight,gradient,rate,steps):
    history=[]
    for _ in range(steps):
        history.append(weight); weight-=rate*gradient(weight)
    return weight,history
