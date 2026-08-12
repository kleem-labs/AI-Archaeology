# Volume I — We Build a Mind

We begin with nothing but observations. By the final chapter, the same chain of necessities has produced a tiny language model that can learn and generate.

One discovery will create the need for the next; the object under construction never resets.

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

A tiger recorded as weight 220, speed 65, and age 6 becomes [220, 65, 6]. The first slot must always mean weight; otherwise [220, 65, 6] could describe nonsense.

- **x** is the object we needed to carry as one package.
- **x₁ through xₙ** are its agreed measurements; subscripts preserve which feature is which.
- **n** exists because different problems keep different numbers of features.
- The brackets bind the measurements without adding or comparing them yet.

This says only: one object carries an ordered measurement for each of $n$ agreed features.

##### Why these operations are forced

- [Brackets](../MATHEMATICAL_MOVES.md#brackets) keep tiger weight, speed, and age together without pretending they should be added; each observation must remain recoverable.
- [Subscripts](../MATHEMATICAL_MOVES.md#indices) give each retained feature an address. The dots mean the same pattern continues until feature n; they do not hide another operation.
- [The equals sign](../MATHEMATICAL_MOVES.md#equals) says that **x** is our short name for this complete ordered list.

Only now can we compress that reasoning:

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

- **x** is only a nickname for Tiger A's ordered measurements.
- **y** is only a nickname for Tiger B's ordered measurements.
- **x1 and y1** are their weights; index 2 means speed; index 3 means age.
- **xi−yi** abbreviates “compare the same named property,” exactly as above.
- Squaring repairs the cancellation we just witnessed.
- Summing combines weight, speed, and age into one answer.
- The root changes total 27 into distance 5.20.
- **d(x,y)** merely names “the one separation between these two tigers.”

##### Why these operations are forced

- [Subtracting](../MATHEMATICAL_MOVES.md#subtraction) tiger height from tiger height and tiger speed from tiger speed isolates each like-for-like disagreement. Adding would measure a total, not a gap.
- [Squaring](../MATHEMATICAL_MOVES.md#powers) stops a smaller and larger feature from cancelling and makes a large mismatch count more strongly. Absolute value could stop cancellation too, but would produce a different geometry in which many small misses and one large miss trade differently.
- [Adding the squared disagreements](../MATHEMATICAL_MOVES.md#summation) lets every retained feature contribute to one separation. Multiplying would let one perfect feature match erase all other disagreement by making the product zero.
- [The square root](../MATHEMATICAL_MOVES.md#square-root) returns the accumulated squared separation to the features' ordinary scale; it is omitted when squared distance itself is all an algorithm needs.

Only now can we compress that reasoning:

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

A rescue party marks its camp on a paper map. It walks five kilometres east and two kilometres south to reach an injured ranger. Those instructions still work if a second party begins from another camp: move five east and two south. Only after the route has a meaning do we record east–west and north–south change as `[5, -2]`.

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

##### Why these operations are forced

- [Destination minus starting point](../MATHEMATICAL_MOVES.md#subtraction) is forced because we want the change that would carry **a** to **b**, not their combined location.
- [A negative coordinate](../MATHEMATICAL_MOVES.md#negative-sign) keeps direction: −2 means move two units opposite that axis, not that the movement has an impossible size.
- [Adding the change back](../MATHEMATICAL_MOVES.md#addition) is the check: starting place plus the discovered movement must recover the destination.

Only now can we compress that reasoning:

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

A ranger must turn two observations—how heavy an animal looks and how fast it moves—into two decisions: danger and whether pursuit is possible. For danger she counts the weight clue twice and the speed clue three times. For pursuit she ignores weight and counts speed four times. Writing the two recipes as rows lets one reusable machine apply both judgments to every animal report.

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.

Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

##### Why these operations are forced

- [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets each clue's importance scale that clue. A zero weight silences it; a weight of three makes it count three times.
- [Addition](../MATHEMATICAL_MOVES.md#addition) combines the scaled clues because they are separate contributions to the same judgment. Multiplying them would make any zero clue erase the entire decision and would claim interaction we never asked for.
- [Each equals sign](../MATHEMATICAL_MOVES.md#equals) records that the verbal judgment, its arithmetic recipe, and its final score are three descriptions of the same result.

Only now can we compress that reasoning:

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

##### Why these operations are forced

- [The arrow](../MATHEMATICAL_MOVES.md#arrows) means “represent this token as,” not equality: a word and its numerical representation are different kinds of object.
- [The membership sign](../MATHEMATICAL_MOVES.md#membership) says the embedding is allowed to live among d-coordinate real vectors.
- [The superscript d](../MATHEMATICAL_MOVES.md#powers) counts coordinate slots here; it is dimension, not an instruction to raise each number to a power.

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

Mary, John, and the book are possible sources for the word *she*. The sentence gives Mary the strongest relevance, the book a weaker connection, and John the weakest. Raw relevance can be negative or arbitrarily large, so it cannot yet say what share each source should contribute. Exponentiation turns every candidate into positive evidence; dividing by their shared total converts that evidence into portions of one whole.

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.

For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

##### Why these operations are forced

- [Exponentiation](../MATHEMATICAL_MOVES.md#exponential) makes every raw score positive while preserving order and turning score gaps into stable ratios. Squaring would make a large negative score look strong; clipping would destroy gap information.
- [The sum](../MATHEMATICAL_MOVES.md#summation) gathers every candidate's positive weight because all candidates must share one unit of attention. A product would not describe a total available amount.
- [Dividing by that total](../MATHEMATICAL_MOVES.md#division) converts each weight into its share. Without it, multiplying every score scale would change the amount of information mixed rather than only its distribution.

Only now can we compress that reasoning:

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

A librarian hears, “Find me the book about a striped predator.” The request emphasizes *animal* and *stripes*. A catalogue card advertises the same properties; matching request-property to catalogue-property produces relevance. If that card wins three quarters of the attention, three quarters of the book's stored content—not three quarters of its catalogue description—travels into the answer. The request becomes the query, the catalogue becomes the key, and the retrievable content becomes the value only after those jobs are distinct.

- **qᵢ** states what receiving token i needs; **kⱼ** states what source j offers.
- Multiplying matching coordinates rewards aligned needs and offers; opposite signs become negative evidence.
- Summing over feature r turns many alignments into one score sᵢⱼ.
- **αᵢⱼ** is that score after normalization: how much i listens to j.
- **vⱼ** is the content source j contributes; multiplying by α scales its voice.
- Summing over j combines every permitted source into output oᵢ.

Learned matrices create query, key, and value views from each current representation. Their formulas record three roles we already needed; they are not arbitrary symmetry.

##### Why these operations are forced

- [The dot product](../MATHEMATICAL_MOVES.md#dot-product) multiplies query height-need by key height-offer, stripe-need by stripe-offer, and so on, then adds those aligned agreements into one relevance score.
- [Multiplication inside the dot product](../MATHEMATICAL_MOVES.md#multiplication) is required because a query feature should matter only when the matching key feature is present too; addition would reward a key for merely being large on unrelated features.
- [The first sum](../MATHEMATICAL_MOVES.md#summation) combines feature-level evidence into one match. The second sum combines each source's value after its attention weight scales how loudly that source contributes.

Only now can we compress that reasoning:

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

In “The tiger that chased the deer was tired,” one reader follows grammar to discover what *was tired* describes, while another follows reference to keep tiger separate from deer. Averaging their notes too early destroys which evidence came from which question. Keeping the two notes side by side lets a later learned map decide how much grammar and reference the sentence needs.

- **X** is the shared sequence of token representations.
- Each **headₕ** is an independent Q/K/V retrieval space, needed because relationships should not compete in one distribution.
- Concatenation preserves each report instead of averaging distinctions away.
- **H** counts the parallel heads.
- **W_O** is learned because the model must decide how the preserved reports should interact and return to the shared width.

Each head is the query–key–value mechanism from the previous excavation with independent learned projections.

The analogy has limits. Heads do not always become clean, human-readable professions. Some overlap; some are difficult to interpret. The architectural point is parallel relationship spaces, not a promise of tidy labels.

##### Why these operations are forced

- [Concatenation](../MATHEMATICAL_MOVES.md#concatenation) keeps the grammar expert, reference expert, and distance expert side by side. Adding them immediately would erase which head supplied which evidence.
- [Multiplication by the output matrix](../MATHEMATICAL_MOVES.md#multiplication) lets the model learn how those preserved expert coordinates should interact; a fixed sum would impose the same mixture everywhere.

Only now can we compress that reasoning:

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

Attention tells the word *tiger* what the rest of the sentence said. Now imagine several small workshops inside that token: one notices whether an animal is dangerous, another recognizes whether it is acting or being described. A gate closes workshops whose evidence is negative and leaves useful ones open. A second mixing step combines only the surviving discoveries. Without the gate, the two mixing steps collapse into one fixed recipe and no conditional workshop can exist.

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

##### Why these operations are forced

- [Each matrix multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets learned weights decide how strongly one incoming feature should affect each hidden or outgoing feature.
- [Adding a bias](../MATHEMATICAL_MOVES.md#addition) lets a detector have a baseline threshold even when all incoming features are zero; multiplication alone must always map zero input to zero output.
- [The activation function](../MATHEMATICAL_MOVES.md#function-application) bends the intermediate result. Without that nonlinearity, the two matrix stages collapse into one linear transformation.

Only now can we compress that reasoning:

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

A cartographer already has a useful map of the forest. A new survey reports that one trail bends half a kilometre east and one kilometre south. Replacing the whole map with that small report would destroy everything known; adding it as a correction preserves the map and changes only the trail. If the survey discovers nothing useful, adding a zero correction leaves the original untouched.

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.

The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

##### Why these operations are forced

- [Addition](../MATHEMATICAL_MOVES.md#addition) preserves the old message **x** and treats the block as a proposed change **F(x)**. Replacing x would force every block to reconstruct all useful old information.
- [F(x)](../MATHEMATICAL_MOVES.md#function-application) says the proposed change depends on this exact incoming representation rather than being one fixed correction for every token.

Only now can we compress that reasoning:

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

Three microphones hear the same roar at volumes 1, 2, and 3 because one sits closer to the tiger. Their shared centre is 2. Subtracting it leaves the pattern `[-1, 0, 1]`: quieter, typical, louder. Dividing by the pattern's spread makes that relative shape comparable with another set recorded by more sensitive microphones. A tiny safety amount is needed when all microphones report the same value and the spread is zero.

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

##### Why these operations are forced

- [Summing and dividing by d](../MATHEMATICAL_MOVES.md#mean) finds the token's average feature level. A raw sum would grow merely because the representation has more coordinates.
- [Subtracting the mean](../MATHEMATICAL_MOVES.md#subtraction) asks how each feature differs from this token's centre; addition would move the whole pattern farther from centre.
- [Squaring and averaging those differences](../MATHEMATICAL_MOVES.md#variance) measures spread without quieter and louder features cancelling each other.
- [The square root](../MATHEMATICAL_MOVES.md#square-root) returns variance to ordinary feature scale, and [division by that spread](../MATHEMATICAL_MOVES.md#division) removes arbitrary volume while preserving relative shape.
- Adding ε is a safety floor: when every feature is identical, spread is zero and division would be undefined. See [addition](../MATHEMATICAL_MOVES.md#addition) and [division](../MATHEMATICAL_MOVES.md#division).

Only now can we compress that reasoning:

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

A tiger alarm has one adjustable dial: how strongly a stripe should raise danger. The dial is currently 8, but repeated verified encounters suggest 3 would fit better. Its present squared mistake is 25, and a tiny upward test reveals that increasing the dial makes error rise with sensitivity 10. Reversing one tenth of that uphill suggestion moves the dial from 8 to 7 and lowers the mistake to 16.

- **θ** is the current collection of learnable weights.
- **L** is the measured prediction failure.
- **∇L** collects how increasing each weight would increase loss.
- The minus sign reverses that uphill direction.
- **η** controls step size because direction alone does not say how far to move.
- The arrow means replace the old weights with the improved ones.

$\theta$ is the current state of the weights, $\nabla L$ is a vector of advised change, and $\eta$ controls how large a step to take.

##### Why these operations are forced

- [The gradient](../MATHEMATICAL_MOVES.md#gradient) collects one local loss sensitivity for every adjustable weight so the whole parameter state receives coordinated advice.
- [The minus sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses the gradient because the gradient points toward increasing loss and learning wants the locally decreasing direction.
- [Multiplying by η](../MATHEMATICAL_MOVES.md#multiplication) chooses how much of that direction to trust. Without η, the gradient's magnitude would dictate the whole step even when it is too large or too small.
- The update arrow means “replace the old parameter state with this new one”; it is an action, not symmetric equality. See [arrows](../MATHEMATICAL_MOVES.md#arrows).

Only now can we compress that reasoning:

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

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/016-emergence/README.md).*

---

## Part III — Learning from Error

The Transformer can construct a useful interpretation, but it cannot honestly pretend that every interpretation is certain. Footprints, words, and predictions all leave several possible stories alive. The expedition now needs a way to preserve uncertainty, price error, trace responsibility, and let error alter the machine.

---

### Excavation 017 — Probability — Counting What We Do Not Know

The Transformer has begun to infer hidden causes from the footprints of language. But inference without certainty is dangerous: the same rustle may have been made by a tiger, a deer, or only the wind.

An obvious shortcut is to choose the most common cause and declare certainty. This works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act.

That failure tells us to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

- **A** is the uncertain event we need to discuss.
- The numerator counts observations where A occurred.
- The denominator counts all comparable opportunities, because an isolated count has no scale.
- Division turns the count into a share between zero and one.
- **P(A)** names that evidence-dependent share, not a guarantee.

##### Why these operations are forced

- [Division](../MATHEMATICAL_MOVES.md#division) turns a tiger count into a share of comparable encounters. The count alone grows when we watch longer even if the underlying chance is unchanged.
- [Probability](../MATHEMATICAL_MOVES.md#probability) preserves several possible causes as parts of one whole instead of forcing certainty from incomplete evidence.

Only now can we compress that reasoning:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$

Probability is a weather forecast: not a promise, but an honest description of uncertainty that can still guide action.

#### Limits

Probabilities depend on evidence and assumptions. When new evidence arrives, the shares must change.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/017-probability/README.md).*

---

### Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

Perhaps we ask which story is generally more believable. That ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

So we reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

- **θ** is one proposed hidden explanation.
- **x** is the evidence already observed.
- The vertical bar means “under the assumption that.”
- **P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
- **L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

##### Why these operations are forced

- [The conditional bar](../MATHEMATICAL_MOVES.md#conditional-bar) deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.
- [Equality](../MATHEMATICAL_MOVES.md#equals) renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.

Only now can we compress that reasoning:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

#### Limits

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/018-likelihood/README.md).*

---

### Excavation 019 — Information — Why Surprise Needs a Number

Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.

We first try to measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

We need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

- **P(x)** measures how expected observation x was.
- The logarithm is needed because independent probabilities multiply while information from independent messages should add.
- Probabilities below one have negative logs, so the minus sign makes information nonnegative.
- A certain event has P=1 and therefore zero information; rarer events receive more.

##### Why these operations are forced

- [The logarithm](../MATHEMATICAL_MOVES.md#logarithm) is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.
- [The negative sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.
- Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.

Only now can we compress that reasoning:

$$
I(x)=-\log P(x)
$$

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

#### Limits

Information depends on the probability model. A surprise to one observer may be expected to another.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/019-information/README.md).*

---

### Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.

One tempting answer is to count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

Now we can see what is missing: we must average the information of every possible outcome, weighted by how often that outcome occurs.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

- **pᵢ** is the probability of possible outcome i.
- **−log pᵢ** is the information received if i occurs.
- Multiplying by pᵢ weights that surprise by how often it is expected to occur.
- Summing over every i computes average surprise before the outcome is known.
- **H(P)** names uncertainty of the whole distribution P.

##### Why these operations are forced

- [Multiplying each surprise by pᵢ](../MATHEMATICAL_MOVES.md#multiplication) lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.
- [Summing](../MATHEMATICAL_MOVES.md#summation) combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.
- [The log](../MATHEMATICAL_MOVES.md#logarithm) still converts probability products into additive information, and [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) keeps that information nonnegative.

Only now can we compress that reasoning:

$$
H(P)=-\sum_i p_i\log p_i
$$

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

#### Limits

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/020-entropy/README.md).*

---

### Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.

At first we use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

That failure tells us to charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

- **P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
- **Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
- **−log qᵢ** makes confident neglect extremely costly.
- Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

##### Why these operations are forced

- [−log qᵢ](../MATHEMATICAL_MOVES.md#logarithm) charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.
- [Multiplying by pᵢ](../MATHEMATICAL_MOVES.md#multiplication) asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.
- [The sum](../MATHEMATICAL_MOVES.md#summation) forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.

Only now can we compress that reasoning:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

#### Limits

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/021-cross-entropy/README.md).*

---

### Excavation 022 — Derivatives — Asking One Weight What It Changed

Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.

Using what we have, we try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

So we nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

- **w** is the one weight whose responsibility we are probing.
- **ε** is a small experimental nudge.
- **L(w+ε)−L(w)** measures the loss change caused by that nudge.
- Dividing by ε turns total change into change per unit of weight.
- The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
- **dL/dw** names that local sensitivity.

##### Why these operations are forced

- [The numerator subtracts](../MATHEMATICAL_MOVES.md#subtraction) old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.
- [Division by the weight nudge](../MATHEMATICAL_MOVES.md#division) converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.
- [The limit](../MATHEMATICAL_MOVES.md#limit) lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

#### Limits

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/022-derivatives/README.md).*

---

### Excavation 023 — The Chain Rule — Following One Change Through Many Machines

A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.

An obvious shortcut is to measure only the first effect or only the final effect. Either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

We need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

- **w→x→y→L** is the causal path through successive machines.
- Each fraction is one local sensitivity: how its output changes when its input changes.
- Multiplication is forced because a change is scaled at every link it traverses.
- The product gives the effect of w on L without pretending they touch directly.

##### Why these operations are forced

- Each [derivative](../MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
- [Multiplying the rates](../MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

#### Limits

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/023-chain-rule/README.md).*

---

### Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.

Perhaps we perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

Now we can see what is missing: we must compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

- **x̄** means accumulated sensitivity of final loss to intermediate x.
- A node can influence several child results y, so every downstream path must contribute.
- **ȳ** is blame already accumulated at child y.
- **∂y/∂x** says how strongly x affected that child locally.
- Multiplication passes blame through one edge; summation combines all outgoing paths.

##### Why these operations are forced

- [The partial derivative](../MATHEMATICAL_MOVES.md#partial-derivative) measures one local edge while other inputs are held fixed.
- [Multiplying child blame by edge sensitivity](../MATHEMATICAL_MOVES.md#multiplication) passes downstream responsibility through that edge; either factor being zero should block that path.
- [Summing over children](../MATHEMATICAL_MOVES.md#summation) reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.

Only now can we compress that reasoning:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

#### Limits

Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/024-backpropagation/README.md).*

---

### Excavation 025 — Gradient Descent — Teaching a Tiny Network

Backpropagation can now return one local sensitivity to every adjustable weight. Sensitivity is advice, not learning: the network still needs a rule that turns millions of local directions into a new parameter state.

We first try to jump directly opposite the gradient with no step control; the model may overshoot and diverge. Take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

That failure tells us to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

- **θ_t** packages the current weights; our tiny example has only 8.
- **L** is the mistake measure; here it is (weight − 3)².
- **∇_θL** packages local sensitivities; our example has only 10.
- The minus sign reverses the uphill direction.
- **η** is the chosen fraction of the correction; here it is 0.1.
- **t** means before this correction; **t+1** means after it.

Substitute real values before compact symbols:

~~~text
next weight = current weight - learning rate × uphill sensitivity
            = 8              - 0.1           × 10
            = 7
~~~

##### Why these operations are forced

- [The time indices](../MATHEMATICAL_MOVES.md#indices) distinguish the parameter state before update t from the state after it.
- [The gradient](../MATHEMATICAL_MOVES.md#gradient) supplies one local uphill sensitivity for each parameter; [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) reverses that direction toward lower loss.
- [Multiplying by η](../MATHEMATICAL_MOVES.md#multiplication) supplies the missing travel distance. A direction alone does not say whether to move one millimetre or one kilometre.

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

#### Limits

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/025-gradient-descent/README.md).*

---

### Excavation 026 — Mini-Batches — Learning from More Than One Example

Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.

One tempting answer is to use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

So we average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

- **B** is the selected mini-batch and **|B|** its number of examples.
- **Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
- Summing combines the witnesses.
- Dividing by batch size prevents merely using more examples from making the step proportionally larger.
- **g_B** is the batch's less noisy gradient estimate.

##### Why these operations are forced

- [The sum](../MATHEMATICAL_MOVES.md#summation) lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.
- [Dividing by |B|](../MATHEMATICAL_MOVES.md#division) asks for advice per example, so merely inviting twice as many witnesses does not double the update.
- [i ∈ B](../MATHEMATICAL_MOVES.md#membership) restricts the sum to examples actually selected for this mini-batch; [|B|](../MATHEMATICAL_MOVES.md#cardinality) means the number of those examples.

Only now can we compress that reasoning:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/026-mini-batches/README.md).*

---

### Excavation 027 — Learning Rate — How Large Should the Next Step Be?

A mini-batch replaces one noisy witness with the average advice of a small council. The council can point downhill, but its vote still says nothing about how far the network should move.

At first we always take a huge step: leap across the valley and oscillate. Always take a microscopic step: improve so slowly that the expedition ends first.

We need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.

##### Why these operations are forced

- [gₜ](../MATHEMATICAL_MOVES.md#gradient) gives direction but not distance.
- [Multiplying by ηₜ](../MATHEMATICAL_MOVES.md#multiplication) turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.
- [Subtraction](../MATHEMATICAL_MOVES.md#negative-sign) moves opposite the locally uphill gradient rather than making loss rise faster.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/027-learning-rate/README.md).*

---

### Excavation 028 — Momentum — Remembering Which Way Downhill Persists

The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.

Using what we have, we obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

Now we can see what is missing: we must keep a fading memory of past gradients and combine it with the new one.

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

- **g_t** is the newest noisy gradient.
- **v_{t−1}** stores direction accumulated previously.
- **β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
- Addition combines memory with new evidence into velocity v_t.
- **η** scales that velocity before it changes θ.

##### Why these operations are forced

- [Multiplying old velocity by β](../MATHEMATICAL_MOVES.md#multiplication) fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.
- [Adding the new gradient](../MATHEMATICAL_MOVES.md#addition) lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.
- The final [η scaling](../MATHEMATICAL_MOVES.md#multiplication) chooses travel distance and [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) turns remembered uphill direction into a downhill update.

Only now can we compress that reasoning:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/028-momentum/README.md).*

---

### Excavation 029 — Initialization — Where Should Learning Begin?

Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.

An obvious shortcut is to set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

That failure tells us to draw small random weights whose scale depends on how many inputs feed the neuron.

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

- **w** is one newly initialized weight.
- **Var(w)** measures the typical squared spread of starting weights, not their meaning.
- **n_in** counts signals entering the neuron.
- Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
- “Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

##### Why these operations are forced

- [Variance](../MATHEMATICAL_MOVES.md#variance) describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.
- [Dividing by the number of incoming signals](../MATHEMATICAL_MOVES.md#division) makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.
- [The approximately sign](../MATHEMATICAL_MOVES.md#approximation) admits a design target rather than claiming every finite random sample has exactly this variance; see [equality](../MATHEMATICAL_MOVES.md#equals) for the stronger claim it avoids.

Only now can we compress that reasoning:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/029-initialization/README.md).*

---

### Excavation 030 — Activation Functions — Why a Network Must Bend

Careful initialization keeps early signals alive and breaks symmetry. But a tower made only from linear transformations still collapses algebraically into one linear transformation, no matter how many layers we stack.

Perhaps we add more linear layers. Depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

So we place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

- **x** is the incoming representation.
- **W** mixes its features; **b** permits learned thresholds and offsets.
- **φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
- **h** is the hidden representation after both mixing and gating.

##### Why these operations are forced

- [Wx](../MATHEMATICAL_MOVES.md#multiplication) lets every learned input weight scale and mix its matching feature; [adding b](../MATHEMATICAL_MOVES.md#addition) supplies a learnable baseline.
- [Applying φ](../MATHEMATICAL_MOVES.md#function-application) bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.

Only now can we compress that reasoning:

$$
h=\phi(Wx+b)
$$

A railway switch changes which route a signal can take. Without switches, many track segments still form only one fixed route.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/030-activation-functions/README.md).*

---

### Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

Activation gates let the network bend and build conditional internal paths. That flexibility also makes a new deception possible: the machine can reproduce every training example without learning what should survive beyond them.

We first try to celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

We need to reserve unseen cases and compare training success with performance outside the training memory.

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

- **L_train** measures error on examples allowed to shape the model.
- **L_unseen** measures error on held-out observations.
- Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
- A positive generalization gap is evidence that training success did not fully survive.

##### Why these operations are forced

- [Unseen loss minus training loss](../MATHEMATICAL_MOVES.md#subtraction) isolates how much performance deteriorates beyond memorized examples. Adding the losses would measure total error, not the transfer gap.
- The order matters: a positive answer naturally means unseen cases are worse. Reversing the subtraction would reverse that interpretation.

Only now can we compress that reasoning:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

A student who memorizes answer positions can ace the practice sheet and fail when the same ideas are rearranged.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/031-overfitting/README.md).*

---

### Excavation 032 — Regularization — Making Memorization More Expensive

Overfitting reveals that low training error can be perfect memory wearing the costume of intelligence. The learner therefore needs pressure against fragile, unnecessarily extreme explanations.

One tempting answer is to forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

Now we can see what is missing: we must add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.

##### Why these operations are forced

- [Addition](../MATHEMATICAL_MOVES.md#addition) puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.
- [The squared norm](../MATHEMATICAL_MOVES.md#norm) combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.
- [λ scales the penalty](../MATHEMATICAL_MOVES.md#multiplication) because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.

Only now can we compress that reasoning:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

A map that explains every pebble with a separate rule is less trustworthy than one road system that explains many journeys.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/032-regularization/README.md).*

---

### Excavation 033 — Validation — Testing Without Peeking at the Final Exam

Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.

At first we use training loss for every choice; it rewards memorization. Check the test set repeatedly; every decision leaks test information back into development.

That failure tells us to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

- **D** is all available data.
- The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
- Union means they reconstruct the available collection.
- The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

##### Why these operations are forced

- [Union](../MATHEMATICAL_MOVES.md#union) says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.
- Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.

Only now can we compress that reasoning:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

A practice exam guides study. A sealed final exam measures what survived without feedback.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/033-validation/README.md).*

---

### Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

Validation lets us choose among models without opening the sealed test set. Even an honest test can come from yesterday's hospital, dialect, season, or camera while tomorrow arrives from somewhere else.

Using what we have, we assume all future observations come from exactly the same source as training. Or demand good performance on every imaginable world, which no finite evidence can guarantee.

So we state the deployment world, test meaningful shifts, and build representations around relationships likely to survive those shifts.

The repair solves the immediate failure, but no benchmark proves universal intelligence. Future distributions can change in ways neither data nor designers anticipated.

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

- **θ** is one trained model and **f_θ(x)** its prediction for input x.
- **L(f_θ(x),y)** measures failure against outcome y.
- **P_future** names the deployment world we actually care about.
- Sampling (x,y) from that world prevents training data from silently defining success.
- The expectation averages loss over future cases; **R(θ)** names that future risk.

##### Why these operations are forced

- [Expectation](../MATHEMATICAL_MOVES.md#expectation) weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.
- [fθ(x)](../MATHEMATICAL_MOVES.md#function-application) feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.
- The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.

Only now can we compress that reasoning:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

A boat tested on one calm lake has not proved itself at sea. We must name the waters we expect it to cross.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/034-generalization/README.md).*

---

### Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.

An obvious shortcut is to hide everything behind a framework call. The code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

We need to build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

- **x** is observed input.
- **Wx+b** mixes features and supplies offsets.
- **φ** bends the mapping so depth adds new behavior.
- **ŷ** is the prediction and **L** measures its failure.
- **∇_θL** assigns local correction directions to all parameters θ.
- **θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

##### Why these operations are forced

- [Arrows](../MATHEMATICAL_MOVES.md#arrows) preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.
- [The gradient stage](../MATHEMATICAL_MOVES.md#gradient) changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.

Only now can we compress that reasoning:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/035-tiny-neural-network/README.md).*

---

## Part IV — Building a Tiny GPT

The learner can change its weights when examples are already numerical. Real language does not arrive that way. We now follow one sentence from raw characters to tokens, positions, honest prediction lessons, vocabulary probabilities, and finally generation.

---

### Excavation 036 — Tokenization: What Can a Language Model See?

The tiny neural network now learns from numbered examples. People do not speak in fixed numerical columns; they produce an open stream of words, punctuation, names, code, and writing systems.

Perhaps we give every complete word one ID. Spaces appear to provide the boundaries.

Now we can see what is missing: we must use characters. Any new spelling can now be represented.

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

- **a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
- The star marks the pair selected for merging.
- **arg max** returns the pair itself, not its count, because that pair must be replaced.
- Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

##### Why these operations are forced

- [The first equality](../MATHEMATICAL_MOVES.md#equals) defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.
- [Arg max](../MATHEMATICAL_MOVES.md#arg-max) returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.
- [The star](../MATHEMATICAL_MOVES.md#symbol-decorations) marks the selected winner; it is a label on a and b, not multiplication or exponentiation.

Only now can we compress that reasoning:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\underset{(a,b)}{\text{arg max}} c(a,b)
$$

Early readers sound out letters. With experience they recognize recurring fragments and whole familiar words while retaining the ability to sound out something new.

#### Concrete Discovery

For low, lower, and lowest, the pair l-o repeats three times. Merge it into lo. The pair lo-w then repeats three times, so low becomes reusable. Nobody declared low meaningful; repetition made keeping it whole economical.

#### Limits

Tokenization chooses pieces, not meanings. IDs remain arbitrary, and the chosen vocabulary affects sequence length, cost, multilingual coverage, and which patterns are easy to notice.

Token IDs still contain no relationships. The next excavation must give tokens learnable coordinates and preserve their order.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/036-tokenization/README.md).*

---

### Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

Tokenization gives the machine repeatable pieces and assigns each piece an address. An address distinguishes tokens but says nothing about how their meanings should begin.

We first try to feed token IDs directly into the network. Since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one.

That failure tells us to give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.

A vocabulary of 50,000 tokens produces 50,000-dimensional vectors containing 49,999 zeros. Every distinct pair is equally distant. We preserved identity but learned no relationship.

The network needs a compact set of coordinates whose positions can change when prediction errors reveal useful relationships.

Let the embedding table contain one row for each vocabulary item:

The tokenizer assigns shelf address 2 to *tiger*. Looking up address 2 retrieves a small card of adjustable coordinates learned from tiger's usage. The address itself says nothing about meaning; moving the tiger card to shelf 7 would not change its learned contents. The table is therefore a collection of learned starting descriptions, while the token ID is merely the address used to fetch one.

- **V** is the vocabulary and **|V|** its number of token addresses.
- **d** is the compact representation width chosen for the model.
- **E** therefore needs one row per token and d learnable coordinates per row.
- **i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
- **e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.

Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

##### Why these operations are forced

- [E ∈ ℝ](../MATHEMATICAL_MOVES.md#membership) states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.
- [E[i]](../MATHEMATICAL_MOVES.md#indices) treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.
- [One-hot multiplication](../MATHEMATICAL_MOVES.md#multiplication) gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.

Only now can we compress that reasoning:

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

A library call number is not the book's meaning. It is an address used to retrieve the book. Token IDs are call numbers; embedding rows are the learnable content retrieved from the shelf.

#### How Learning Changes the Table

Suppose tiger repeatedly appears where danger, stripes, and hunting matter. Prediction errors send corrections into its row. Lion receives some similar corrections and some different ones. Their vectors may become nearby—not because their IDs were nearby, but because useful predictions demanded shared structure.

This reconnects to Excavation 007. There we needed geometry for meaning. Here we have finally installed that geometry as a trainable component inside the language model.

#### Limits

The same token initially retrieves the same row in every sentence. Bank beside river and bank beside money start from one vector. Attention will later contextualize it.

Worse, the embedding table contains no order. Swapping dog bites man with man bites dog selects the same three rows in a different sequence, but self-attention alone has no built-in idea that one row arrived first.

Tokens now have learnable coordinates, but no position. Excavation 038 must make order visible without confusing position with meaning.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/037-input-embeddings/README.md).*

---

### Excavation 038 — Position — Why Order Must Enter the Model

An embedding table gives every token a learned starting description. The sentences “dog bites man” and “man bites dog” still contain the same three descriptions, so the machine cannot tell who did what.

One tempting answer is to sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

So we add a position-specific vector to each token vector before attention. Content says what; position says where.

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

Compare “tiger chases deer” with “deer chases tiger.” The same three word cards appear, so content alone cannot distinguish hunter from hunted. Give the first slot one reusable position mark, the second another, and the third another. Adding the appropriate mark to each word leaves *tiger* recognizable while also telling later attention whether this occurrence came first or last.

- **token_i** is the vocabulary address appearing at sequence location i.
- **E[token_i]** retrieves what that token currently represents.
- **P_i** represents where the occurrence sits.
- Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
- **z_i** is the combined input at position i.

##### Why these operations are forced

- [Addition](../MATHEMATICAL_MOVES.md#addition) overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.
- [The shared index i](../MATHEMATICAL_MOVES.md#indices) forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.

Only now can we compress that reasoning:

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

Seat numbers do not describe passengers, but they preserve who sat where.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/038-position/README.md).*

---

### Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

At first we train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

We need to process all positions together while blocking attention from position i to every later position j.

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

##### Why these operations are forced

- [Cases](../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
- [j ≤ i and j > i](../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
- Zero leaves an allowed attention score unchanged. [Negative infinity](../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

Only now can we compress that reasoning:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/039-causal-mask/README.md).*

---

### Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.

Using what we have, we treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

Now we can see what is missing: we must shift the sequence by one position so every visible prefix predicts the token immediately following it.

Padding and document boundaries can create false targets unless their losses are masked.

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

##### Why these operations are forced

- [Parentheses](../MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
- [The shifted indices](../MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

A reading teacher pauses after every word, not only at the final period.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/040-next-token-examples/README.md).*

---

### Excavation 041 — Logits — Let Every Vocabulary Token Compete

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

An obvious shortcut is to choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

That failure tells us to use a learned linear map to produce one raw score for every vocabulary item.

Logits have no standalone probability meaning and can shift together without changing the final distribution.

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

##### Why these operations are forced

- [Multiplication by Wvocab](../MATHEMATICAL_MOVES.md#multiplication) lets every contextual feature contribute a learned amount to every vocabulary candidate's score.
- [The bias](../MATHEMATICAL_MOVES.md#addition) gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.
- The index i selects one output candidate; it does not mean the token with the largest ID should win. See [indices](../MATHEMATICAL_MOVES.md#indices).

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$

The equation arrives after every operation has a job.

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/041-logits/README.md).*

---

### Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; neither the reader nor the loss can treat them as comparable beliefs yet.

Perhaps we divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

So we exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

- **ℓ_i** is candidate i's raw score.
- Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
- **y** is the observed next-token index, so p_y is the probability assigned to what happened.
- The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

##### Why these operations are forced

- [Exponentials](../MATHEMATICAL_MOVES.md#exponential) create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.
- [Summing all weights](../MATHEMATICAL_MOVES.md#summation) measures the whole amount to be shared, and [division](../MATHEMATICAL_MOVES.md#division) turns each candidate's weight into a probability share.
- [The log](../MATHEMATICAL_MOVES.md#logarithm) turns the probability assigned to the observed token into additive information cost; [the minus sign](../MATHEMATICAL_MOVES.md#negative-sign) makes low probability expensive and certainty cost zero.

Only now can we compress that reasoning:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}}
$$

$$
L=-\log p_y
$$

The equation arrives after every operation has a job.

A race score becomes odds only after every competitor is considered together.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/042-vocabulary-probabilities/README.md).*

---

### Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

Softmax turns vocabulary scores into a distribution. Generation now faces a choice that training did not settle: should the machine always take the winner or sometimes follow another plausible continuation?

We first try to always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

We need to control the distribution with temperature and optionally restrict it to a credible top set before sampling.

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

- **ℓ_i** is candidate i's raw logit.
- **T** is temperature: dividing by T changes score gaps before exponentiation.
- T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
- Exponentiation preserves ranking while making evidence positive.
- Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

##### Why these operations are forced

- [Dividing every logit by T](../MATHEMATICAL_MOVES.md#division) changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.
- [Exponentiation](../MATHEMATICAL_MOVES.md#exponential) then turns the adjusted gaps into positive ratios, while [summing](../MATHEMATICAL_MOVES.md#summation) and dividing make one probability distribution.

Only now can we compress that reasoning:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$

The equation arrives after every operation has a job.

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/043-sampling/README.md).*

---

### Excavation 044 — Context Windows — How Much Past Can the Model Carry?

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

One tempting answer is to attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

Now we can see what is missing: we must choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

- **n** is the number of tokens inside the active context.
- Each of n queries can compare with n keys, creating roughly n×n score pairs.
- That repeated pairwise work is why cost grows proportionally to n² rather than n.
- The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

##### Why these operations are forced

- [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
- [The square](../MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

Only now can we compress that reasoning:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/044-context-window/README.md).*

---

### Excavation 045 — A Tiny GPT — Close the Prediction Loop

A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.

At first we call a framework Transformer and hide the causal chain. Or connect the parts without checking shapes, leakage, and target alignment.

That failure tells us to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program.

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

Begin with the prompt “the tiger.” Its token addresses fetch learned starting descriptions; position marks preserve order; masked attention gathers only allowed context; token workshops transform what was gathered; and the output scores every possible next word. Suppose sampling chooses *sleeps*. Appending that choice creates “the tiger sleeps,” and the same mechanism now faces a new prediction. The language model exists only when this entire loop closes.

- **tokens** are discrete addresses produced by the tokenizer.
- **embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
- **logits** score every next-token candidate; **loss** compares those scores with the observed answer.
- **update** changes parameters using backpropagated error.
- **sample** chooses a continuation and feeds it back as the next token.
- The arrows encode one closed causal loop, not an unexplained algebraic equality.

##### Why these operations are forced

- [Arrows](../MATHEMATICAL_MOVES.md#arrows) show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.
- The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.

Only now can we compress that reasoning:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$

The equation arrives after every operation has a job.

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

The mechanism now runs. The next excavations must test what it learned, where it fails, and how modern systems extend it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/045-tiny-gpt/README.md).*
