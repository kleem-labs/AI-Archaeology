"""Excavation 194: dependency-free evidence for this chapter.
"""

import hashlib
def complete(expected,shards):
    present={name for name,data in shards.items() if hashlib.sha256(data).hexdigest()==expected.get(name)}
    return present==set(expected)
def demo():
    data={"rank0":b"weights-a","rank1":b"weights-b"}; expected={k:hashlib.sha256(v).hexdigest() for k,v in data.items()}; assert complete(expected,data) and not complete(expected,{"rank0":data["rank0"]})
    return {"complete":True,"required_shards":sorted(expected)}

if __name__ == "__main__":
    print(demo())
