"""Excavation 126: tensor form of the same explicit gate."""
+try:
+    import torch
+except ImportError:
+    raise SystemExit("Install PyTorch to run this stage.")
+
def accept(rows):
+    return rows.bool().all(dim=1)
+
+if __name__ == "__main__":
+    result = accept(torch.tensor([[1, 0, 1], [1, 1, 1]]))
+    assert result.tolist() == [False, True]
+    print(result)
