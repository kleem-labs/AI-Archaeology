# Excavation 211 — Jacobians — When Many Outputs Change Together

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



The gradient gathers how one loss responds to many parameters. A network layer, camera transform, or robot model produces several outputs at once, each responding differently to every input.

Far below the Transformer, Jacobians begins with an ordinary situation and a tool that almost—but not quite—solves it.

A tracker converts two measurements—weight and stride—into two outputs: danger score and estimated speed. Changing weight affects both outputs, but not by the same amount.

The chamber has reduced the abstraction to one physical thing: **a wall of levers facing a wall of bells**. The question carved beside it asks: *How does every output respond when every input is allowed to move?*

With no standard method to recite, the most economical proposal is to differentiate only the first output and reuse that gradient as the sensitivity of the entire transformation.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. The second output's response disappears. Downstream uncertainty, volume change, and chain-rule propagation become wrong because one row of evidence impersonates the whole map.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Jacobians
```

The next idea is forced only because the evidence asks us to give every output its own gradient row and arrange all output-input sensitivities into one matrix.

The failure and repair now form one continuous argument for Jacobians: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside jacobians

The symbols for jacobians will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Jacobians against the named case

Suppose danger is `2w+s` and estimated speed is `w-s`. Increasing w by one changes the outputs by `[2,1]`; increasing s by one changes them by `[1,-1]`. Put the response to w in the first column and the response to s in the second. The resulting matrix `[[2,1],[1,-1]]` predicts the small output change produced by any small input change.

### Naming what is already on the table

**fᵢ** is output i and **xⱼ** input j. Each entry **∂fᵢ/∂xⱼ** asks how that particular output responds to that particular input. Row order preserves outputs; column order preserves inputs. **J** names the complete local linear map.

### Why the melody needs these exact notes

[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one output-input relationship. [Tables](../../MATHEMATICAL_MOVES.md#tables) preserve the exact row-column mapping, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets the Jacobian act on a small input change. A sum would collapse distinct outputs and inputs into one ambiguous sensitivity.

Every operation required by jacobians now has a visible job in the named case, so the complete construction can be written compactly:

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

## A real-world echo

A theatre lighting board has many sliders and many lamps. The Jacobian is the local wiring chart saying how each lamp responds to each slider.

## What this unlocks elsewhere

Backpropagation multiplies local Jacobian effects without usually materializing the full matrices; normalizing flows use Jacobian determinants; robustness asks how input perturbations propagate through this map.

## Where the promise of jacobians breaks

The Jacobian is a first-order description. Two landscapes can share the same slope at one point while bending into a bowl, ridge, or saddle immediately afterward.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Jacobians tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 212: Hessians and Curvature — Why the Same Slope Can Hide Different Valleys](../212-hessians-curvature/README.md)
