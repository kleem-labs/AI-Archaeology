"""Excavation 222: rebuild the chapter with no numerical library."""

def next_distribution(state,transitions): return transitions[state]
def demo():
    transitions={"forest":{"river":.7,"village":.3},"river":{"forest":.4,"village":.6}}; out=next_distribution("forest",transitions); assert out["river"]==.7; return out

if __name__ == "__main__":
    print(demo())
