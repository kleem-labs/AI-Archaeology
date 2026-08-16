"""Excavation 182: dependency-free evidence for this chapter.
"""

def lineage(document_id,source,steps,shard): return {"id":document_id,"source":source,"steps":list(steps),"shard":shard}
def demo():
    row=lineage("river-0042","field-v3",["lang:en","dedup:cluster-7","redact:v2"],"shard-01@128"); assert row["steps"][1]=="dedup:cluster-7"
    return row

if __name__ == "__main__":
    print(demo())
