"""Excavation 164: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def tied_logits(hidden, embeddings): return [sum(a*b for a,b in zip(hidden,row)) for row in embeddings]
def demo():
    E=[[1,0],[0,1]]; logits=tied_logits([.8,.2],E); assert logits==[.8,.2]
    return {"embedding_table":E,"logits":logits}

if __name__ == "__main__":
    print(demo())
