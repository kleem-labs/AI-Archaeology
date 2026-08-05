def q_target(reward,next_values,discount): return reward+discount*max(next_values)
