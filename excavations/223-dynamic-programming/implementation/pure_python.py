"""Excavation 223: rebuild the chapter with no numerical library."""

def backup(actions,discount=.9):
    return max((reward+discount*future,name) for name,reward,future in actions)
def demo():
    value,action=backup([("cross",2,8),("wait",1,6)]); assert action=="cross" and abs(value-9.2)<1e-12; return action,value

if __name__ == "__main__":
    print(demo())
