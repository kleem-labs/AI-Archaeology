"""A small byte-pair-style tokenizer using only Python."""
from collections import Counter
END="</w>"
def split_word(word): return tuple(word)+(END,)
def pair_counts(vocabulary):
 counts=Counter()
 for pieces,frequency in vocabulary.items():
  for pair in zip(pieces,pieces[1:]): counts[pair]+=frequency
 return counts
def merge_pair(pieces,pair):
 out=[]; i=0
 while i<len(pieces):
  if i+1<len(pieces) and pieces[i:i+2]==pair: out.append(pair[0]+pair[1]); i+=2
  else: out.append(pieces[i]); i+=1
 return tuple(out)
def train(words,merges):
 vocabulary=Counter(split_word(w) for w in words); rules=[]
 for _ in range(merges):
  counts=pair_counts(vocabulary)
  if not counts: break
  pair=max(counts,key=lambda p:(counts[p],p)); rules.append(pair)
  vocabulary=Counter({merge_pair(p,pair):f for p,f in vocabulary.items()})
 return rules
def encode(word,rules):
 pieces=split_word(word)
 for pair in rules: pieces=merge_pair(pieces,pair)
 return list(pieces)
def decode(pieces): return "".join(pieces).replace(END,"")
