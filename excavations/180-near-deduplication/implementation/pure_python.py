"""Excavation 180: dependency-free evidence for this chapter.
"""

def shingles(text,width=2):
    words=text.lower().split(); return {tuple(words[i:i+width]) for i in range(len(words)-width+1)}
def jaccard(a,b): return len(a&b)/len(a|b) if a|b else 1.0
def demo():
    a=shingles("tiger tracks beside the river bank"); b=shingles("tiger tracks beside a river bank"); score=jaccard(a,b); assert 0<score<1
    return {"near_duplicate_score":score}

if __name__ == "__main__":
    print(demo())
