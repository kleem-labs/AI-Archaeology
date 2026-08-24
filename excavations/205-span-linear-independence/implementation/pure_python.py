"""Excavation 205: rebuild the chapter with no numerical library."""

def combine(weights,vectors): return [sum(w*v[j] for w,v in zip(weights,vectors)) for j in range(len(vectors[0]))]
def demo():
    directions=[(1,0),(0,1),(1,1)]; witness=(-1,-1,1); assert combine(witness,directions)==[0,0]; return {"independent":False,"witness":witness}

if __name__ == "__main__":
    print(demo())
