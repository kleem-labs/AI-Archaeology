# Volume VI — We Descend to the Mathematical Roots

The accountable machine is complete. We descend beneath it to recover the older mathematical inventions—sets, spaces, change, uncertainty, evidence, decisions, optimization, and stable computation—as necessities a reader could have discovered.

One discovery will create the need for the next; the object under construction never resets.

## Overture

The sixth volume descends into the Undercroft of First Principles. Familiar names are covered. Sets, functions, linear algebra, calculus, probability, statistics, decision theory, and numerical analysis must be recovered from concrete failures before their symbols are allowed to return.

```text
observation → attempt → fracture → repair → symbol → connected memory
```

In this volume:

- [Part XIV — The Mathematical Roots Beneath the Machine](#part-xiv--the-mathematical-roots-beneath-the-machine)

---

## Part XIV — The Mathematical Roots Beneath the Machine

The complete AI system has been using an older inheritance. We uncover that inheritance from lived problems: how objects belong, how spaces hold directions, how change accumulates, how uncertainty becomes evidence, how futures are valued, and how exact ideas survive finite machines.

---

### Excavation 201 — Sets — Drawing a Boundary Around ‘Belongs’

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

The accountable factory can trace every document and gate. Its ledgers repeatedly say that a document belongs to a corpus, a token belongs to a vocabulary, or a release belongs to the approved collection, yet we have never excavated what *belongs* must mean.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Sets** has been covered so that only the unsolved situation remains.

Below the Archive Foundry, a circular vault contains three stone trays: **observed animals**, **animals near water**, and **all recorded animals**. The archivist places tiger, deer, and otter cards on the floor and asks which trays should receive each card.

The first move is honest because it uses the nearest tool already in our hands: **write each tray as an ordinary list and scan every position whenever membership, overlap, or exclusion is questioned**.

The proposal deserves a real trial, not a ceremonial rejection. The same animal can occur twice, order pretends to matter, and asking which animals occupy both trays requires a new hand-written loop every time. The list stores a sequence; the question concerns a boundary.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Sets
```

Now the reader can name the requirement before the textbook can name the method: we must treat each tray as a collection whose identity depends on membership rather than order or repetition, then construct overlap by retaining exactly the objects admitted by both boundaries.

This is the hinge of the Sets excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Sets on the stone workbench

Let the observed tray contain tiger, deer, and otter. Let the near-water tray contain tiger, otter, and frog. Put each named animal against both boundaries. Tiger passes both tests; otter passes both; deer fails the water boundary; frog fails the observed boundary. The overlap is therefore `{tiger, otter}`—not because we memorized an intersection rule, but because those are the only cards that survive both questions.

The point of keeping the objects named while rebuilding Sets is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside sets

Return to the named Sets scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**A** names the observed-animal set and **B** the near-water set. **x ∈ A** says the card named x passes A's boundary. **A ∩ B** names the new set formed by the cards that pass both boundaries. The double arrow says the two descriptions admit exactly the same cards.

##### Why the melody needs these exact notes

[Membership](../MATHEMATICAL_MOVES.md#membership) asks one yes-or-no boundary question. [Intersection](../MATHEMATICAL_MOVES.md#intersection) retains only shared members, and [logical and](../MATHEMATICAL_MOVES.md#logical-and) requires both tests to succeed. A union would answer ‘in either tray’; counting would report a size while forgetting which animals survived.

The operations inside Sets form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
x\in A\cap B\Longleftrightarrow (x\in A)\text{ and }(x\in B)
$$

Read the Sets line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A guest list, an allowed tool set, and a dataset split all perform the same act: they draw a boundary and make admission inspectable.

That echo helps Sets remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

The corpus manifest in Excavation 176 was already acting like a set. The authority boundary in Excavation 056 was too. Sets reveal the quiet skeleton shared by data and permission.

The older excavation and this Sets chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of sets breaks

A set can say which objects belong, but not how one member is connected to another. Flattening a road map or knowledge graph into membership alone destroys its edges.

The boundary belongs beside the discovery of Sets because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/201-sets/README.md).*

---

### Excavation 202 — Relations — When Two Objects Are Connected

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Graphs & Relational Structures](../MATHEMATICS_ATLAS.md#graphs) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Sets give the vault honest boundaries. The animal cards can now belong to villages, habitats, and observation days, but separate membership lists cannot preserve statements such as ‘tiger was seen beside river’ or ‘report cites photograph.’

In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **Relations**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.

The stone floor becomes a map. Cards name tiger, river, cave, and village; lengths of red thread record *near*, while blue thread records *reported-by*. The objects matter, but the colored pairings carry the new information.

Nothing yet suggests a new invention. We naturally place connected objects in the same set and assume co-membership tells us the nature and direction of their connection.

For a moment the shortcut feels complete. Then the smallest contrary case arrives. Putting tiger, river, and village into one collection cannot distinguish tiger-near-river from village-reports-tiger. It also cannot distinguish an arrow from tiger to river from the reverse arrow.

```text
observation
    ↓
our own proposal ──▶ test case ──▶ impossible answer
                                      ↓
                              preserve what vanished
                                      ↓
                                    Relations
```

What survives the failure is a precise demand. The repaired construction must store each connection as an ordered pair and let a named relation be the set of all pairs carrying the same kind of edge.

This is the hinge of the Relations excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Relations on the stone workbench

For the relation *near*, lay down `(tiger, river)` and `(otter, river)`. For *reported-by*, lay down `(tiger, village)`. The first position names the object the arrow leaves; the second names where it arrives. Swapping the positions produces a different claim, which is exactly why the pair must be ordered.

The point of keeping the objects named while rebuilding Relations is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside relations

Return to the named Relations scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**A** is the set of animals and **B** the set of places. **A × B** means all animal-place pairs that could be considered. **R** keeps only the pairs for which the named relationship is true. **(a,b) ∈ R** says that one particular directed edge exists.

##### Why the melody needs these exact notes

[Tuples](../MATHEMATICAL_MOVES.md#tuples) preserve first and second position, so direction survives. [Membership](../MATHEMATICAL_MOVES.md#membership) says whether a proposed edge belongs to the relation. A flat union would preserve the endpoints but erase which endpoint was paired with which.

The operations inside Relations form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
R\subseteq A\times B,\quad (a,b)\in R
$$

Read the Relations line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A railway map is not the set of cities printed on it. Its meaning lives in the ordered connections showing which journey can follow which.

That echo helps Relations remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Attention masks, provenance graphs, knowledge graphs, and state transitions were all relations before we used that name. Their arrows were mathematical objects, not decoration.

The older excavation and this Relations chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of relations breaks

A relation may connect one input to no outputs, one output, or many incompatible outputs. A deterministic machine needs a stronger promise about what follows from each allowed input.

The boundary belongs beside the discovery of Relations because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/202-relations/README.md).*

---

### Excavation 203 — Functions — A Reusable Promise from Input to Output

> **Mathematical roots:** [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
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

#### Functions on the stone workbench

The weight machine maps tiger to 220, deer to 90, and otter to 12. Tiger may be inserted repeatedly, but its arrow still lands on 220. Deer and another animal could both weigh 90 without violating the promise; the requirement concerns one output *per input*, not one private output per animal.

The point of keeping the objects named while rebuilding Functions is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside functions

Return to the named Functions scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**A** names the domain of allowed inputs and **B** the codomain in which outputs live. **f** names the complete mapping promise. **f(x)** is the unique output assigned to input x. The arrow records direction from domain to codomain rather than numerical equality.

##### Why the melody needs these exact notes

[Arrows](../MATHEMATICAL_MOVES.md#arrows) preserve the direction of the machine. [Function application](../MATHEMATICAL_MOVES.md#function-application) asks for the output belonging to this input, and [equality](../MATHEMATICAL_MOVES.md#equals) records the returned value. Allowing several outputs would describe a general relation, not the deterministic responsibility we need.

The operations inside Functions form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f:A\to B,\quad y=f(x)
$$

Read the Functions line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A function is a sealed promise: hand it an allowed question and it owes you one answer, even when many different questions happen to share that answer.

That echo helps Functions remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Every layer in the neural network, every preprocessing stage, and every operation in the training factory is a function. Composition works only because each stage knows what object the preceding stage produces.

The older excavation and this Functions chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of functions breaks

A function promises an output but says nothing about which numerical description is most revealing. The same geometric object can receive different coordinates without becoming a different object.

The boundary belongs beside the discovery of Functions because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/203-functions/README.md).*

---

### Excavation 204 — Bases and Coordinates — The Same Object in Another Language

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Functions turn inputs into dependable outputs. Our vector functions seem to operate directly on lists of coordinates, yet rotating the ruler changes every coordinate while leaving the animal's physical displacement untouched.

Another vault door opens. The carving that once named **Bases and Coordinates** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

A ranger walks three steps east and two north. On the square floor this is recorded as `[3,2]`. Another ranger carries diagonal rulers: one points northeast, the other northwest. The same walk must acquire different numbers in that language.

The old machinery invites a plausible shortcut: treat the coordinate list as the vector itself and conclude that changing the list changes the underlying displacement.

The stone does not object with terminology; it objects with a result we already know cannot be right. The east-north list `[3,2]` and its diagonal-coordinate list disagree numerically even though both return the ranger to the same physical endpoint. Coordinates depend on the chosen measuring directions.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Bases and Coordinates
```

We do not leap to a famous formula. We carry one missing responsibility forward: choose a set of basis directions and define coordinates as the amounts of those directions whose combination reconstructs the vector.

This is the hinge of the Bases and Coordinates excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Bases and Coordinates on the stone workbench

With basis arrows east `[1,0]` and north `[0,1]`, the walk is `3 east + 2 north`. If the new basis uses northeast `[1,1]` and northwest `[-1,1]`, then `2.5 northeast - 0.5 northwest` reconstructs `[3,2]`. The coefficients changed; the endpoint did not.

The point of keeping the objects named while rebuilding Bases and Coordinates is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside bases and coordinates

Return to the named Bases and Coordinates scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**v** is the displacement being described. **b₁,…,bₙ** are the chosen basis directions. **c₁,…,cₙ** are coordinates in that basis. Multiplying a basis direction by its coordinate stretches or reverses it; adding the contributions reconstructs v.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales each basis direction by the amount required. [Addition](../MATHEMATICAL_MOVES.md#addition) joins independent directional contributions. Concatenating the numbers would merely store them side by side and would not reconstruct the displacement.

The operations inside Bases and Coordinates form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\mathbf v=c_1\mathbf b_1+c_2\mathbf b_2+\cdots+c_n\mathbf b_n
$$

Read the Bases and Coordinates line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

The same melody can be written for piano or violin. The marks change because the instrument's basis changes; the melody's relationships survive.

That echo helps Bases and Coordinates remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Embeddings choose learned coordinates, attention projects them into query and key bases, and RoPE rotates coordinate pairs. A representation is always a choice of mathematical language.

The older excavation and this Bases and Coordinates chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of bases and coordinates breaks

A collection of candidate basis directions may contain redundancy or fail to reach part of the space. We need to know which directions are genuinely new and what region their combinations can cover.

The boundary belongs beside the discovery of Bases and Coordinates because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/204-bases-coordinates/README.md).*

---

### Excavation 205 — Span and Linear Independence — Which Directions Are Truly New?

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

A basis gives coordinates meaning only if its directions reach the required space without secretly repeating one another. Adding more arrows to the table can create the appearance of capacity while contributing no new possible movement.

Far below the Transformer, the Undercroft stores no formula sheet. For **Span and Linear Independence**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

The cartographer offers east `[1,0]`, north `[0,1]`, and northeast `[1,1]` as three foundational directions on a two-dimensional map. The third feels useful, but the first two can already reconstruct it.

With no standard method to recite, the most economical proposal is to count every stored direction as a new dimension and assign each one an independent coordinate.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. Northeast equals east plus north, so the same displacement receives many coefficient lists. The coordinate system can no longer tell which explanation is unique, and parameter count exaggerates true capacity.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Span and Linear Independence
```

The next idea is forced only because the evidence asks us to call the reachable collection of combinations the span, and call directions independent only when no nontrivial weighted combination collapses to zero.

This is the hinge of the Span and Linear Independence excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Span and Linear Independence on the stone workbench

Ask whether `a·east + b·north + c·northeast` can return to `[0,0]` without all weights being zero. Choosing `a=-1`, `b=-1`, and `c=1` does exactly that. Northeast therefore adds no new reachable point. East and north alone span the entire floor and give each displacement one coordinate pair.

The point of keeping the objects named while rebuilding Span and Linear Independence is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside span and linear independence

Return to the named Span and Linear Independence scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**span(v₁,…,vₖ)** is every vector obtainable by scaling and adding the listed directions. **aᵢ** are proposed weights. The zero vector represents no movement. If the only weights producing zero are all zero, no direction can be reconstructed from the others.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales candidate directions and [summation](../MATHEMATICAL_MOVES.md#summation) combines them. [Equality](../MATHEMATICAL_MOVES.md#equals) asks whether the combination collapses to zero. Merely counting vectors cannot detect that one is already contained in the others' span.

The operations inside Span and Linear Independence form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
a_1\mathbf v_1+\cdots+a_k\mathbf v_k=\mathbf0\Longrightarrow a_1=\cdots=a_k=0
$$

Read the Span and Linear Independence line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

Three keys on a ring do not open three doors when one key is only a copy. Independence counts new access, not metal objects.

That echo helps Span and Linear Independence remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Superposition asks how many useful feature directions share a space; LoRA asks how many update directions are actually needed. Rank and independence make those capacity claims precise.

The older excavation and this Span and Linear Independence chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of span and linear independence breaks

Independence tells which directions are new but not how a transformation repeatedly stretches the space. Some directions persist under repeated application while others turn and mix.

The boundary belongs beside the discovery of Span and Linear Independence because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/205-span-linear-independence/README.md).*

---

### Excavation 206 — Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Mathematical roots beneath the machine

Span and independence reveal the true directions available in a space. When one matrix is applied again and again—one transition, message-passing step, or layer after another—the coordinate picture can still become difficult to follow.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Eigenvectors and Eigenvalues** first as an ordinary human need, before anyone has decided what marks should record it.

On the vault floor, a transformation doubles east-west displacement but leaves north-south displacement unchanged. Most arrows change both length and direction. An arrow pointing exactly east does something quieter: it remains east and only stretches.

We try to spend no new mathematics at all and simply track every coordinate of every repeatedly transformed arrow and hope the long-term pattern becomes obvious.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. Coordinate expressions grow while the persistent behavior stays hidden. Two initial arrows can look unrelated even when repeated transformation eventually makes both align with the same dominant direction.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Eigenvectors and Eigenvalues becomes necessary
```

At last there is something worth inventing. Whatever we build must search for nonzero directions that the transformation only scales, and record the corresponding scale factors.

This is the hinge of the Eigenvectors and Eigenvalues excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Eigenvectors and Eigenvalues on the stone workbench

Apply the matrix `[[2,0],[0,1]]` to east `[1,0]`: the result is `[2,0]`, exactly twice east. Apply it to north `[0,1]`: the result remains north. East has scale 2 and north scale 1. Apply it repeatedly and any arrow with an east component becomes increasingly east-dominated.

The point of keeping the objects named while rebuilding Eigenvectors and Eigenvalues is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside eigenvectors and eigenvalues

Return to the named Eigenvectors and Eigenvalues scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**A** is the transformation. **v** is a nonzero direction. **λ** is the scalar stretch, shrinkage, or sign reversal. Equality says transforming v and merely scaling v reach the same arrow, so direction is preserved.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) applies the transformation to the direction. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales that same direction, and [equality](../MATHEMATICAL_MOVES.md#equals) demands the two routes coincide. Adding λ would translate the arrow rather than describe proportional stretching.

The operations inside Eigenvectors and Eigenvalues form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
A\mathbf v=\lambda\mathbf v
$$

Read the Eigenvectors and Eigenvalues line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

In a river, most leaves swirl, but a leaf placed on the main current keeps pointing downstream while its distance from the bridge changes predictably.

That echo helps Eigenvectors and Eigenvalues remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

PageRank studies a persistent direction of repeated link transitions; covariance eigenvectors become principal directions; training stability depends on repeated transformations' spectral behavior.

The older excavation and this Eigenvectors and Eigenvalues chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of eigenvectors and eigenvalues breaks

Not every matrix has enough real eigenvectors to form a basis, and rectangular matrices do not even map a space back into itself. We still need a way to cast the closest shadow and expose the important input-output directions of any matrix.

The boundary belongs beside the discovery of Eigenvectors and Eigenvalues because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/206-eigenvectors-eigenvalues/README.md).*

