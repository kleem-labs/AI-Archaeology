# Part XIII Plan — A Pretraining Factory We Can Account For

Excavation 175 assembles a modern tiny language-model engine and keeps a
reference path beside every optimization. The engine can run, but it still has
nothing trustworthy to learn from and no recoverable plan for a long training
run. Part XIII builds that missing factory without resetting the model.

## The single experiment

The ranger station wants to turn a changing archive of field reports, public
documents, code, and reference material into one reproducible pretraining run.
Every document must remain traceable. Every filtering decision must leave a
count. Every distributed worker must contribute to the same update. Every
checkpoint must be sufficient to continue the same experiment rather than
beginning a similar one.

| Movement | Excavations | Necessity |
|---|---:|---|
| Make the corpus inspectable | 176–180 | Record sources, preserve document boundaries, identify languages, and remove exact and disguised repetition. |
| Curate without hiding judgment | 181–185 | Measure quality, preserve provenance, reduce personal-data risk, choose domain shares, and turn those shares into a reproducible stream. |
| Budget the run | 186–190 | Translate steps into tokens and compute, warm up fragile optimizer memory, cool late updates, and find when larger batches stop buying useful evidence. |
| Make many devices behave like one experiment | 191–195 | Average independent witnesses, pipeline layers, compose parallel dimensions, save all shards, and resume the exact state. |
| Watch, audit, and report | 196–200 | Detect abnormal loss, validate on a clean stream, probe memorization, document the run, and assemble one tiny pretraining factory. |

## Narrative rule

No curation or scaling technique appears because a frontier lab uses it. Each
one begins with a visible failure in the same corpus or training run. The
reader must be able to say what information was lost, duplicated, leaked,
overrepresented, or left unrecoverable before the standard name appears.

## Mathematical rule

Before every displayed equation, the reader performs its arithmetic with named
documents, domains, workers, tokens, or checkpoints. The chapter then explains
why each operation is forced and why the nearest alternative answers a
different question, linking every move to `MATHEMATICAL_MOVES.md`.

## Primary research trail

- [CCNet](https://arxiv.org/abs/1911.00359)
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499)
- [Dolma](https://arxiv.org/abs/2402.00159)
- [DataComp-LM](https://arxiv.org/abs/2406.11794)
- [DoReMi](https://arxiv.org/abs/2305.10429)
- [Compute-optimal training / Chinchilla](https://arxiv.org/abs/2203.15556)
- [An Empirical Model of Large-Batch Training](https://arxiv.org/abs/1812.06162)
- [GPipe](https://arxiv.org/abs/1811.06965)
- [Megatron-LM at scale](https://arxiv.org/abs/2104.04473)
- [DataStates-LLM checkpointing](https://arxiv.org/abs/2406.10707)
- [Spike No More](https://arxiv.org/abs/2312.16903)
- [Extracting Training Data from Language Models](https://arxiv.org/abs/2012.07805)
- [Model Cards](https://arxiv.org/abs/1810.03993)
