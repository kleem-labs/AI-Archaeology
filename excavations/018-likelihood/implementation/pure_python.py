"""Stage 1: visible lists, loops, and scalar operations."""

def likelihood(observations,p_event):
    result=1.0
    for seen in observations: result*=p_event if seen else 1-p_event
    return result
