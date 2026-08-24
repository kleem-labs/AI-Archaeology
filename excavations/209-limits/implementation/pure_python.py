"""Excavation 209: rebuild the chapter with no numerical library."""

def reciprocal_sequence(count): return [1/n for n in range(1,count+1)]
def demo():
    values=reciprocal_sequence(1000); assert values[-1]<.002 and all(a>b for a,b in zip(values,values[1:])); return values[-5:]

if __name__ == "__main__":
    print(demo())
