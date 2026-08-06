# The Field-Lab Protocol

A laboratory is not a second explanation. It is where your explanation risks being wrong.

Use every lab in this order:

1. **Predict** — write what you think will happen before running anything.
2. **Run** — observe the actual intermediate values, not only the final answer.
3. **Explain** — say which concrete job each operation performed.
4. **Break** — change one assumption until the method fails.
5. **Repair** — invent the smallest change that fixes that failure.

The assertion checks are experimental boundaries. If one fails, do not merely
edit it away. Ask which belief the experiment disproved.

| Field lab | Excavation | What you can break |
|---|---|---|
| [Tiger distance](01_distance_lab.py) | [003 Distance](../excavations/003-distance/README.md) | cancellation, feature scale |
| [Softmax temperature](02_softmax_lab.py) | [009 Softmax](../excavations/009-softmax/README.md) | indecision, overconfidence |
| [Query, key, value](03_attention_lab.py) | [010 QKV](../excavations/010-query-key-value/README.md) | matching versus contributed content |
| [Gradient step size](04_gradient_lab.py) | [025 Gradient Descent](../excavations/025-gradient-descent/README.md) | steps too timid or too large |
| [Generation loop](05_generation_lab.py) | [045 Tiny GPT](../excavations/045-tiny-gpt/README.md) | score, choice, and context feedback |

Run all experiments and their checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

These five are the first polished laboratory trail. They establish the design
standard that each remaining excavation must eventually meet; they do not
pretend that 126 chapters have already received equally deep experiments.
