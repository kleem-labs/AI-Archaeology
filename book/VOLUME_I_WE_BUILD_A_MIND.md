# Volume I — We Build a Mind

We begin with nothing but observations. By the final chapter, the same chain of necessities has produced a tiny language model that can learn and generate.

One discovery will create the need for the next; the object under construction never resets.

## Overture

The book opens in a valley where mathematics has no names. Keep watch for one recurring transformation: an observation becomes a mark, the mark becomes a relationship, and the relationship becomes a machine. The tiger crossing the valley is not an example pasted onto a formula; its tracks are the pressure from which the formula will grow.

```text
tracks → marks → relationships → a mind begins
```

In this volume:

- [Part I — Measuring Reality](#part-i--measuring-reality)
- [Part II — Inventing Meaning](#part-ii--inventing-meaning)
- [Part III — Learning from Error](#part-iii--learning-from-error)
- [Part IV — Building a Tiny GPT](#part-iv--building-a-tiny-gpt)

---

## Part I — Measuring Reality

A community in the valley can recognize danger but cannot yet compare one observation with another. Counting, features, vectors, distance, and matrices will not arrive as school subjects. Each will be invented because the previous description fails during the same attempt to understand the animals around the camp.

---

### Excavation 000 — Before Mathematics Existed

Forget school. Forget equations. Imagine that you are the first person trying to understand the world.

You have no numbers, no names, and no inherited explanations. You have only what reaches your senses: a rustle in the grass, a striped animal at the river, heat from a fire, clouds before rain.

At first, every moment is separate. Then the rustle happens again—and the striped animal appears again. Clouds gather—and rain follows again. One observation begins to help with the next.

That repeatability is the first opening for intelligence. In a world where fire was sometimes hot, sometimes cold, and sometimes became water for no reason, no lesson could survive from yesterday. Prediction would be impossible.

#### The first failed idea: remember everything

Suppose you try to preserve every detail of every tiger: every hair, shadow, scar, sound, and viewing angle. The next tiger will never match. It stands elsewhere. The light has changed. It may be younger, muddier, or missing a leg.

Exact memory says that nothing is ever the same twice.

So your mind does something more useful. It discards most details and keeps what repeats: stripes, teeth, movement, danger. Thousands of experiences become one reusable pattern.

```text
many encounters
      ↓
what keeps repeating?
      ↓
one reusable pattern
```

This is abstraction, and it is a kind of compression. Intelligence begins when repeated experience can be compressed without throwing away what matters for the next decision.

#### Why patterns were not enough

Recognizing a tiger helps you survive one encounter. But soon you need answers that a pattern cannot provide:

- How many tigers were there?
- Where are they?
- How fast can they run?

Those were your questions in our original expedition. They are the reason the journey cannot stop at recognition.

“How many?” demands quantity. “Where?” demands space. “How fast?” demands change. Mathematics does not arrive as a collection of symbols. It arrives because reality keeps asking questions that vague words cannot answer reliably.

That gives us the method for every excavation ahead:

```text
reality → question → inadequate idea → better representation → mathematics
```

The equation, when one finally appears, will be the last step: a compressed record of reasoning we already understand.

We have more observations than memory can hold, and more questions than a name can answer. We need to decide which properties of an experience deserve to be kept.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/000-before-mathematics-existed/README.md).*

---

### Excavation 001 — Why Features Exist

Your tribe now recognizes tigers. That is not enough. Ten animals are moving through the valley, and you must decide which ones threaten the camp.

For each animal you could remember the whole encounter: the exact light, every hair, every sound. But those details change even when the danger does not. Perfect memory gives you more information and less ability to compare.

#### First attempt: use the name

“Tiger” is useful to a person who already understands the word. It gives a machine nothing it can measure. A name distinguishes one category from another; it does not explain what evidence created the category.

#### Second attempt: choose one property

Perhaps stripes mean danger. Then a zebra becomes a tiger. Perhaps four legs are enough. Then deer, dogs, and tigers collapse together. A three-legged tiger exposes the opposite failure: one missing property should not erase all the other evidence.

We need several observations, chosen because each can help with the decision:

```text
animal
├── weight
├── speed
├── teeth
├── stripes
└── movement toward camp
```

Only now do we name these observations **features**.

A feature is not a decorative fact and not an eternal truth about an object. It is a measurable property retained because it may help answer a question. Location matters when deciding who is in danger. Tooth length matters when judging threat. Fur color may matter much less at night.

That explains why choosing features is part of reasoning. The world offers unlimited detail; intelligence has to decide what deserves a place in the representation.

#### The user's discovery

You did not say, “put every attribute together.” You said:

> Put similar attributes together and calculate their difference.

That word—*similar*—is essential. Weight must be compared with weight, speed with speed, and age with age. If the positions change meaning from one animal to the next, the arithmetic can be correct while the thought is nonsense.

| feature | tiger A | tiger B |
|---|---:|---:|
| weight | 220 | 225 |
| speed | 65 | 66 |
| age | 6 | 5 |

We have turned an animal into an organized set of comparable measurements. No formula was needed. The structure came first.

#### A serious limitation

Features do not arrive objectively. Kilograms can overwhelm a binary stripe value simply because the numeric scales differ. A useful representation may omit an important clue or preserve a misleading one. Mathematics can only operate on what we decide to record.

With thousands of animals and many features, separate facts become difficult to store and manipulate. We need one object that keeps their meaning through an agreed order.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/001-why-features-exist/README.md).*

---

### Excavation 002 — Vectors

The tribe has learned to keep only useful features: weight, speed, age, distance from camp. But those features are still loose facts. When reports begin arriving all day, copying or comparing one animal means chasing its measurements across the record.

The crisis is no longer noticing. It is keeping the observations that belong to one animal together.

Reports now look like this:

```text
tiger near river
three deer north
hunter injured
water low
```

A table helps: one row per animal, one column per property. But to compare, copy, or transform one animal, we want to lift its row out as a single object.

#### The package

First agree on an order:

```text
[weight, speed, age]
```

Then an animal can be carried as:

```text
tiger = [220, 65, 6]
rabbit = [2, 45, 1]
```

The brackets are not the discovery. The discovery is that many related measurements can travel together without losing which feature each position represents. Only now do we call that ordered package a **vector**.

#### What fails if order is ignored

If one person writes `[weight, speed, age]` and another reads `[age, weight, speed]`, the numbers survive but the meaning does not. A vector is never “just numbers.” It is numbers plus an agreement about what each coordinate means.

#### From a package to a place

Imagine using only weight and speed. Every animal now has a location—not in the jungle, but in a space whose directions mean properties.

```text
speed
  ↑       rabbit •
  |
  |                         • tiger
  +--------------------------------→ weight
```

The tiger's properties locate it. With three features it lies in three-dimensional feature space. With ten thousand features the same idea continues, even though we cannot picture it.

This was the great leap in your original excavation: geometry stopped meaning only “Where is the tiger?” It could now help answer “What is the tiger like?”

Nearby locations can represent similar objects. A movie can be located by humor, romance, and violence. A song can be located by tempo, instrumentation, and mood. Modern AI uses the same move: turn something difficult to compare into a point whose coordinates can be compared.

#### The first equation earns its place

We already understand the object, so notation can compress it:

#### The calculation hidden inside vectors

A tiger recorded as weight 220, speed 65, and age 6 becomes [220, 65, 6]. The first slot must always mean weight; otherwise [220, 65, 6] could describe nonsense.

##### Naming what is already on the table

- **x** is the object we needed to carry as one package.
- **x₁ through xₙ** are its agreed measurements; subscripts preserve which feature is which.
- **n** exists because different problems keep different numbers of features.
- The brackets bind the measurements without adding or comparing them yet.

This says only: one object carries an ordered measurement for each of $n$ agreed features.

##### Why the melody needs these exact notes

[Brackets](../MATHEMATICAL_MOVES.md#brackets) keep tiger weight, speed, and age together without pretending they should be added; each observation must remain recoverable.
[Subscripts](../MATHEMATICAL_MOVES.md#indices) give each retained feature an address. The dots mean the same pattern continues until feature n; they do not hide another operation.
[The equals sign](../MATHEMATICAL_MOVES.md#equals) says that **x** is our short name for this complete ordered list.

Nothing remains unnamed in the vectors case on the dust-map. We can finally trade the long route for its compact map:

$$
\mathbf{x}=[x_1,x_2,\ldots,x_n]
$$

A thousand feature differences still give a thousand answers. To say which animal is closest, we need those differences to become one number.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/002-vectors/README.md).*

---

### Excavation 003 — Distance

The king asks for the animal most similar to Tiger A.

```text
Tiger A = [220, 65, 6]
Tiger B = [225, 66, 5]
Rabbit  = [  2, 45, 1]
```

The answer feels obvious. A computer still needs a procedure.

#### First attempt: compare one feature

Weight alone can find a crocodile that weighs the same as a tiger. Add speed and another unrelated animal may still match. Every omitted property is a place for a false conclusion to hide.

#### Second attempt: keep every difference

Comparing Tiger A with Tiger B gives:

```text
weight:  5
speed:   1
age:    -1
```

This is accurate, but it is not a decision. With a thousand attributes we receive a thousand answers. We need one measure of separation.

#### Your derivation

You proposed the entire path yourself:

> Find the difference of similar features. If it is negative, that is wrong for distance, so square the differences, add them, and take the root.

Why not simply add? Because opposite differences cancel. A change of `100` and `-100` would produce zero, falsely declaring two objects identical.

Why square? Every changed coordinate becomes positive, and a large disagreement contributes more strongly than a small one.

Why add? We need every feature to contribute to one answer.

Why take the root? The direct line across a space is not the sum of its side lengths. A move of 3 in one direction and 4 in another forms a right triangle whose direct separation is 5. The root returns us from squared separation to ordinary distance.

Only after the reasoning is complete does the notation help:

#### The calculation hidden inside distance

Tiger A has weight 220 kg, speed 65 km/h, and age 6 years.

Tiger B has weight 225 kg, speed 66 km/h, and age 5 years.

Compare the same property with the same property:

~~~text
weight difference = 225 - 220 =  5
speed difference  =  66 -  65 =  1
age difference    =   5 -   6 = -1
~~~

Adding gives 5 + 1 - 1 = 5. That is wrong: being one year younger cancelled part of the other disagreement.

~~~text
weight disagreement squared = 5 squared    = 25
speed disagreement squared  = 1 squared    =  1
age disagreement squared    = (-1) squared =  1
total                                      = 27
~~~

The total is in squared differences. Its square root gives one ordinary separation: about 5.20.

##### Naming what is already on the table

- **x** is only a nickname for Tiger A's ordered measurements.
- **y** is only a nickname for Tiger B's ordered measurements.
- **x1 and y1** are their weights; index 2 means speed; index 3 means age.
- **xi−yi** abbreviates “compare the same named property,” exactly as above.
- Squaring repairs the cancellation we just witnessed.
- Summing combines weight, speed, and age into one answer.
- The root changes total 27 into distance 5.20.
- **d(x,y)** merely names “the one separation between these two tigers.”

##### Why the melody needs these exact notes

[Subtracting](../MATHEMATICAL_MOVES.md#subtraction) tiger height from tiger height and tiger speed from tiger speed isolates each like-for-like disagreement. Adding would measure a total, not a gap.
[Squaring](../MATHEMATICAL_MOVES.md#powers) stops a smaller and larger feature from cancelling and makes a large mismatch count more strongly. Absolute value could stop cancellation too, but would produce a different geometry in which many small misses and one large miss trade differently.
[Adding the squared disagreements](../MATHEMATICAL_MOVES.md#summation) lets every retained feature contribute to one separation. Multiplying would let one perfect feature match erase all other disagreement by making the product zero.
[The square root](../MATHEMATICAL_MOVES.md#square-root) returns the accumulated squared separation to the features' ordinary scale; it is omitted when squared distance itself is all an algorithm needs.

The symbols are about to change costume, but their work has appeared before: **the chisel**—what is shared is removed so the remaining change can be seen; **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. This is how distant excavations begin to sound like variations of one melody.

The story of distance has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
d(\mathbf{x},\mathbf{y})
=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$

The formula is your procedure written compactly.

#### A limit we must remember

If weight is measured in kilograms and a stripe flag is only zero or one, weight can dominate. Distance treats coordinate scales as meaningful. Representation and normalization therefore matter as much as arithmetic.

Distance also answers **similarity**, not every kind of relationship. That distinction will become decisive when we reach attention.

So far a vector has described where an object is in feature space. But an arrow can also describe how something changes. That second meaning will lead us toward transformations.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/003-distance/README.md).*

---

### Excavation 004 — Vectors as Change

Distance has given the trackers one number for how far apart two places are. It throws away something they now urgently need: which way to walk from one place to the other.

You are standing in the jungle. Someone tells you, “Walk five meters.” You cannot obey.

Five tells you how much, but movement also needs a direction. “Five meters north” is complete. It does not describe where you are; it describes what must change.

#### Location and instruction are different

Yesterday you began at the river. Today you begin at the camp. The instruction “five meters north” remains the same, although the destination changes.

That is the second life of a vector: not a state, but a reusable description of change.

```text
state + change = new state
```

Suppose a traveler starts at `[2, 3]` and ends at `[7, 1]`. We can discover the change coordinate by coordinate: `+5` in the first direction and `-2` in the second. The change vector is `[5, -2]`.

Only now is an equation useful:

#### The calculation hidden inside vectors as change

A rescue party marks its camp on a paper map. It walks five kilometres east and two kilometres south to reach an injured ranger. Those instructions still work if a second party begins from another camp: move five east and two south. Only after the route has a meaning do we record east–west and north–south change as `[5, -2]`.

##### Naming what is already on the table

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

##### Why the melody needs these exact notes

[Destination minus starting point](../MATHEMATICAL_MOVES.md#subtraction) is forced because we want the change that would carry **a** to **b**, not their combined location.
[A negative coordinate](../MATHEMATICAL_MOVES.md#negative-sign) keeps direction: −2 means move two units opposite that axis, not that the movement has an impossible size.
[Adding the change back](../MATHEMATICAL_MOVES.md#addition) is the check: starting place plus the discovered movement must recover the destination.

Inside vectors as change, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the joining river**—separate contributions meet without losing where they came from. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about vectors as change and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\Delta=\mathbf{b}-\mathbf{a}=[7-2,1-3]=[5,-2]
$$

Add it back and the meaning becomes visible:

$$
\mathbf{a}+\Delta=\mathbf{b}
$$

#### Why changes add

Walk three steps east, then two north. Could one instruction replace both? Yes: the diagonal change that produces the same destination.

Vector addition was not chosen because brackets look convenient. Independent changes accumulate. Two pushes on a box, two deposits into an account, and two corrections to a model all demand one equivalent net change.

You supplied three memorable cancellation examples:

- sending and receiving the same amount;
- eating and burning 100 calories;
- throwing a ball up and catching it at the starting height.

Opposite changes cancel because the final state contains no net displacement along that feature.

#### Why distance was not enough

Distance says how much separation exists but discards direction. Many destinations are five units from the same start. A change vector preserves both magnitude and direction.

This distinction matters in learning. A model's current parameters are a state. Training must say which weights to increase, which to decrease, and by how much. That instruction is a vector of change.

One fixed change is useful. We now want a machine that receives any vector and produces an appropriate new vector consistently.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/004-vectors-as-change/README.md).*

---

### Excavation 005 — Matrices

One vector can now describe one particular change. The rangers next want a reusable machine: give it any animal report and let the same set of rules produce several new judgments. Adding one fixed change cannot do that, because a heavy slow animal and a light fast animal should not be altered identically.

Imagine two arrows starting at the same point. A machine stretches both, but sends them toward different final places depending on their original directions.

Does that matter? You answered simply:

> Yes. They end up in different places.

That answer exposes the need. A transformation cannot be one fixed movement added to everything. It must respond to the input vector.

#### First attempt: store a separate answer

We could write a transformed result for every possible vector. But there are infinitely many vectors. A lookup table can memorize examples; it cannot describe a general rule.

#### Second attempt: transform each coordinate alone

Suppose output one depends only on input one and output two only on input two. That can stretch or shrink axes, but it cannot let weight influence danger while speed also influences danger. Real representations interact.

We need a compact machine in which every output may receive a chosen contribution from every input.

```text
input features → weighted contributions → output features
```

Take an input `[4, 5]`. One output question might say: take twice the first feature and three times the second. Another might ignore the first and take four times the second.

Each question needs a row of weights:

```text
[2, 3]
[0, 4]
```

Stacking the questions creates a **matrix**. Only after that idea is clear do we calculate:

#### The calculation hidden inside matrices

A ranger must turn two observations—how heavy an animal looks and how fast it moves—into two decisions: danger and whether pursuit is possible. For danger she counts the weight clue twice and the speed clue three times. For pursuit she ignores weight and counts speed four times. Writing the two recipes as rows lets one reusable machine apply both judgments to every animal report.

##### Naming what is already on the table

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.

Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets each clue's importance scale that clue. A zero weight silences it; a weight of three makes it count three times.
[Addition](../MATHEMATICAL_MOVES.md#addition) combines the scaled clues because they are separate contributions to the same judgment. Multiplying them would make any zero clue erase the entire decision and would claim interaction we never asked for.
[Each equals sign](../MATHEMATICAL_MOVES.md#equals) records that the verbal judgment, its arithmetic recipe, and its final score are three descriptions of the same result.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The dust-map already contains the complete matrices mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\text{threat score}=2(4)+3(5)=23
$$

$$
\text{chase score}=0(4)+4(5)=20
$$

#### Why order and shape matter

If the input has three features, every output question needs three weights. A matrix with four rows asks four questions and therefore creates four output features.

```text
4 questions × 3 input features
          ↓
3 input numbers → 4 output numbers
```

Shape is the contract between what the machine expects and what it produces.

#### The AI connection

A neural network layer repeatedly does this: receive one representation, mix its features according to learned weights, and produce another representation. The matrix is a transformation machine. Training will eventually decide the weights; for now we only needed a coherent way to express all interactions together.

We can transform measurable properties. Language gives us a harder object: a word whose meaning is not available from any physical measuring instrument.

#### The first constellation

The valley began with unnamed observations. A feature kept one distinction; a vector kept several; distance turned disagreement into separation; a matrix turned several judgments into one reusable machine. None was a separate school subject. Each was the shape left behind when the earlier tool broke.

```text
observation → feature → vector → distance → transformation
```

The trail called *the first constellation* is what remains when one necessity becomes another.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/005-matrices/README.md).*

---

## Part II — Inventing Meaning

The community can now store measurements and transformations. Its records contain words, however, and a word changes its work from one sentence to another. The old measuring tools must be turned toward context until meaning, attention, and the Transformer emerge from the pressure.

---

### Excavation 006 — Meaning Without a Dictionary

Matrices can transform measurements once we know what each input coordinate means. The community's richest records are not measurement tables, however. They are warnings, stories, and instructions made of words—and no measuring instrument tells us what an unknown word means.

Suppose you arrive with no language and read:

```text
blar eats miku
```

What does *blar* mean? What does *eats* mean?

The tempting explanation says that *blar* must be alive because living things eat. You caught the hidden assumption immediately:

> If I do not know what “eat” means, how can I infer what “blar” means?

You cannot. One sentence, from absolute zero, gives almost no meaning. At most it reveals that three symbols occur in a recurring arrangement.

#### The dictionary fails first

A dictionary defines words with other words. If none of them are grounded yet, definitions only move the mystery around. Arbitrary IDs solve storage but add no relationships.

#### Structure appears before meaning

Now read more:

```text
blar eats miku
zon eats miku
blar drinks wug
zon sleeps
```

We still cannot translate the symbols. But *blar* and *zon* behave similarly. They appear in some of the same positions and relationships. Structure has emerged before definition.

With millions of sentences, each occurrence supplies a constraint. No sentence declares what *blar* is. Together they narrow what it can plausibly be.

```text
clue 1 ─┐
clue 2 ─┼─→ a smaller region of possible meaning
clue 3 ─┘
```

The same process happens to *eats*. It repeatedly connects one family of symbols with another. No word must be learned first. All the representations adjust together, like a spider web in which pulling one node shifts the rest.

#### What nearby words cannot tell us

You raised a second objection: without grammar, how can a system know whether nearby words should be close or far?

It cannot solve this by proximity alone.

```text
dog bites man
man bites dog
```

The words are identical; the relationships differ. Order and wider context must constrain the representation too. Likewise, *bank* in “deposit money at the bank” and “sit on the river bank” cannot receive one fixed meaning from the token alone.

Meaning is therefore not a secret definition stored inside a word. It emerges from a network of usage, order, and relationships. Text alone reveals linguistic structure; grounding it fully in lived reality is a deeper problem we should not pretend has vanished.

We need a geometry that can move symbols toward representations satisfying many contextual constraints at once.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/006-meaning/README.md).*

---

### Excavation 007 — A Place for Meaning to Live

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

#### Make room without inventing meaning

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

#### Let the sentences move the points

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

#### Let the symbols arrive last

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

##### Why the melody needs these exact notes

[The arrow](../MATHEMATICAL_MOVES.md#arrows) means “represent this token as,” not equality: a word and its numerical representation are different kinds of object.
[The membership sign](../MATHEMATICAL_MOVES.md#membership) says the embedding is allowed to live among d-coordinate real vectors.
[The superscript d](../MATHEMATICAL_MOVES.md#powers) counts coordinate slots here; it is dimension, not an instruction to raise each number to a power.

Only now is the compact notation useful:

$$
\text{token}\longrightarrow \mathbf{e}\in\mathbb{R}^d
$$

Here, $\mathbf{e}$ is merely a short name for the learned list of coordinates.
$d$ is how many coordinates we chose to provide. $\mathbb{R}^d$ says that all
$d$ entries may be ordinary real numbers—positive, negative, or zero. The
equation has added no new idea. It records the space you just constructed.

#### The word that refuses to stay still

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

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/007-embeddings/README.md).*

---

### Excavation 008 — Why Attention Had to Exist

An embedding gives a word a useful starting place, but *bank* still begins at the same place beside *money* and beside *river*. Its present meaning must be rebuilt from the words around this occurrence. The first question is how any word can reach the earlier evidence it needs.

Imagine a messenger reading one word at a time. The messenger may carry one summary forward but may never look back.

After a few words this seems fine. After five hundred, one compressed state must preserve every name, place, relationship, and detail that might become important later.

#### Two bad choices

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

#### The trophy and the suitcase

> The trophy does not fit in the suitcase because it is too big.

When you reached *it*, you did not choose the nearest noun blindly. You reasoned that *it* should look toward things—especially *trophy* and *suitcase*—and that “fit inside” creates a relative size relationship between an object and a container. Your world model made *trophy* the stronger explanation.

That is already selective attention. It is not a hardcoded grammar rule. It is a learned judgment about relationships.

#### What attention has not solved yet

Saying “look back” is not enough. Every previous token needs a relevance score for the current need. Those scores should not be fixed, because *she*, *born*, and *big* seek different information.

At this stage we deliberately avoid the famous attention equation. We have not earned it. We know only the required behavior:

1. each token can seek information;
2. each possible source can advertise what it offers;
3. relevance depends on the pair;
4. selected sources must contribute information to a new representation.

The relevance scores may be negative, huge, or expressed on unstable scales. Before they can mix information, they must become usable weights.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/008-attention/README.md).*

---

### Excavation 009 — From Scores to Attention

Suppose *she* compares itself with earlier words and receives:

```text
John   2
Mary   8
book   4
```

The ranking is useful, but these are not yet mixing weights. Another sentence may produce `200, 800, 400`, or include negatives. We need a stable answer to: how much should each source contribute?

#### Failed ideas

Choose only the maximum, and uncertainty disappears. Mary may matter most while *book* still supplies useful context.

Divide by the sum, and negative scores can create negative shares or the total can be zero.

Clip negatives, and a tiny movement across zero abruptly switches a path on or off. We want smooth corrections during learning.

The desired transformation should:

- make every share positive;
- preserve which score is larger;
- make strong evidence more decisive;
- let bad negative matches fade toward zero;
- normalize the shares to a total of one.

#### Let the requirements choose the operation

An exponential does something useful: positive evidence grows quickly, while negative evidence becomes a small positive number.

```text
score:          2      4       8
exponential:   ~7     ~55    ~2981
```

Squares also amplify large scores, but they turn `-5` into `25`, converting strong negative evidence into a strong positive match. Exponentials preserve order instead.

After exponentiating, divide each result by their total. Now the values are positive and sum to one. Only after deriving those requirements do we name the result **softmax**:

#### The calculation hidden inside from scores to attention

Mary, John, and the book are possible sources for the word *she*. The sentence gives Mary the strongest relevance, the book a weaker connection, and John the weakest. Raw relevance can be negative or arbitrarily large, so it cannot yet say what share each source should contribute. Exponentiation turns every candidate into positive evidence; dividing by their shared total converts that evidence into portions of one whole.

##### Naming what is already on the table

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.

For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

##### Why the melody needs these exact notes

[Exponentiation](../MATHEMATICAL_MOVES.md#exponential) makes every raw score positive while preserving order and turning score gaps into stable ratios. Squaring would make a large negative score look strong; clipping would destroy gap information.
[The sum](../MATHEMATICAL_MOVES.md#summation) gathers every candidate's positive weight because all candidates must share one unit of attention. A product would not describe a total available amount.
[Dividing by that total](../MATHEMATICAL_MOVES.md#division) converts each weight into its share. Without it, multiplying every score scale would change the amount of information mixed rather than only its distribution.

The calculation borrows several gestures already encountered elsewhere: **the rising flame**—a small score difference becomes positive relative evidence; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. from scores to attention feels new because the objects are new; the gestures remain recognizably human.

The story of from scores to attention has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\mathrm{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
$$

#### The missing question

We now know **who matters**, but weights are not knowledge. If a historian receives weight `0.90`, what does the historian actually say? That distinction leads to values.

We must derive both the relevance scores and the information being mixed. Those are different jobs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/009-softmax/README.md).*

---

### Excavation 010 — Query, Key, and Value

Return to the trophy sentence. The word *it* is looking for something like “a previously mentioned physical object that can participate in this size relationship.” Each earlier word offers different clues.

This suggests two cards:

```text
Query: what information am I looking for?
Key:   what kind of match can I offer?
```

#### Similarity is the wrong question

At first we might reuse Euclidean distance. You rejected that for the right reason:

> Distance says similar. Here we are looking for relevant.

A doctor and a hospital are not similar objects, yet they can be strongly related. Attention asks a directional question: “How useful are you to me right now?”

#### Your scoring operation

You proposed comparing corresponding features, multiplying them, and adding everything to get one score.

Suppose a query is `[1, 2, 3]` and a key is `[2, 1, 4]`. Feature by feature:

```text
1×2 contributes 2
2×1 contributes 2
3×4 contributes 12
```

If both sides care strongly about the same feature, the contribution is large. If one side has zero interest, the contribution vanishes. Opposing signs create negative evidence rather than being discarded. Adding the contributions gives one relevance score.

Only now do we write the operation you rediscovered—the dot product:

#### The calculation hidden inside query, key, and value

A librarian hears, “Find me the book about a striped predator.” The request emphasizes *animal* and *stripes*. A catalogue card advertises the same properties; matching request-property to catalogue-property produces relevance. If that card wins three quarters of the attention, three quarters of the book's stored content—not three quarters of its catalogue description—travels into the answer. The request becomes the query, the catalogue becomes the key, and the retrievable content becomes the value only after those jobs are distinct.

##### Naming what is already on the table

- **qᵢ** states what receiving token i needs; **kⱼ** states what source j offers.
- Multiplying matching coordinates rewards aligned needs and offers; opposite signs become negative evidence.
- Summing over feature r turns many alignments into one score sᵢⱼ.
- **αᵢⱼ** is that score after normalization: how much i listens to j.
- **vⱼ** is the content source j contributes; multiplying by α scales its voice.
- Summing over j combines every permitted source into output oᵢ.

Learned matrices create query, key, and value views from each current representation. Their formulas record three roles we already needed; they are not arbitrary symmetry.

##### Why the melody needs these exact notes

[The dot product](../MATHEMATICAL_MOVES.md#dot-product) multiplies query height-need by key height-offer, stripe-need by stripe-offer, and so on, then adds those aligned agreements into one relevance score.
[Multiplication inside the dot product](../MATHEMATICAL_MOVES.md#multiplication) is required because a query feature should matter only when the matching key feature is present too; addition would reward a key for merely being large on unrelated features.
[The first sum](../MATHEMATICAL_MOVES.md#summation) combines feature-level evidence into one match. The second sum combines each source's value after its attention weight scales how loudly that source contributes.

Three old motions cast new shadows here: **the meeting of arrows**—matching directions reinforce while opposing directions resist; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Cover the prose about query, key, and value and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
s_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j
=\sum_r q_{ir}k_{jr}
$$

For each receiving word, its whole query is compared with the whole key of every available source word. The feature-wise products happen inside each comparison; the sum creates one score per source.

#### Why a third vector exists

Query and key decide who matters. They do not say what information should travel.

When asked how three experts should contribute, you answered:

> Each expert contributes what they do—the knowledge related to their profession and domain.

Exactly. A historian's matching description is not the historical knowledge we want to retrieve. Each source therefore needs a **Value**: the content it contributes if selected.

```text
Query ↔ Key → score → softmax weight
Value × weight → contributed information
```

The output for one token is finally the weighted sum of source values:

$$
\mathbf{o}_i=\sum_j \alpha_{ij}\mathbf{v}_j
$$

One relevance system can pursue one mixture of relationships. Language needs several kinds of relevance at the same time.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/010-query-key-value/README.md).*

---

### Excavation 011 — Multi-Head Attention

Ask one expert to interpret a sentence. The expert may follow reference, grammar, distance, or topic—but one attention distribution forces every relationship to compete in the same set of weights.

#### Failed attempt: make one expert bigger

A wider query and key can hold more information, but one head still produces one distribution for each receiving token. A nearby adjective and a distant subject may both matter for different reasons. One compromise can blur both jobs.

#### Your expert model

You supplied the better design:

> Each expert contributes what they do, related to their profession and domain of knowledge.

Imagine parallel specialists reading the same sentence:

- one notices who a pronoun refers to;
- one follows grammatical agreement;
- one notices nearby modifiers;
- one tracks the broader topic.

We do not assign those professions by hand. We give each specialist its own learned query, key, and value views, then let training reward useful specializations.

That is **multi-head attention**.

```text
same token representations
   ├── head 1: its own Q, K, V → result 1
   ├── head 2: its own Q, K, V → result 2
   └── head 3: its own Q, K, V → result 3
                         ↓
              preserve and recombine
```

#### Why not average immediately?

Averaging would erase which expert supplied which coordinates before the model can use the distinction. Concatenation keeps their reports separate; a final learned transformation decides how to combine them.

Only now does the compact expression earn its place:

#### The calculation hidden inside multi-head attention

In “The tiger that chased the deer was tired,” one reader follows grammar to discover what *was tired* describes, while another follows reference to keep tiger separate from deer. Averaging their notes too early destroys which evidence came from which question. Keeping the two notes side by side lets a later learned map decide how much grammar and reference the sentence needs.

##### Naming what is already on the table

- **X** is the shared sequence of token representations.
- Each **headₕ** is an independent Q/K/V retrieval space, needed because relationships should not compete in one distribution.
- Concatenation preserves each report instead of averaging distinctions away.
- **H** counts the parallel heads.
- **W_O** is learned because the model must decide how the preserved reports should interact and return to the shared width.

Each head is the query–key–value mechanism from the previous excavation with independent learned projections.

The analogy has limits. Heads do not always become clean, human-readable professions. Some overlap; some are difficult to interpret. The architectural point is parallel relationship spaces, not a promise of tidy labels.

##### Why the melody needs these exact notes

[Concatenation](../MATHEMATICAL_MOVES.md#concatenation) keeps the grammar expert, reference expert, and distance expert side by side. Adding them immediately would erase which head supplied which evidence.
[Multiplication by the output matrix](../MATHEMATICAL_MOVES.md#multiplication) lets the model learn how those preserved expert coordinates should interact; a fixed sum would impose the same mixture everywhere.

The symbols are about to change costume, but their work has appeared before: **the binding loom**—distinct pieces remain side by side instead of being blended away; and **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The long cedar table already contains the complete multi-head attention mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{MultiHead}(X)
=\mathrm{Concat}(\text{head}_1,\ldots,\text{head}_H)W_O
$$

The experts have exchanged information. Each token must now transform what it received into new internal knowledge.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/011-multi-head-attention/README.md).*

---

### Excavation 012 — Feed-Forward Networks

Attention lets tokens communicate. Communication is not the same as thinking.

Imagine several experts place evidence on your desk. You still need to interpret it, combine patterns, and form a new conclusion. In a Transformer, each token needs a private processing step after it gathers information.

#### Failed attempt: stack transformation matrices

Apply one matrix, then another, then another. This looks deep, but if every step is purely linear, the whole chain can be replaced by one matrix. More layers have added notation without adding a new kind of behavior.

The missing ability is to respond differently depending on which patterns are present—to open some paths and close others.

#### A small internal workshop

For each token independently:

1. expand its representation into a wider workspace;
2. allow only some intermediate signals through;
3. recombine the surviving signals back into the shared width.

```text
token → many candidate features → gate → recombined token
```

A simple gate such as ReLU turns negative signals off and leaves positive ones available. Because different inputs activate different intermediate features, the surrounding matrices no longer collapse into one fixed transformation.

Only now does the familiar expression describe an understood machine:

#### The calculation hidden inside feed-forward networks

Attention tells the word *tiger* what the rest of the sentence said. Now imagine several small workshops inside that token: one notices whether an animal is dangerous, another recognizes whether it is acting or being described. A gate closes workshops whose evidence is negative and leaves useful ones open. A second mixing step combines only the surviving discoveries. Without the gate, the two mixing steps collapse into one fixed recipe and no conditional workshop can exist.

##### Naming what is already on the table

- **x** is one token after communication.
- **W₁x+b₁** expands it into candidate features; b₁ lets a feature activate without forcing the boundary through zero.
- **σ** is the nonlinear gate that prevents two linear maps collapsing into one.
- **W₂** recombines active candidates into the model width.
- **b₂** permits an output offset after recombination.

The same workshop is applied separately to every token. It does not communicate across positions; attention already handled that.

```text
attention: who should I hear?
feed-forward: what do I make of what I heard?
```

The phrase “feed-forward” can sound like the entire model. Here it means the position-wise transformation inside each Transformer block.

##### Why the melody needs these exact notes

[Each matrix multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets learned weights decide how strongly one incoming feature should affect each hidden or outgoing feature.
[Adding a bias](../MATHEMATICAL_MOVES.md#addition) lets a detector have a baseline threshold even when all incoming features are zero; multiplication alone must always map zero input to zero output.
[The activation function](../MATHEMATICAL_MOVES.md#function-application) bends the intermediate result. Without that nonlinearity, the two matrix stages collapse into one linear transformation.

Inside feed-forward networks, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for feed-forward networks is now visible on the long cedar table. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathrm{FFN}(\mathbf{x})
=W_2 \sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$

If every workshop completely replaces its input, useful information can be damaged as it passes through many layers. We need a safer way to build depth.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/012-feed-forward-networks/README.md).*

---

### Excavation 013 — Residual Connections

Imagine rewriting an important message fifty times. If every editor replaces the entire document, one poor edit can erase something later editors need.

A deep network faces the same danger. Attention and feed-forward blocks transform a representation repeatedly. Requiring each block to reproduce everything worth keeping while also improving it is an unnecessarily hard job.

#### Failed attempt: trust replacement

Let each layer output a completely new representation. To do nothing useful, the layer must learn a perfect copy operation. Errors compound, and the learning signal must pass through every transformation on its way backward.

#### Let each layer propose a correction

Keep the original stream and ask the block only for a change:

```text
original representation ─────────────┐
        └→ transformation → proposal ├→ add → new representation
```

If the proposal is useful, add it. If no change is needed, a proposal near zero leaves the original intact.

This reconnects directly with Excavation 004: a vector can describe a state, and another vector can describe how that state should change.

Only now do we need the compact rule:

#### The calculation hidden inside residual connections

A cartographer already has a useful map of the forest. A new survey reports that one trail bends half a kilometre east and one kilometre south. Replacing the whole map with that small report would destroy everything known; adding it as a correction preserves the map and changes only the trail. If the survey discovers nothing useful, adding a zero correction leaves the original untouched.

##### Naming what is already on the table

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.

The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) preserves the old message **x** and treats the block as a proposed change **F(x)**. Replacing x would force every block to reconstruct all useful old information.
[F(x)](../MATHEMATICAL_MOVES.md#function-application) says the proposed change depends on this exact incoming representation rather than being one fixed correction for every token.

Trace each operation by touch rather than by name: **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The keeper of words reads the journey of residual connections once more across the long cedar table, then lets the words contract without losing their order:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$

Repeated transformations and additions can make some representations numerically huge and others tiny. The next block needs a more stable working scale.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/013-residual-connections/README.md).*

---

### Excavation 014 — Layer Normalization

Several experts are speaking into a shared system. One whispers; another shouts. Even if both carry useful patterns, the next operation may respond mostly to volume.

Representations drift similarly. After many transformations and residual additions, one token may contain values around `0.01`, another around `100`. Dot products and gates react very differently to those scales.

#### Failed attempt: one global volume knob

A single dataset-wide adjustment cannot respond to the current feature pattern of each token. We want every token to arrive at the next workshop on a predictable scale while preserving the relative pattern inside it.

#### Recenter, then rescale

For one token's feature vector:

1. find its average level;
2. subtract that level from every feature;
3. measure how spread out the centered features are;
4. divide by that spread.

The transformation `[1, 2, 3]` and `[10, 20, 30]` then produces the same normalized pattern. Absolute volume disappears; relative shape remains.

Only after this procedure feels natural do we compress it:

#### The calculation hidden inside layer normalization

Three microphones hear the same roar at volumes 1, 2, and 3 because one sits closer to the tiger. Their shared centre is 2. Subtracting it leaves the pattern `[-1, 0, 1]`: quieter, typical, louder. Dividing by the pattern's spread makes that relative shape comparable with another set recorded by more sensitive microphones. A tiny safety amount is needed when all microphones report the same value and the spread is zero.

##### Naming what is already on the table

- **xᵢ** is one feature of a token and **d** is its number of features.
- Summing and dividing by d creates μ, the token's average level.
- Subtracting μ recenters every feature.
- Squaring centered values prevents cancellation; averaging them creates variance σ².
- The square root converts variance to ordinary scale.
- Dividing produces comparable spread; ε prevents division by zero when no spread exists.
- **x̂ᵢ** is the normalized feature.

The small $\epsilon$ prevents division by zero when every feature is equal.

Forcing every representation to remain permanently standardized would itself be restrictive. Learned scale and shift parameters therefore let the model restore useful volumes and offsets after normalization.

Layer normalization is not intelligence and does not create meaning. It creates stable numerical conditions in which learned transformations can operate.

##### Why the melody needs these exact notes

[Summing and dividing by d](../MATHEMATICAL_MOVES.md#mean) finds the token's average feature level. A raw sum would grow merely because the representation has more coordinates.
[Subtracting the mean](../MATHEMATICAL_MOVES.md#subtraction) asks how each feature differs from this token's centre; addition would move the whole pattern farther from centre.
[Squaring and averaging those differences](../MATHEMATICAL_MOVES.md#variance) measures spread without quieter and louder features cancelling each other.
[The square root](../MATHEMATICAL_MOVES.md#square-root) returns variance to ordinary feature scale, and [division by that spread](../MATHEMATICAL_MOVES.md#division) removes arbitrary volume while preserving relative shape.
- Adding ε is a safety floor: when every feature is identical, spread is zero and division would be undefined. See [addition](../MATHEMATICAL_MOVES.md#addition) and [division](../MATHEMATICAL_MOVES.md#division).

The mandala has curved back upon itself. In this chamber we meet **the chisel**—what is shared is removed so the remaining change can be seen; **the road home**—a squared construction returns to the scale of the world that created it; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Nothing remains unnamed in the layer normalization case on the long cedar table. We can finally trade the long route for its compact map:

$$
\mu=\frac1d\sum_i x_i,
$$

$$
\sigma^2=\frac1d\sum_i(x_i-\mu)^2
$$

$$
\widehat{x}_i=\frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}
$$

We now have the parts of a Transformer, but every matrix begins random. Architecture provides a brain-shaped machine, not knowledge.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/014-layer-normalization/README.md).*

---

### Excavation 015 — How a Dead Brain Learns

Build a complete Transformer with embeddings, attention, feed-forward networks, residual paths, and normalization. Ask it a question.

It answers nonsense.

The instrument exists; the skill does not. Every learned weight began as an arbitrary number.

#### Memorization fails

Show it:

```text
cat eats fish
```

It can store that sequence, but “dog eats ___” exposes the limitation. We need a process that improves on examples and generalizes beyond exact memories.

Prediction provides a relentless exercise. Pause after “The cat sat on the ___.” To succeed consistently, the model must use grammar, context, relationships, and facts. Prediction is not proof of complete understanding, but it puts pressure on useful internal structure.

#### “Wrong” is not precise enough

An arrow landing ten centimeters from a target is different from one landing ten meters away. Learning needs a number saying how bad the current prediction is. We call that number **loss**.

Now imagine loss as height in an enormous landscape. Every model weight is one direction in that landscape. Training wants to move downhill.

#### Random wiggling fails

Change one weight, run the model again, and keep the change if loss improves. With billions of weights, trying directions one at a time is hopeless.

Instead ask, for each weight:

> If I move this number a tiny amount, how does the loss change?

That question—not a symbol—is the derivative. It measures sensitivity. All those sensitivities together form the gradient, a local direction of steepest increase. To reduce loss, move a small step the other way.

Only now does the update rule earn its place:

#### The calculation hidden inside how a dead brain learns

A tiger alarm has one adjustable dial: how strongly a stripe should raise danger. The dial is currently 8, but repeated verified encounters suggest 3 would fit better. Its present squared mistake is 25, and a tiny upward test reveals that increasing the dial makes error rise with sensitivity 10. Reversing one tenth of that uphill suggestion moves the dial from 8 to 7 and lowers the mistake to 16.

##### Naming what is already on the table

- **θ** is the current collection of learnable weights.
- **L** is the measured prediction failure.
- **∇L** collects how increasing each weight would increase loss.
- The minus sign reverses that uphill direction.
- **η** controls step size because direction alone does not say how far to move.
- The arrow means replace the old weights with the improved ones.

$\theta$ is the current state of the weights, $\nabla L$ is a vector of advised change, and $\eta$ controls how large a step to take.

##### Why the melody needs these exact notes

[The gradient](../MATHEMATICAL_MOVES.md#gradient) collects one local loss sensitivity for every adjustable weight so the whole parameter state receives coordinated advice.
[The minus sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses the gradient because the gradient points toward increasing loss and learning wants the locally decreasing direction.
[Multiplying by η](../MATHEMATICAL_MOVES.md#multiplication) chooses how much of that direction to trust. Without η, the gradient's magnitude would dictate the whole step even when it is too large or too small.
- The update arrow means “replace the old parameter state with this new one”; it is an action, not symmetric equality. See [arrows](../MATHEMATICAL_MOVES.md#arrows).

Before the line is compressed, notice its recurring motions: **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The story of how a dead brain learns has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\theta\leftarrow\theta-\eta\nabla L
$$

#### How does blame reach billions of weights?

Trace the prediction backward through the operations. Ask how much each intermediate result contributed to the error, then how much each earlier result contributed to that. Backpropagation is organized blame assignment through the chain of computations.

Each training step is therefore:

```text
predict → measure loss → trace responsibility backward → nudge weights
```

Repeated over enormous amounts of text, small corrections reshape the entire web.

Why should next-token prediction produce grammar, facts, abstraction, or reasoning at all? The answer lies behind the visible words.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/015-learning/README.md).*

---

### Excavation 016 — The Hidden World Behind Words

Walk through a forest and find footprints. Are the footprints the thing you want to understand—or evidence of the animal that made them?

Words are footprints.

#### The shallow explanation

“A language model predicts the next token.” This is technically true, but it describes the measurement task rather than all the structure that can make the task succeed.

Imagine an alien that cannot see Earth and hears only conversations:

```text
it is raining → take an umbrella
the glass fell → it broke
it is sunny → wear sunglasses
```

No one gives the alien a direct lesson on weather, gravity, fragility, or human preferences. Yet a system that predicts these conversations well benefits from representing the regularities that produce them.

#### Failed attempt: memorize every footprint

Memorization can reproduce familiar sentences. It fails when familiar pieces appear in a new arrangement. A smaller set of reusable patterns can explain far more observations: seasons explain many weather reports; “repair” connects programmers fixing bugs, mechanics fixing engines, and doctors treating patients.

Compression favors hidden causes that account for many visible traces.

#### Shadows of one world

A cube casts different shadows when turned. The shadows differ, but one hidden object explains them.

Language behaves similarly:

```text
reality
  ↓
events
  ↓
human thought
  ↓
language
  ↓
tokens visible to the model
```

Training begins at the bottom. Better prediction can pressure the model to infer some of the regularities above it. It is an inverse problem: use visible traces to recover useful hidden structure.

That does not mean a model reconstructs reality perfectly, experiences the world as humans do, or never relies on memorization. Text is incomplete and sometimes false. Many different internal mechanisms can produce the same prediction. The serious claim is narrower: prediction rewards representations of recurring structure when those representations help across many contexts.

#### Why abilities can appear unprogrammed

No engineer labels a single weight “repair,” “gravity,” or “pronoun resolution.” These patterns can become distributed across the network because they reduce many prediction errors together. The useful behavior belongs to the interaction of learned parts, not to an explicitly written rule.

This is **emergence** in the sense established by our expedition: system-level abilities arise from repeated local prediction and correction, even though the abilities were not inserted as separate hand-coded modules.

```text
many examples
    ↓
shared constraints
    ↓
compressed internal structure
    ↓
new general behavior
```

We began with a prehistoric human compressing repeated encounters into patterns. We end with a model compressing repeated linguistic evidence into representations. The scale changed; the archaeological question did not:

> What hidden structure must exist for these observations to make sense together?

#### What we have uncovered

Observations became features. Features became vectors. Vectors became geometry and change. Matrices transformed representations. Context shaped embeddings. Attention retrieved relevant information. Parallel heads followed several relationships. Feed-forward networks processed what was retrieved. Residuals preserved a path, normalization stabilized it, and prediction supplied the pressure to learn.

No equation began the journey. Each one appeared only after a problem made it necessary.

The reconstruction leaves one danger unresolved. A rustle, a footprint, or a sentence can support several hidden stories at once. If the model chooses one and calls it certain, inference becomes guessing with confidence. The next excavation must let several possibilities remain alive and give each only the share of belief the evidence has earned.

#### When measurements learned to listen

The instruments of Part I have changed character. Vectors no longer describe only bodies; they hold fragments of meaning. A dot product is no longer only geometry; it becomes relevance. Weighted sums become attention, and layered corrections become a Transformer. The old mathematics did not disappear. It learned a new song.

```text
geometry → relevance → attention → context → emergence
```

The trail called *when measurements learned to listen* is what remains when one necessity becomes another.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/016-emergence/README.md).*

---

## Part III — Learning from Error

The Transformer can construct a useful interpretation, but it cannot honestly pretend that every interpretation is certain. Footprints, words, and predictions all leave several possible stories alive. The expedition now needs a way to preserve uncertainty, price error, trace responsibility, and let error alter the machine.

---

### Excavation 017 — Probability — Counting What We Do Not Know

The Transformer has begun to infer hidden causes from the footprints of language. But inference without certainty is dangerous: the same rustle may have been made by a tiger, a deer, or only the wind.

Morning reaches the Lantern Observatory before anyone has a name for today's difficulty. Beside the ring of glass lanterns, the keeper of uncertain stories tries the smallest continuation of what already works: choose the most common cause and declare certainty.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: this works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   choose the most common cause and… this works until the rare tiger…
            \        /
             \      /
              keep every plausible outcome and give…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: this works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act. The cover is lifted, restoring the ability to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason probability exists.

What must change for probability is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total. That threshold is where **Probability** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In probability, that memory takes a precise form: whenever this works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act, preserve enough structure to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total. Every lantern in probability remembers an older operation. Probability keeps several stories lit; logarithms turn compounded uncertainty into steps; summation lets separate surprises form one account. Learning begins when those lights can alter the machine that reads them.

#### The calculation hidden inside probability

The keeper of uncertain stories carries the probability scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

##### Naming what is already on the table

**A** is the uncertain event we need to discuss.
The numerator counts observations where A occurred.
The denominator counts all comparable opportunities, because an isolated count has no scale.
Division turns the count into a share between zero and one.
**P(A)** names that evidence-dependent share, not a guarantee.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) turns a tiger count into a share of comparable encounters. The count alone grows when we watch longer even if the underlying chance is unchanged.
[Probability](../MATHEMATICAL_MOVES.md#probability) preserves several possible causes as parts of one whole instead of forcing certainty from incomplete evidence.

The calculation borrows several gestures already encountered elsewhere: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. probability feels new because the objects are new; the gestures remain recognizably human.

The ring of glass lanterns already contains the complete probability mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$

#### Probability beyond this one case

Probability is a weather forecast: not a promise, but an honest description of uncertainty that can still guide action.

#### Where probability runs out

Probabilities depend on evidence and assumptions. When new evidence arrives, the shares must change.

Here the new path ends honestly. Probability can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the ring of glass lanterns

Rebuild the probability scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/017-probability/README.md).*

---

### Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: ask which story is generally more believable.

For a moment the mark looks complete. Then the evidence refuses to fit: that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ ask which story is generally more… ──▶ that ignores the actual print. Or ask…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ reverse the question: if this story… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “ask which story is generally more believable.” Its path ends where that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge. The second receives the same evidence but is allowed to reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. Held to the light, the sheets separate at exactly one decision.

No one reaches for a likelihood formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. When the ink dries, the name **Likelihood** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge, while the other can reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. That fork—not the vocabulary—is where likelihood lives.

#### The calculation hidden inside likelihood

The keeper of uncertain stories carries the likelihood scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

##### Naming what is already on the table

**θ** is one proposed hidden explanation.
**x** is the evidence already observed.
The vertical bar means “under the assumption that.”
**P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
**L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

##### Why the melody needs these exact notes

[The conditional bar](../MATHEMATICAL_MOVES.md#conditional-bar) deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.
[Equality](../MATHEMATICAL_MOVES.md#equals) renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.

Every mark needed for likelihood is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

#### Likelihood beyond this one case

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

#### Where likelihood runs out

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

At the Lantern Observatory, the keeper of uncertain stories leaves a blank beneath the new mark. Likelihood has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the ring of glass lanterns

Rebuild the likelihood scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/018-likelihood/README.md).*

---

### Excavation 019 — Information — Why Surprise Needs a Number

Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: measure information by message length.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add. More confidence cannot repair information that never entered the rule.

*The keeper of uncertain stories sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ measure information by message length ──▶ blurred: a long predictable greeting can…
      │
      └── new lens ──▶ we need rare events to carry more… ──▶ distinction survives
```

Two trails now cross the ring of glass lanterns. The pale trail bears the instruction “measure information by message length.” It disappears into the observed failure: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add. The darker trail carries one additional capacity—to we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed information mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the ring of glass lanterns is altered in exactly one way: we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. Much later, people will call this territory **Information**. Here the name is only a memory of the failure it can survive.

The ring of glass lanterns has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and information looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### The calculation hidden inside information

The keeper of uncertain stories carries the information scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

##### Naming what is already on the table

**P(x)** measures how expected observation x was.
The logarithm is needed because independent probabilities multiply while information from independent messages should add.
Probabilities below one have negative logs, so the minus sign makes information nonnegative.
A certain event has P=1 and therefore zero information; rarer events receive more.

##### Why the melody needs these exact notes

[The logarithm](../MATHEMATICAL_MOVES.md#logarithm) is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.
[The negative sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.
Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.

The symbols are about to change costume, but their work has appeared before: **the spiral stair**—compounded chances become steps that can be accumulated; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. This is how distant excavations begin to sound like variations of one melody.

The keeper of uncertain stories reads the journey of information once more across the ring of glass lanterns, then lets the words contract without losing their order:

$$
I(x)=-\log P(x)
$$

#### Information beyond this one case

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

#### Where information runs out

Information depends on the probability model. A surprise to one observer may be expected to another.

The ring of glass lanterns answers today's question and falls silent at the next. That silence is precise: Information was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the ring of glass lanterns

Rebuild the information scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/019-information/README.md).*

---

### Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.

Inside the Lantern Observatory, every old tool is given one honest chance. The keeper of uncertain stories sets the ring of glass lanterns between the evidence and the desired answer, then tries to count the number of outcomes.

Reality answers without terminology: both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: count the number of outcomes
possible road B ─┘              └── loses: both bags contain stones, and both…

same roads ──▶ repaired map ──▶ average the information of every…
```

The ring of glass lanterns is divided down the middle. Left side: “count the number of outcomes.” Its final mark records both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. Right side: the same starting evidence, now allowed to average the information of every possible outcome, weighted by how often that outcome occurs. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given entropy a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: average the information of every possible outcome, weighted by how often that outcome occurs. The name **Entropy** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to count the number of outcomes; on the other lies the observed fact that both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. The bridge called entropy has exactly the planks needed to average the information of every possible outcome, weighted by how often that outcome occurs.

#### The calculation hidden inside entropy

The keeper of uncertain stories carries the entropy scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

##### Naming what is already on the table

**pᵢ** is the probability of possible outcome i.
**−log pᵢ** is the information received if i occurs.
Multiplying by pᵢ weights that surprise by how often it is expected to occur.
Summing over every i computes average surprise before the outcome is known.
**H(P)** names uncertainty of the whole distribution P.

##### Why the melody needs these exact notes

[Multiplying each surprise by pᵢ](../MATHEMATICAL_MOVES.md#multiplication) lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.
[Summing](../MATHEMATICAL_MOVES.md#summation) combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.
[The log](../MATHEMATICAL_MOVES.md#logarithm) still converts probability products into additive information, and [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) keeps that information nonnegative.

Inside entropy, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the spiral stair**—compounded chances become steps that can be accumulated. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the entropy case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
H(P)=-\sum_i p_i\log p_i
$$

#### Entropy beyond this one case

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

#### Where entropy runs out

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

A final test reaches beyond the new instrument. It does not refute Entropy; it reveals the edge of what was constructed. The keeper of uncertain stories carries that edge into the following room.

#### Return to the ring of glass lanterns

Rebuild the entropy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/020-entropy/README.md).*

---

### Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.

A new case arrives at the Lantern Observatory, but the keeper of uncertain stories first reaches for the familiar ring of glass lanterns. Its promise is simple: use zero for correct and one for wrong.

Then the quiet test arrives: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: use zero for correct and one for wrong
                         │
                         └── mismatch: it treats barely wrong and…

reference evidence ──▶ measured repair: charge the information cost assigned…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, use zero for correct and one for wrong, the evidence ends in the same contradiction: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction. A second engraving adds only the power to charge the information cost assigned by the predicted distribution to the outcome that actually occurred. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two cross-entropy cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The keeper of uncertain stories writes **Cross-Entropy** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories does not memorize cross-entropy. Instead, the keeper of uncertain stories memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The formal name merely lets that motion be shared.

#### The calculation hidden inside cross-entropy

The keeper of uncertain stories carries the cross-entropy scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

##### Naming what is already on the table

**P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
**Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
**−log qᵢ** makes confident neglect extremely costly.
Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

##### Why the melody needs these exact notes

[−log qᵢ](../MATHEMATICAL_MOVES.md#logarithm) charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.
[Multiplying by pᵢ](../MATHEMATICAL_MOVES.md#multiplication) asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.
[The sum](../MATHEMATICAL_MOVES.md#summation) forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.

Trace each operation by touch rather than by name: **the spiral stair**—compounded chances become steps that can be accumulated; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they form the smallest mechanism that survives the counterexample.

The story of cross-entropy has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$

#### Cross-Entropy beyond this one case

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

#### Where cross-entropy runs out

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

One unsolved mark remains on the ring of glass lanterns. None of the responsibilities inside Cross-Entropy can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the ring of glass lanterns

Rebuild the cross-entropy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/021-cross-entropy/README.md).*

---

### Excavation 022 — Derivatives — Asking One Weight What It Changed

Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.

The doors of the Lantern Observatory close against the wind. On the ring of glass lanterns, the keeper of uncertain stories writes the cheapest rule that might still be true: try a large jump and keep it if loss falls.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: large jumps can leap over improvements. Try every possible value; there are infinitely many. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[try a large jump and keep it if loss…]
    │
    ╳  large jumps can leap over…
    │
    ▼
[nudge the weight by a tiny amount,…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “try a large jump and keep it if loss falls”; the other knows how to nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero. When the failure—large jumps can leap over improvements. Try every possible value; there are infinitely many—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to derivatives. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero. This problem and its repair will travel under the name **Derivatives**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—try a large jump and keep it if loss falls? The answer remains large jumps can leap over improvements. Try every possible value; there are infinitely many. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### The calculation hidden inside derivatives

The keeper of uncertain stories carries the derivatives scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

##### Naming what is already on the table

**w** is the one weight whose responsibility we are probing.
**ε** is a small experimental nudge.
**L(w+ε)−L(w)** measures the loss change caused by that nudge.
Dividing by ε turns total change into change per unit of weight.
The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
**dL/dw** names that local sensitivity.

##### Why the melody needs these exact notes

[The numerator subtracts](../MATHEMATICAL_MOVES.md#subtraction) old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.
[Division by the weight nudge](../MATHEMATICAL_MOVES.md#division) converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.
[The limit](../MATHEMATICAL_MOVES.md#limit) lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.

The mandala has curved back upon itself. In this chamber we meet **the chisel**—what is shared is removed so the remaining change can be seen; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about derivatives and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

#### Derivatives beyond this one case

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

#### Where derivatives runs out

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

The derivatives repair holds, but the world asks for something it was never given. At the Lantern Observatory, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the ring of glass lanterns

Rebuild the derivatives scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/022-derivatives/README.md).*

---

### Excavation 023 — The Chain Rule — Following One Change Through Many Machines

A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.

Nothing in the Lantern Observatory yet bears today's mathematical name. There is only the keeper of uncertain stories, the ring of glass lanterns, and one plausible action: measure only the first effect or only the final effect.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   measure only the first effect or only… either breaks the causal path.…
            \        /
             \      /
              we need to multiply local…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work. The cover is lifted, restoring the ability to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason chain rule exists.

What must change for chain rule is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward. That threshold is where **The Chain Rule** enters the story.

The marks on the ring of glass lanterns form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. chain rule is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### The calculation hidden inside the chain rule

The keeper of uncertain stories carries the chain rule scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

##### Naming what is already on the table

**w→x→y→L** is the causal path through successive machines.
Each fraction is one local sensitivity: how its output changes when its input changes.
Multiplication is forced because a change is scaled at every link it traverses.
The product gives the effect of w on L without pretending they touch directly.

##### Why the melody needs these exact notes

Each [derivative](../MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
[Multiplying the rates](../MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

Before the line is compressed, notice its recurring motions: **the whispered question**—the present slope answers how a tiny movement would alter the outcome; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The ring of glass lanterns already contains the complete chain rule mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

#### The Chain Rule beyond this one case

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

#### Where the chain rule runs out

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

Here the new path ends honestly. Chain Rule can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the ring of glass lanterns

Rebuild the chain rule scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/023-chain-rule/README.md).*

---

### Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.

At the Lantern Observatory, the keeper of uncertain stories returns to the ring of glass lanterns. Yesterday's instrument still lies open, so the first move asks for no new magic: perturb each weight and rerun the model.

For a moment the mark looks complete. Then the evidence refuses to fit: this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ perturb each weight and rerun the… ──▶ this needs at least one extra forward…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ compute the prediction once, remember… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “perturb each weight and rerun the model.” Its path ends where this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again. The second receives the same evidence but is allowed to compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. Held to the light, the sheets separate at exactly one decision.

No one reaches for a backpropagation formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. When the ink dries, the name **Backpropagation** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The ring of glass lanterns keeps both histories. Its older mark still says, ‘perturb each weight and rerun the model’; beside it, the newer mark says, ‘compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.’ The distance between those sentences is the exact shape of backpropagation: no larger than the failure required, and no smaller than reality permits.

#### The calculation hidden inside backpropagation

The keeper of uncertain stories carries the backpropagation scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

##### Naming what is already on the table

**x̄** means accumulated sensitivity of final loss to intermediate x.
A node can influence several child results y, so every downstream path must contribute.
**ȳ** is blame already accumulated at child y.
**∂y/∂x** says how strongly x affected that child locally.
Multiplication passes blame through one edge; summation combines all outgoing paths.

##### Why the melody needs these exact notes

[The partial derivative](../MATHEMATICAL_MOVES.md#partial-derivative) measures one local edge while other inputs are held fixed.
[Multiplying child blame by edge sensitivity](../MATHEMATICAL_MOVES.md#multiplication) passes downstream responsibility through that edge; either factor being zero should block that path.
[Summing over children](../MATHEMATICAL_MOVES.md#summation) reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.

Listen beneath backpropagation: **the whispered question**—one decision is asked what would change if only it moved; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for backpropagation is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

#### Backpropagation beyond this one case

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

#### Where backpropagation runs out

Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.

At the Lantern Observatory, the keeper of uncertain stories leaves a blank beneath the new mark. Backpropagation has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the ring of glass lanterns

Rebuild the backpropagation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/024-backpropagation/README.md).*

---

### Excavation 025 — Gradient Descent — Teaching a Tiny Network

Backpropagation can now return one local sensitivity to every adjustable weight. Sensitivity is advice, not learning: the network still needs a rule that turns millions of local directions into a new parameter state.

Morning reaches the Lantern Observatory before anyone has a name for today's difficulty. Beside the ring of glass lanterns, the keeper of uncertain stories tries the smallest continuation of what already works: jump directly opposite the gradient with no step control; the model may overshoot and diverge.

The rule survives the easy cases. The next case leaves a crack through the middle of it: take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another. More confidence cannot repair information that never entered the rule.

*The keeper of uncertain stories sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ jump directly opposite the gradient… ──▶ blurred: take microscopic steps; learning may…
      │
      └── new lens ──▶ move every parameter a controlled… ──▶ distinction survives
```

Two trails now cross the ring of glass lanterns. The pale trail bears the instruction “jump directly opposite the gradient with no step control; the model may overshoot and diverge.” It disappears into the observed failure: take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another. The darker trail carries one additional capacity—to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed gradient descent mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the ring of glass lanterns is altered in exactly one way: move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. Much later, people will call this territory **Gradient Descent**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the ring of glass lanterns. The failed path remains visible beneath the repair, because gradient descent is easier to remember when its scar remains attached to it. The scar reads, ‘take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another’; the new line exists only to keep that loss from happening again.

#### The calculation hidden inside gradient descent

The keeper of uncertain stories carries the gradient descent scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

##### Naming what is already on the table

**θ_t** packages the current weights; our tiny example has only 8.
**L** is the mistake measure; here it is (weight − 3)².
**∇_θL** packages local sensitivities; our example has only 10.
The minus sign reverses the uphill direction.
**η** is the chosen fraction of the correction; here it is 0.1.
**t** means before this correction; **t+1** means after it.

Substitute real values before compact symbols:

~~~text
next weight = current weight - learning rate × uphill sensitivity
            = 8              - 0.1           × 10
            = 7
~~~

##### Why the melody needs these exact notes

[The time indices](../MATHEMATICAL_MOVES.md#indices) distinguish the parameter state before update t from the state after it.
[The gradient](../MATHEMATICAL_MOVES.md#gradient) supplies one local uphill sensitivity for each parameter; [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses that direction toward lower loss.
[Multiplying by η](../MATHEMATICAL_MOVES.md#multiplication) supplies the missing travel distance. A direction alone does not say whether to move one millimetre or one kilometre.

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$

#### Gradient Descent beyond this one case

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

#### Where gradient descent runs out

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

The ring of glass lanterns answers today's question and falls silent at the next. That silence is precise: Gradient Descent was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the ring of glass lanterns

Rebuild the gradient descent scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/025-gradient-descent/README.md).*

---

### Excavation 026 — Mini-Batches — Learning from More Than One Example

Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: use one example per update.

Reality answers without terminology: it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: use one example per update
possible road B ─┘              └── loses: it is fast, but noisy accidents…

same roads ──▶ repaired map ──▶ average the evidence from a small…
```

The ring of glass lanterns is divided down the middle. Left side: “use one example per update.” Its final mark records it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. Right side: the same starting evidence, now allowed to average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given mini-batches a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. The name **Mini-Batches** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from mini-batches through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### The calculation hidden inside mini-batches

The keeper of uncertain stories carries the mini-batches scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

##### Naming what is already on the table

**B** is the selected mini-batch and **|B|** its number of examples.
**Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
Summing combines the witnesses.
Dividing by batch size prevents merely using more examples from making the step proportionally larger.
**g_B** is the batch's less noisy gradient estimate.

##### Why the melody needs these exact notes

[The sum](../MATHEMATICAL_MOVES.md#summation) lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.
[Dividing by |B|](../MATHEMATICAL_MOVES.md#division) asks for advice per example, so merely inviting twice as many witnesses does not double the update.
[i ∈ B](../MATHEMATICAL_MOVES.md#membership) restricts the sum to examples actually selected for this mini-batch; [|B|](../MATHEMATICAL_MOVES.md#cardinality) means the number of those examples.

Three old motions cast new shadows here: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Nothing remains unnamed in the mini-batches case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

#### Mini-Batches beyond this one case

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

#### Return to the ring of glass lanterns

Rebuild the mini-batches scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/026-mini-batches/README.md).*

---

### Excavation 027 — Learning Rate — How Large Should the Next Step Be?

A mini-batch replaces one noisy witness with the average advice of a small council. The council can point downhill, but its vote still says nothing about how far the network should move.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: always take a huge step: leap across the valley and oscillate.

Then the quiet test arrives: always take a microscopic step: improve so slowly that the expedition ends first. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: always take a huge step: leap across…
                         │
                         └── mismatch: always take a microscopic step:…

reference evidence ──▶ measured repair: we need to multiply the gradient by a…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, always take a huge step: leap across the valley and oscillate, the evidence ends in the same contradiction: always take a microscopic step: improve so slowly that the expedition ends first. A second engraving adds only the power to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two learning rate cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. The keeper of uncertain stories writes **Learning Rate** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories places a finger over the new distinction. At once the two cases collapse and always take a microscopic step: improve so slowly that the expedition ends first. Lifting the finger restores only this capacity: multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. That tiny reversible motion is the chapter's proof of necessity.

#### The calculation hidden inside learning rate

The keeper of uncertain stories carries the learning rate scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

##### Naming what is already on the table

**g_t** is the downhill evidence measured at step t.
**η_t** converts direction into a chosen travel distance and may change with time.
The minus sign moves against increasing loss.
**θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.

##### Why the melody needs these exact notes

[gₜ](../MATHEMATICAL_MOVES.md#gradient) gives direction but not distance.
[Multiplying by ηₜ](../MATHEMATICAL_MOVES.md#multiplication) turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.
[Subtraction](../MATHEMATICAL_MOVES.md#negative-sign) moves opposite the locally uphill gradient rather than making loss rise faster.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. This is how distant excavations begin to sound like variations of one melody.

The story of learning rate has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

#### Learning Rate beyond this one case

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

#### Return to the ring of glass lanterns

Rebuild the learning rate scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/027-learning-rate/README.md).*

---

### Excavation 028 — Momentum — Remembering Which Way Downhill Persists

The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.

Inside the Lantern Observatory, every old tool is given one honest chance. The keeper of uncertain stories sets the ring of glass lanterns between the evidence and the desired answer, then tries to obey only the newest gradient.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[obey only the newest gradient]
    │
    ╳  sideways noise repeatedly cancels…
    │
    ▼
[keep a fading memory of past…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “obey only the newest gradient”; the other knows how to keep a fading memory of past gradients and combine it with the new one. When the failure—sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to momentum. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: keep a fading memory of past gradients and combine it with the new one. This problem and its repair will travel under the name **Momentum**, but the name carries no knowledge the scene has not earned.

What changed on the ring of glass lanterns can be said without symbols. Before, the method could only obey only the newest gradient; now it can also keep a fading memory of past gradients and combine it with the new one. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### The calculation hidden inside momentum

The keeper of uncertain stories carries the momentum scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

##### Naming what is already on the table

**g_t** is the newest noisy gradient.
**v_{t−1}** stores direction accumulated previously.
**β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
Addition combines memory with new evidence into velocity v_t.
**η** scales that velocity before it changes θ.

##### Why the melody needs these exact notes

[Multiplying old velocity by β](../MATHEMATICAL_MOVES.md#multiplication) fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.
[Adding the new gradient](../MATHEMATICAL_MOVES.md#addition) lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.
The final [η scaling](../MATHEMATICAL_MOVES.md#multiplication) chooses travel distance and [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) turns remembered uphill direction into a downhill update.

Inside momentum, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the joining river**—separate contributions meet without losing where they came from; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about momentum and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

#### Momentum beyond this one case

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

#### Return to the ring of glass lanterns

Rebuild the momentum scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/028-momentum/README.md).*

---

### Excavation 029 — Initialization — Where Should Learning Begin?

Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.

A new case arrives at the Lantern Observatory, but the keeper of uncertain stories first reaches for the familiar ring of glass lanterns. Its promise is simple: set every weight to zero.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   set every weight to zero   neurons receive identical evidence…
            \        /
             \      /
              draw small random weights whose scale…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate. The cover is lifted, restoring the ability to draw small random weights whose scale depends on how many inputs feed the neuron, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason initialization exists.

What must change for initialization is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: draw small random weights whose scale depends on how many inputs feed the neuron. That threshold is where **Initialization** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In initialization, that memory takes a precise form: whenever neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate, preserve enough structure to draw small random weights whose scale depends on how many inputs feed the neuron.

#### The calculation hidden inside initialization

The keeper of uncertain stories carries the initialization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

##### Naming what is already on the table

**w** is one newly initialized weight.
**Var(w)** measures the typical squared spread of starting weights, not their meaning.
**n_in** counts signals entering the neuron.
Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
“Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

##### Why the melody needs these exact notes

[Variance](../MATHEMATICAL_MOVES.md#variance) describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.
[Dividing by the number of incoming signals](../MATHEMATICAL_MOVES.md#division) makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.
[The approximately sign](../MATHEMATICAL_MOVES.md#approximation) admits a design target rather than claiming every finite random sample has exactly this variance; see [equality](../MATHEMATICAL_MOVES.md#equals) for the stronger claim it avoids.

Trace each operation by touch rather than by name: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they form the smallest mechanism that survives the counterexample.

The ring of glass lanterns already contains the complete initialization mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

#### Initialization beyond this one case

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

#### Return to the ring of glass lanterns

Rebuild the initialization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/029-initialization/README.md).*

---

### Excavation 030 — Activation Functions — Why a Network Must Bend

Careful initialization keeps early signals alive and breaks symmetry. But a tower made only from linear transformations still collapses algebraically into one linear transformation, no matter how many layers we stack.

The doors of the Lantern Observatory close against the wind. On the ring of glass lanterns, the keeper of uncertain stories writes the cheapest rule that might still be true: add more linear layers.

For a moment the mark looks complete. Then the evidence refuses to fit: depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ add more linear layers ──▶ depth increases, but expressive power…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ place an activation after a linear… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “add more linear layers.” Its path ends where depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient. The second receives the same evidence but is allowed to place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. Held to the light, the sheets separate at exactly one decision.

No one reaches for a activation functions formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. When the ink dries, the name **Activation Functions** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient, while the other can place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. That fork—not the vocabulary—is where activation functions lives.

#### The calculation hidden inside activation functions

The keeper of uncertain stories carries the activation functions scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

##### Naming what is already on the table

**x** is the incoming representation.
**W** mixes its features; **b** permits learned thresholds and offsets.
**φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
**h** is the hidden representation after both mixing and gating.

##### Why the melody needs these exact notes

[Wx](../MATHEMATICAL_MOVES.md#multiplication) lets every learned input weight scale and mix its matching feature; [adding b](../MATHEMATICAL_MOVES.md#addition) supplies a learnable baseline.
[Applying φ](../MATHEMATICAL_MOVES.md#function-application) bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for activation functions is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
h=\phi(Wx+b)
$$

#### Activation Functions beyond this one case

A railway switch changes which route a signal can take. Without switches, many track segments still form only one fixed route.

#### Return to the ring of glass lanterns

Rebuild the activation functions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/030-activation-functions/README.md).*

---

### Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

Activation gates let the network bend and build conditional internal paths. That flexibility also makes a new deception possible: the machine can reproduce every training example without learning what should survive beyond them.

Nothing in the Lantern Observatory yet bears today's mathematical name. There is only the keeper of uncertain stories, the ring of glass lanterns, and one plausible action: celebrate zero training error.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail. More confidence cannot repair information that never entered the rule.

*The keeper of uncertain stories sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ celebrate zero training error ──▶ blurred: the model may have memorized…
      │
      └── new lens ──▶ we need to reserve unseen cases and… ──▶ distinction survives
```

Two trails now cross the ring of glass lanterns. The pale trail bears the instruction “celebrate zero training error.” It disappears into the observed failure: the model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail. The darker trail carries one additional capacity—to reserve unseen cases and compare training success with performance outside the training memory. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed overfitting mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the ring of glass lanterns is altered in exactly one way: we need to reserve unseen cases and compare training success with performance outside the training memory. Much later, people will call this territory **Overfitting**. Here the name is only a memory of the failure it can survive.

The ring of glass lanterns has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and overfitting looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### The calculation hidden inside overfitting

The keeper of uncertain stories carries the overfitting scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

##### Naming what is already on the table

**L_train** measures error on examples allowed to shape the model.
**L_unseen** measures error on held-out observations.
Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
A positive generalization gap is evidence that training success did not fully survive.

##### Why the melody needs these exact notes

[Unseen loss minus training loss](../MATHEMATICAL_MOVES.md#subtraction) isolates how much performance deteriorates beyond memorized examples. Adding the losses would measure total error, not the transfer gap.
The order matters: a positive answer naturally means unseen cases are worse. Reversing the subtraction would reverse that interpretation.

Before the line is compressed, notice its recurring motions: **the chisel**—what is shared is removed so the remaining change can be seen. They are the handholds by which the reader can later climb back from notation to meaning.

The keeper of uncertain stories reads the journey of overfitting once more across the ring of glass lanterns, then lets the words contract without losing their order:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

#### Overfitting beyond this one case

A student who memorizes answer positions can ace the practice sheet and fail when the same ideas are rearranged.

#### Return to the ring of glass lanterns

Rebuild the overfitting scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/031-overfitting/README.md).*

---

### Excavation 032 — Regularization — Making Memorization More Expensive

Overfitting reveals that low training error can be perfect memory wearing the costume of intelligence. The learner therefore needs pressure against fragile, unnecessarily extreme explanations.

At the Lantern Observatory, the keeper of uncertain stories returns to the ring of glass lanterns. Yesterday's instrument still lies open, so the first move asks for no new magic: forbid complexity by making the model too small; it may lose real structure too.

Reality answers without terminology: stop training at an arbitrary time without observing unseen performance. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: forbid complexity by making the model…
possible road B ─┘              └── loses: stop training at an arbitrary time…

same roads ──▶ repaired map ──▶ add a cost for large weights, remove…
```

The ring of glass lanterns is divided down the middle. Left side: “forbid complexity by making the model too small; it may lose real structure too.” Its final mark records stop training at an arbitrary time without observing unseen performance. Right side: the same starting evidence, now allowed to add a cost for large weights, remove random paths during training, or stop when validation performance stops improving. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given regularization a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: add a cost for large weights, remove random paths during training, or stop when validation performance stops improving. The name **Regularization** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to forbid complexity by making the model too small; it may lose real structure too; on the other lies the observed fact that stop training at an arbitrary time without observing unseen performance. The bridge called regularization has exactly the planks needed to add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

#### The calculation hidden inside regularization

The keeper of uncertain stories carries the regularization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

##### Naming what is already on the table

**L_data** rewards fitting observations.
**θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
**λ** expresses how strongly we prefer smaller machinery relative to data fit.
Addition forces training to negotiate prediction accuracy and complexity in one objective.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.
[The squared norm](../MATHEMATICAL_MOVES.md#norm) combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.
[λ scales the penalty](../MATHEMATICAL_MOVES.md#multiplication) because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.

Listen beneath regularization: **the joining river**—separate contributions meet without losing where they came from; and **the lock and key**—one influence matters through another, and either missing factor can close the path. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Nothing remains unnamed in the regularization case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

#### Regularization beyond this one case

A map that explains every pebble with a separate rule is less trustworthy than one road system that explains many journeys.

#### Return to the ring of glass lanterns

Rebuild the regularization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/032-regularization/README.md).*

---

### Excavation 033 — Validation — Testing Without Peeking at the Final Exam

Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.

Morning reaches the Lantern Observatory before anyone has a name for today's difficulty. Beside the ring of glass lanterns, the keeper of uncertain stories tries the smallest continuation of what already works: use training loss for every choice; it rewards memorization.

Then the quiet test arrives: check the test set repeatedly; every decision leaks test information back into development. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: use training loss for every choice;…
                         │
                         └── mismatch: check the test set repeatedly; every…

reference evidence ──▶ measured repair: split data by role: training changes…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, use training loss for every choice; it rewards memorization, the evidence ends in the same contradiction: check the test set repeatedly; every decision leaks test information back into development. A second engraving adds only the power to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two validation cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. The keeper of uncertain stories writes **Validation** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories does not memorize validation. Instead, the keeper of uncertain stories memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. The formal name merely lets that motion be shared.

#### The calculation hidden inside validation

The keeper of uncertain stories carries the validation scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

##### Naming what is already on the table

**D** is all available data.
The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
Union means they reconstruct the available collection.
The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

##### Why the melody needs these exact notes

[Union](../MATHEMATICAL_MOVES.md#union) says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.
Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.

The story of validation has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

#### Validation beyond this one case

A practice exam guides study. A sealed final exam measures what survived without feedback.

#### Return to the ring of glass lanterns

Rebuild the validation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/033-validation/README.md).*

---

### Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

Validation lets us choose among models without opening the sealed test set. Even an honest test can come from yesterday's hospital, dialect, season, or camera while tomorrow arrives from somewhere else.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: assume all future observations come from exactly the same source as training.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: or demand good performance on every imaginable world, which no finite evidence can guarantee. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[assume all future observations come…]
    │
    ╳  or demand good performance on every…
    │
    ▼
[state the deployment world, test…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “assume all future observations come from exactly the same source as training”; the other knows how to state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts. When the failure—or demand good performance on every imaginable world, which no finite evidence can guarantee—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to generalization. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts. This problem and its repair will travel under the name **Generalization**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—assume all future observations come from exactly the same source as training? The answer remains or demand good performance on every imaginable world, which no finite evidence can guarantee. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### The calculation hidden inside generalization

The keeper of uncertain stories carries the generalization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but no benchmark proves universal intelligence. Future distributions can change in ways neither data nor designers anticipated.

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

##### Naming what is already on the table

**θ** is one trained model and **f_θ(x)** its prediction for input x.
**L(f_θ(x),y)** measures failure against outcome y.
**P_future** names the deployment world we actually care about.
Sampling (x,y) from that world prevents training data from silently defining success.
The expectation averages loss over future cases; **R(θ)** names that future risk.

##### Why the melody needs these exact notes

[Expectation](../MATHEMATICAL_MOVES.md#expectation) weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.
[fθ(x)](../MATHEMATICAL_MOVES.md#function-application) feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.
The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.

Three old motions cast new shadows here: **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Cover the prose about generalization and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

#### Generalization beyond this one case

A boat tested on one calm lake has not proved itself at sea. We must name the waters we expect it to cross.

#### Return to the ring of glass lanterns

Rebuild the generalization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/034-generalization/README.md).*

---

### Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: hide everything behind a framework call.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   hide everything behind a framework… the code runs, but the causal chain…
            \        /
             \      /
              we need to build a two-layer network,…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: the code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning. The cover is lifted, restoring the ability to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason tiny neural network exists.

What must change for tiny neural network is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data. That threshold is where **A Tiny Neural Network** enters the story.

The marks on the ring of glass lanterns form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. tiny neural network is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### The calculation hidden inside a tiny neural network

The keeper of uncertain stories carries the tiny neural network scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

##### Naming what is already on the table

**x** is observed input.
**Wx+b** mixes features and supplies offsets.
**φ** bends the mapping so depth adds new behavior.
**ŷ** is the prediction and **L** measures its failure.
**∇_θL** assigns local correction directions to all parameters θ.
**θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

##### Why the melody needs these exact notes

[Arrows](../MATHEMATICAL_MOVES.md#arrows) preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.
[The gradient stage](../MATHEMATICAL_MOVES.md#gradient) changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.

The ring of glass lanterns already contains the complete tiny neural network mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

#### A Tiny Neural Network beyond this one case

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

#### The circle that teaches itself

Uncertainty became information; information became loss; loss became local sensitivity; sensitivities flowed backward; and a chosen step changed the machine. The circle is closed only because every arrow can be walked in ordinary language.

```text
prediction → surprise → loss → blame → update → new prediction
```

The trail called *the circle that teaches itself* is what remains when one necessity becomes another.

#### Return to the ring of glass lanterns

Rebuild the tiny neural network scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/035-tiny-neural-network/README.md).*

---

## Part IV — Building a Tiny GPT

The learner can change its weights when examples are already numerical. Real language does not arrive that way. We now follow one sentence from raw characters to tokens, positions, honest prediction lessons, vocabulary probabilities, and finally generation.

---

### Excavation 036 — Tokenization: What Can a Language Model See?

The tiny neural network now learns from numbered examples. People do not speak in fixed numerical columns; they produce an open stream of words, punctuation, names, code, and writing systems.

Inside the Clockwork Scriptorium, every old tool is given one honest chance. The mechanist sets the sentence-wheel between the evidence and the desired answer, then tries to give every complete word one ID.

For a moment the mark looks complete. Then the evidence refuses to fit: spaces appear to provide the boundaries. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The mechanist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ give every complete word one ID ──▶ blurred: spaces appear to provide the…
      │
      └── new lens ──▶ use characters. Any new spelling can… ──▶ distinction survives
```

The mechanist lays two translucent sheets over the sentence-wheel. The first is inscribed, “give every complete word one ID.” Its path ends where spaces appear to provide the boundaries. The second receives the same evidence but is allowed to use characters. Any new spelling can now be represented. Held to the light, the sheets separate at exactly one decision.

No one reaches for a tokenization formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The mechanist changes only that one responsibility: use characters. Any new spelling can now be represented. When the ink dries, the name **Tokenization** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The sentence-wheel keeps both histories. Its older mark still says, ‘give every complete word one ID’; beside it, the newer mark says, ‘use characters. Any new spelling can now be represented.’ The distance between those sentences is the exact shape of tokenization: no larger than the failure required, and no smaller than reality permits. The sentence-wheel turns with machinery earned long before language: indices retrieve, vectors carry features, dot products compare directions, and weighted sums gather context. tokenization changes what travels through the machine, not why those operations exist.

#### The calculation hidden inside tokenization

The mechanist carries the tokenization scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

##### Naming what is already on the table

**a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
The star marks the pair selected for merging.
**arg max** returns the pair itself, not its count, because that pair must be replaced.
Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

##### Why the melody needs these exact notes

[The first equality](../MATHEMATICAL_MOVES.md#equals) defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.
[Arg max](../MATHEMATICAL_MOVES.md#arg-max) returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.
[The star](../MATHEMATICAL_MOVES.md#symbol-decorations) marks the selected winner; it is a label on a and b, not multiplication or exponentiation.

Every mark needed for tokenization is now visible on the sentence-wheel. The symbols do not add an idea; they bind the discovered moves into one line:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\underset{(a,b)}{\text{arg max}} c(a,b)
$$

#### Tokenization beyond this one case

Early readers sound out letters. With experience they recognize recurring fragments and whole familiar words while retaining the ability to sound out something new.

#### Concrete Discovery

For low, lower, and lowest, the pair l-o repeats three times. Merge it into lo. The pair lo-w then repeats three times, so low becomes reusable. Nobody declared low meaningful; repetition made keeping it whole economical.

#### Where tokenization runs out

Tokenization chooses pieces, not meanings. IDs remain arbitrary, and the chosen vocabulary affects sequence length, cost, multilingual coverage, and which patterns are easy to notice.

At the Clockwork Scriptorium, the mechanist leaves a blank beneath the new mark. Tokenization has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the sentence-wheel

Rebuild the tokenization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/036-tokenization/README.md).*

---

### Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

Tokenization gives the machine repeatable pieces and assigns each piece an address. An address distinguishes tokens but says nothing about how their meanings should begin.

A new case arrives at the Clockwork Scriptorium, but the mechanist first reaches for the familiar sentence-wheel. Its promise is simple: feed token IDs directly into the network.

The rule survives the easy cases. The next case leaves a crack through the middle of it: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one. More confidence cannot repair information that never entered the rule.

*The mechanist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: feed token IDs directly into the…
possible road B ─┘              └── loses: since 417 is larger than 92,…

same roads ──▶ repaired map ──▶ give every vocabulary item a one-hot…
```

Two trails now cross the sentence-wheel. The pale trail bears the instruction “feed token IDs directly into the network.” It disappears into the observed failure: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one. The darker trail carries one additional capacity—to give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed input embeddings mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the sentence-wheel is altered in exactly one way: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. Much later, people will call this territory **Input Embeddings**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the sentence-wheel. The failed path remains visible beneath the repair, because input embeddings is easier to remember when its scar remains attached to it. The scar reads, ‘since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one’; the new line exists only to keep that loss from happening again.

#### The calculation hidden inside input embeddings

The mechanist carries the input embeddings scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A vocabulary of 50,000 tokens produces 50,000-dimensional vectors containing 49,999 zeros. Every distinct pair is equally distant. We preserved identity but learned no relationship.

The network needs a compact set of coordinates whose positions can change when prediction errors reveal useful relationships.

Let the embedding table contain one row for each vocabulary item:

The tokenizer assigns shelf address 2 to *tiger*. Looking up address 2 retrieves a small card of adjustable coordinates learned from tiger's usage. The address itself says nothing about meaning; moving the tiger card to shelf 7 would not change its learned contents. The table is therefore a collection of learned starting descriptions, while the token ID is merely the address used to fetch one.

##### Naming what is already on the table

**V** is the vocabulary and **|V|** its number of token addresses.
**d** is the compact representation width chosen for the model.
**E** therefore needs one row per token and d learnable coordinates per row.
**i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
**e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.

Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

##### Why the melody needs these exact notes

[E ∈ ℝ](../MATHEMATICAL_MOVES.md#membership) states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.
[E[i]](../MATHEMATICAL_MOVES.md#indices) treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.
[One-hot multiplication](../MATHEMATICAL_MOVES.md#multiplication) gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they form the smallest mechanism that survives the counterexample.

The mechanist reads the journey of input embeddings once more across the sentence-wheel, then lets the words contract without losing their order:

$$
E\in\mathbb{R}^{|V|\times d}
$$

For token ID $i$, retrieve:

$$
\mathbf{x}_i=E[i]
$$

The one-hot view gives the same result:

$$
\mathbf{x}_i=\mathbf{e}_iE
$$

#### Input Embeddings beyond this one case

A library call number is not the book's meaning. It is an address used to retrieve the book. Token IDs are call numbers; embedding rows are the learnable content retrieved from the shelf.

#### How Learning Changes the Table

Suppose tiger repeatedly appears where danger, stripes, and hunting matter. Prediction errors send corrections into its row. Lion receives some similar corrections and some different ones. Their vectors may become nearby—not because their IDs were nearby, but because useful predictions demanded shared structure.

This reconnects to Excavation 007. There we needed geometry for meaning. Here we have finally installed that geometry as a trainable component inside the language model.

#### Where input embeddings runs out

The same token initially retrieves the same row in every sentence. Bank beside river and bank beside money start from one vector. Attention will later contextualize it.

Worse, the embedding table contains no order. Swapping dog bites man with man bites dog selects the same three rows in a different sequence, but self-attention alone has no built-in idea that one row arrived first.

The sentence-wheel answers today's question and falls silent at the next. That silence is precise: Input Embeddings was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the sentence-wheel

Rebuild the input embeddings scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/037-input-embeddings/README.md).*

---

### Excavation 038 — Position — Why Order Must Enter the Model

An embedding table gives every token a learned starting description. The sentences “dog bites man” and “man bites dog” still contain the same three descriptions, so the machine cannot tell who did what.

The doors of the Clockwork Scriptorium close against the wind. On the sentence-wheel, the mechanist writes the cheapest rule that might still be true: sort tokens by ID or trust their array slot without exposing it to the model.

Reality answers without terminology: the first invents arbitrary order; the second stores position outside the computation. The sentence-wheel now holds two situations the old rule cannot keep apart.

*The mechanist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: sort tokens by ID or trust their…
                         │
                         └── mismatch: the first invents arbitrary order;…

reference evidence ──▶ measured repair: add a position-specific vector to…
```

The sentence-wheel is divided down the middle. Left side: “sort tokens by ID or trust their array slot without exposing it to the model.” Its final mark records the first invents arbitrary order; the second stores position outside the computation. Right side: the same starting evidence, now allowed to add a position-specific vector to each token vector before attention. Content says what; position says where. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given position a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: add a position-specific vector to each token vector before attention. Content says what; position says where. The name **Position** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from position through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the first invents arbitrary order; the second stores position outside the computation. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### The calculation hidden inside position

The mechanist carries the position scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

Compare “tiger chases deer” with “deer chases tiger.” The same three word cards appear, so content alone cannot distinguish hunter from hunted. Give the first slot one reusable position mark, the second another, and the third another. Adding the appropriate mark to each word leaves *tiger* recognizable while also telling later attention whether this occurrence came first or last.

##### Naming what is already on the table

**token_i** is the vocabulary address appearing at sequence location i.
**E[token_i]** retrieves what that token currently represents.
**P_i** represents where the occurrence sits.
Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
**z_i** is the combined input at position i.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.
[The shared index i](../MATHEMATICAL_MOVES.md#indices) forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.

The mandala has curved back upon itself. In this chamber we meet **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Nothing remains unnamed in the position case on the sentence-wheel. We can finally trade the long route for its compact map:

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

#### Position beyond this one case

Seat numbers do not describe passengers, but they preserve who sat where.

#### Return to the sentence-wheel

Rebuild the position scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/038-position/README.md).*

---

### Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

Nothing in the Clockwork Scriptorium yet bears today's mathematical name. There is only the mechanist, the sentence-wheel, and one plausible action: train each prefix in a separate forward pass.

Then the quiet test arrives: it prevents cheating but repeats nearly identical work. What looked like simplicity is revealed as a missing distinction.

*The mechanist sketches the break before changing it:*

```text
observation
    │
    ▼
[train each prefix in a separate…]
    │
    ╳  it prevents cheating but repeats…
    │
    ▼
[we need to process all positions…]
```

The mechanist turns the sentence-wheel toward the light. Through the old engraving, train each prefix in a separate forward pass, the evidence ends in the same contradiction: it prevents cheating but repeats nearly identical work. A second engraving adds only the power to process all positions together while blocking attention from position i to every later position j. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The mechanist circles the place where the two causal masking cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to process all positions together while blocking attention from position i to every later position j. The mechanist writes **Causal Masking** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The mechanist places a finger over the new distinction. At once the two cases collapse and it prevents cheating but repeats nearly identical work. Lifting the finger restores only this capacity: process all positions together while blocking attention from position i to every later position j. That tiny reversible motion is the chapter's proof of necessity.

#### The calculation hidden inside causal masking

The mechanist carries the causal masking scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

##### Naming what is already on the table

**i** is the receiving position and **j** a possible source position.
When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
When j>i, the source is future; adding −∞ makes its later softmax weight zero.
**M_ij** stores that allowed-or-forbidden correction for every pair.

##### Why the melody needs these exact notes

[Cases](../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
[j ≤ i and j > i](../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
Zero leaves an allowed attention score unchanged. [Negative infinity](../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

Before the line is compressed, notice its recurring motions: **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. They are the handholds by which the reader can later climb back from notation to meaning.

The story of causal masking has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

#### Causal Masking beyond this one case

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

#### Return to the sentence-wheel

Rebuild the causal masking scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/039-causal-mask/README.md).*

---

### Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.

At the Clockwork Scriptorium, the mechanist returns to the sentence-wheel. Yesterday's instrument still lies open, so the first move asks for no new magic: treat an entire sentence as one training example with one answer.

The mechanist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: most of its transitions provide no learning signal. The failure is stable enough to become evidence.

*The mechanist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   treat an entire sentence as one… most of its transitions provide no…
            \        /
             \      /
              shift the sequence by one position so…
```

Across the sentence-wheel, the old path and the repaired path run side by side. One carries “treat an entire sentence as one training example with one answer”; the other knows how to shift the sequence by one position so every visible prefix predicts the token immediately following it. When the failure—most of its transitions provide no learning signal—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to next-token examples. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: shift the sequence by one position so every visible prefix predicts the token immediately following it. This problem and its repair will travel under the name **Next-Token Examples**, but the name carries no knowledge the scene has not earned.

What changed on the sentence-wheel can be said without symbols. Before, the method could only treat an entire sentence as one training example with one answer; now it can also shift the sequence by one position so every visible prefix predicts the token immediately following it. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### The calculation hidden inside next-token examples

The mechanist carries the next-token examples scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Padding and document boundaries can create false targets unless their losses are masked.

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

##### Naming what is already on the table

**t₀…t_n** are consecutive tokens from one observed sequence.
Input x stops one token early because each position needs an answer to its right.
Target y starts one token later so y_i is exactly the next token after x_i.
The shared length lets one forward pass create a supervised lesson at every position.

##### Why the melody needs these exact notes

[Parentheses](../MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
[The shifted indices](../MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

Cover the prose about next-token examples and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

#### Next-Token Examples beyond this one case

A reading teacher pauses after every word, not only at the final period.

#### Return to the sentence-wheel

Rebuild the next-token examples scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/040-next-token-examples/README.md).*

---

### Excavation 041 — Logits — Let Every Vocabulary Token Compete

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

Morning reaches the Clockwork Scriptorium before anyone has a name for today's difficulty. Beside the sentence-wheel, the mechanist tries the smallest continuation of what already works: choose the nearest input embedding directly.

At the edge of the sentence-wheel, the shortcut produces its consequence: that restricts the scoring rule and hides how every vocabulary candidate should compete. That consequence, not a textbook, earns the next move.

*The mechanist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ choose the nearest input embedding… ──▶ that restricts the scoring rule and…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ use a learned linear map to produce… ──▶ accountable result
```

The mechanist covers the new mark and the old contradiction returns: that restricts the scoring rule and hides how every vocabulary candidate should compete. The cover is lifted, restoring the ability to use a learned linear map to produce one raw score for every vocabulary item, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason logits exists.

What must change for logits is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: use a learned linear map to produce one raw score for every vocabulary item. That threshold is where **Logits** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In logits, that memory takes a precise form: whenever that restricts the scoring rule and hides how every vocabulary candidate should compete, preserve enough structure to use a learned linear map to produce one raw score for every vocabulary item.

#### The calculation hidden inside logits

The mechanist carries the logits scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Logits have no standalone probability meaning and can shift together without changing the final distribution.

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

##### Naming what is already on the table

**h** is one contextual token vector containing what the Transformer currently knows.
**W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
**b** allows each token a learned baseline tendency.
**ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

##### Why the melody needs these exact notes

[Multiplication by Wvocab](../MATHEMATICAL_MOVES.md#multiplication) lets every contextual feature contribute a learned amount to every vocabulary candidate's score.
[The bias](../MATHEMATICAL_MOVES.md#addition) gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.
The index i selects one output candidate; it does not mean the token with the largest ID should win. See [indices](../MATHEMATICAL_MOVES.md#indices).

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. logits feels new because the objects are new; the gestures remain recognizably human.

The sentence-wheel already contains the complete logits mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\ell_i=hW_{\text{vocab}}+b
$$

The equation arrives after every operation has a job.

#### Logits beyond this one case

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

#### Return to the sentence-wheel

Rebuild the logits scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/041-logits/README.md).*

---

### Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; neither the reader nor the loss can treat them as comparable beliefs yet.

The sentence-wheel at the Clockwork Scriptorium still carries the marks of the previous discovery. The mechanist follows them as far as they seem willing to go: divide each logit by their sum.

For a moment the mark looks complete. Then the evidence refuses to fit: negative values break probability and shifting all scores changes the result. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The mechanist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ divide each logit by their sum ──▶ blurred: negative values break probability and…
      │
      └── new lens ──▶ exponentiate relative scores,… ──▶ distinction survives
```

The mechanist lays two translucent sheets over the sentence-wheel. The first is inscribed, “divide each logit by their sum.” Its path ends where negative values break probability and shifting all scores changes the result. The second receives the same evidence but is allowed to exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. Held to the light, the sheets separate at exactly one decision.

No one reaches for a vocabulary probabilities formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The mechanist changes only that one responsibility: exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. When the ink dries, the name **Vocabulary Probabilities** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because negative values break probability and shifting all scores changes the result, while the other can exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. That fork—not the vocabulary—is where vocabulary probabilities lives.

#### The calculation hidden inside vocabulary probabilities

The mechanist carries the vocabulary probabilities scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

##### Naming what is already on the table

**ℓ_i** is candidate i's raw score.
Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
**y** is the observed next-token index, so p_y is the probability assigned to what happened.
The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

##### Why the melody needs these exact notes

[Exponentials](../MATHEMATICAL_MOVES.md#exponential) create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.
[Summing all weights](../MATHEMATICAL_MOVES.md#summation) measures the whole amount to be shared, and [division](../MATHEMATICAL_MOVES.md#division) turns each candidate's weight into a probability share.
[The log](../MATHEMATICAL_MOVES.md#logarithm) turns the probability assigned to the observed token into additive information cost; [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) makes low probability expensive and certainty cost zero.

Three old motions cast new shadows here: **the rising flame**—a small score difference becomes positive relative evidence; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for vocabulary probabilities is now visible on the sentence-wheel. The symbols do not add an idea; they bind the discovered moves into one line:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}}
$$

$$
L=-\log p_y
$$

The equation arrives after every operation has a job.

#### Vocabulary Probabilities beyond this one case

A race score becomes odds only after every competitor is considered together.

#### Return to the sentence-wheel

Rebuild the vocabulary probabilities scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/042-vocabulary-probabilities/README.md).*

---

### Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

Softmax turns vocabulary scores into a distribution. Generation now faces a choice that training did not settle: should the machine always take the winner or sometimes follow another plausible continuation?

Night gathers around the Clockwork Scriptorium. Under the light of the sentence-wheel, the mechanist refuses to invent prematurely and begins with the plain rule: always use argmax.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text. More confidence cannot repair information that never entered the rule.

*The mechanist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: always use argmax
possible road B ─┘              └── loses: the same prompt follows the same…

same roads ──▶ repaired map ──▶ we need to control the distribution…
```

Two trails now cross the sentence-wheel. The pale trail bears the instruction “always use argmax.” It disappears into the observed failure: the same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text. The darker trail carries one additional capacity—to control the distribution with temperature and optionally restrict it to a credible top set before sampling. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed sampling mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the sentence-wheel is altered in exactly one way: we need to control the distribution with temperature and optionally restrict it to a credible top set before sampling. Much later, people will call this territory **Sampling**. Here the name is only a memory of the failure it can survive.

The sentence-wheel has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and sampling looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### The calculation hidden inside sampling

The mechanist carries the sampling scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

##### Naming what is already on the table

**ℓ_i** is candidate i's raw logit.
**T** is temperature: dividing by T changes score gaps before exponentiation.
T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
Exponentiation preserves ranking while making evidence positive.
Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

##### Why the melody needs these exact notes

[Dividing every logit by T](../MATHEMATICAL_MOVES.md#division) changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.
[Exponentiation](../MATHEMATICAL_MOVES.md#exponential) then turns the adjusted gaps into positive ratios, while [summing](../MATHEMATICAL_MOVES.md#summation) and dividing make one probability distribution.

The symbols are about to change costume, but their work has appeared before: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the rising flame**—a small score difference becomes positive relative evidence; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. This is how distant excavations begin to sound like variations of one melody.

The mechanist reads the journey of sampling once more across the sentence-wheel, then lets the words contract without losing their order:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$

The equation arrives after every operation has a job.

#### Sampling beyond this one case

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

#### Return to the sentence-wheel

Rebuild the sampling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/043-sampling/README.md).*

---

### Excavation 044 — Context Windows — How Much Past Can the Model Carry?

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

Inside the Clockwork Scriptorium, every old tool is given one honest chance. The mechanist sets the sentence-wheel between the evidence and the desired answer, then tries to attend to the entire history forever.

Reality answers without terminology: computation and memory grow, and the model eventually exceeds positions it was trained to handle. The sentence-wheel now holds two situations the old rule cannot keep apart.

*The mechanist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: attend to the entire history forever
                         │
                         └── mismatch: computation and memory grow, and the…

reference evidence ──▶ measured repair: choose a maximum context, train…
```

The sentence-wheel is divided down the middle. Left side: “attend to the entire history forever.” Its final mark records computation and memory grow, and the model eventually exceeds positions it was trained to handle. Right side: the same starting evidence, now allowed to choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given context windows a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. The name **Context Windows** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to attend to the entire history forever; on the other lies the observed fact that computation and memory grow, and the model eventually exceeds positions it was trained to handle. The bridge called context windows has exactly the planks needed to choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

#### The calculation hidden inside context windows

The mechanist carries the context windows scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

##### Naming what is already on the table

**n** is the number of tokens inside the active context.
Each of n queries can compare with n keys, creating roughly n×n score pairs.
That repeated pairwise work is why cost grows proportionally to n² rather than n.
The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

##### Why the melody needs these exact notes

[Proportionality](../MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
[The square](../MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

Inside context windows, familiar operations return with stricter duties: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the context windows case on the sentence-wheel. We can finally trade the long route for its compact map:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

#### Context Windows beyond this one case

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

#### Return to the sentence-wheel

Rebuild the context windows scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/044-context-window/README.md).*

---

### Excavation 045 — A Tiny GPT — Close the Prediction Loop

A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.

A new case arrives at the Clockwork Scriptorium, but the mechanist first reaches for the familiar sentence-wheel. Its promise is simple: call a framework Transformer and hide the causal chain.

Then the quiet test arrives: or connect the parts without checking shapes, leakage, and target alignment. What looked like simplicity is revealed as a missing distinction.

*The mechanist sketches the break before changing it:*

```text
observation
    │
    ▼
[call a framework Transformer and hide…]
    │
    ╳  or connect the parts without checking…
    │
    ▼
[assemble token and position…]
```

The mechanist turns the sentence-wheel toward the light. Through the old engraving, call a framework Transformer and hide the causal chain, the evidence ends in the same contradiction: or connect the parts without checking shapes, leakage, and target alignment. A second engraving adds only the power to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The mechanist circles the place where the two tiny gpt cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. The mechanist writes **A Tiny GPT** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The mechanist does not memorize tiny gpt. Instead, the mechanist memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. The formal name merely lets that motion be shared.

#### The calculation hidden inside a tiny gpt

The mechanist carries the tiny gpt scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

Begin with the prompt “the tiger.” Its token addresses fetch learned starting descriptions; position marks preserve order; masked attention gathers only allowed context; token workshops transform what was gathered; and the output scores every possible next word. Suppose sampling chooses *sleeps*. Appending that choice creates “the tiger sleeps,” and the same mechanism now faces a new prediction. The language model exists only when this entire loop closes.

##### Naming what is already on the table

**tokens** are discrete addresses produced by the tokenizer.
**embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
**logits** score every next-token candidate; **loss** compares those scores with the observed answer.
**update** changes parameters using backpropagated error.
**sample** chooses a continuation and feeds it back as the next token.
The arrows encode one closed causal loop, not an unexplained algebraic equality.

##### Why the melody needs these exact notes

[Arrows](../MATHEMATICAL_MOVES.md#arrows) show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.
The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.

The story of tiny gpt has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$

The equation arrives after every operation has a job.

#### A Tiny GPT beyond this one case

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

#### A sentence enters; a future leaves

Characters became tokens, tokens found coordinates, positions supplied order, masks protected honesty, and logits opened a competition among possible next words. The tiny GPT is not one invention. It is a procession of necessities moving through a sentence.

```text
text → tokens → positions → context → probabilities → next token
```

The trail called *a sentence enters; a future leaves* is what remains when one necessity becomes another.

#### Return to the sentence-wheel

Rebuild the tiny gpt scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/045-tiny-gpt/README.md).*
