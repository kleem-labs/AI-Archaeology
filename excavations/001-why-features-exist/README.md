# Excavation 001 — Why Features Exist

[Previous: Before Mathematics Existed](../000-before-mathematics-existed/README.md)


## Take the First Step Yourself

> **Your problem:** Which observations would you keep if the camp must identify dangerous animals?

> **Try your first idea:** Try stripes alone, then four legs alone. Test the rules on a zebra and an injured tiger.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

Your tribe now recognizes tigers. That is not enough. Ten animals are moving through the valley, and you must decide which ones threaten the camp.

For each animal you could remember the whole encounter: the exact light, every hair, every sound. But those details change even when the danger does not. Perfect memory gives you more information and less ability to compare.

## First attempt: use the name

“Tiger” is useful to a person who already understands the word. It gives a machine nothing it can measure. A name distinguishes one category from another; it does not explain what evidence created the category.

## Second attempt: choose one property

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

## The user's discovery

You did not say, “put every attribute together.” You said:

> Put similar attributes together and calculate their difference.

That word—*similar*—is essential. Weight must be compared with weight, speed with speed, and age with age. If the positions change meaning from one animal to the next, the arithmetic can be correct while the thought is nonsense.

| feature | tiger A | tiger B |
|---|---:|---:|
| weight | 220 | 225 |
| speed | 65 | 66 |
| age | 6 | 5 |

We have turned an animal into an organized set of comparable measurements. No formula was needed. The structure came first.

## A serious limitation

Features do not arrive objectively. Kilograms can overwhelm a binary stripe value simply because the numeric scales differ. A useful representation may omit an important clue or preserve a misleading one. Mathematics can only operate on what we decide to record.

## Challenge

For deciding whether an animal will reach camp soon, choose three useful features and one tempting but irrelevant detail. Explain the decision, not merely the list.

## What the next excavation needs

With thousands of animals and many features, separate facts become difficult to store and manipulate. We need one object that keeps their meaning through an agreed order.

[Next: Vectors](../002-vectors/README.md)