---

### Excavation 207 — Orthogonality and Projection — Finding the Closest Shadow

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Eigenvectors expose directions preserved by a transformation. The vault now presents a simpler geometric failure: an observed arrow does not lie on the one-dimensional rail our model is allowed to use.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Orthogonality and Projection** has been covered so that only the unsolved situation remains.

A tiger track points `[3,2]`, but the ranger's simplified map retains only the eastward rail `[1,0]`. We need the point on that rail that misrepresents the track as little as possible.

The first move is honest because it uses the nearest tool already in our hands: **copy whichever coordinate looks largest or slide to an arbitrary point on the allowed rail**.

The proposal deserves a real trial, not a ceremonial rejection. The chosen point changes when coordinates are renamed and gives no proof that another allowed point is not closer. The discarded error may still point partly along the rail, revealing that more of the track could have been retained.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Orthogonality and Projection
```

Now the reader can name the requirement before the textbook can name the method: we must choose the shadow whose leftover error is perpendicular to the allowed direction, because then no further movement along the rail can reduce the distance.

This is the hinge of the Orthogonality and Projection excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Orthogonality and Projection on the stone workbench

Project `[3,2]` onto east `[1,0]`. Their dot product is 3; east's dot product with itself is 1; the required scale is therefore 3. The shadow is `[3,0]`, leaving error `[0,2]`. That error has zero dot product with east, so every remaining disagreement points outside the allowed rail.

The point of keeping the objects named while rebuilding Orthogonality and Projection is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside orthogonality and projection

Return to the named Orthogonality and Projection scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**v** is the observed track and **u** the allowed direction. **v·u** measures alignment; **u·u** measures u's squared length. Their ratio finds how much u fits inside v. Multiplying u by that ratio constructs the shadow.

##### Why the melody needs these exact notes

[The dot product](../MATHEMATICAL_MOVES.md#dot-product) measures directional agreement. [Division](../MATHEMATICAL_MOVES.md#division) removes dependence on the chosen length of u, and [multiplication](../MATHEMATICAL_MOVES.md#multiplication) rebuilds the shadow in the allowed direction. Using raw v·u alone would change the answer if the same rail were described by a longer basis arrow.

The operations inside Orthogonality and Projection form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\mathrm{proj}_{\mathbf u}(\mathbf v)=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u
$$

Read the Orthogonality and Projection line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A sundial's shadow is not the object, but under a fixed light it is the closest information the ground plane can retain.

That echo helps Orthogonality and Projection remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Linear probes project hidden states onto readable directions; least squares projects observations into a model subspace; attention projects embeddings into query, key, and value spaces.

The older excavation and this Orthogonality and Projection chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of orthogonality and projection breaks

Projection handles one chosen subspace. For an arbitrary rectangular matrix, we still need to discover the paired input and output directions that carry most of its action.

The boundary belongs beside the discovery of Orthogonality and Projection because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/207-orthogonality-projection/README.md).*

---

### Excavation 208 — Singular Value Decomposition — The Important Directions of Any Matrix

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Mathematical roots beneath the machine

Projection finds the closest shadow once an allowed direction is known. A large weight matrix offers thousands of possible directions, and neither its raw entries nor ordinary eigenvectors tell us which input directions carry most strongly into which output directions.

In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **Singular Value Decomposition**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.

The enginewright lowers a rectangular brass plate with many input grooves and fewer output bells. Some coordinated pushes ring loudly; others barely move the mechanism. We want the simplest faithful account of those channels.

Nothing yet suggests a new invention. We naturally keep the largest individual matrix entries and set the rest to zero.

For a moment the shortcut feels complete. Then the smallest contrary case arrives. A useful direction may be distributed across many modest entries, while one large entry may contribute little to the matrix's coordinated behavior. Entry size ignores how rows and columns act together.

```text
observation
    ↓
