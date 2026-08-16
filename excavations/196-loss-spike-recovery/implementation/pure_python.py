"""Excavation 196: dependency-free evidence for this chapter.
"""

def z_score(current,history):
    center=sum(history)/len(history); spread=(sum((x-center)**2 for x in history)/len(history))**.5; return (current-center)/(spread or 1)
def persistent_alarm(losses,window=4,threshold=3):
    baseline=losses[:window]
    return len(losses)>=window+2 and all(z_score(x,baseline)>threshold for x in losses[-2:])
def demo():
    transient=[2.0,2.1,1.9,2.0,2.35,2.0]; sustained=[2.0,2.1,1.9,2.0,2.6,2.7]; assert not persistent_alarm(transient) and persistent_alarm(sustained)
    return {"transient_alarm":False,"sustained_alarm":True}

if __name__ == "__main__":
    print(demo())
