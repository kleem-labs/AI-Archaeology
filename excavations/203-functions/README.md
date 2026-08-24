# Excavation 203 — Functions — A Reusable Promise from Input to Output

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Mathematical roots beneath the machine

Relations preserve arbitrary connections. When the factory applies a tokenizer, matrix, filter, or model, however, repeating the same recorded input under the same state must not silently select two incompatible outputs.

The corridor bends beneath every model we have built. Here **Functions** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.

At the vault's next table, each animal card enters a brass slot marked *measured weight*. Tiger enters twice. If the slot returns 220 kg once and 17 kg the next time, downstream comparison becomes impossible.

If we were the first people in this chamber, we would probably keep any relation between inputs and outputs, then choose one of the available outputs whenever the procedure runs.

We let the idea touch the evidence. The fracture appears exactly where information was lost. The relation may omit an input entirely or attach several outputs to it. A reusable procedure cannot promise what it will do, and composition breaks because the next machine may receive nothing or an arbitrary value.

```text
             what the world shows
                      │
         ┌────────────┴────────────┐
         │                         │
   old explanation           counterexample
         │                         │
         └──────── breaks ─────────┘
                      │
               repair the promise
                      │
                    Functions
```

The broken attempt has done its work. It tells us, in ordinary language, to require every allowed input to point to exactly one output, while permitting different inputs to share the same output.

This is the hinge of the Functions excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Functions on the stone workbench

The weight machine maps tiger to 220, deer to 90, and otter to 12. Tiger may be inserted repeatedly, but its arrow still lands on 220. Deer and another animal could both weigh 90 without violating the promise; the requirement concerns one output *per input*, not one private output per animal.

The point of keeping the objects named while rebuilding Functions is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside functions

Return to the named Functions scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**A** names the domain of allowed inputs and **B** the codomain in which outputs live. **f** names the complete mapping promise. **f(x)** is the unique output assigned to input x. The arrow records direction from domain to codomain rather than numerical equality.

### Why the melody needs these exact notes

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve the direction of the machine. [Function application](../../MATHEMATICAL_MOVES.md#function-application) asks for the output belonging to this input, and [equality](../../MATHEMATICAL_MOVES.md#equals) records the returned value. Allowing several outputs would describe a general relation, not the deterministic responsibility we need.

The operations inside Functions form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f:A\to B,\quad y=f(x)
$$

Read the Functions line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A function is a sealed promise: hand it an allowed question and it owes you one answer, even when many different questions happen to share that answer.

That echo helps Functions remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Every layer in the neural network, every preprocessing stage, and every operation in the training factory is a function. Composition works only because each stage knows what object the preceding stage produces.

The older excavation and this Functions chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of functions breaks

A function promises an output but says nothing about which numerical description is most revealing. The same geometric object can receive different coordinates without becoming a different object.

The boundary belongs beside the discovery of Functions because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Functions tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 204: Bases and Coordinates — The Same Object in Another Language](../204-bases-coordinates/README.md)
