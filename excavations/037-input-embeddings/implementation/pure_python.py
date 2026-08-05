"""A visible embedding table built from lists."""
import random

def create_table(vocabulary_size,width,seed=0):
 random.seed(seed)
 return [[random.uniform(-.1,.1) for _ in range(width)] for _ in range(vocabulary_size)]

def lookup(table,token_ids):
 return [table[token_id][:] for token_id in token_ids]

def update_row(table,token_id,gradient,learning_rate):
 if len(table[token_id])!=len(gradient): raise ValueError("gradient width must match embedding width")
 table[token_id]=[value-learning_rate*change for value,change in zip(table[token_id],gradient)]

if __name__=="__main__":
 table=create_table(5,3)
 print(lookup(table,[2,4,2]))
 update_row(table,2,[.1,-.2,.3],.05)
 print(lookup(table,[2]))
