from math import exp
def preference_probability(reward_a,reward_b): return 1/(1+exp(-(reward_a-reward_b)))
