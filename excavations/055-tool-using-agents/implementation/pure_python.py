def act(tool,arguments,allowed):
 if tool not in allowed: raise PermissionError(tool)
 return allowed[tool](**arguments)
