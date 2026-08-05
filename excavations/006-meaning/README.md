# Excavation 006 — Meaning

## The Hardest Measurement So Far

We know how to represent legs, mass, sweetness, and position. They can be measured against the physical world. Now consider *promise*, *justice*, *bank*, or *almost*.

What instrument measures the meaning of a word?

A child rarely learns *dog* from a formal definition. The word appears while dogs bark, run, play, and appear in stories. Meaning emerges from repeated situations and relationships.

## Failed Attempt 1: Give the Machine a Dictionary

A dictionary defines *cat* using words such as *small*, *domesticated*, *carnivorous*, and *mammal*. To understand the definition, the machine must already understand those words. Their definitions use still more words.

The circle eventually reaches shared experience. A dictionary organizes meaning; it does not create meaning from nothing.

## Failed Attempt 2: Assign Every Word an Arbitrary ID

We could map `cat → 17`, `dog → 42`, and `car → 91`. IDs solve storage, but the numbers falsely suggest that dog is “25 units” from cat. Changing the IDs changes every apparent relationship while the language remains the same.

Identifiers distinguish words. They do not represent similarity.

## A Clue Hidden in Missing Words

Complete these sentences:

1. “The cat drank the ___.”
2. “She deposited cash at the ___.”
3. “They sat on the river ___.”

For the first, *milk* and *water* fit. For the second and third, the same word—*bank*—fits for different reasons. The surrounding words constrain which meanings are plausible.

Now compare *cat* and *dog*. Both appear near *pet*, *fur*, *food*, *vet*, *runs*, and *sleeps*. *Car* appears near *road*, *engine*, *drive*, and *fuel*. Context reveals relationships without requiring us to write a definition first.

This is the **distributional hypothesis**: words used in similar linguistic environments tend to have related meanings.

## Turning Context into Measurements

Take a tiny corpus:

```text
the cat drinks milk
the dog drinks water
the cat is a pet
the dog is a loyal pet
```

Using a window of two words, count neighbors:

| Target | Nearby evidence |
|---|---|
| cat | the, drinks, is, a |
| dog | the, drinks, is, a, loyal |
| milk | cat, drinks |

Cat and dog receive similar contextual profiles. We have converted an elusive idea into observable statistics.

## The Window Changes the Question

A one-word window emphasizes local grammar. A wide window captures broader topic. In “the curious cat quietly watched the bird,” a narrow window connects *cat* to *curious* and *quietly*; a wider one also connects it to *bird*.

There is no neutral context size. It determines what kind of relationship becomes visible.

## Ambiguity: One Word, Several Regions of Meaning

All occurrences of *bank* get mixed together. River contexts and financial contexts enter one profile. A single global record may become an average of unrelated meanings.

Later, attention will build a representation for each occurrence using its current sentence. For now, ambiguity exposes the limitation of static meaning.

## Code Walkthrough

`implementation.py` first tokenizes each sentence. `context_counts` walks across every word, slices out a neighborhood, and updates a `Counter`.

Run:

```bash
python3 excavations/006-meaning/implementation.py
```

Change `window=2` to `window=1`. Add “the dog chased the cat.” Observe that meaning statistics are not fixed facts; they change with evidence and collection choices.

## Common Misconceptions

**“Words appearing together must mean the same thing.”** Opposites such as *hot* and *cold* can share contexts. Distribution captures relationships, not only synonymy.

**“More text guarantees true meaning.”** Text contains errors, stereotypes, omissions, and unequal representation.

**“Co-occurrence means genuine understanding.”** It supplies powerful evidence about use. Whether that constitutes understanding is a deeper philosophical and empirical question.

## The New Problem

A context-count vector has one dimension for every vocabulary word. For a million-word vocabulary, it is huge and mostly zero. We need a compact space that preserves useful relationships.

---

Previous: [005 — Matrices](../005-matrices/README.md) · Next: [007 — Embeddings](../007-embeddings/README.md)
