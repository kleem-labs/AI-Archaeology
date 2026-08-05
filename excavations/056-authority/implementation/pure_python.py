def authorize(action,allowed,requires_approval,approved=False):
 if action not in allowed: return False
 return approved if action in requires_approval else True
