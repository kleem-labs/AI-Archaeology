# Implementations — From Visible Operations to Frameworks

Read the excavation before its implementation. The three stages answer different questions:

1. [`from_scratch.py`](from_scratch.py) uses lists and loops so no mathematical operation disappears.
2. [`numpy_stage.py`](numpy_stage.py) reveals the same ideas as vectorized array operations.
3. [`torch_stage.py`](torch_stage.py) assembles a small, recognizable Transformer block with trainable parameters.

Run the transparent demonstrations:

```bash
python3 implementations/from_scratch.py
```

Run all dependency-free checks:

```bash
python3 -m unittest discover -s tests -v
```

NumPy and PyTorch are optional. They are later views of ideas already exposed by the plain-Python stage.
