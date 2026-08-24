# Excavation 211 — Jacobians — When Many Outputs Change Together

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Mathematical roots beneath the machine

The gradient gathers how one loss responds to many parameters. A network layer, camera transform, or robot model produces several outputs at once, each responding differently to every input.

Far below the Transformer, the Undercroft stores no formula sheet. For **Jacobians**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

A tracker converts two measurements—weight and stride—into two outputs: danger score and estimated speed. Changing weight affects both outputs, but not by the same amount.

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

This is the hinge of the Jacobians excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Jacobians on the stone workbench

Suppose danger is `2w+s` and estimated speed is `w-s`. Increasing w by one changes the outputs by `[2,1]`; increasing s by one changes them by `[1,-1]`. Put the response to w in the first column and the response to s in the second. The resulting matrix `[[2,1],[1,-1]]` predicts the small output change produced by any small input change.

The point of keeping the objects named while rebuilding Jacobians is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside jacobians

Return to the named Jacobians scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**fᵢ** is output i and **xⱼ** input j. Each entry **∂fᵢ/∂xⱼ** asks how that particular output responds to that particular input. Row order preserves outputs; column order preserves inputs. **J** names the complete local linear map.

### Why the melody needs these exact notes

[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one output-input relationship. [Tables](../../MATHEMATICAL_MOVES.md#tables) preserve the exact row-column mapping, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets the Jacobian act on a small input change. A sum would collapse distinct outputs and inputs into one ambiguous sensitivity.

The operations inside Jacobians form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

Read the Jacobians line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A theatre lighting board has many sliders and many lamps. The Jacobian is the local wiring chart saying how each lamp responds to each slider.

That echo helps Jacobians remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Backpropagation multiplies local Jacobian effects without usually materializing the full matrices; normalizing flows use Jacobian determinants; robustness asks how input perturbations propagate through this map.

The older excavation and this Jacobians chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of jacobians breaks

The Jacobian is a first-order description. Two landscapes can share the same slope at one point while bending into a bowl, ridge, or saddle immediately afterward.

The boundary belongs beside the discovery of Jacobians because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Jacobians tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 212: Hessians and Curvature — Why the Same Slope Can Hide Different Valleys](../212-hessians-curvature/README.md)
