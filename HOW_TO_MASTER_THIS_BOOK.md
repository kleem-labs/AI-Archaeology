# How to Master AI Archaeology

This repository is not meant to be consumed like documentation. It is meant to
be **reconstructed**.

The goal is not to remember that distance uses a square root, attention uses a
dot product, or learning uses a gradient. The goal is to become the person who
could recover those ideas after their names and formulas had been erased.

By the end, a chapter should live in you as a causal film:

```text
observation
    ↓
your attempted invention
    ↓
the smallest case that breaks it
    ↓
the missing responsibility you discover
    ↓
the concrete repair
    ↓
the equation as a compressed memory
    ↓
code, experiment, boundary, connection
```

This guide explains how to make that happen.

## Begin here

Use these surfaces in this order:

1. [The six-volume book](book/README.md) gives you the uninterrupted story.
2. The matching [excavation folder](excavations/000-before-mathematics-existed/README.md) gives you code, diagrams, mistakes, exercises, references, and visual material.
3. The [Memory Palace](MEMORY_PALACE.md) lets you recover the discovery from one transforming object.
4. The [Laboratory](LABORATORY.md) lets reality challenge what you think you understood.
5. The [Mathematical Gist](MATHEMATICAL_GIST.md) becomes useful after derivation, when you want the ordered mathematical spine.
6. [Mathematical Moves](MATHEMATICAL_MOVES.md) explains why an operation adds, multiplies, divides, squares, logs, differentiates, or chooses a maximum.
7. The [Mathematical Mandala](math-mandala/README.md) shows how equations depend on one another.
8. The [Mathematics Atlas](MATHEMATICS_ATLAS.md) reorganizes the journey into calculus, probability, linear algebra, optimization, and the other traditional families.

Do not begin with the Gist, Mandala, or Atlas. They are maps of territory you
must first walk. Begin with [Excavation 000](excavations/000-before-mathematics-existed/README.md).

## The three passages through the book

Trying to read the prose, master every equation, run three implementations,
finish every exercise, and memorize every connection in one sitting creates
exhaustion rather than depth. Walk through each part three times with different
purposes.

### Passage I — Discovery

Read in excavation order. Your job is to feel the pressure that creates the
idea.

Keep the formal solution covered as long as possible. Make a real proposal,
let the counterexample defeat it, and state what the repaired idea must preserve
before accepting the chapter's answer.

At the end, close the file and replay its five-frame memory film:

```text
question → object → visible failure → transformation → memory seal
```

You are ready to continue when you can explain why the previous chapter was no
longer enough.

### Passage II — Construction

Return to the excavation folders. Work the named numerical example on paper,
then build the idea in three stages:

1. **Pure Python:** lists, loops, conditions, and explicit intermediate values. This reveals the mechanism.
2. **NumPy:** arrays and matrix operations. This reveals the mathematical structure.
3. **PyTorch:** tensors and trainable machinery. This reveals how the idea enters modern AI systems.

Before running code, predict its important intermediate values. After running
it, change one input until the old failure reappears. Code that merely prints
the expected answer has not yet become an experiment.

### Passage III — Retrieval and transfer

Now remove the chapter from view. Start from its physical object in the Memory
Palace and reconstruct:

- the human question;
- your tempting attempt;
- the counterexample;
- the missing responsibility;
- the reason for every mathematical operation;
- the equation;
- the implementation idea;
- the boundary where the invention stops helping;
- the next chapter it makes necessary.

Then invent a different real-world situation that needs the same mathematical
promise. If distance exists only for two tigers in your memory, you remember an
example. If you can reinvent it for patients, songs, stars, or search results,
you possess the idea.

## The chapter ritual

Use this ritual for every excavation. A first discovery session usually takes
30–60 minutes. A full construction session may take another 45–120 minutes.

### 1. Enter with empty hands

Read the opening observation and problem. Do not search the chapter for its
equation. In your notebook, describe what the people in the scene can actually
observe without using the mathematical name.