our own proposal ──▶ test case ──▶ impossible answer
                                      ↓
                              preserve what vanished
                                      ↓
                                    Singular Value Decomposition
```

What survives the failure is a precise demand. The repaired construction must rotate the input into orthogonal right-singular directions, scale each by a nonnegative singular value, and rotate into orthogonal output directions; keep the strongest channels for a principled low-rank approximation.

This is the hinge of the Singular Value Decomposition excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Singular Value Decomposition on the stone workbench

For the diagonal plate `[[3,0],[0,1]]`, the east input rings with strength 3 and the north input with strength 1. Keeping only the first channel produces `[[3,0],[0,0]]`: the best rank-one approximation under squared error. The omitted channel's strength, 1, states exactly what was lost.

The point of keeping the objects named while rebuilding Singular Value Decomposition is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside singular value decomposition

Return to the named Singular Value Decomposition scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**Vᵀ** changes from ordinary input coordinates to right-singular directions. **Σ** scales those directions by singular values ordered strongest first. **U** expresses the results in output directions. **Aₖ** keeps only the first k channels.

##### Why the melody needs these exact notes

[Function composition](../MATHEMATICAL_MOVES.md#function-composition) fixes the order: rotate input, scale channels, rotate output. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets each stage act through the previous one. Keeping arbitrary entries would not preserve the strongest coordinated directions or give the best rank-k squared-error approximation.

The operations inside Singular Value Decomposition form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
A=U\Sigma V^T,\quad A_k=U_k\Sigma_kV_k^T
$$

Read the Singular Value Decomposition line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A prism does not rank individual patches of glass. It reveals the hidden channels through which the whole beam can travel.

That echo helps Singular Value Decomposition remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

LoRA assumes useful updates occupy a low-rank subspace; embedding analysis and compression rely on singular directions; numerical solvers use singular values to expose ill-conditioning.

The older excavation and this Singular Value Decomposition chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of singular value decomposition breaks

SVD organizes finite linear transformations. Our learning chapters repeatedly spoke of changes becoming ‘infinitely small,’ but finite examples alone have not made that passage precise.

The boundary belongs beside the discovery of Singular Value Decomposition because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/208-singular-value-decomposition/README.md).*

---

### Excavation 209 — Limits — Approaching What Cannot Be Reached in One Step

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

SVD exposes what a finite matrix preserves and discards. Calculus asks a stranger question: what does a procedure approach as a step becomes smaller without ever requiring a final smallest positive step?

The corridor bends beneath every model we have built. Here **Limits** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.

A messenger must cross one metre to the next stone mark. First the remaining gap is one half, then one quarter, one eighth, and so on. No listed move is zero, yet the marks gather around the destination.

If we were the first people in this chamber, we would probably declare that a sequence reaches its destination only when one finite term equals the destination exactly.

We let the idea touch the evidence. The fracture appears exactly where information was lost. The gaps `1/2, 1/4, 1/8, ...` never equal zero, so the rule denies the visible fact that they can be made smaller than any requested tolerance.

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
                    Limits
```

The broken attempt has done its work. It tells us, in ordinary language, to define the destination by a guarantee: however tiny a permitted error is chosen, all sufficiently late terms fall inside it.

This is the hinge of the Limits excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Limits on the stone workbench

If the required gap is below 0.01, choose n greater than 100 and `1/n` is small enough. If the requirement tightens to 0.0001, choose n greater than 10,000. The destination zero is earned not by arriving at a final term, but by defeating every positive tolerance.

The point of keeping the objects named while rebuilding Limits is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside limits

Return to the named Limits scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**n** counts the step and grows without bound. **1/n** is the remaining gap. **lim** names the value approached. The arrow toward infinity describes unbounded growth in n; equality names the unique destination whose every tolerance can eventually be met.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) makes the gap shrink as the count grows. [The limit](../MATHEMATICAL_MOVES.md#limit) records the tolerance guarantee rather than substituting infinity as an ordinary number. Writing `1/∞` would hide the reasoning because infinity is not a final denominator reached by the sequence.

The operations inside Limits form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\lim_{n\to\infty}\frac{1}{n}=0
$$

Read the Limits line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A distant mountain does not jump closer. It fills more of the window as you walk, and every demanded closeness determines how far you must travel.

That echo helps Limits remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Derivatives, continuous activations, convergence of optimization, integrals, and probability laws all depend on limits. The quiet symbol carries an entire challenge-and-response guarantee.

The older excavation and this Limits chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of limits breaks

A scalar limit describes one approaching quantity. A neural loss depends on millions of parameters, so we must ask how one output changes along every coordinate direction.

The boundary belongs beside the discovery of Limits because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/209-limits/README.md).*

---

### Excavation 210 — Partial Derivatives and Gradients — One Landscape, Many Directions

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Mathematical roots beneath the machine

Limits make ‘arbitrarily small’ precise. A loss surface has not one input but millions, and moving stripe sensitivity while freezing weight sensitivity answers a different question from moving both together.

Another vault door opens. The carving that once named **Partial Derivatives and Gradients** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

The tiger alarm has two dials: stripe weight w₁ and size weight w₂. Its local loss is a hillside over the floor. The ranger can nudge east, north, or diagonally and observe different changes.

The old machinery invites a plausible shortcut: compute one ordinary derivative as if the entire parameter vector were a single undifferentiated number.

