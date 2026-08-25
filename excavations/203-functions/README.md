# Excavation 203 — Functions — A Reusable Promise from Input to Output

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Relations preserve arbitrary connections. When the factory applies a tokenizer, matrix, filter, or model, however, repeating the same recorded input under the same state must not silently select two incompatible outputs.

The corridor toward Functions carries the unresolved consequence of the preceding excavation into a new physical scene.

At the vault's next table, each animal card enters a brass slot marked *measured weight*. Tiger enters twice. If the slot returns 220 kg once and 17 kg the next time, downstream comparison becomes impossible.

The chamber has reduced the abstraction to one physical thing: **a brass slot with one input door and one output chute**. The question carved beside it asks: *What promise lets the next machine trust the answer of this one?*

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

The failure and repair now form one continuous argument for Functions: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside functions

The symbols for functions will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Functions against the named case

The weight machine maps tiger to 220, deer to 90, and otter to 12. Tiger may be inserted repeatedly, but its arrow still lands on 220. Deer and another animal could both weigh 90 without violating the promise; the requirement concerns one output *per input*, not one private output per animal.

### Naming what is already on the table

**A** names the domain of allowed inputs and **B** the codomain in which outputs live. **f** names the complete mapping promise. **f(x)** is the unique output assigned to input x. The arrow records direction from domain to codomain rather than numerical equality.

### Why the melody needs these exact notes

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve the direction of the machine. [Function application](../../MATHEMATICAL_MOVES.md#function-application) asks for the output belonging to this input, and [equality](../../MATHEMATICAL_MOVES.md#equals) records the returned value. Allowing several outputs would describe a general relation, not the deterministic responsibility we need.

Every operation required by functions now has a visible job in the named case, so the complete construction can be written compactly:

$$
f:A\to B,\quad y=f(x)
$$

## A real-world echo

A function is a sealed promise: hand it an allowed question and it owes you one answer, even when many different questions happen to share that answer.

## What this unlocks elsewhere

Every layer in the neural network, every preprocessing stage, and every operation in the training factory is a function. Composition works only because each stage knows what object the preceding stage produces.

## Where the promise of functions breaks

A function promises an output but says nothing about which numerical description is most revealing. The same geometric object can receive different coordinates without becoming a different object.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Functions tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 204: Bases and Coordinates — The Same Object in Another Language](../204-bases-coordinates/README.md)
