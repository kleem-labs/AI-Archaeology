def ucb(mean,visits,total,c=1.4):
 from math import log,sqrt
 return mean+c*sqrt(log(total)/visits)