The stone does not object with terminology; it objects with a result we already know cannot be right. The answer cannot say which dial caused which part of the change or which physical direction rises fastest. Different paths through the same point produce different slopes.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Partial Derivatives and Gradients
```

We do not leap to a famous formula. We carry one missing responsibility forward: hold every other dial fixed to measure one partial derivative at a time, then gather those coordinate sensitivities into the gradient vector.

This is the hinge of the Partial Derivatives and Gradients excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Partial Derivatives and Gradients on the stone workbench

Near the current setting, nudging w₁ by 0.01 raises loss by about 0.03, giving sensitivity 3. Nudging w₂ by 0.01 lowers loss by about 0.01, giving sensitivity -1. The gradient `[3,-1]` points toward fastest local increase; its negative points toward fastest local decrease under ordinary Euclidean distance.

The point of keeping the objects named while rebuilding Partial Derivatives and Gradients is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside partial derivatives and gradients

Return to the named Partial Derivatives and Gradients scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**L** is the loss landscape and **w₁,…,wₙ** its adjustable coordinates. **∂L/∂wᵢ** asks what L does when only wᵢ moves infinitesimally. **∇L** stores every such answer in coordinate order.

##### Why the melody needs these exact notes

[Partial derivatives](../MATHEMATICAL_MOVES.md#partial-derivative) isolate one coordinate while others are fixed. [Concatenation](../MATHEMATICAL_MOVES.md#concatenation) preserves the separate sensitivities as one ordered vector. Summing them would erase direction and could let positive and negative effects cancel.

The operations inside Partial Derivatives and Gradients form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\nabla L(\mathbf w)=\left[\frac{\partial L}{\partial w_1},\ldots,\frac{\partial L}{\partial w_n}\right]
$$

Read the Partial Derivatives and Gradients line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

At a mountain pass, ‘the slope’ is incomplete until you say which way you face. The gradient is the compass arrow assembled from every coordinate-facing slope.

That echo helps Partial Derivatives and Gradients remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Gradient descent, backpropagation, Adam, clipping, and attribution all use this object. Earlier chapters used it operationally; this excavation reveals why its components must remain ordered.

The older excavation and this Partial Derivatives and Gradients chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of partial derivatives and gradients breaks

A gradient describes one scalar output. A layer often maps many inputs to many outputs, so one vector cannot preserve every input-output sensitivity.

The boundary belongs beside the discovery of Partial Derivatives and Gradients because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/210-partial-derivatives-gradients/README.md).*

---

### Excavation 211 — Jacobians — When Many Outputs Change Together

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
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

#### Jacobians on the stone workbench

Suppose danger is `2w+s` and estimated speed is `w-s`. Increasing w by one changes the outputs by `[2,1]`; increasing s by one changes them by `[1,-1]`. Put the response to w in the first column and the response to s in the second. The resulting matrix `[[2,1],[1,-1]]` predicts the small output change produced by any small input change.

The point of keeping the objects named while rebuilding Jacobians is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside jacobians

Return to the named Jacobians scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**fᵢ** is output i and **xⱼ** input j. Each entry **∂fᵢ/∂xⱼ** asks how that particular output responds to that particular input. Row order preserves outputs; column order preserves inputs. **J** names the complete local linear map.

##### Why the melody needs these exact notes

[Partial derivatives](../MATHEMATICAL_MOVES.md#partial-derivative) isolate one output-input relationship. [Tables](../MATHEMATICAL_MOVES.md#tables) preserve the exact row-column mapping, and [multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets the Jacobian act on a small input change. A sum would collapse distinct outputs and inputs into one ambiguous sensitivity.

The operations inside Jacobians form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

Read the Jacobians line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A theatre lighting board has many sliders and many lamps. The Jacobian is the local wiring chart saying how each lamp responds to each slider.

That echo helps Jacobians remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Backpropagation multiplies local Jacobian effects without usually materializing the full matrices; normalizing flows use Jacobian determinants; robustness asks how input perturbations propagate through this map.

The older excavation and this Jacobians chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of jacobians breaks

The Jacobian is a first-order description. Two landscapes can share the same slope at one point while bending into a bowl, ridge, or saddle immediately afterward.

The boundary belongs beside the discovery of Jacobians because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/211-jacobians/README.md).*

---

### Excavation 212 — Hessians and Curvature — Why the Same Slope Can Hide Different Valleys

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Mathematical roots beneath the machine

Jacobians record first-order response. At a flat-looking point the gradient may be zero, yet the point could be the bottom of a safe bowl, the top of a hill, or a saddle that rises east and falls north.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Hessians and Curvature** first as an ordinary human need, before anyone has decided what marks should record it.

The vault floor contains two stone surfaces. At the centre both feel level. One curves upward in every direction; the other curves upward east-west and downward north-south.

We try to spend no new mathematics at all and simply declare every zero-gradient point a successful minimum and stop moving.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. The saddle also has zero first-order slope. Stopping there mistakes balanced opposing curvature for completion, while choosing a large step without curvature can leap across a narrow bowl.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Hessians and Curvature becomes necessary
```

At last there is something worth inventing. Whatever we build must differentiate the gradient again and store how every pair of coordinates changes the local slope.

This is the hinge of the Hessians and Curvature excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Hessians and Curvature on the stone workbench

For `L(w₁,w₂)=w₁²-w₂²`, both partial derivatives vanish at `[0,0]`. The second derivative along w₁ is 2; along w₂ it is -2; cross-effects are zero. The Hessian `[[2,0],[0,-2]]` exposes a saddle because one direction bends up and another down.

The point of keeping the objects named while rebuilding Hessians and Curvature is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside hessians and curvature

Return to the named Hessians and Curvature scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**Hᵢⱼ** asks how the sensitivity in direction i changes when coordinate j moves. Diagonal entries describe coordinate curvature; off-diagonal entries describe coupled bending. The complete matrix is the local curvature map.

##### Why the melody needs these exact notes

[Partial derivatives](../MATHEMATICAL_MOVES.md#partial-derivative) are applied a second time because curvature is change in slope. [Tables](../MATHEMATICAL_MOVES.md#tables) preserve pairwise coordinate effects. Looking only at the diagonal would miss rotations and coupled directions; summing entries would destroy the geometry.

The operations inside Hessians and Curvature form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
H_{ij}=\frac{\partial^2L}{\partial w_i\partial w_j}
$$

Read the Hessians and Curvature line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A marble at a level point needs more than a spirit level. The surrounding bend tells whether it rests in a bowl, balances on a dome, or waits on a saddle.

That echo helps Hessians and Curvature remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Initialization, learning rates, Newton-like methods, loss-landscape analysis, and sharpness all depend on curvature even when large models approximate it indirectly.

The older excavation and this Hessians and Curvature chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of hessians and curvature breaks

Exact Hessians are expensive and local curvature still describes only a neighborhood. We need a disciplined way to approximate a complicated function near the point using the derivatives already measured.

The boundary belongs beside the discovery of Hessians and Curvature because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/212-hessians-curvature/README.md).*

---

### Excavation 213 — Taylor Approximation — Borrowing a Function’s Local Shape

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Mathematical roots beneath the machine

The Hessian reveals local bending. Re-evaluating a complicated model for every nearby possibility remains costly, and a slope alone fails as soon as curvature matters.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Taylor Approximation** has been covered so that only the unsolved situation remains.

The ranger knows a signal's value, slope, and curvature at dial setting a. A nearby setting a+h must be estimated before the expensive full detector can run.

The first move is honest because it uses the nearest tool already in our hands: **extend the tangent line indefinitely and assume constant slope everywhere**.

The proposal deserves a real trial, not a ceremonial rejection. For a curved signal the linear prediction drifts, and doubling h can more than double the error. The tangent remembers direction but forgets that the direction itself changes.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Taylor Approximation
```

Now the reader can name the requirement before the textbook can name the method: we must build a local polynomial: start with the known value, add slope times displacement, then add curvature times squared displacement with the counting factor required by repeated differentiation.

This is the hinge of the Taylor Approximation excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Taylor Approximation on the stone workbench

Use `f(x)=eˣ` near zero. Its value, slope, and curvature at zero are all 1. At h=0.1, the second-order estimate is `1 + 0.1 + 0.1²/2 = 1.105`, close to the true 1.10517. Removing the squared term gives 1.1 and visibly loses curvature.

The point of keeping the objects named while rebuilding Taylor Approximation is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside taylor approximation

Return to the named Taylor Approximation scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**a** is the known location and **h** the nearby displacement. **f(a)** anchors the estimate. **f′(a)h** carries local slope through the displacement. **f″(a)h²/2** repairs the first curvature error. The approximation sign admits omitted higher-order terms.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) lets distinct orders contribute without erasing one another. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) makes each derivative act through its displacement, while [powers](../MATHEMATICAL_MOVES.md#powers) make curvature shrink faster than slope as h becomes tiny. Multiplying all terms together would make any zero term erase the approximation.

The operations inside Taylor Approximation form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f(a+h)\approx f(a)+f'(a)h+\frac{f''(a)}{2}h^2
$$

Read the Taylor Approximation line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A sculptor reconstructs the nearby curve from how the stone faces now, how its direction changes, and how quickly that change itself bends.

That echo helps Taylor Approximation remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Gradient descent trusts the first-order term; Newton methods use the second; neural tangent analyses study regimes where the local linear picture remains informative.

The older excavation and this Taylor Approximation chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of taylor approximation breaks

Taylor pieces describe local behavior. To recover total water, distance, probability, or change across a whole interval, many small contributions must be accumulated rather than inspected near one point.

The boundary belongs beside the discovery of Taylor Approximation because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/213-taylor-approximation/README.md).*

---

### Excavation 214 — Integrals — Reconstructing a Whole from Infinitesimal Pieces

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Taylor approximation reconstructs a function near one point. The factory's meters report rates—tokens per second, energy per second, water flow per minute—but the final account needs a total across time.

In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **Integrals**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.

A rescue tank fills at a changing rate r(t). The ranger reads the rate at many moments but wants the total water delivered between dawn a and dusk b.

Nothing yet suggests a new invention. We naturally multiply one chosen rate by the entire duration.

For a moment the shortcut feels complete. Then the smallest contrary case arrives. The flow is slow at dawn and fast at noon, so one sample grants every moment the wrong rate. Taking more samples helps, but their contributions need a rule that survives as slices become thinner.

```text
observation
    ↓
