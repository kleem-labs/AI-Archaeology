# Visual Field Guide

These diagrams do not summarize formulas. They show the pressure that creates each idea. Read the linked chapter first.

## 000–003 — Observation becomes measurable comparison

```mermaid
flowchart LR
  A["Repeated tiger encounters"] --> B["Exact memory fails: every encounter differs"]
  B --> C["Keep recurring evidence: features"]
  C --> D["Agree on an order: vector"]
  D --> E["Many signed differences"]
  E --> F["Cancellation fails"]
  F --> G["Square, add, root: distance"]
```

## 004–005 — Description becomes change

```mermaid
flowchart LR
  A["Where am I?"] --> B["State vector"]
  C["How should I move?"] --> D["Change vector"]
  B --> E["state + change"]
  D --> E
  E --> F["One fixed change is insufficient"]
  F --> G["Input-dependent machine: matrix"]
```

## 006–010 — Words become contextual retrieval

```mermaid
flowchart LR
  A["A word alone is ambiguous"] --> B["Contexts constrain meaning"]
  B --> C["Geometry of usage: embedding"]
  C --> D["One static point still fails"]
  D --> E["Retrieve what matters now: attention"]
  E --> F["Similarity is not relevance"]
  F --> G["Query meets keys"]
  G --> H["Softmax weights"]
  H --> I["Weighted values"]
```

## One token asking the sentence for help

```mermaid
flowchart TD
  Q["Query: what do I need?"] --> S1["dot Key(John)"]
  Q --> S2["dot Key(Mary)"]
  Q --> S3["dot Key(book)"]
  S1 --> W["softmax: usable weights"]
  S2 --> W
  S3 --> W
  V1["Value(John)"] --> M["weighted mixture"]
  V2["Value(Mary)"] --> M
  V3["Value(book)"] --> M
  W --> M
```

## 011–014 — One retrieval becomes a deep block

```mermaid
flowchart LR
  A["One relationship space blurs different jobs"] --> B["Parallel heads"]
  B --> C["Tokens have communicated"]
  C --> D["Private processing: FFN"]
  D --> E["Replacement risks erasure"]
  E --> F["Residual correction"]
  F --> G["Scale drifts"]
  G --> H["Layer normalization"]
```

## 015–016 — Error becomes hidden structure

```mermaid
flowchart LR
  A["Random machine predicts"] --> B["Measure the mistake"]
  B --> C["Trace sensitivity backward"]
  C --> D["Change weights"]
  D --> A
  D --> E["Reusable patterns reduce many errors"]
  E --> F["Infer hidden causes behind words"]
  F --> G["New general behavior"]
```

The full dependency is not a list of fashionable terms. It is a chain of unfinished problems: each right-hand box becomes inadequate and creates the next chapter.
