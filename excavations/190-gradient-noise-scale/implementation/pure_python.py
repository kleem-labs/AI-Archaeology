"""Excavation 190: dependency-free evidence for this chapter.
"""

def noise_scale(gradients):
    width=len(gradients[0]); mean=[sum(g[j] for g in gradients)/len(gradients) for j in range(width)]; variance=sum(sum((g[j]-mean[j])**2 for g in gradients)/len(gradients) for j in range(width)); signal=sum(x*x for x in mean)
    return variance/signal if signal else float("inf")
def demo():
    agree=noise_scale([[2,1],[2.1,.9],[1.9,1.1]]); disagree=noise_scale([[4,-2],[0,4],[2,1]]); assert disagree>agree
    return {"agreeing_scale":agree,"disagreeing_scale":disagree}

if __name__ == "__main__":
    print(demo())
