# AI Archaeology

**Rediscover the ideas behind modern AI from the problems that forced them to exist.**

This book does not begin with formulas. It begins with a person facing reality without inherited mathematics.

Every excavation follows the same discipline:

```text
reality → question → naive attempt → failure → discovery → equation
```

The reader should want the mathematics before seeing it. Symbols are compressed records of reasoning, not substitutes for reasoning.

## Excavations

| # | Excavation | The question that opens it |
|---:|---|---|
| 000 | [Before Mathematics Existed](excavations/000-before-mathematics-existed/README.md) | Why can experience teach us anything? |
| 001 | [Why Features Exist](excavations/001-why-features-exist/README.md) | Which details should survive compression? |
| 002 | [Vectors](excavations/002-vectors/README.md) | How can related measurements travel as one object? |
| 003 | [Distance](excavations/003-distance/README.md) | How can many differences become one comparison? |
| 004 | [Vectors as Change](excavations/004-vectors-as-change/README.md) | How do we describe direction as well as amount? |
| 005 | [Matrices](excavations/005-matrices/README.md) | How can one machine transform any input vector? |
| 006 | [Meaning](excavations/006-meaning/README.md) | How can symbols constrain one another without a dictionary? |
| 007 | [Embeddings](excavations/007-embeddings/README.md) | How can those constraints become geometry? |
| 008 | [Attention](excavations/008-attention/README.md) | How can a token retrieve what matters now? |
| 009 | [Softmax](excavations/009-softmax/README.md) | How do unstable scores become usable weights? |
| 010 | [Query, Key, and Value](excavations/010-query-key-value/README.md) | Who is relevant, and what should they contribute? |
| 011 | [Multi-Head Attention](excavations/011-multi-head-attention/README.md) | How can several relationships be followed at once? |
| 012 | [Feed-Forward Networks](excavations/012-feed-forward-networks/README.md) | After communication, how does each token process what it heard? |
| 013 | [Residual Connections](excavations/013-residual-connections/README.md) | How can depth improve a message without repeatedly erasing it? |
| 014 | [Layer Normalization](excavations/014-layer-normalization/README.md) | How can representations work at a stable numerical volume? |
| 015 | [Learning](excavations/015-learning/README.md) | How does a random machine turn mistakes into improvement? |
| 016 | [Emergence](excavations/016-emergence/README.md) | What hidden world must be inferred to predict its linguistic traces? |
| 017 | [Probability — Counting What We Do Not Know](excavations/017-probability/README.md) | How can we act without pretending to be certain? |
| 018 | [Likelihood — Which Hidden Story Produced This Evidence?](excavations/018-likelihood/README.md) | Which hidden story best explains the evidence? |
| 019 | [Information — Why Surprise Needs a Number](excavations/019-information/README.md) | Why does a rare message teach us more? |
| 020 | [Entropy — Measuring the Uncertainty of a Whole Situation](excavations/020-entropy/README.md) | How uncertain is an entire situation? |
| 021 | [Cross-Entropy — Paying for Confidently Wrong Predictions](excavations/021-cross-entropy/README.md) | How should confident mistakes be penalized? |
| 022 | [Derivatives — Asking One Weight What It Changed](excavations/022-derivatives/README.md) | Which way should one weight move? |
| 023 | [The Chain Rule — Following One Change Through Many Machines](excavations/023-chain-rule/README.md) | How does one change travel through many machines? |
| 024 | [Backpropagation — Reusing Blame Instead of Recomputing It](excavations/024-backpropagation/README.md) | How can shared blame be calculated once and reused? |
| 025 | [Gradient Descent — Teaching a Tiny Network](excavations/025-gradient-descent/README.md) | How do local sensitivities become repeated learning? |
| 026 | [Mini-Batches — Learning from More Than One Example](excavations/026-mini-batches/README.md) | How can we learn without trusting one noisy example? |
| 027 | [Learning Rate — How Large Should the Next Step Be?](excavations/027-learning-rate/README.md) | How far should we move downhill? |
| 028 | [Momentum — Remembering Which Way Downhill Persists](excavations/028-momentum/README.md) | How can persistent direction survive noisy gradients? |
| 029 | [Initialization — Where Should Learning Begin?](excavations/029-initialization/README.md) | Where should learning begin? |
| 030 | [Activation Functions — Why a Network Must Bend](excavations/030-activation-functions/README.md) | Why must a deep network bend? |
| 031 | [Overfitting — When Perfect Memory Pretends to Be Intelligence](excavations/031-overfitting/README.md) | When does perfect memory stop being intelligence? |
| 032 | [Regularization — Making Memorization More Expensive](excavations/032-regularization/README.md) | How can brittle memorization become expensive? |
| 033 | [Validation — Testing Without Peeking at the Final Exam](excavations/033-validation/README.md) | How can we test without leaking the answers? |
| 034 | [Generalization — What Should Survive Beyond the Dataset?](excavations/034-generalization/README.md) | What should survive beyond the dataset? |
| 035 | [A Tiny Neural Network — Assemble the Entire Learning Loop](excavations/035-tiny-neural-network/README.md) | How do all the learning pieces become one working machine? |
| 036 | [Tokenization](excavations/036-tokenization/README.md) | What pieces can a language model actually see? |

| 037 | [Input Embeddings](excavations/037-input-embeddings/README.md) | How can arbitrary token IDs become learnable coordinates? |

## A note on style

The questions and discoveries that shaped the original conversation are part of the argument, not side anecdotes: “How many tigers?”, “Where are they?”, comparing like attributes, squaring and rooting differences, distinguishing relevance from similarity, multiplying aligned features, and letting each expert contribute knowledge from its domain.

Each excavation is one coherent Markdown chapter. Diagrams and challenges appear only when they advance the reasoning.

## Build what you discover

The narrative is the spine, but this is not a notes-only project. Every excavation directory keeps its chapter, diagram, exercises, and relevant implementation together. Start with the chapter; open its companions only after the problem has made them meaningful.

## Project standard

The repository is periodically checked against the original teaching agreement in [AUDIT.md](AUDIT.md). Contributions must preserve the observation → failure → discovery sequence; see [CONTRIBUTING.md](CONTRIBUTING.md).