our own proposal ──▶ test case ──▶ impossible answer
                                      ↓
                              preserve what vanished
                                      ↓
                                    Integrals
```

What survives the failure is a precise demand. The repaired construction must divide time into small intervals, multiply each interval's width by a representative rate, add the resulting little volumes, and take the limit as the widest interval shrinks toward zero.

This is the hinge of the Integrals excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Integrals on the stone workbench

Over four one-minute intervals the measured rates are 1, 2, 3, and 4 litres per minute. Rectangles give `1×1 + 2×1 + 3×1 + 4×1 = 10` litres. Halving the interval uses more, thinner rectangles and follows the changing flow more closely. The integral is the value these sums approach as no interval remains visibly wide.

The point of keeping the objects named while rebuilding Integrals is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside integrals

Return to the named Integrals scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**[a,b]** is the time interval. **Δtᵢ** is one slice width and **r(tᵢ)** its sampled rate. Their product is a small amount, not a rate. Summation combines slice amounts; the limit removes dependence on a coarse partition. The integral sign names the accumulated whole.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) converts rate times duration into amount. [Summation](../MATHEMATICAL_MOVES.md#summation) joins disjoint amounts; multiplication among slices would make one zero-flow moment erase all water. [The limit](../MATHEMATICAL_MOVES.md#limit) forces the partition error arbitrarily small.

The operations inside Integrals form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\int_a^b r(t)dt=\lim_{\max\Delta t_i\to0}\sum_i r(t_i)\Delta t_i
$$

Read the Integrals line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A mosaic becomes an image because each tiny tile contributes colour to a place; making the tiles finer reveals the curve rather than changing the scene.

That echo helps Integrals remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Expected values are integrals over possible outcomes, Neural ODEs integrate hidden-state change, and continuous-time signals become discrete computations through numerical quadrature.

The older excavation and this Integrals chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of integrals breaks

Accumulation tells how much signal exists but can hide the simple repeating components inside it. Audio waves that look tangled in time may become sparse when described by frequency.

The boundary belongs beside the discovery of Integrals because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/214-integrals/README.md).*

---

### Excavation 215 — Fourier Analysis — Hearing Frequencies Hidden Inside Time

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Mathematical roots beneath the machine

Integrals recover wholes from local pieces. A microphone's whole waveform still looks like an unruly sequence of pressures, even when a listener hears a pure low note, a high whistle, and a repeating wingbeat.

The corridor bends beneath every model we have built. Here **Fourier Analysis** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.

The Scriptorium lowers a string of microphone samples into the vault. The values rise and fall, but no sample announces which repeating rhythms created the pattern.

If we were the first people in this chamber, we would probably compare waveforms only sample by sample in time.

We let the idea touch the evidence. The fracture appears exactly where information was lost. The same note shifted slightly appears very different at every position, and two overlapping tones hide inside one jagged trace. Time coordinates expose when, not which frequency.

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
                    Fourier Analysis
```

The broken attempt has done its work. It tells us, in ordinary language, to compare the signal with a family of rotating sine-and-cosine patterns and add the agreements, producing one coefficient for each candidate frequency.

This is the hinge of the Fourier Analysis excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Fourier Analysis on the stone workbench

Take four samples `[1,0,-1,0]`. They complete one oscillation: high, centre, low, centre. Multiplying them against the matching rotating pattern makes the four contributions reinforce; mismatched frequencies alternate and largely cancel. The coefficient's magnitude reports how strongly that rhythm is present.

The point of keeping the objects named while rebuilding Fourier Analysis is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside fourier analysis

Return to the named Fourier Analysis scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**xₙ** is sample n among N samples. **k** names a candidate frequency. The complex exponential is a compact rotating cosine-and-sine ruler. Multiplying tests phase-aligned agreement; summing gathers evidence across time. **Xₖ** is the coefficient for frequency k.

##### Why the melody needs these exact notes

[The exponential](../MATHEMATICAL_MOVES.md#exponential) supplies a regularly rotating comparison pattern. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) measures sample-by-pattern agreement, [summation](../MATHEMATICAL_MOVES.md#summation) lets aligned evidence reinforce, and the [negative sign](../MATHEMATICAL_MOVES.md#negative-sign) fixes the analysis rotation direction. Adding raw samples would keep only the zero-frequency total.

The operations inside Fourier Analysis form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
X_k=\sum_{n=0}^{N-1}x_n e^{-2\pi i kn/N}
$$

Read the Fourier Analysis line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A prism separates colours already travelling together in white light. Fourier analysis is a prism for rhythms.

That echo helps Fourier Analysis remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Speech features, positional rotations, convolution, image filtering, and Fourier neural operators all move between coordinate systems where different structure becomes simple.

The older excavation and this Fourier Analysis chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of fourier analysis breaks

Fourier coefficients describe deterministic signal content. Real observations also vary unpredictably, so the next object must turn uncertain outcomes into numerical quantities with distributions.

The boundary belongs beside the discovery of Fourier Analysis because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/215-fourier-analysis/README.md).*

---

### Excavation 216 — Random Variables and Distributions — Turning Outcomes into Quantities

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Fourier analysis gives deterministic signals new coordinates. The ranger's camera, however, may record zero, one, or several tigers tomorrow; before the observation, the count is not an unknown fixed number but a quantity attached to several possible worlds.

Another vault door opens. The carving that once named **Random Variables and Distributions** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

Three cards describe tomorrow: no tiger, one tiger, and two tigers. Each card has a probability, but the station wants to compute expected food use and variation in the *count*.

The old machinery invites a plausible shortcut: treat the outcome label itself as a number and perform arithmetic directly on names such as ‘no sighting’ and ‘two sightings’.

The stone does not object with terminology; it objects with a result we already know cannot be right. Outcomes may be stories, images, or paths rather than numbers, and the same numerical question can group many different outcomes. Arithmetic needs a mapping from possible worlds to values.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Random Variables and Distributions
```

We do not leap to a famous formula. We carry one missing responsibility forward: define a random variable as a function assigning a numerical value to every outcome, then transfer probability mass through that mapping to form its distribution.

This is the hinge of the Random Variables and Distributions excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Random Variables and Distributions on the stone workbench

Let Ω contain four equally likely camera histories. Two contain no tiger, one contains one tiger, and one contains two. The counting function X maps them to 0, 0, 1, and 2. Therefore `P(X=0)=2/4`, `P(X=1)=1/4`, and `P(X=2)=1/4`. Different histories can share one count without becoming the same history.

The point of keeping the objects named while rebuilding Random Variables and Distributions is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside random variables and distributions

Return to the named Random Variables and Distributions scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**Ω** is the sample space of possible histories. **X** is the function turning a history into a real count. **P(X=x)** gathers the probability of every history mapped to value x. The distribution is the resulting allocation of probability across possible numerical values.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) converts each outcome into the quantity we care about. [Probability](../MATHEMATICAL_MOVES.md#probability) preserves how much possibility maps to each value, and [summation](../MATHEMATICAL_MOVES.md#summation) combines different outcomes sharing the same value. Multiplying their probabilities would describe all histories occurring together, a different event.

The operations inside Random Variables and Distributions form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
P(X=x)=\sum_{\omega:X(\omega)=x}P(\omega)
$$

Read the Random Variables and Distributions line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

Weather is a story; temperature is a random variable extracted from that story. The number is a question asked of the world, not the whole world itself.

That echo helps Random Variables and Distributions remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Loss, reward, token count, model output, and gradient noise are random variables. Their distributions—not isolated values—determine learning and evaluation.

The older excavation and this Random Variables and Distributions chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of random variables and distributions breaks

A distribution describes current uncertainty. When a paw print arrives, probabilities must be rearranged according to how compatible each hidden story was with that evidence.

The boundary belongs beside the discovery of Random Variables and Distributions because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/216-random-variables-distributions/README.md).*

---

### Excavation 217 — Conditional Probability and Bayes’ Rule — Let Evidence Rearrange Belief

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Random variables turn possible worlds into measurable quantities. A fresh paw print should change the tiger probability, but merely retaining yesterday's distribution ignores the reason observation matters.

Far below the Transformer, the Undercroft stores no formula sheet. For **Conditional Probability and Bayes’ Rule**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

Before seeing tracks, the valley expects tiger on one day in ten and deer on nine. Deep clawed tracks are likely under tiger and rare under deer. The print has arrived; the old shares can no longer remain untouched.

With no standard method to recite, the most economical proposal is to compare only how well each animal explains the print and choose the largest likelihood.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. Likelihood ignores how common each animal was before the evidence. A moderately diagnostic clue could make an extremely rare story look certain if prior plausibility is discarded.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Conditional Probability and Bayes’ Rule
```

