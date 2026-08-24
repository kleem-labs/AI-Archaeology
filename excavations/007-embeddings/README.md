# Excavation 007 — A Place for Meaning to Live

In the last excavation, you learned something strange. You could know almost
nothing about the word *blar*, yet repeated sentences slowly fenced in what it
could mean. A word appearing where animals usually appear was probably not a
color. A word connecting creatures to food was probably not a place.

Each sentence pulled on the others. Meaning began to look less like a
definition and more like a web of constraints.

But a web is only a picture in our heads. A machine needs somewhere to keep
what the web has taught it.

Suppose your first idea is simply to number the words:

```text
cat = 17       dog = 42       car = 91
```

The machine can now tell the words apart. Has it learned anything about their
relationships?

Try subtracting the IDs. The gap from *cat* to *dog* is 25; the gap from *dog*
to *car* is 49. That seems to claim that *cat* is more closely related to
*dog*—until someone reorganizes the dictionary:

```text
cat = 91       dog = 17       car = 42
```

Nothing about English changed, but all the gaps did. The apparent geometry
came from our numbering scheme, not from language. IDs can preserve identity;
they cannot preserve meaning.

You need a representation whose distances are allowed to be learned rather
than assigned accidentally.

## Make room without inventing meaning

Give every word its own private coordinate:

```text
cat = [1, 0, 0]
dog = [0, 1, 0]
car = [0, 0, 1]
```

Now renumbering cannot create a false closeness. But calculate the distance
between each pair. Every answer is the same. This space says *cat is different
from dog* and *cat is different from car*, but it has no way to say that one
difference is smaller than the other.

So you face a choice. Fixed coordinates preserve identity without
relationships. Arbitrary IDs appear to contain relationships that are not
real. What would a useful space have to do?

It would need to begin without assumptions, then let actual usage move the
words.

## Let the sentences move the points

Place *cat*, *dog*, and *car* at random positions. The starting locations mean
nothing. Then hide one word in a sentence:

```text
the ___ chased the mouse
```

Imagine the system predicts *car*. The surrounding words have exposed a
failure: whatever position currently represents *car* makes it behave too much
like things that chase mice. Move the points a little so *cat* and *dog* become
easier answers here and *car* becomes harder.

Now try another sentence:

```text
we parked the ___ beside the road
```

This time the pressure moves *car* toward words that fit vehicle contexts.
Repeat the process across many sentences. No single example announces what a
word means. Each one adds a small pull:

```text
                         "chased the mouse"
                       cat  ←────  dog
                        ↑           ↑
       "drank milk" ────┘           └──── "wagged its tail"

              car  ←──── "parked beside the road"
```

You have not labelled an axis *animalness*. You have not stored a dictionary
definition inside coordinate one. You have merely allowed thousands of
prediction failures to reshape the space until words facing similar demands
occupy useful relative positions.

That learned position is what we call an **embedding**.

## Let the symbols arrive last

Take one concrete snapshot. Suppose we decided that every word gets three
adjustable coordinates, and training has currently placed *tiger* here:

```text
tiger → [0.8, 0.2, -0.4]
```

Every part now has a job you already understand:

- *tiger* is the discrete token—the identity we started with.
- The arrow means “represent this token by,” not “these two things are equal.”
- `[0.8, 0.2, -0.4]` is the position training has produced so far.
- Three is the width we chose for this tiny world. A real model usually needs
  many more adjustable coordinates.
- The coordinates need not have private names. A relationship can be spread
  across several of them.

### Why the melody needs these exact notes

[The arrow](../../MATHEMATICAL_MOVES.md#arrows) means “represent this token as,” not equality: a word and its numerical representation are different kinds of object.
[The membership sign](../../MATHEMATICAL_MOVES.md#membership) says the embedding is allowed to live among d-coordinate real vectors.
[The superscript d](../../MATHEMATICAL_MOVES.md#powers) counts coordinate slots here; it is dimension, not an instruction to raise each number to a power.

Only now is the compact notation useful:

$$
\text{token}\longrightarrow \mathbf{e}\in\mathbb{R}^d
$$

Here, $\mathbf{e}$ is merely a short name for the learned list of coordinates.
$d$ is how many coordinates we chose to provide. $\mathbb{R}^d$ says that all
$d$ entries may be ordinary real numbers—positive, negative, or zero. The
equation has added no new idea. It records the space you just constructed.

## The word that refuses to stay still

You might think the problem is solved. Then the same token appears twice:

```text
deposit money at the bank
sit on the river bank
```

The lookup begins both occurrences of *bank* at the same learned position. Yet
one occurrence must gather financial meaning and the other geographical
meaning. A static embedding can provide a useful starting point, but it cannot
decide what this particular occurrence means.

Read that distinction once more:

```text
embedding              where the token begins
contextual representation   what this occurrence becomes here
```

How can the second *bank* change without erasing what training already taught
the token? It must look outward. It must discover which surrounding words
matter now and retrieve information from them.

That unresolved need—not a desire to introduce another famous equation—is
what forces the next invention.

## Before you leave the excavation

Build a three-word world containing *cat*, *dog*, and *car*. First use IDs,
then private one-hot coordinates. Explain exactly what each representation can
preserve and what it cannot. Finally, describe in ordinary language how the
sentence “the dog chased the cat” should pull the learned positions. Do not use
the word *embedding* until your procedure has already created one.

[Mistakes worth preserving](mistakes.md)
[Diagram](diagram.md)
[Pure Python → NumPy → PyTorch](implementation/README.md)
[References](references.md)

[Next: Why Attention Had to Exist](../008-attention/README.md)

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->
