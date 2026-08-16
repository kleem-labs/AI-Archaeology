"""Excavation 182: NumPy form of the chapter experiment.
"""
import numpy as np

edges=np.array([["raw","normalized"],["normalized","redacted"],["redacted","shard-01"]]); assert edges[-1,1]=="shard-01"; print({"lineage_edges":edges})
