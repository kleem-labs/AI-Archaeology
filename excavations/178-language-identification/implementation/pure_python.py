"""Excavation 178: dependency-free evidence for this chapter.
"""

def identify(scores,threshold=.8):
    label=max(scores,key=scores.get); return label if scores[label]>=threshold else "unknown"
def demo():
    assert identify({"en":.93,"es":.05})=="en" and identify({"en":.44,"es":.41})=="unknown"
    return {"confident":"en","uncertain":"unknown"}

if __name__ == "__main__":
    print(demo())
