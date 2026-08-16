"""Excavation 188: dependency-free evidence for this chapter.
"""

def warmup(step,warm_steps,peak): return peak*min(1,step/warm_steps)
def demo():
    rates=[warmup(t,100,.001) for t in (0,25,50,100)]; assert rates==[0,.00025,.0005,.001]
    return {"rates":rates}

if __name__ == "__main__":
    print(demo())
