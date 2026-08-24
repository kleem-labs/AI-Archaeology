"""Excavation 217: rebuild the chapter with no numerical library."""

def bayes(prior,likelihood):
    evidence=sum(prior[h]*likelihood[h] for h in prior); return {h:prior[h]*likelihood[h]/evidence for h in prior}
def demo():
    posterior=bayes({"tiger":.1,"deer":.9},{"tiger":.8,"deer":.1}); assert abs(posterior["tiger"]-8/17)<1e-12; return posterior

if __name__ == "__main__":
    print(demo())