The next idea is forced only because the evidence asks us to multiply each prior belief by that story's support for the evidence, then divide by the total support across all stories so the surviving weights again form one distribution.

This is the hinge of the Conditional Probability and Bayes’ Rule excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Conditional Probability and Bayes’ Rule on the stone workbench

Out of 100 imagined days, expect 10 tiger days and 90 deer days. Suppose deep tracks appear on 8 of 10 tiger days but only 9 of 90 deer days. Among the 17 deep-track days, 8 involve tiger. After observing deep tracks, tiger probability becomes `8/17`, not 0.8 and not the old 0.1.

The point of keeping the objects named while rebuilding Conditional Probability and Bayes’ Rule is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside conditional probability and bayes’ rule

Return to the named Conditional Probability and Bayes’ Rule scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**H** is one hidden story and **E** the observed evidence. **P(H)** is prior plausibility. **P(E|H)** is likelihood. Their product is the joint share where H and E occur. **P(E)** totals all routes to the evidence. Division asks what fraction of evidence-compatible worlds contain H.

##### Why the melody needs these exact notes

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) states which fact is held as known. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) requires both prior story and compatible evidence, while [division](../MATHEMATICAL_MOVES.md#division) restricts attention to worlds where E occurred. Adding prior and likelihood would mix quantities that do not form a joint share.

The operations inside Conditional Probability and Bayes’ Rule form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

Read the Conditional Probability and Bayes’ Rule line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

Evidence is a gate, not paint. It does not colour every old belief equally; it admits worlds in proportion to how naturally they could have produced what was seen.

That echo helps Conditional Probability and Bayes’ Rule remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Likelihood, calibration, Bayesian updating, filtering, and uncertainty-aware planning all reuse this rearrangement. Excavation 102 used it; here we expose the counting skeleton underneath.

The older excavation and this Conditional Probability and Bayes’ Rule chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of conditional probability and bayes’ rule breaks

A posterior distribution can still be too rich to carry everywhere. One mean alone, however, hides whether beliefs are tightly gathered, widely spread, or moving together.

The boundary belongs beside the discovery of Conditional Probability and Bayes’ Rule because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/217-conditional-probability-bayes/README.md).*

---

### Excavation 218 — Expectation, Variance, and Covariance — Centre, Spread, and Shared Motion

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Mathematical roots beneath the machine

Bayes' rule returns a full distribution after evidence. To budget supplies or compare models, the station needs summaries, but one central value must not pretend that uncertainty and joint movement disappeared.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Expectation, Variance, and Covariance** first as an ordinary human need, before anyone has decided what marks should record it.

Two routes both average one tiger sighting per day. Route A always sees exactly one. Route B sees zero half the time and two half the time. The means agree; their risks do not.

We try to spend no new mathematics at all and simply report only the average and treat distributions sharing it as interchangeable.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. The average hides spread. It also cannot reveal whether tiger count and alarm count rise together or move independently, which matters when one is used to predict the other.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Expectation, Variance, and Covariance becomes necessary
```

At last there is something worth inventing. Whatever we build must compute expectation as a probability-weighted centre, variance as average squared departure from that centre, and covariance as average product of paired departures.

This is the hinge of the Expectation, Variance, and Covariance excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Expectation, Variance, and Covariance on the stone workbench

Route A's count is always 1, so every departure from mean 1 is zero and variance is zero. Route B's departures are -1 and +1; squaring gives 1 in either case, so variance is 1. If alarm departures carry the same signs as tiger departures, their products are positive and covariance reveals shared movement.

The point of keeping the objects named while rebuilding Expectation, Variance, and Covariance is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside expectation, variance, and covariance

Return to the named Expectation, Variance, and Covariance scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**μ** is the expected centre. **X-μ** is one departure. Squaring prevents low and high outcomes from cancelling in variance. **Y-E[Y]** is the paired departure of a second quantity. Multiplying paired departures records same-direction as positive and opposite-direction as negative.

##### Why the melody needs these exact notes

[Expectation](../MATHEMATICAL_MOVES.md#expectation) lets each possible value contribute in proportion to its probability. [Variance](../MATHEMATICAL_MOVES.md#variance) uses squared departures so opposite errors do not cancel. [Covariance](../MATHEMATICAL_MOVES.md#covariance) multiplies paired departures; adding them would lose whether the two quantities moved together on the same occasion.

The operations inside Expectation, Variance, and Covariance form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
E[X]=\sum_x xP(X=x),\quad Var(X)=E[(X-E[X])^2],\quad Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
$$

Read the Expectation, Variance, and Covariance line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

The centre of a flock says where to look; its spread says how wide to search; synchronized turns say which birds respond to the same wind.

That echo helps Expectation, Variance, and Covariance remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Normalization uses means and variances, PCA diagonalizes covariance, initialization controls signal variance, and gradient-noise analysis compares shared direction with disagreement.

The older excavation and this Expectation, Variance, and Covariance chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of expectation, variance, and covariance breaks

These quantities are usually estimated from samples. Before trusting them, we need a reason that accumulating more independent evidence makes sample averages settle rather than wander forever.

The boundary belongs beside the discovery of Expectation, Variance, and Covariance because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/218-expectation-variance-covariance/README.md).*

---

### Excavation 219 — The Law of Large Numbers — Why Averages Eventually Settle

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Expectation, variance, and covariance describe a distribution. The ranger sees only a finite stream of days and must justify why the observed average can stand in for the hidden expected value.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **The Law of Large Numbers** has been covered so that only the unsolved situation remains.

A fair coin decides whether the camera opens the north gate. After one toss the observed head rate is either zero or one—both far from the expected half.

The first move is honest because it uses the nearest tool already in our hands: **demand that every short sample reproduce the population expectation exactly**.

The proposal deserves a real trial, not a ceremonial rejection. Chance has not failed when the first three tosses are all heads. Short runs fluctuate, so exact equality would reject honest randomness and make estimation impossible.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           The Law of Large Numbers
```

Now the reader can name the requirement before the textbook can name the method: we must study the sample mean as the number of independent observations grows and ask whether the probability of a substantial error shrinks toward zero.

This is the hinge of the The Law of Large Numbers excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### The Law of Large Numbers on the stone workbench

After 10 tosses, 7 heads gives average 0.7. After 100, perhaps 54 heads gives 0.54. After 10,000, 5,013 heads gives 0.5013. No run is promised monotonic improvement, but large persistent deviations become increasingly unlikely under the same fair process.

The point of keeping the objects named while rebuilding The Law of Large Numbers is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside the law of large numbers

Return to the named The Law of Large Numbers scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**Xᵢ** is observation i with expected value μ. The sum combines independent evidence. Division by n forms the per-observation average. The arrow toward μ describes convergence as sample size grows, not equality at any finite n.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every observation vote. [Division](../MATHEMATICAL_MOVES.md#division) prevents the total from growing merely because more observations arrived, and [the limit](../MATHEMATICAL_MOVES.md#limit) states the large-sample guarantee. Multiplying observations would let one zero erase the entire history.

The operations inside The Law of Large Numbers form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\overline X_n=\frac1n\sum_{i=1}^{n}X_i\longrightarrow\mu
$$

Read the The Law of Large Numbers line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

One drop cannot reveal the river's average depth. Many well-spaced soundings do not eliminate variation, but they make a persistent false average harder to sustain.

That echo helps The Law of Large Numbers remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Mini-batches, evaluation means, Monte Carlo estimates, calibration bins, and distributed gradient averages rely on this settling behavior—plus assumptions about sampling and dependence.

The older excavation and this The Law of Large Numbers chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of the law of large numbers breaks

The law explains where the average goes but not the shape of its remaining error. Across many experiments, normalized averages often approach a bell-shaped distribution.

The boundary belongs beside the discovery of The Law of Large Numbers because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/219-law-large-numbers/README.md).*

---

### Excavation 220 — The Central Limit Theorem — Why Bell Shapes Keep Appearing

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

The law of large numbers says sample averages settle. It does not tell the station how far a finite average is likely to lie from the truth or why sums of very different small disturbances often share one familiar bell shape.

In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **The Central Limit Theorem**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.

Each daily sensor error is bounded but irregular. The monthly average combines heat, battery noise, wind, and rounding. The exact distribution of each source is inconvenient and different.

Nothing yet suggests a new invention. We naturally assume the average has the same distributional shape as each individual disturbance.

