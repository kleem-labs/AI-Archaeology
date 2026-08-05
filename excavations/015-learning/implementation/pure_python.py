"""Stage 1 — gradient learning, with lists and loops visible."""

def discover(x,gradient,rate,steps):
 history=[x]
 for _ in range(steps): x-=rate*gradient(x); history.append(x)
 return history
