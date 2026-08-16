"""Excavation 187: dependency-free evidence for this chapter.
"""

def training_flops(parameters,tokens,factor=6): return factor*parameters*tokens
def demo():
    small=training_flops(100_000_000,2_000_000_000); large=training_flops(200_000_000,1_000_000_000); assert small==large
    return {"equal_compute":small,"candidates":["more_tokens","more_parameters"]}

if __name__ == "__main__":
    print(demo())
