"""Stage 1 — Context Windows — How Much Past Can the Model Carry?, with operations visible."""

def crop(tokens,maximum): return tokens[-maximum:]
def append_cache(keys,values,new_key,new_value,maximum): return (keys+[new_key])[-maximum:],(values+[new_value])[-maximum:]
