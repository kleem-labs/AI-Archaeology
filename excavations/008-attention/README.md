# Excavation 008 — Why Attention Had to Exist

An embedding gives a word a useful starting place, but *bank* still begins at the same place beside *money* and beside *river*. Its present meaning must be rebuilt from the words around this occurrence. The first question is how any word can reach the earlier evidence it needs.

Imagine a messenger reading one word at a time. The messenger may carry one summary forward but may never look back.

After a few words this seems fine. After five hundred, one compressed state must preserve every name, place, relationship, and detail that might become important later.

## Two bad choices

Store every word equally, and memory and computation grow without discrimination. Compress everything into one summary, and the detail needed by a future question may disappear.

Consider:

> John gave Mary the keys because she had forgotten hers.

A summary such as “people, keys, forgotten” loses who *she* refers to. The important information depends on the question being asked now.

Humans do something different. Asked where John was born, we do not replay every memory equally. The question guides retrieval.

```text
current need
     ↓
search the available context
     ↓
retrieve what matters now
```

This is the birth of **attention**: preserve access to the context and let each current token decide which earlier information matters to it.

## The trophy and the suitcase

> The trophy does not fit in the suitcase because it is too big.

When you reached *it*, you did not choose the nearest noun blindly. You reasoned that *it* should look toward things—especially *trophy* and *suitcase*—and that “fit inside” creates a relative size relationship between an object and a container. Your world model made *trophy* the stronger explanation.

That is already selective attention. It is not a hardcoded grammar rule. It is a learned judgment about relationships.

## What attention has not solved yet

Saying “look back” is not enough. Every previous token needs a relevance score for the current need. Those scores should not be fixed, because *she*, *born*, and *big* seek different information.

At this stage we deliberately avoid the famous attention equation. We have not earned it. We know only the required behavior:

1. each token can seek information;
2. each possible source can advertise what it offers;
3. relevance depends on the pair;
4. selected sources must contribute information to a new representation.

## Challenge

In “The animal did not cross the street because it was flooded,” identify what *it* should retrieve. Then change only the final word to *tired* and explain why the retrieval should change.

## What the next excavation needs

The relevance scores may be negative, huge, or expressed on unstable scales. Before they can mix information, they must become usable weights.

[Next: Softmax](../009-softmax/README.md)

<!-- book-prose-v2 -->
