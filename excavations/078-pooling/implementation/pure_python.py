def max_pool(values,width): return [max(values[i:i+width]) for i in range(0,len(values),width)]
