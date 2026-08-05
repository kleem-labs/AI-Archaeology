def assign(tasks,owners):
 if len(set(owners))!=len(owners): raise ValueError("ownership must be unique")
 return dict(zip(owners,tasks))
