"""Excavation 179: dependency-free evidence for this chapter.
"""

import hashlib
def normalize(text): return " ".join(text.split()).lower()
def fingerprint(text): return hashlib.sha256(normalize(text).encode()).hexdigest()
def demo():
    a=fingerprint("Tiger  near river\n"); b=fingerprint(" tiger near   river "); assert a==b
    return {"same_fingerprint":a==b,"fingerprint":a}

if __name__ == "__main__":
    print(demo())
