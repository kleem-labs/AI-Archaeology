"""Excavation 203: rebuild the chapter with no numerical library."""

def apply(mapping,item):
    if item not in mapping: raise KeyError("input outside the function's domain")
    return mapping[item]
def demo():
    weights={"tiger":220,"deer":90,"otter":12}; assert apply(weights,"tiger")==220; return weights

if __name__ == "__main__":
    print(demo())
