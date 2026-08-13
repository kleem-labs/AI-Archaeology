"""Excavation 175: executable evidence for the chapter.

Pure Python keeps every operation visible before vectorization.
"""

def modern_config():
    return ["packing","rope","gqa","tiled_attention","pre_rmsnorm","swiglu","tied_embeddings","adamw","clipping","mixed_precision","accumulation","checkpointing","kv_cache","speculative_verification"]
def demo():
    config=modern_config(); assert config[0]=="packing" and config[-1]=="speculative_verification"
    return {"earned_components":config,"count":len(config)}

if __name__ == "__main__":
    print(demo())
