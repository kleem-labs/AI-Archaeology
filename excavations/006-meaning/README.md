# Excavation 006 — Meaning

## The Problem

We can represent measurable objects with vectors. Language contains things we cannot weigh directly: *promise*, *justice*, *because*, and *almost*.

Where does a word's meaning come from?

## First Attempt: Write a Definition

A dictionary replaces one word with more words. Those words need definitions too. Eventually the explanation circles back or rests on shared experience. Definitions are useful, but they do not give a machine an independent foundation.

## Meaning Through Use

Consider the unfinished sentence:

> The cat drank the ___

Words such as *water* and *milk* fit; *mountain* usually does not. A word's surroundings constrain what it can mean. Words appearing in similar contexts often play similar roles.

This is the **distributional hypothesis**: linguistic items with similar distributions tend to have related meanings.

## Context as Evidence

We can collect nearby-word counts for every target word. *Cat* may frequently occur near *pet*, *fur*, and *purr*. *Dog* occurs near many of the same words. Their contextual records will resemble each other.

Meaning has become a pattern of relationships rather than a label supplied from outside.

## What This Misses

Co-occurrence is evidence, not perfect understanding. It inherits ambiguity, stereotypes, and omissions from its text. It also gives every word a long, sparse list with one position per context word.

## The New Problem

We need to compress contextual patterns into small vectors in which related meanings are nearby. These are embeddings.

---

Previous: [005 — Matrices](../005-matrices/README.md) · Next: [007 — Embeddings](../007-embeddings/README.md)
