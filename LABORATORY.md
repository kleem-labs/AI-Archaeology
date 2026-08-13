# AI Archaeology Laboratory

The book asks why an idea must exist. The laboratory lets you break and rebuild
it.

Run every dependency-free experiment:

~~~bash
python3 -m unittest discover -s tests -v
python3 tools/check_guided_discovery.py
python3 tools/check_chapter_continuity.py
python3 tools/check_equation_explanations.py
python3 tools/check_operation_reasoning.py
python3 tools/check_latex_portability.py
python3 tools/check_reasoned_limits.py
python3 tools/check_human_math_examples.py
python3 tools/build_mathematical_gist.py --check
python3 tools/build_continuous_book.py --check
python3 tools/check_book_lab.py
~~~

## Field labs

| Lab | Excavations | What you vary | What should become visible |
|---|---|---|---|
| [Distance](labs/01_distance_lab.py) | 001–003 | feature values and scales | cancellation and scale domination |
| [Softmax](labs/02_softmax_lab.py) | 009, 043 | scores and temperature | confidence sharpening and flattening |
| [Attention](labs/03_attention_lab.py) | 008–010 | queries, keys, values | relevance versus contributed content |
| [Gradient descent](labs/04_gradient_lab.py) | 022–028 | learning rate | slow learning, progress, and overshoot |
| [Tiny generation loop](labs/05_generation_lab.py) | 036–045 | logits, seed, context | tokenize → score → sample → append |
| [Measured engine rebuild](labs/06_engine_rebuild_lab.py) | 151–175 | overlap, KV heads, precision, draft support | faster and smaller paths that remain accountable to a frozen reference |

Each lab prints intermediate values and contains assertions for the failure it
was designed to expose. Read the linked excavation first; the lab is evidence,
not a substitute for the narrative.
