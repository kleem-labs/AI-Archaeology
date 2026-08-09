"""Excavation 129: evaluate a batch of candidate gates."""
+import numpy as np

def accept(rows):
    rows = np.asarray(rows, dtype=bool)
    return rows.all(axis=1)

if __name__ == "__main__":
    result = accept([[1, 0, 1], [1, 1, 1]])
    assert result.tolist() == [False, True]
    print(result)
