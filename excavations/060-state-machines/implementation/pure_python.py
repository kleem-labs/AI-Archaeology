def transition(state,event,allowed):
 key=(state,event)
 if key not in allowed: raise ValueError(key)
 return allowed[key]
