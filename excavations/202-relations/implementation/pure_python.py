"""Excavation 202: rebuild the chapter with no numerical library."""

def related(relation,left,right): return (left,right) in relation
def demo():
    near={("tiger","river"),("otter","river")}; assert related(near,"tiger","river") and not related(near,"river","tiger"); return near

if __name__ == "__main__":
    print(demo())