Ask:

> If humanity had never solved this, what would I try first?

Write one concrete procedure. “Use vectors” is not a procedure. “Record each
animal's weight, speed, and age in the same order” is.

### 2. Commit to your attempt

Do not keep the proposal vague enough to escape criticism. Give it a small,
named example and calculate or simulate what it would do.

This matters because an untested idea can always pretend it meant something
else. A precise attempt can teach you through its wreckage.

### 3. Let the smallest counterexample break it

Read the failure only after making your prediction. Identify the exact lost
information or false assumption.

Do not write “it does not work.” Write something such as:

> Weight disagreement and age disagreement cancel because I added signed
> differences. Two visibly different tigers therefore received zero
> separation.

That sentence is the real beginning of the mathematics.

### 4. Name the missing responsibility

Before reading the accepted repair, complete this sentence:

> Whatever I invent next must preserve __________.

Examples include direction, order, uncertainty, shared evidence, scale,
authority, causal responsibility, or numerical range. Do not name a standard
technique yet. Name the job.

### 5. Rebuild the repair with named objects

Use tiger height, river flow, lantern brightness, token position, model loss,
or another object already present in the scene. Follow each operation on those
objects.

If a symbol cannot be translated into a visible object or action, it has
arrived too early.

### 6. Earn every mark in the equation

For each symbol and operation, answer four questions:

1. What concrete thing does it name?
2. Which failure forced it to appear?
3. Why is this operation used rather than a plausible alternative?
4. What wrong human conclusion would follow if it were removed?

For example, do not stop at “we divide by batch size.” Explain that adding ten
witnesses should make the direction less noisy, not make the step ten times
larger merely because more witnesses entered the room.

Only after every answer is clear should you write the complete equation from
memory.

### 7. Cross the three code bridges

Open the chapter's `implementation` folder.

- In Pure Python, point to the line performing every human responsibility.
- In NumPy, identify which loops contracted into array operations.
- In PyTorch, identify which values may learn, which operations remain fixed, and what industrial convenience is being supplied.

Change the example. Break the implementation deliberately. Restore the missing
invariant. The code becomes yours when you can predict the break before running
it.

### 8. Attempt the invention exercises

Write before executing. The exercises are not quizzes about vocabulary; they
ask whether you can invent under new pressure.

Keep wrong answers in `mistakes.md` spirit: record why the idea was attractive,
the case that defeated it, and what requirement its failure exposed.

### 9. Close the chamber

Close the chapter and use only the Memory Palace object. Replay all five frames
and perform the chapter's gesture. Then walk backward:

```text
memory seal → transformation → failure → object → original question
```

Forward recall checks familiarity. Backward recall checks whether the causal
structure is truly connected.

### 10. Connect without flattening

Only now open the Gist, Moves guide, Mandala, and Atlas.

- Use the **Gist** to place the equation in discovery order.
- Use **Mathematical Moves** to compare this use of an operation with its uses elsewhere.
- Use the **Mandala** to follow dependencies between equations.
- Use the **Atlas** to learn the traditional mathematical family.

The chapter should remain a living discovery even after it acquires an academic
address.

## The mastery ladder

Mark a chapter by the highest level you can perform without looking.

| Level | Evidence |
|---:|---|
| 0 — Recognize | You recognize the term or equation when shown. |
| 1 — Retell | You can replay the chapter's five-frame film. |
| 2 — Reconstruct | You can derive the repair and explain every term and operation. |
| 3 — Build | You can implement and test the idea without copying the finished code. |
| 4 — Transfer | You can recognize and solve a new problem requiring the same promise. |
| 5 — Teach | Another reader can reconstruct the idea from your explanation without being handed the formula. |

Recognition is not mastery. A chapter is operationally mastered at Level 4.
Level 5 makes the knowledge durable and shareable.

