"""Excavation 213: rebuild the chapter with no numerical library."""

def exp_taylor(change,terms=5):
    total=1.; factorial=1.; power=1.
    for n in range(1,terms): factorial*=n; power*=change; total+=power/factorial
    return total
def demo():
    estimate=exp_taylor(.1); assert abs(estimate-1.105170)<1e-5; return estimate

if __name__ == "__main__":
    print(demo())
