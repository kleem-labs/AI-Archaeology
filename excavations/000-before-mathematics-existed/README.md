# Excavation 000 — Before Mathematics Existed

## Wake Up Before Mathematics

Imagine waking in a world with no numbers, no written language, no measuring instruments, and no inherited explanations. Nobody can tell you what a tiger is. The words *animal*, *four*, *orange*, and *dangerous* do not exist yet.

You still possess something: experience.

You see a striped creature near the river. Your body reacts before you can explain why. Days later, another striped creature appears. It is not the same creature—the scars differ and the tail is shorter—but you treat the two encounters as related.

That tiny act contains the seed of intelligence. You ignored thousands of differences and preserved a small pattern.

## Failed Attempt 1: Remember Reality Perfectly

Perhaps intelligence begins with perfect memory. Store every hair, shadow, sound, and smell from the first encounter, then compare the next creature with that memory.

This fails immediately:

- The sun is in a different position.
- The creature is viewed from the other side.
- Mud covers its legs.
- It is younger and smaller.
- No two moments contain exactly the same pixels, sounds, or smells.

Exact matching says that nothing is ever the same twice.

## Failed Attempt 2: Give Every Experience a Name

We could invent a separate name for every sight: `creature-1`, `creature-2`, and so on. This stores identity, but it creates no reusable knowledge. Knowing that `creature-438` attacked does not help with `creature-439` unless we can say how they are alike.

Names point. They do not generalize.

## The First Invention: Keep What Matters

From the overwhelming observation, you preserve a few regularities:

- It has stripes.
- It moves on four legs.
- It has long teeth.
- It stalks rather than grazes.
- Similar creatures have attacked before.

You have performed **compression**: replacing a huge experience with a smaller description.

Compression alone is not enough. A blurry photograph is compressed, but may discard the teeth that matter for survival. Intelligent compression preserves information useful for a future decision.

## A Worked Thought Experiment

Suppose you remember these facts about three creatures:

| Creature | Legs | Stripes | Long teeth | Stalks prey |
|---|---:|---:|---:|---:|
| A | 4 | yes | yes | yes |
| B | 4 | yes | no | no |
| C | 4 | no | yes | yes |

A new creature has four legs, stripes, long teeth, and stalks prey. Which past creature should guide your reaction?

Probably A. But notice what happened: before comparing creatures, you chose the questions in the table. The comparison depends on those choices.

If you had recorded only color, A and B might look identical. If you had recorded only leg count, all three would look identical. Representation comes before reasoning.

## The Three Decisions Hidden Inside Every Representation

Any intelligent system must decide:

1. **What to observe.** Is sound relevant? Temperature? Position?
2. **What to discard.** Which differences are noise for this task?
3. **What to preserve.** Which regularities may predict what happens next?

Modern AI still faces exactly these questions. Cameras provide pixels, microphones provide pressure measurements, and text systems receive tokens. None of those raw inputs arrives labeled with what matters.

## Common Misconception: “The Data Contains the Answer”

Data contains evidence, not a guaranteed representation. The same photograph can support many tasks: identify the animal, estimate its distance, judge the weather, or count trees. The useful information changes with the question.

There is no universally perfect description of an observation.

## Why There Is No Code Yet

The accompanying `implementation.py` is intentionally empty of computation. Code requires us to decide what values enter the machine. This chapter stops one step earlier, at the decision that makes all later code possible.

## What We Unearthed

- Intelligence requires generalizing across experiences that are never exactly identical.
- Generalization requires discarding some detail.
- Useful compression preserves information relevant to a goal.
- The questions we choose determine what the system can later discover.

The moment we turn those questions into repeatable measurements, we invent **features**.

---

Next: [Excavation 001 — Why Features Exist](../001-why-features-exist/README.md)