Record progress in the [Mastery Ledger](MASTERY_LEDGER.md).

## The recall rhythm

Memory strengthens when retrieval is difficult but still possible. Review each
chapter on this rhythm:

| When | What to reconstruct without looking |
|---|---|
| End of the first session | The five-frame film and the next unmet need |
| One day later | The counterexample, repair, and equation |
| Three days later | The Pure Python mechanism on changed numbers |
| One week later | The film backward and one new analogy |
| Three weeks later | The equation from the human need and every operation's job |
| Two months later | A new application, implementation sketch, and connection to two other chapters |

Do not reread first. Attempt retrieval, mark the missing link, and reread only
that portion. Difficulty during recall is not evidence of failure; it is the
event that strengthens the path.

## When to leave a chapter

Continue to the next excavation when you can do all of the following:

- state the opening problem without the formal term;
- reproduce the tempting attempt;
- give the counterexample that breaks it;
- name the missing responsibility in ordinary language;
- explain every operation in the equation using the named example;
- predict what the Pure Python implementation will do;
- state the invention's honest boundary;
- explain why that boundary creates the next chapter.

You do not need Level 5 before continuing. Reach Level 2 during discovery,
Level 3 during construction, then use scheduled retrieval to reach Levels 4 and
5.

## Checkpoints at the end of a part

Do not immediately begin the next part. Spend one session rebuilding the arc
you just completed.

1. Draw the dependency chain from memory.
2. Explain how every excavation was forced by the previous one's boundary.
3. Choose three equations and derive them without notes.
4. Run or extend the relevant field lab.
5. Walk the part's chambers in the Memory Palace without opening the chapters.
6. Teach the part as one story to an imaginary first human who knows none of its terminology.

If one chapter floats as an isolated fact, return to its failure and reconnect
it on both sides.

## Choose a sustainable pace

Depth matters more than speed.

| Route | New excavations | Construction and review | Approximate character |
|---|---:|---|---|
| Contemplative | 2–3 per week | one long laboratory session | deepest reflection and note-making |
| Steady | 4–6 per week | two construction sessions | sustainable alongside work or study |
| Intensive | 8–10 per week | daily coding and recall | demanding full-time study |

These are new-chapter counts, not total study sessions. Every route includes
older retrieval. Slowing down when calculus, probability, or implementation
becomes unfamiliar is correct; the dependency chain is telling you where a
foundation needs reinforcement.

## If you become stuck

Use the smallest tool that restores discovery:

1. Return from symbols to the named physical object.
2. Run the naive attempt on the smallest counterexample.
3. Read the chapter's `mistakes.md` without reading the correct equation.
4. Inspect `diagram.md` and predict the final frame.
5. Run `pure_python.py` and print every intermediate value.
6. Follow one unfamiliar operation into [Mathematical Moves](MATHEMATICAL_MOVES.md).
7. Return to the prerequisite chapter through the Mandala or chapter connection.

Never punish confusion by reading faster. Confusion usually identifies the
exact relationship that has not yet become concrete.

## Two ways not to use this repository

Do not memorize the Mathematical Gist before deriving the chapters. That turns
compressed conclusions into disconnected marks.

Do not run every implementation and call the successful output understanding.
Execution proves that the stored code works. Prediction, modification, failure,
and repair show that the mechanism has entered your reasoning.

## The final test

When you finish the repository, choose an unfamiliar intelligent system—a
search engine, recommender, image generator, language model, robot, or agent.
Without looking at the book:

1. begin from its observations;
2. reconstruct the representations it needs;
3. identify how relevance, uncertainty, learning, action, evidence, and authority enter;
4. derive the essential equations from their human jobs;
5. sketch the Pure Python mechanisms;
6. name the system's failure boundaries and the experiments needed to test them;
7. place every mathematical dependency in your remembered palace.

If you can do that, you have not merely finished AI Archaeology. You have
learned how to excavate ideas that are not in the book yet.
