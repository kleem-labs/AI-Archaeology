"""Vectorized row lookup and sparse row updates."""
import numpy as np

def create_table(vocabulary_size,width,seed=0):
 return np.random.default_rng(seed).normal(0,.02,(vocabulary_size,width))

def lookup(table,token_ids):
 return table[np.asarray(token_ids,dtype=np.int64)]

def update_rows(table,token_ids,gradients,learning_rate):
 np.add.at(table,np.asarray(token_ids),-learning_rate*np.asarray(gradients))
