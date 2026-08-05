"""Stage 1 — representation learning and emergence, with lists and loops visible."""

def discover(examples,rule,item): return examples.get(item,rule(item))
