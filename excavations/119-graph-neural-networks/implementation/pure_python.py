def aggregate(node,neighbors,message,update): return update(node,sum((message(node,n) for n in neighbors),0))
