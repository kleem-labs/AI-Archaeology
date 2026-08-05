"""Stage 1 — attention, with lists and loops visible."""

def discover(need,labels,values,score):
 scores=[score(need,x) for x in labels]; return values[max(range(len(scores)),key=scores.__getitem__)]
