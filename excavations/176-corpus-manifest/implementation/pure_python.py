"""Excavation 176: dependency-free evidence for this chapter.
"""

import hashlib
def manifest(sources):
    rows=[]
    for name,documents in sorted(sources.items()):
        joined="\n".join(documents).encode(); rows.append({"source":name,"documents":len(documents),"sha256":hashlib.sha256(joined).hexdigest()})
    return rows
def demo():
    out=manifest({"field-v3":["tiger","river"]}); assert out[0]["documents"]==2
    return {"manifest":out}

if __name__ == "__main__":
    print(demo())
