import numpy as np
def pad_batch(sequences,pad_id=0):
 width=max(map(len,sequences)); ids=np.full((len(sequences),width),pad_id,dtype=np.int64); mask=np.zeros_like(ids,dtype=bool)
 for row,seq in enumerate(sequences): ids[row,:len(seq)]=seq; mask[row,:len(seq)]=True
 return ids,mask
