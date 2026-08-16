"""Excavation 199: dependency-free evidence for this chapter.
"""

def build_report(manifest,run,evaluations,incidents):
    required=("corpus_hash","tokens","compute","artifact_hash"); assert all(key in {**manifest,**run} for key in required)
    return {"manifest":manifest,"run":run,"evaluations":evaluations,"incidents":incidents,"limitations":["finite audits","documented scope only"]}
def demo():
    report=build_report({"corpus_hash":"abc"},{"tokens":8192,"compute":49152,"artifact_hash":"xyz"},{"field_loss":2.1},["restored step 200"]); assert report["limitations"]
    return report

if __name__ == "__main__":
    print(demo())