For a moment the shortcut feels complete. Then the smallest contrary case arrives. Averaging changes scale and shape. A single skewed measurement and the mean of one hundred such measurements do not have the same uncertainty.

```text
observation
    ↓
our own proposal ──▶ test case ──▶ impossible answer
                                      ↓
                              preserve what vanished
                                      ↓
                                    The Central Limit Theorem
```

What survives the failure is a precise demand. The repaired construction must centre the sample mean at μ, divide by its standard error σ/√n, and study the distribution of that normalized error as n grows.

This is the hinge of the The Central Limit Theorem excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### The Central Limit Theorem on the stone workbench

Suppose individual measurements have mean 10 and standard deviation 2. An average of 100 independent readings still centres at 10, but its standard error is `2/√100 = 0.2`. Repeating the entire 100-reading experiment produces normalized errors that increasingly resemble a standard bell even when individual readings are not bell-shaped.

The point of keeping the objects named while rebuilding The Central Limit Theorem is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside the central limit theorem

Return to the named The Central Limit Theorem scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**μ** and **σ** are the population mean and standard deviation. **X̄ₙ-μ** is estimation error. **σ/√n** is the error's natural scale under independent finite-variance sampling. Dividing creates a dimensionless quantity comparable across n. **N(0,1)** names the limiting standard normal distribution.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) isolates estimation error. [The square root](../MATHEMATICAL_MOVES.md#square-root) appears because independent variances add while standard deviations are square roots of variance. [Division](../MATHEMATICAL_MOVES.md#division) expresses error in standard-error units; dividing by n would shrink too quickly.

The operations inside The Central Limit Theorem form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\frac{\overline X_n-\mu}{\sigma/\sqrt n}\Longrightarrow N(0,1)
$$

Read the The Central Limit Theorem line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

Many uneven footsteps become a smooth crowd rhythm when heard from far away—not because individuals became identical, but because independent deviations accumulated on a shared scale.

That echo helps The Central Limit Theorem remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Confidence intervals, uncertainty estimates, initialization theory, approximate Bayesian inference, and Gaussian-process limits of wide networks all borrow versions of this phenomenon.

The older excavation and this The Central Limit Theorem chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of the central limit theorem breaks

A bell approximation still does not decide whether an observed improvement is convincing, practically meaningful, or produced by a flawed experiment. Evidence needs an explicit claim and error procedure.

The boundary belongs beside the discovery of The Central Limit Theorem because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/220-central-limit-theorem/README.md).*

---

### Excavation 221 — Hypothesis Tests and Confidence Intervals — When Is an Improvement Convincing?

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Mathematical roots beneath the machine

The central limit theorem gives the shape and scale of repeated sample averages. It still does not decide whether a measured model improvement is evidence of a real change or an ordinary tremor of sampling.

The corridor bends beneath every model we have built. Here **Hypothesis Tests and Confidence Intervals** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.

Two assistants answer the same 100 field questions. The new assistant scores, on average, 0.4 points higher. The room wants to celebrate, but daily paired differences wobble with a standard deviation of 2 points.

If we were the first people in this chamber, we would probably declare every positive sample difference a discovery.

We let the idea touch the evidence. The fracture appears exactly where information was lost. Another sample from unchanged systems can land above zero by chance. A positive sign says which side won this sample; it does not say how surprising that victory would be if the true average difference were zero.

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
                    Hypothesis Tests and Confidence Intervals
```

The broken attempt has done its work. It tells us, in ordinary language, to state the no-improvement claim, measure the observed mean difference in units of its standard error, and report both a test statistic and the range of effects compatible with the sampling noise.

This is the hinge of the Hypothesis Tests and Confidence Intervals excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Hypothesis Tests and Confidence Intervals on the stone workbench

For the 100 paired questions, the mean difference is 0.4 and the standard deviation of differences is 2. The standard error is `2/√100 = 0.2`, so the improvement sits `0.4/0.2 = 2` standard errors above zero. A rough 95% interval is `0.4 ± 1.96×0.2`, or about `[0.008, 0.792]`. Zero lies just outside, yet the interval also warns that the practical gain may be tiny.

The point of keeping the objects named while rebuilding Hypothesis Tests and Confidence Intervals is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside hypothesis tests and confidence intervals

Return to the named Hypothesis Tests and Confidence Intervals scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**dᵢ** is the score difference on paired question i. **d̄** is their observed mean. Zero is the null claim of no average improvement. **s/√n** estimates how much the sample mean would wobble. **z** tells how many such wobble-units separate the observation from the null.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) makes each question compare like with like. [The mean](../MATHEMATICAL_MOVES.md#mean) lets all paired questions contribute. [The square root](../MATHEMATICAL_MOVES.md#square-root) converts sample count into the scale of average noise, and [division](../MATHEMATICAL_MOVES.md#division) asks how large the effect is relative to that noise. Dividing only by s would ignore that one hundred witnesses stabilize a mean more than one witness.

The operations inside Hypothesis Tests and Confidence Intervals form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
z=\frac{\overline d-0}{s/\sqrt n}
$$

Read the Hypothesis Tests and Confidence Intervals line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A distant bell may be real or merely wind in the tower. Evidence asks not only whether you heard a sound, but how loud it was compared with the night's ordinary noise.

That echo helps Hypothesis Tests and Confidence Intervals remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Benchmark uncertainty, A/B tests, ablations, model comparisons, and safety evaluations need this separation between observed effect, sampling uncertainty, and practical importance.

The older excavation and this Hypothesis Tests and Confidence Intervals chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of hypothesis tests and confidence intervals breaks

A test depends on sampling assumptions, a chosen error rate, and a claim selected before inspection. It cannot rescue biased data, repeated unreported testing, or a meaningless metric. Nor does statistical significance guarantee useful significance.

The boundary belongs beside the discovery of Hypothesis Tests and Confidence Intervals because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/221-hypothesis-tests-confidence-intervals/README.md).*

---

### Excavation 222 — Markov Chains — When the Present Carries the Relevant Past

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Mathematical roots beneath the machine

Statistical tests judge evidence gathered from repeated trials. Many intelligent systems instead inhabit a sequence: the next room, token, or state depends on what has already happened, and carrying the entire history soon becomes impossible.

Another vault door opens. The carving that once named **Markov Chains** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

A ranger moves among forest, river, and village. Tomorrow's location depends strongly on today's location. The station has years of paths, but planning one step ahead should not require rereading every footprint since the expedition began.

The old machinery invites a plausible shortcut: assign one fixed next-location distribution regardless of the current location.

The stone does not object with terminology; it objects with a result we already know cannot be right. The river makes village likely while deep forest makes river likely. Erasing the present state destroys exactly the information that changes the next step.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Markov Chains
```

We do not leap to a famous formula. We carry one missing responsibility forward: choose a state description rich enough that, once the present state is known, earlier history adds no further information about the next-state distribution.

This is the hinge of the Markov Chains excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Markov Chains on the stone workbench

Suppose that from forest the ranger moves to river with probability 0.7 and village with 0.3; from river the probabilities differ. If today's state is forest, the forest row supplies tomorrow's distribution. Yesterday may have been cave or village, but under this model it has already influenced the prediction by determining today's forest state.

The point of keeping the objects named while rebuilding Markov Chains is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside markov chains

Return to the named Markov Chains scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**Xₜ** names the state at time t. The left side conditions tomorrow on the complete recorded history. The right side conditions only on today. Equality is the modelling promise that the chosen present state contains every historical detail relevant to one-step prediction.

##### Why the melody needs these exact notes

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) holds known history fixed while asking about the next state. [Equality](../MATHEMATICAL_MOVES.md#equals) claims that discarding older conditions changes no next-step probability. Multiplying every transition probability here would answer the probability of a complete path, not the one-step memory question.

The operations inside Markov Chains form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
P(X_{t+1}\mid X_t,X_{t-1},\ldots,X_0)=P(X_{t+1}\mid X_t)
$$

Read the Markov Chains line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A good travel diary can be compressed into your present location only when that location carries everything the next turn needs. If hunger or weather also matters, they must enter the state.

That echo helps Markov Chains remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Autoregressive generation, hidden-state models, reinforcement learning, diffusion steps, and queueing systems all choose states intended to make the future conditionally manageable.

The older excavation and this Markov Chains chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of markov chains breaks

The Markov property does not say the physical world has no memory; it says our state representation has captured the relevant memory. Even with that representation, choosing actions for long-term reward still requires comparing branching futures.

The boundary belongs beside the discovery of Markov Chains because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/222-markov-chains/README.md).*

---

### Excavation 223 — Dynamic Programming — Remembering the Value of Futures Already Solved

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Mathematical roots beneath the machine

A Markov state makes the next step depend on the present rather than the entire visible past. Planning remains expensive because every action opens more states, whose futures overlap and are recalculated along many paths.

Far below the Transformer, the Undercroft stores no formula sheet. For **Dynamic Programming**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

