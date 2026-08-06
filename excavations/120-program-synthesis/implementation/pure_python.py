def synthesize(candidates,examples): return [f for f in candidates if all(f(x)==y for x,y in examples)]
