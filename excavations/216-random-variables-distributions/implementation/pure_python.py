"""Excavation 216: rebuild the chapter with no numerical library."""

def distribution(outcomes,probabilities,measure):
    result={}
    for outcome,p in zip(outcomes,probabilities): result[measure(outcome)]=result.get(measure(outcome),0)+p
    return result
def demo():
    histories=["none-a","none-b","one","two"]; d=distribution(histories,[.25]*4,lambda h:0 if h.startswith("none") else (1 if h=="one" else 2)); assert d[0]==.5; return d

if __name__ == "__main__":
    print(demo())
