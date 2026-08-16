"""Excavation 195: dependency-free evidence for this chapter.
"""

def next_step(state):
    value=(state["rng"]*1103515245+12345)%2**31; state=dict(state,rng=value,step=state["step"]+1,cursor=state["cursor"]+1); return state,value%100
def demo():
    saved={"weights":[1.0],"moments":[.2],"step":200,"cursor":800,"rng":7}; a,out1=next_step(saved); b,out2=next_step(saved); assert a==b and out1==out2
    return {"next_state":a,"next_draw":out1}

if __name__ == "__main__":
    print(demo())