From forest, the ranger can walk toward river or village. Both routes may later reach the same bridge. Drawing every complete journey separately solves the bridge's remaining journey again each time it is encountered.

With no standard method to recite, the most economical proposal is to enumerate every possible full action sequence and total its reward independently.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. The number of paths grows exponentially with horizon, and shared suffixes are recomputed. A ten-step tree may contain many copies of the same state with the same remaining problem.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Dynamic Programming
```

The next idea is forced only because the evidence asks us to give each state one stored value equal to the best immediate reward plus the discounted expected value of its possible next states, then reuse that value wherever the state reappears.

This is the hinge of the Dynamic Programming excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Dynamic Programming on the stone workbench

At the bridge, suppose crossing now gives 2 and leads to home worth 8 next step; waiting gives 1 and leaves a future worth 6. With discount 0.9, crossing is worth `2 + 0.9×8 = 9.2`; waiting is worth `1 + 0.9×6 = 6.4`. Record 9.2 once. Every route arriving at the bridge can now reuse it.

The point of keeping the objects named while rebuilding Dynamic Programming is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside dynamic programming

Return to the named Dynamic Programming scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**V(s)** is the best future value stored for state s. **a** is a candidate action. **r(s,a)** is immediate reward. **P(s′|s,a)** weighs possible next states. **γ** reduces the influence of distant reward. The maximum keeps the action with the best complete prospect.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) weights each future by both probability and discount. [Summation](../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive next-state possibilities; multiplying them would demand all next states occur together. [Maximum](../MATHEMATICAL_MOVES.md#maximum) chooses among actions after each has been fully valued, while [addition](../MATHEMATICAL_MOVES.md#addition) joins reward now with reward later.

The operations inside Dynamic Programming form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
V(s)=\max_a\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right]
$$

Read the Dynamic Programming line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

Instead of recounting every road to the sea, a cartographer writes the remaining distance on each crossroads. Every upstream route inherits the solved suffix.

That echo helps Dynamic Programming remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Bellman backups power value iteration, Q-learning, tree search, decoding variants, and many ways of turning a long decision into reusable local subproblems.

The older excavation and this Dynamic Programming chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of dynamic programming breaks

Exact dynamic programming requires states and transitions that can be represented and revisited. Huge or continuous worlds need approximation, and a value function with arbitrary shape may still be difficult to optimize reliably.

The boundary belongs beside the discovery of Dynamic Programming because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/223-dynamic-programming/README.md).*

---

### Excavation 224 — Convexity — A Landscape Without Hidden Valleys

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Dynamic programming replaces repeated futures with stored values, but learning those values or fitting a model still asks an optimizer to descend a landscape. Some landscapes conceal many valleys; others make every local descent globally trustworthy.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Convexity** first as an ordinary human need, before anyone has decided what marks should record it.

Stretch a string between two points on a bowl. Everywhere between the endpoints, the string floats on or above the bowl. Try the same across a rippled cave floor and the string can cut below a hill.

We try to spend no new mathematics at all and simply trust any small local minimum as the best possible solution.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. On a rippled landscape, a nearby valley may be higher than another valley beyond a ridge. Local slope alone cannot certify that no better point exists elsewhere.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Convexity becomes necessary
```

At last there is something worth inventing. Whatever we build must require every chord between two points to lie on or above the function, preventing a hidden hump from separating a local minimum from a lower global one.

This is the hinge of the Convexity excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Convexity on the stone workbench

For the bowl `f(x)=x²`, choose x=-2, y=2, and λ=1/2. Their midpoint is 0, where the bowl has height 0. The midpoint of endpoint heights is `(4+4)/2=4`; the bowl lies below its chord. Repeating this test for every pair and mixture weight is the geometric promise of convexity.

The point of keeping the objects named while rebuilding Convexity is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside convexity

Return to the named Convexity scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**x** and **y** are any two candidate points. **λ** lies between 0 and 1 and chooses a point along their segment. The left side evaluates the function at the mixed input. The right side mixes the two endpoint heights. The inequality demands that the function never rise above that chord.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) allocates complementary shares λ and 1-λ. [Addition](../MATHEMATICAL_MOVES.md#addition) forms the mixtures. [Inequalities](../MATHEMATICAL_MOVES.md#inequalities) compare the curved surface with its straight chord. Equality alone would describe only affine functions and exclude genuine bowls.

The operations inside Convexity form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f(\lambda x+(1-\lambda)y)\leq\lambda f(x)+(1-\lambda)f(y),\quad 0\leq\lambda\leq1
$$

Read the Convexity line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A valley shaped like a single bowl may be steep or shallow, but it contains no secret lower chamber behind a ridge.

That echo helps Convexity remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Linear regression losses, logistic objectives, support-vector machines, and regularizers expose why some optimization guarantees are possible. Deep neural networks are generally nonconvex, so their success requires more delicate geometry.

The older excavation and this Convexity chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of convexity breaks

Convexity is a powerful global promise, not a description of every useful model. It does not choose a stable numerical representation, prevent overflow, or make finite-precision arithmetic exact.

The boundary belongs beside the discovery of Convexity because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/224-convexity/README.md).*

---

### Excavation 225 — Numerical Stability — Preserving Mathematics Inside a Finite Machine

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

Convexity can make an exact mathematical landscape trustworthy. The machine that evaluates it has finite memory and finite precision, so an algebraically correct formula can still overflow, underflow, or erase a small but important difference.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Numerical Stability** has been covered so that only the unsolved situation remains.

Three logits are 1000, 999, and 998. Their exponentials should have sensible relative sizes, yet an ordinary floating-point calculator cannot store `e¹⁰⁰⁰`; the first operation becomes infinity before normalization can rescue it.

The first move is honest because it uses the nearest tool already in our hands: **evaluate the written formula literally and assume algebraic equivalence guarantees computational equivalence**.

The proposal deserves a real trial, not a ceremonial rejection. Finite arithmetic has ceilings, floors, and rounding. Overflow turns meaningful ratios into `∞/∞`; subtracting nearly equal large numbers can discard the very digits carrying their difference.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Numerical Stability
```

Now the reader can name the requirement before the textbook can name the method: we must rewrite the calculation so intermediate values remain in a safe range while the exact mathematical result stays unchanged.

This is the hinge of the Numerical Stability excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

#### Numerical Stability on the stone workbench

Let m be the largest logit, 1000. Subtract it first, producing `[0,-1,-2]`. Their exponentials are now `[1,e⁻¹,e⁻²]`, all representable. Because factoring out `eᵐ` from the original sum contributes m after the logarithm, the stable result is `1000 + log(1+e⁻¹+e⁻²)`—the same real number reached by a safer path.

The point of keeping the objects named while rebuilding Numerical Stability is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

#### The calculation hidden inside numerical stability

Return to the named Numerical Stability scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

##### Naming what is already on the table

**xᵢ** are the original scores. **m** is their maximum. **xᵢ-m** shifts every score without changing exponential ratios. The inner sum combines safe positive contributions. The outer logarithm returns from exponential scale, and adding m restores the factored scale.

##### Why the melody needs these exact notes

[Maximum](../MATHEMATICAL_MOVES.md#maximum) chooses a shift that makes every exponent nonpositive. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) creates that safe range. [The exponential](../MATHEMATICAL_MOVES.md#exponential) recovers relative positive weights, [summation](../MATHEMATICAL_MOVES.md#summation) combines alternatives, and [the logarithm](../MATHEMATICAL_MOVES.md#logarithm) returns to log scale. Clipping would avoid overflow by changing the answer; this rearrangement preserves it.

The operations inside Numerical Stability form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m},\quad m=\max_i x_i
$$

Read the Numerical Stability line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

#### A real-world echo

A priceless melody can be played on a small instrument only if it is transposed into the instrument's range. The relationships survive although the absolute register temporarily changes.

That echo helps Numerical Stability remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

#### What this chamber was connected to

Stable softmax, log-likelihoods, mixed precision, gradient scaling, normalization, and online attention all distinguish a mathematical identity from a safe computational route.

The older excavation and this Numerical Stability chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

#### Where the promise of numerical stability breaks

Stability cannot restore information already lost to poor data, an ill-conditioned problem, or insufficient precision. It asks a final engineering question: which equivalent path preserves the mathematical meaning on the machine we actually possess?

The boundary belongs beside the discovery of Numerical Stability because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

#### The stair returns to daylight

The final carving is not an answer but a habit. We began with an observation, risked an idea of our own, listened when a small case broke it, and invented only the operation needed to preserve what had vanished. Symbols arrived as nicknames for things our hands and imagination already knew.

That rhythm now runs through the whole archive—from counting tigers to making models accountable. The mandala is not a wall of formulas to memorize. It is a map of human necessities. Touch any node and ask: *What failed so completely that someone had to invent this?* The mathematics will no longer feel borrowed. It will remember the path by which it became yours.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/225-numerical-stability/README.md).*
