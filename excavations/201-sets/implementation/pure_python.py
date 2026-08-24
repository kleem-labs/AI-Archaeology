"""Excavation 201: rebuild the chapter with no numerical library."""

def overlap(observed, near_water):
    return {animal for animal in observed if animal in near_water}
def demo():
    shared=overlap({"tiger","deer","otter"},{"tiger","otter","frog"}); assert shared=={"tiger","otter"}; return shared

if __name__ == "__main__":
    print(demo())
