# Excavation 007 — Embeddings

[Previous: Meaning](../006-meaning/README.md)

We have a web of constraints but no convenient way to store its geometry.

## First attempt: give every word an ID

```text
cat = 17
dog = 42
car = 91
```

The IDs distinguish tokens, but their numeric gaps are accidents. Changing the numbering changes the apparent relationships without changing the language.

## Second attempt: one private coordinate per word

```text
cat = [1, 0, 0]
dog = [0, 1, 0]
car = [0, 0, 1]
```

Identity is perfect, but every word is equally unrelated to every other. The representation says only “different.” It cannot say “different, but used in related ways.”

## Let the constraints shape a space

Start each word at an arbitrary point. Ask the system to use surrounding text to predict missing or nearby words. When it predicts badly, move the relevant points slightly. Repeat across billions of contexts.

No teacher declares an axis called *animalness*. The pressure comes from the whole web:

- *cat* and *dog* repeatedly face similar contextual demands;
- *bank* is pulled differently by financial and river contexts;
- *eat* is constrained by the kinds of words that appear around it and their order.

Eventually the geometry becomes a compact compromise among countless relationships. The learned vector for a token is an **embedding**.

Only now is notation helpful:

$$
\text{token}\longrightarrow \mathbf{e}\in\mathbb{R}^d
$$

This does not claim that coordinate 1 has a simple dictionary name. Meaning may be distributed across many coordinates. What matters is that useful relationships become available to later computations.

## A static embedding still fails

One token can carry different meanings:

```text
deposit money at the bank
sit on the river bank
```

A single stored vector cannot by itself decide which meaning is active. Even worse, a long sentence can connect words separated by many positions. The representation must change with context.

That gives us a crucial distinction:

```text
embedding: where a token begins
contextual representation: what this occurrence becomes here
```

## Challenge

Explain why one-hot vectors are excellent identifiers but poor representations of related meaning. Then explain why a dense embedding still cannot resolve *bank* without context.

## What the next excavation needs

Each word must be able to retrieve the parts of the sentence that matter for understanding this occurrence, rather than accepting one fixed summary of everything.

[Next: Attention](../008-attention/README.md)
