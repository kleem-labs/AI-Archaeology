"""Excavation 221: rebuild the chapter with no numerical library."""

def paired_test(differences):
    n=len(differences); mean=sum(differences)/n; variance=sum((d-mean)**2 for d in differences)/(n-1); se=(variance/n)**.5; return mean,se,mean/se,(mean-1.96*se,mean+1.96*se)
def demo():
    differences=[-1.6,2.4]*50; mean,se,z,interval=paired_test(differences); assert abs(mean-.4)<1e-12 and interval[0]<mean<interval[1]; return mean,se,z,interval

if __name__ == "__main__":
    print(demo())
