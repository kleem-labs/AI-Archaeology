"""Preserve a representation while learning an update."""
def add(a,b):
    if len(a)!=len(b): raise ValueError("residual shapes must match")
    return [x+y for x,y in zip(a,b)]
def transform(x): return [0.1*x[0],-0.2*x[1],0.0*x[2]]
if __name__ == "__main__":
    state=[10.0,5.0,-2.0]
    for _ in range(3):
        state=add(state,transform(state)); print(state)
