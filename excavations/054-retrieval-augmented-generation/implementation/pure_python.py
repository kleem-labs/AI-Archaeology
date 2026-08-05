def retrieve(query,documents,score): return max(documents,key=lambda d:score(query,d))
