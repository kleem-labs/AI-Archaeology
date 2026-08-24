"""Build Part XIV: the mathematical roots beneath the completed machine."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math
import textwrap


ROOT = Path(__file__).parents[1]


@dataclass(frozen=True)
class Chapter:
    number: int
    slug: str
    title: str
    carry: str
    scene: str
    attempt: str
    failure: str
    repair: str
    worked: str
    terms: str
    operations: str
    equation: str
    analogy: str
    connection: str
    limit: str
    references: tuple[tuple[str, str], ...]


ROWS = (
Chapter(201,"sets","Sets — Drawing a Boundary Around ‘Belongs’",
"The accountable factory can trace every document and gate. Its ledgers repeatedly say that a document belongs to a corpus, a token belongs to a vocabulary, or a release belongs to the approved collection, yet we have never excavated what *belongs* must mean.",
"Below the Archive Foundry, a circular vault contains three stone trays: **observed animals**, **animals near water**, and **all recorded animals**. The archivist places tiger, deer, and otter cards on the floor and asks which trays should receive each card.",
"write each tray as an ordinary list and scan every position whenever membership, overlap, or exclusion is questioned",
"the same animal can occur twice, order pretends to matter, and asking which animals occupy both trays requires a new hand-written loop every time. The list stores a sequence; the question concerns a boundary.",
"treat each tray as a collection whose identity depends on membership rather than order or repetition, then construct overlap by retaining exactly the objects admitted by both boundaries",
"Let the observed tray contain tiger, deer, and otter. Let the near-water tray contain tiger, otter, and frog. Put each named animal against both boundaries. Tiger passes both tests; otter passes both; deer fails the water boundary; frog fails the observed boundary. The overlap is therefore `{tiger, otter}`—not because we memorized an intersection rule, but because those are the only cards that survive both questions.",
"**A** names the observed-animal set and **B** the near-water set. **x ∈ A** says the card named x passes A's boundary. **A ∩ B** names the new set formed by the cards that pass both boundaries. The double arrow says the two descriptions admit exactly the same cards.",
"[Membership](../../MATHEMATICAL_MOVES.md#membership) asks one yes-or-no boundary question. [Intersection](../../MATHEMATICAL_MOVES.md#intersection) retains only shared members, and [logical and](../../MATHEMATICAL_MOVES.md#logical-and) requires both tests to succeed. A union would answer ‘in either tray’; counting would report a size while forgetting which animals survived.",
r"x\in A\cap B\Longleftrightarrow (x\in A)\text{ and }(x\in B)",
"A guest list, an allowed tool set, and a dataset split all perform the same act: they draw a boundary and make admission inspectable.",
"The corpus manifest in Excavation 176 was already acting like a set. The authority boundary in Excavation 056 was too. Sets reveal the quiet skeleton shared by data and permission.",
"A set can say which objects belong, but not how one member is connected to another. Flattening a road map or knowledge graph into membership alone destroys its edges.",
(("Cantor, On a Property of the Collection of All Real Algebraic Numbers","https://doi.org/10.1007/BF01446566"),("Kolmogorov, Foundations of the Theory of Probability","https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf"))),
Chapter(202,"relations","Relations — When Two Objects Are Connected",
"Sets give the vault honest boundaries. The animal cards can now belong to villages, habitats, and observation days, but separate membership lists cannot preserve statements such as ‘tiger was seen beside river’ or ‘report cites photograph.’",
"The stone floor becomes a map. Cards name tiger, river, cave, and village; lengths of red thread record *near*, while blue thread records *reported-by*. The objects matter, but the colored pairings carry the new information.",
"place connected objects in the same set and assume co-membership tells us the nature and direction of their connection",
"putting tiger, river, and village into one collection cannot distinguish tiger-near-river from village-reports-tiger. It also cannot distinguish an arrow from tiger to river from the reverse arrow.",
"store each connection as an ordered pair and let a named relation be the set of all pairs carrying the same kind of edge",
"For the relation *near*, lay down `(tiger, river)` and `(otter, river)`. For *reported-by*, lay down `(tiger, village)`. The first position names the object the arrow leaves; the second names where it arrives. Swapping the positions produces a different claim, which is exactly why the pair must be ordered.",
"**A** is the set of animals and **B** the set of places. **A × B** means all animal-place pairs that could be considered. **R** keeps only the pairs for which the named relationship is true. **(a,b) ∈ R** says that one particular directed edge exists.",
"[Tuples](../../MATHEMATICAL_MOVES.md#tuples) preserve first and second position, so direction survives. [Membership](../../MATHEMATICAL_MOVES.md#membership) says whether a proposed edge belongs to the relation. A flat union would preserve the endpoints but erase which endpoint was paired with which.",
r"R\subseteq A\times B,\quad (a,b)\in R",
"A railway map is not the set of cities printed on it. Its meaning lives in the ordered connections showing which journey can follow which.",
"Attention masks, provenance graphs, knowledge graphs, and state transitions were all relations before we used that name. Their arrows were mathematical objects, not decoration.",
"A relation may connect one input to no outputs, one output, or many incompatible outputs. A deterministic machine needs a stronger promise about what follows from each allowed input.",
(("Tarski, On the Calculus of Relations","https://doi.org/10.2307/2268577"),("Bordes et al., Translating Embeddings for Modeling Multi-relational Data","https://arxiv.org/abs/1301.3485"))),
Chapter(203,"functions","Functions — A Reusable Promise from Input to Output",
"Relations preserve arbitrary connections. When the factory applies a tokenizer, matrix, filter, or model, however, repeating the same recorded input under the same state must not silently select two incompatible outputs.",
"At the vault's next table, each animal card enters a brass slot marked *measured weight*. Tiger enters twice. If the slot returns 220 kg once and 17 kg the next time, downstream comparison becomes impossible.",
"keep any relation between inputs and outputs, then choose one of the available outputs whenever the procedure runs",
"the relation may omit an input entirely or attach several outputs to it. A reusable procedure cannot promise what it will do, and composition breaks because the next machine may receive nothing or an arbitrary value.",
"require every allowed input to point to exactly one output, while permitting different inputs to share the same output",
"The weight machine maps tiger to 220, deer to 90, and otter to 12. Tiger may be inserted repeatedly, but its arrow still lands on 220. Deer and another animal could both weigh 90 without violating the promise; the requirement concerns one output *per input*, not one private output per animal.",
"**A** names the domain of allowed inputs and **B** the codomain in which outputs live. **f** names the complete mapping promise. **f(x)** is the unique output assigned to input x. The arrow records direction from domain to codomain rather than numerical equality.",
"[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve the direction of the machine. [Function application](../../MATHEMATICAL_MOVES.md#function-application) asks for the output belonging to this input, and [equality](../../MATHEMATICAL_MOVES.md#equals) records the returned value. Allowing several outputs would describe a general relation, not the deterministic responsibility we need.",
r"f:A\to B,\quad y=f(x)",
"A function is a sealed promise: hand it an allowed question and it owes you one answer, even when many different questions happen to share that answer.",
"Every layer in the neural network, every preprocessing stage, and every operation in the training factory is a function. Composition works only because each stage knows what object the preceding stage produces.",
"A function promises an output but says nothing about which numerical description is most revealing. The same geometric object can receive different coordinates without becoming a different object.",
(("Church, An Unsolvable Problem of Elementary Number Theory","https://www.jstor.org/stable/2371045"),("Hornik, Stinchcombe, and White, Multilayer Feedforward Networks Are Universal Approximators","https://doi.org/10.1016/0893-6080(89)90020-8"))),
Chapter(204,"bases-coordinates","Bases and Coordinates — The Same Object in Another Language",
"Functions turn inputs into dependable outputs. Our vector functions seem to operate directly on lists of coordinates, yet rotating the ruler changes every coordinate while leaving the animal's physical displacement untouched.",
"A ranger walks three steps east and two north. On the square floor this is recorded as `[3,2]`. Another ranger carries diagonal rulers: one points northeast, the other northwest. The same walk must acquire different numbers in that language.",
"treat the coordinate list as the vector itself and conclude that changing the list changes the underlying displacement",
"the east-north list `[3,2]` and its diagonal-coordinate list disagree numerically even though both return the ranger to the same physical endpoint. Coordinates depend on the chosen measuring directions.",
"choose a set of basis directions and define coordinates as the amounts of those directions whose combination reconstructs the vector",
"With basis arrows east `[1,0]` and north `[0,1]`, the walk is `3 east + 2 north`. If the new basis uses northeast `[1,1]` and northwest `[-1,1]`, then `2.5 northeast - 0.5 northwest` reconstructs `[3,2]`. The coefficients changed; the endpoint did not.",
"**v** is the displacement being described. **b₁,…,bₙ** are the chosen basis directions. **c₁,…,cₙ** are coordinates in that basis. Multiplying a basis direction by its coordinate stretches or reverses it; adding the contributions reconstructs v.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales each basis direction by the amount required. [Addition](../../MATHEMATICAL_MOVES.md#addition) joins independent directional contributions. Concatenating the numbers would merely store them side by side and would not reconstruct the displacement.",
r"\mathbf v=c_1\mathbf b_1+c_2\mathbf b_2+\cdots+c_n\mathbf b_n",
"The same melody can be written for piano or violin. The marks change because the instrument's basis changes; the melody's relationships survive.",
"Embeddings choose learned coordinates, attention projects them into query and key bases, and RoPE rotates coordinate pairs. A representation is always a choice of mathematical language.",
"A collection of candidate basis directions may contain redundancy or fail to reach part of the space. We need to know which directions are genuinely new and what region their combinations can cover.",
(("Pearson, On Lines and Planes of Closest Fit to Systems of Points in Space","https://doi.org/10.1080/14786440109462720"),("Elhage et al., A Mathematical Framework for Transformer Circuits","https://transformer-circuits.pub/2021/framework/index.html"))),
Chapter(205,"span-linear-independence","Span and Linear Independence — Which Directions Are Truly New?",
"A basis gives coordinates meaning only if its directions reach the required space without secretly repeating one another. Adding more arrows to the table can create the appearance of capacity while contributing no new possible movement.",
"The cartographer offers east `[1,0]`, north `[0,1]`, and northeast `[1,1]` as three foundational directions on a two-dimensional map. The third feels useful, but the first two can already reconstruct it.",
"count every stored direction as a new dimension and assign each one an independent coordinate",
"northeast equals east plus north, so the same displacement receives many coefficient lists. The coordinate system can no longer tell which explanation is unique, and parameter count exaggerates true capacity.",
"call the reachable collection of combinations the span, and call directions independent only when no nontrivial weighted combination collapses to zero",
"Ask whether `a·east + b·north + c·northeast` can return to `[0,0]` without all weights being zero. Choosing `a=-1`, `b=-1`, and `c=1` does exactly that. Northeast therefore adds no new reachable point. East and north alone span the entire floor and give each displacement one coordinate pair.",
"**span(v₁,…,vₖ)** is every vector obtainable by scaling and adding the listed directions. **aᵢ** are proposed weights. The zero vector represents no movement. If the only weights producing zero are all zero, no direction can be reconstructed from the others.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales candidate directions and [summation](../../MATHEMATICAL_MOVES.md#summation) combines them. [Equality](../../MATHEMATICAL_MOVES.md#equals) asks whether the combination collapses to zero. Merely counting vectors cannot detect that one is already contained in the others' span.",
r"a_1\mathbf v_1+\cdots+a_k\mathbf v_k=\mathbf0\Longrightarrow a_1=\cdots=a_k=0",
"Three keys on a ring do not open three doors when one key is only a copy. Independence counts new access, not metal objects.",
"Superposition asks how many useful feature directions share a space; LoRA asks how many update directions are actually needed. Rank and independence make those capacity claims precise.",
"Independence tells which directions are new but not how a transformation repeatedly stretches the space. Some directions persist under repeated application while others turn and mix.",
(("Hu et al., LoRA: Low-Rank Adaptation of Large Language Models","https://arxiv.org/abs/2106.09685"),("Elhage et al., Toy Models of Superposition","https://arxiv.org/abs/2209.10652"))),
Chapter(206,"eigenvectors-eigenvalues","Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn",
"Span and independence reveal the true directions available in a space. When one matrix is applied again and again—one transition, message-passing step, or layer after another—the coordinate picture can still become difficult to follow.",
"On the vault floor, a transformation doubles east-west displacement but leaves north-south displacement unchanged. Most arrows change both length and direction. An arrow pointing exactly east does something quieter: it remains east and only stretches.",
"track every coordinate of every repeatedly transformed arrow and hope the long-term pattern becomes obvious",
"coordinate expressions grow while the persistent behavior stays hidden. Two initial arrows can look unrelated even when repeated transformation eventually makes both align with the same dominant direction.",
"search for nonzero directions that the transformation only scales, and record the corresponding scale factors",
"Apply the matrix `[[2,0],[0,1]]` to east `[1,0]`: the result is `[2,0]`, exactly twice east. Apply it to north `[0,1]`: the result remains north. East has scale 2 and north scale 1. Apply it repeatedly and any arrow with an east component becomes increasingly east-dominated.",
"**A** is the transformation. **v** is a nonzero direction. **λ** is the scalar stretch, shrinkage, or sign reversal. Equality says transforming v and merely scaling v reach the same arrow, so direction is preserved.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the transformation to the direction. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales that same direction, and [equality](../../MATHEMATICAL_MOVES.md#equals) demands the two routes coincide. Adding λ would translate the arrow rather than describe proportional stretching.",
r"A\mathbf v=\lambda\mathbf v",
"In a river, most leaves swirl, but a leaf placed on the main current keeps pointing downstream while its distance from the bridge changes predictably.",
"PageRank studies a persistent direction of repeated link transitions; covariance eigenvectors become principal directions; training stability depends on repeated transformations' spectral behavior.",
"Not every matrix has enough real eigenvectors to form a basis, and rectangular matrices do not even map a space back into itself. We still need a way to cast the closest shadow and expose the important input-output directions of any matrix.",
(("Page et al., The PageRank Citation Ranking","http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf"),("Perozzi, Al-Rfou, and Skiena, DeepWalk","https://arxiv.org/abs/1403.6652"))),
Chapter(207,"orthogonality-projection","Orthogonality and Projection — Finding the Closest Shadow",
"Eigenvectors expose directions preserved by a transformation. The vault now presents a simpler geometric failure: an observed arrow does not lie on the one-dimensional rail our model is allowed to use.",
"A tiger track points `[3,2]`, but the ranger's simplified map retains only the eastward rail `[1,0]`. We need the point on that rail that misrepresents the track as little as possible.",
"copy whichever coordinate looks largest or slide to an arbitrary point on the allowed rail",
"the chosen point changes when coordinates are renamed and gives no proof that another allowed point is not closer. The discarded error may still point partly along the rail, revealing that more of the track could have been retained.",
"choose the shadow whose leftover error is perpendicular to the allowed direction, because then no further movement along the rail can reduce the distance",
"Project `[3,2]` onto east `[1,0]`. Their dot product is 3; east's dot product with itself is 1; the required scale is therefore 3. The shadow is `[3,0]`, leaving error `[0,2]`. That error has zero dot product with east, so every remaining disagreement points outside the allowed rail.",
"**v** is the observed track and **u** the allowed direction. **v·u** measures alignment; **u·u** measures u's squared length. Their ratio finds how much u fits inside v. Multiplying u by that ratio constructs the shadow.",
"[The dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures directional agreement. [Division](../../MATHEMATICAL_MOVES.md#division) removes dependence on the chosen length of u, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) rebuilds the shadow in the allowed direction. Using raw v·u alone would change the answer if the same rail were described by a longer basis arrow.",
r"\mathrm{proj}_{\mathbf u}(\mathbf v)=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u",
"A sundial's shadow is not the object, but under a fixed light it is the closest information the ground plane can retain.",
"Linear probes project hidden states onto readable directions; least squares projects observations into a model subspace; attention projects embeddings into query, key, and value spaces.",
"Projection handles one chosen subspace. For an arbitrary rectangular matrix, we still need to discover the paired input and output directions that carry most of its action.",
(("Pearson, On Lines and Planes of Closest Fit to Systems of Points in Space","https://doi.org/10.1080/14786440109462720"),("Hu et al., LoRA","https://arxiv.org/abs/2106.09685"))),
Chapter(208,"singular-value-decomposition","Singular Value Decomposition — The Important Directions of Any Matrix",
"Projection finds the closest shadow once an allowed direction is known. A large weight matrix offers thousands of possible directions, and neither its raw entries nor ordinary eigenvectors tell us which input directions carry most strongly into which output directions.",
"The enginewright lowers a rectangular brass plate with many input grooves and fewer output bells. Some coordinated pushes ring loudly; others barely move the mechanism. We want the simplest faithful account of those channels.",
"keep the largest individual matrix entries and set the rest to zero",
"a useful direction may be distributed across many modest entries, while one large entry may contribute little to the matrix's coordinated behavior. Entry size ignores how rows and columns act together.",
"rotate the input into orthogonal right-singular directions, scale each by a nonnegative singular value, and rotate into orthogonal output directions; keep the strongest channels for a principled low-rank approximation",
"For the diagonal plate `[[3,0],[0,1]]`, the east input rings with strength 3 and the north input with strength 1. Keeping only the first channel produces `[[3,0],[0,0]]`: the best rank-one approximation under squared error. The omitted channel's strength, 1, states exactly what was lost.",
"**Vᵀ** changes from ordinary input coordinates to right-singular directions. **Σ** scales those directions by singular values ordered strongest first. **U** expresses the results in output directions. **Aₖ** keeps only the first k channels.",
"[Function composition](../../MATHEMATICAL_MOVES.md#function-composition) fixes the order: rotate input, scale channels, rotate output. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets each stage act through the previous one. Keeping arbitrary entries would not preserve the strongest coordinated directions or give the best rank-k squared-error approximation.",
r"A=U\Sigma V^T,\quad A_k=U_k\Sigma_kV_k^T",
"A prism does not rank individual patches of glass. It reveals the hidden channels through which the whole beam can travel.",
"LoRA assumes useful updates occupy a low-rank subspace; embedding analysis and compression rely on singular directions; numerical solvers use singular values to expose ill-conditioning.",
"SVD organizes finite linear transformations. Our learning chapters repeatedly spoke of changes becoming ‘infinitely small,’ but finite examples alone have not made that passage precise.",
(("Eckart and Young, The Approximation of One Matrix by Another of Lower Rank","https://doi.org/10.1007/BF02288367"),("Hu et al., LoRA","https://arxiv.org/abs/2106.09685"))),
Chapter(209,"limits","Limits — Approaching What Cannot Be Reached in One Step",
"SVD exposes what a finite matrix preserves and discards. Calculus asks a stranger question: what does a procedure approach as a step becomes smaller without ever requiring a final smallest positive step?",
"A messenger must cross one metre to the next stone mark. First the remaining gap is one half, then one quarter, one eighth, and so on. No listed move is zero, yet the marks gather around the destination.",
"declare that a sequence reaches its destination only when one finite term equals the destination exactly",
"the gaps `1/2, 1/4, 1/8, ...` never equal zero, so the rule denies the visible fact that they can be made smaller than any requested tolerance.",
"define the destination by a guarantee: however tiny a permitted error is chosen, all sufficiently late terms fall inside it",
"If the required gap is below 0.01, choose n greater than 100 and `1/n` is small enough. If the requirement tightens to 0.0001, choose n greater than 10,000. The destination zero is earned not by arriving at a final term, but by defeating every positive tolerance.",
"**n** counts the step and grows without bound. **1/n** is the remaining gap. **lim** names the value approached. The arrow toward infinity describes unbounded growth in n; equality names the unique destination whose every tolerance can eventually be met.",
"[Division](../../MATHEMATICAL_MOVES.md#division) makes the gap shrink as the count grows. [The limit](../../MATHEMATICAL_MOVES.md#limit) records the tolerance guarantee rather than substituting infinity as an ordinary number. Writing `1/∞` would hide the reasoning because infinity is not a final denominator reached by the sequence.",
r"\lim_{n\to\infty}\frac{1}{n}=0",
"A distant mountain does not jump closer. It fills more of the window as you walk, and every demanded closeness determines how far you must travel.",
"Derivatives, continuous activations, convergence of optimization, integrals, and probability laws all depend on limits. The quiet symbol carries an entire challenge-and-response guarantee.",
"A scalar limit describes one approaching quantity. A neural loss depends on millions of parameters, so we must ask how one output changes along every coordinate direction.",
(("Cauchy, Cours d’Analyse","https://archive.org/details/coursdanalysede00cauc"),("Chen et al., Neural Ordinary Differential Equations","https://arxiv.org/abs/1806.07366"))),
Chapter(210,"partial-derivatives-gradients","Partial Derivatives and Gradients — One Landscape, Many Directions",
"Limits make ‘arbitrarily small’ precise. A loss surface has not one input but millions, and moving stripe sensitivity while freezing weight sensitivity answers a different question from moving both together.",
"The tiger alarm has two dials: stripe weight w₁ and size weight w₂. Its local loss is a hillside over the floor. The ranger can nudge east, north, or diagonally and observe different changes.",
"compute one ordinary derivative as if the entire parameter vector were a single undifferentiated number",
"the answer cannot say which dial caused which part of the change or which physical direction rises fastest. Different paths through the same point produce different slopes.",
"hold every other dial fixed to measure one partial derivative at a time, then gather those coordinate sensitivities into the gradient vector",
"Near the current setting, nudging w₁ by 0.01 raises loss by about 0.03, giving sensitivity 3. Nudging w₂ by 0.01 lowers loss by about 0.01, giving sensitivity -1. The gradient `[3,-1]` points toward fastest local increase; its negative points toward fastest local decrease under ordinary Euclidean distance.",
"**L** is the loss landscape and **w₁,…,wₙ** its adjustable coordinates. **∂L/∂wᵢ** asks what L does when only wᵢ moves infinitesimally. **∇L** stores every such answer in coordinate order.",
"[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one coordinate while others are fixed. [Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves the separate sensitivities as one ordered vector. Summing them would erase direction and could let positive and negative effects cancel.",
r"\nabla L(\mathbf w)=\left[\frac{\partial L}{\partial w_1},\ldots,\frac{\partial L}{\partial w_n}\right]",
"At a mountain pass, ‘the slope’ is incomplete until you say which way you face. The gradient is the compass arrow assembled from every coordinate-facing slope.",
"Gradient descent, backpropagation, Adam, clipping, and attribution all use this object. Earlier chapters used it operationally; this excavation reveals why its components must remain ordered.",
"A gradient describes one scalar output. A layer often maps many inputs to many outputs, so one vector cannot preserve every input-output sensitivity.",
(("Baydin et al., Automatic Differentiation in Machine Learning: a Survey","https://arxiv.org/abs/1502.05767"),("LeCun, Bengio, and Hinton, Deep Learning","https://doi.org/10.1038/nature14539"))),
Chapter(211,"jacobians","Jacobians — When Many Outputs Change Together",
"The gradient gathers how one loss responds to many parameters. A network layer, camera transform, or robot model produces several outputs at once, each responding differently to every input.",
"A tracker converts two measurements—weight and stride—into two outputs: danger score and estimated speed. Changing weight affects both outputs, but not by the same amount.",
"differentiate only the first output and reuse that gradient as the sensitivity of the entire transformation",
"the second output's response disappears. Downstream uncertainty, volume change, and chain-rule propagation become wrong because one row of evidence impersonates the whole map.",
"give every output its own gradient row and arrange all output-input sensitivities into one matrix",
"Suppose danger is `2w+s` and estimated speed is `w-s`. Increasing w by one changes the outputs by `[2,1]`; increasing s by one changes them by `[1,-1]`. Put the response to w in the first column and the response to s in the second. The resulting matrix `[[2,1],[1,-1]]` predicts the small output change produced by any small input change.",
"**fᵢ** is output i and **xⱼ** input j. Each entry **∂fᵢ/∂xⱼ** asks how that particular output responds to that particular input. Row order preserves outputs; column order preserves inputs. **J** names the complete local linear map.",
"[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one output-input relationship. [Tables](../../MATHEMATICAL_MOVES.md#tables) preserve the exact row-column mapping, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets the Jacobian act on a small input change. A sum would collapse distinct outputs and inputs into one ambiguous sensitivity.",
r"J_{ij}=\frac{\partial f_i}{\partial x_j}",
"A theatre lighting board has many sliders and many lamps. The Jacobian is the local wiring chart saying how each lamp responds to each slider.",
"Backpropagation multiplies local Jacobian effects without usually materializing the full matrices; normalizing flows use Jacobian determinants; robustness asks how input perturbations propagate through this map.",
"The Jacobian is a first-order description. Two landscapes can share the same slope at one point while bending into a bowl, ridge, or saddle immediately afterward.",
(("Baydin et al., Automatic Differentiation in Machine Learning","https://arxiv.org/abs/1502.05767"),("Chen et al., Neural Ordinary Differential Equations","https://arxiv.org/abs/1806.07366"))),
Chapter(212,"hessians-curvature","Hessians and Curvature — Why the Same Slope Can Hide Different Valleys",
"Jacobians record first-order response. At a flat-looking point the gradient may be zero, yet the point could be the bottom of a safe bowl, the top of a hill, or a saddle that rises east and falls north.",
"The vault floor contains two stone surfaces. At the centre both feel level. One curves upward in every direction; the other curves upward east-west and downward north-south.",
"declare every zero-gradient point a successful minimum and stop moving",
"the saddle also has zero first-order slope. Stopping there mistakes balanced opposing curvature for completion, while choosing a large step without curvature can leap across a narrow bowl.",
"differentiate the gradient again and store how every pair of coordinates changes the local slope",
"For `L(w₁,w₂)=w₁²-w₂²`, both partial derivatives vanish at `[0,0]`. The second derivative along w₁ is 2; along w₂ it is -2; cross-effects are zero. The Hessian `[[2,0],[0,-2]]` exposes a saddle because one direction bends up and another down.",
"**Hᵢⱼ** asks how the sensitivity in direction i changes when coordinate j moves. Diagonal entries describe coordinate curvature; off-diagonal entries describe coupled bending. The complete matrix is the local curvature map.",
"[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) are applied a second time because curvature is change in slope. [Tables](../../MATHEMATICAL_MOVES.md#tables) preserve pairwise coordinate effects. Looking only at the diagonal would miss rotations and coupled directions; summing entries would destroy the geometry.",
r"H_{ij}=\frac{\partial^2L}{\partial w_i\partial w_j}",
"A marble at a level point needs more than a spirit level. The surrounding bend tells whether it rests in a bowl, balances on a dome, or waits on a saddle.",
"Initialization, learning rates, Newton-like methods, loss-landscape analysis, and sharpness all depend on curvature even when large models approximate it indirectly.",
"Exact Hessians are expensive and local curvature still describes only a neighborhood. We need a disciplined way to approximate a complicated function near the point using the derivatives already measured.",
(("Dauphin et al., Identifying and Attacking the Saddle Point Problem","https://arxiv.org/abs/1406.2572"),("Baydin et al., Automatic Differentiation in Machine Learning","https://arxiv.org/abs/1502.05767"))),
Chapter(213,"taylor-approximation","Taylor Approximation — Borrowing a Function’s Local Shape",
"The Hessian reveals local bending. Re-evaluating a complicated model for every nearby possibility remains costly, and a slope alone fails as soon as curvature matters.",
"The ranger knows a signal's value, slope, and curvature at dial setting a. A nearby setting a+h must be estimated before the expensive full detector can run.",
"extend the tangent line indefinitely and assume constant slope everywhere",
"for a curved signal the linear prediction drifts, and doubling h can more than double the error. The tangent remembers direction but forgets that the direction itself changes.",
"build a local polynomial: start with the known value, add slope times displacement, then add curvature times squared displacement with the counting factor required by repeated differentiation",
"Use `f(x)=eˣ` near zero. Its value, slope, and curvature at zero are all 1. At h=0.1, the second-order estimate is `1 + 0.1 + 0.1²/2 = 1.105`, close to the true 1.10517. Removing the squared term gives 1.1 and visibly loses curvature.",
"**a** is the known location and **h** the nearby displacement. **f(a)** anchors the estimate. **f′(a)h** carries local slope through the displacement. **f″(a)h²/2** repairs the first curvature error. The approximation sign admits omitted higher-order terms.",
"[Addition](../../MATHEMATICAL_MOVES.md#addition) lets distinct orders contribute without erasing one another. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) makes each derivative act through its displacement, while [powers](../../MATHEMATICAL_MOVES.md#powers) make curvature shrink faster than slope as h becomes tiny. Multiplying all terms together would make any zero term erase the approximation.",
r"f(a+h)\approx f(a)+f'(a)h+\frac{f''(a)}{2}h^2",
"A sculptor reconstructs the nearby curve from how the stone faces now, how its direction changes, and how quickly that change itself bends.",
"Gradient descent trusts the first-order term; Newton methods use the second; neural tangent analyses study regimes where the local linear picture remains informative.",
"Taylor pieces describe local behavior. To recover total water, distance, probability, or change across a whole interval, many small contributions must be accumulated rather than inspected near one point.",
(("Jacot, Gabriel, and Hongler, Neural Tangent Kernel","https://arxiv.org/abs/1806.07572"),("Chen et al., Neural Ordinary Differential Equations","https://arxiv.org/abs/1806.07366"))),
Chapter(214,"integrals","Integrals — Reconstructing a Whole from Infinitesimal Pieces",
"Taylor approximation reconstructs a function near one point. The factory's meters report rates—tokens per second, energy per second, water flow per minute—but the final account needs a total across time.",
"A rescue tank fills at a changing rate r(t). The ranger reads the rate at many moments but wants the total water delivered between dawn a and dusk b.",
"multiply one chosen rate by the entire duration",
"the flow is slow at dawn and fast at noon, so one sample grants every moment the wrong rate. Taking more samples helps, but their contributions need a rule that survives as slices become thinner.",
"divide time into small intervals, multiply each interval's width by a representative rate, add the resulting little volumes, and take the limit as the widest interval shrinks toward zero",
"Over four one-minute intervals the measured rates are 1, 2, 3, and 4 litres per minute. Rectangles give `1×1 + 2×1 + 3×1 + 4×1 = 10` litres. Halving the interval uses more, thinner rectangles and follows the changing flow more closely. The integral is the value these sums approach as no interval remains visibly wide.",
"**[a,b]** is the time interval. **Δtᵢ** is one slice width and **r(tᵢ)** its sampled rate. Their product is a small amount, not a rate. Summation combines slice amounts; the limit removes dependence on a coarse partition. The integral sign names the accumulated whole.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) converts rate times duration into amount. [Summation](../../MATHEMATICAL_MOVES.md#summation) joins disjoint amounts; multiplication among slices would make one zero-flow moment erase all water. [The limit](../../MATHEMATICAL_MOVES.md#limit) forces the partition error arbitrarily small.",
r"\int_a^b r(t)dt=\lim_{\max\Delta t_i\to0}\sum_i r(t_i)\Delta t_i",
"A mosaic becomes an image because each tiny tile contributes colour to a place; making the tiles finer reveals the curve rather than changing the scene.",
"Expected values are integrals over possible outcomes, Neural ODEs integrate hidden-state change, and continuous-time signals become discrete computations through numerical quadrature.",
"Accumulation tells how much signal exists but can hide the simple repeating components inside it. Audio waves that look tangled in time may become sparse when described by frequency.",
(("Chen et al., Neural Ordinary Differential Equations","https://arxiv.org/abs/1806.07366"),("Kovachki et al., Neural Operator","https://arxiv.org/abs/2108.08481"))),
Chapter(215,"fourier-analysis","Fourier Analysis — Hearing Frequencies Hidden Inside Time",
"Integrals recover wholes from local pieces. A microphone's whole waveform still looks like an unruly sequence of pressures, even when a listener hears a pure low note, a high whistle, and a repeating wingbeat.",
"The Scriptorium lowers a string of microphone samples into the vault. The values rise and fall, but no sample announces which repeating rhythms created the pattern.",
"compare waveforms only sample by sample in time",
"the same note shifted slightly appears very different at every position, and two overlapping tones hide inside one jagged trace. Time coordinates expose when, not which frequency.",
"compare the signal with a family of rotating sine-and-cosine patterns and add the agreements, producing one coefficient for each candidate frequency",
"Take four samples `[1,0,-1,0]`. They complete one oscillation: high, centre, low, centre. Multiplying them against the matching rotating pattern makes the four contributions reinforce; mismatched frequencies alternate and largely cancel. The coefficient's magnitude reports how strongly that rhythm is present.",
"**xₙ** is sample n among N samples. **k** names a candidate frequency. The complex exponential is a compact rotating cosine-and-sine ruler. Multiplying tests phase-aligned agreement; summing gathers evidence across time. **Xₖ** is the coefficient for frequency k.",
"[The exponential](../../MATHEMATICAL_MOVES.md#exponential) supplies a regularly rotating comparison pattern. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) measures sample-by-pattern agreement, [summation](../../MATHEMATICAL_MOVES.md#summation) lets aligned evidence reinforce, and the [negative sign](../../MATHEMATICAL_MOVES.md#negative-sign) fixes the analysis rotation direction. Adding raw samples would keep only the zero-frequency total.",
r"X_k=\sum_{n=0}^{N-1}x_n e^{-2\pi i kn/N}",
"A prism separates colours already travelling together in white light. Fourier analysis is a prism for rhythms.",
"Speech features, positional rotations, convolution, image filtering, and Fourier neural operators all move between coordinate systems where different structure becomes simple.",
"Fourier coefficients describe deterministic signal content. Real observations also vary unpredictably, so the next object must turn uncertain outcomes into numerical quantities with distributions.",
(("Li et al., Fourier Neural Operator for Parametric Partial Differential Equations","https://arxiv.org/abs/2010.08895"),("Kovachki et al., Neural Operator","https://arxiv.org/abs/2108.08481"))),
Chapter(216,"random-variables-distributions","Random Variables and Distributions — Turning Outcomes into Quantities",
"Fourier analysis gives deterministic signals new coordinates. The ranger's camera, however, may record zero, one, or several tigers tomorrow; before the observation, the count is not an unknown fixed number but a quantity attached to several possible worlds.",
"Three cards describe tomorrow: no tiger, one tiger, and two tigers. Each card has a probability, but the station wants to compute expected food use and variation in the *count*.",
"treat the outcome label itself as a number and perform arithmetic directly on names such as ‘no sighting’ and ‘two sightings’",
"outcomes may be stories, images, or paths rather than numbers, and the same numerical question can group many different outcomes. Arithmetic needs a mapping from possible worlds to values.",
"define a random variable as a function assigning a numerical value to every outcome, then transfer probability mass through that mapping to form its distribution",
"Let Ω contain four equally likely camera histories. Two contain no tiger, one contains one tiger, and one contains two. The counting function X maps them to 0, 0, 1, and 2. Therefore `P(X=0)=2/4`, `P(X=1)=1/4`, and `P(X=2)=1/4`. Different histories can share one count without becoming the same history.",
"**Ω** is the sample space of possible histories. **X** is the function turning a history into a real count. **P(X=x)** gathers the probability of every history mapped to value x. The distribution is the resulting allocation of probability across possible numerical values.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) converts each outcome into the quantity we care about. [Probability](../../MATHEMATICAL_MOVES.md#probability) preserves how much possibility maps to each value, and [summation](../../MATHEMATICAL_MOVES.md#summation) combines different outcomes sharing the same value. Multiplying their probabilities would describe all histories occurring together, a different event.",
r"P(X=x)=\sum_{\omega:X(\omega)=x}P(\omega)",
"Weather is a story; temperature is a random variable extracted from that story. The number is a question asked of the world, not the whole world itself.",
"Loss, reward, token count, model output, and gradient noise are random variables. Their distributions—not isolated values—determine learning and evaluation.",
"A distribution describes current uncertainty. When a paw print arrives, probabilities must be rearranged according to how compatible each hidden story was with that evidence.",
(("Kolmogorov, Foundations of the Theory of Probability","https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf"),("Kingma and Welling, Auto-Encoding Variational Bayes","https://arxiv.org/abs/1312.6114"))),
Chapter(217,"conditional-probability-bayes","Conditional Probability and Bayes’ Rule — Let Evidence Rearrange Belief",
"Random variables turn possible worlds into measurable quantities. A fresh paw print should change the tiger probability, but merely retaining yesterday's distribution ignores the reason observation matters.",
"Before seeing tracks, the valley expects tiger on one day in ten and deer on nine. Deep clawed tracks are likely under tiger and rare under deer. The print has arrived; the old shares can no longer remain untouched.",
"compare only how well each animal explains the print and choose the largest likelihood",
"likelihood ignores how common each animal was before the evidence. A moderately diagnostic clue could make an extremely rare story look certain if prior plausibility is discarded.",
"multiply each prior belief by that story's support for the evidence, then divide by the total support across all stories so the surviving weights again form one distribution",
"Out of 100 imagined days, expect 10 tiger days and 90 deer days. Suppose deep tracks appear on 8 of 10 tiger days but only 9 of 90 deer days. Among the 17 deep-track days, 8 involve tiger. After observing deep tracks, tiger probability becomes `8/17`, not 0.8 and not the old 0.1.",
"**H** is one hidden story and **E** the observed evidence. **P(H)** is prior plausibility. **P(E|H)** is likelihood. Their product is the joint share where H and E occur. **P(E)** totals all routes to the evidence. Division asks what fraction of evidence-compatible worlds contain H.",
"[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) states which fact is held as known. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) requires both prior story and compatible evidence, while [division](../../MATHEMATICAL_MOVES.md#division) restricts attention to worlds where E occurred. Adding prior and likelihood would mix quantities that do not form a joint share.",
r"P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}",
"Evidence is a gate, not paint. It does not colour every old belief equally; it admits worlds in proportion to how naturally they could have produced what was seen.",
"Likelihood, calibration, Bayesian updating, filtering, and uncertainty-aware planning all reuse this rearrangement. Excavation 102 used it; here we expose the counting skeleton underneath.",
"A posterior distribution can still be too rich to carry everywhere. One mean alone, however, hides whether beliefs are tightly gathered, widely spread, or moving together.",
(("Bayes, An Essay towards Solving a Problem in the Doctrine of Chances","https://doi.org/10.1098/rstl.1763.0053"),("Gal and Ghahramani, Dropout as a Bayesian Approximation","https://arxiv.org/abs/1506.02142"))),
Chapter(218,"expectation-variance-covariance","Expectation, Variance, and Covariance — Centre, Spread, and Shared Motion",
"Bayes' rule returns a full distribution after evidence. To budget supplies or compare models, the station needs summaries, but one central value must not pretend that uncertainty and joint movement disappeared.",
"Two routes both average one tiger sighting per day. Route A always sees exactly one. Route B sees zero half the time and two half the time. The means agree; their risks do not.",
"report only the average and treat distributions sharing it as interchangeable",
"the average hides spread. It also cannot reveal whether tiger count and alarm count rise together or move independently, which matters when one is used to predict the other.",
"compute expectation as a probability-weighted centre, variance as average squared departure from that centre, and covariance as average product of paired departures",
"Route A's count is always 1, so every departure from mean 1 is zero and variance is zero. Route B's departures are -1 and +1; squaring gives 1 in either case, so variance is 1. If alarm departures carry the same signs as tiger departures, their products are positive and covariance reveals shared movement.",
"**μ** is the expected centre. **X-μ** is one departure. Squaring prevents low and high outcomes from cancelling in variance. **Y-E[Y]** is the paired departure of a second quantity. Multiplying paired departures records same-direction as positive and opposite-direction as negative.",
"[Expectation](../../MATHEMATICAL_MOVES.md#expectation) lets each possible value contribute in proportion to its probability. [Variance](../../MATHEMATICAL_MOVES.md#variance) uses squared departures so opposite errors do not cancel. [Covariance](../../MATHEMATICAL_MOVES.md#covariance) multiplies paired departures; adding them would lose whether the two quantities moved together on the same occasion.",
r"E[X]=\sum_x xP(X=x),\quad Var(X)=E[(X-E[X])^2],\quad Cov(X,Y)=E[(X-E[X])(Y-E[Y])]",
"The centre of a flock says where to look; its spread says how wide to search; synchronized turns say which birds respond to the same wind.",
"Normalization uses means and variances, PCA diagonalizes covariance, initialization controls signal variance, and gradient-noise analysis compares shared direction with disagreement.",
"These quantities are usually estimated from samples. Before trusting them, we need a reason that accumulating more independent evidence makes sample averages settle rather than wander forever.",
(("Ioffe and Szegedy, Batch Normalization","https://arxiv.org/abs/1502.03167"),("Pearson, On Lines and Planes of Closest Fit","https://doi.org/10.1080/14786440109462720"))),
Chapter(219,"law-large-numbers","The Law of Large Numbers — Why Averages Eventually Settle",
"Expectation, variance, and covariance describe a distribution. The ranger sees only a finite stream of days and must justify why the observed average can stand in for the hidden expected value.",
"A fair coin decides whether the camera opens the north gate. After one toss the observed head rate is either zero or one—both far from the expected half.",
"demand that every short sample reproduce the population expectation exactly",
"chance has not failed when the first three tosses are all heads. Short runs fluctuate, so exact equality would reject honest randomness and make estimation impossible.",
"study the sample mean as the number of independent observations grows and ask whether the probability of a substantial error shrinks toward zero",
"After 10 tosses, 7 heads gives average 0.7. After 100, perhaps 54 heads gives 0.54. After 10,000, 5,013 heads gives 0.5013. No run is promised monotonic improvement, but large persistent deviations become increasingly unlikely under the same fair process.",
"**Xᵢ** is observation i with expected value μ. The sum combines independent evidence. Division by n forms the per-observation average. The arrow toward μ describes convergence as sample size grows, not equality at any finite n.",
"[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every observation vote. [Division](../../MATHEMATICAL_MOVES.md#division) prevents the total from growing merely because more observations arrived, and [the limit](../../MATHEMATICAL_MOVES.md#limit) states the large-sample guarantee. Multiplying observations would let one zero erase the entire history.",
r"\overline X_n=\frac1n\sum_{i=1}^{n}X_i\longrightarrow\mu",
"One drop cannot reveal the river's average depth. Many well-spaced soundings do not eliminate variation, but they make a persistent false average harder to sustain.",
"Mini-batches, evaluation means, Monte Carlo estimates, calibration bins, and distributed gradient averages rely on this settling behavior—plus assumptions about sampling and dependence.",
"The law explains where the average goes but not the shape of its remaining error. Across many experiments, normalized averages often approach a bell-shaped distribution.",
(("Kolmogorov, Foundations of the Theory of Probability","https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf"),("Goyal et al., Accurate, Large Minibatch SGD","https://arxiv.org/abs/1706.02677"))),
Chapter(220,"central-limit-theorem","The Central Limit Theorem — Why Bell Shapes Keep Appearing",
"The law of large numbers says sample averages settle. It does not tell the station how far a finite average is likely to lie from the truth or why sums of very different small disturbances often share one familiar bell shape.",
"Each daily sensor error is bounded but irregular. The monthly average combines heat, battery noise, wind, and rounding. The exact distribution of each source is inconvenient and different.",
"assume the average has the same distributional shape as each individual disturbance",
"averaging changes scale and shape. A single skewed measurement and the mean of one hundred such measurements do not have the same uncertainty.",
"centre the sample mean at μ, divide by its standard error σ/√n, and study the distribution of that normalized error as n grows",
"Suppose individual measurements have mean 10 and standard deviation 2. An average of 100 independent readings still centres at 10, but its standard error is `2/√100 = 0.2`. Repeating the entire 100-reading experiment produces normalized errors that increasingly resemble a standard bell even when individual readings are not bell-shaped.",
"**μ** and **σ** are the population mean and standard deviation. **X̄ₙ-μ** is estimation error. **σ/√n** is the error's natural scale under independent finite-variance sampling. Dividing creates a dimensionless quantity comparable across n. **N(0,1)** names the limiting standard normal distribution.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) isolates estimation error. [The square root](../../MATHEMATICAL_MOVES.md#square-root) appears because independent variances add while standard deviations are square roots of variance. [Division](../../MATHEMATICAL_MOVES.md#division) expresses error in standard-error units; dividing by n would shrink too quickly.",
r"\frac{\overline X_n-\mu}{\sigma/\sqrt n}\Longrightarrow N(0,1)",
"Many uneven footsteps become a smooth crowd rhythm when heard from far away—not because individuals became identical, but because independent deviations accumulated on a shared scale.",
"Confidence intervals, uncertainty estimates, initialization theory, approximate Bayesian inference, and Gaussian-process limits of wide networks all borrow versions of this phenomenon.",
"A bell approximation still does not decide whether an observed improvement is convincing, practically meaningful, or produced by a flawed experiment. Evidence needs an explicit claim and error procedure.",
(("Lee et al., Deep Neural Networks as Gaussian Processes","https://arxiv.org/abs/1711.00165"),("Matthews et al., Gaussian Process Behaviour in Wide Deep Neural Networks","https://arxiv.org/abs/1804.11271"))),
Chapter(221,"hypothesis-tests-confidence-intervals","Hypothesis Tests and Confidence Intervals — When Is an Improvement Convincing?",
"The central limit theorem gives the shape and scale of repeated sample averages. It still does not decide whether a measured model improvement is evidence of a real change or an ordinary tremor of sampling.",
"Two assistants answer the same 100 field questions. The new assistant scores, on average, 0.4 points higher. The room wants to celebrate, but daily paired differences wobble with a standard deviation of 2 points.",
"declare every positive sample difference a discovery",
"another sample from unchanged systems can land above zero by chance. A positive sign says which side won this sample; it does not say how surprising that victory would be if the true average difference were zero.",
"state the no-improvement claim, measure the observed mean difference in units of its standard error, and report both a test statistic and the range of effects compatible with the sampling noise",
"For the 100 paired questions, the mean difference is 0.4 and the standard deviation of differences is 2. The standard error is `2/√100 = 0.2`, so the improvement sits `0.4/0.2 = 2` standard errors above zero. A rough 95% interval is `0.4 ± 1.96×0.2`, or about `[0.008, 0.792]`. Zero lies just outside, yet the interval also warns that the practical gain may be tiny.",
"**dᵢ** is the score difference on paired question i. **d̄** is their observed mean. Zero is the null claim of no average improvement. **s/√n** estimates how much the sample mean would wobble. **z** tells how many such wobble-units separate the observation from the null.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) makes each question compare like with like. [The mean](../../MATHEMATICAL_MOVES.md#mean) lets all paired questions contribute. [The square root](../../MATHEMATICAL_MOVES.md#square-root) converts sample count into the scale of average noise, and [division](../../MATHEMATICAL_MOVES.md#division) asks how large the effect is relative to that noise. Dividing only by s would ignore that one hundred witnesses stabilize a mean more than one witness.",
r"z=\frac{\overline d-0}{s/\sqrt n}",
"A distant bell may be real or merely wind in the tower. Evidence asks not only whether you heard a sound, but how loud it was compared with the night's ordinary noise.",
"Benchmark uncertainty, A/B tests, ablations, model comparisons, and safety evaluations need this separation between observed effect, sampling uncertainty, and practical importance.",
"A test depends on sampling assumptions, a chosen error rate, and a claim selected before inspection. It cannot rescue biased data, repeated unreported testing, or a meaningless metric. Nor does statistical significance guarantee useful significance.",
(("Neyman and Pearson, On the Problem of the Most Efficient Tests of Statistical Hypotheses","https://doi.org/10.1098/rsta.1933.0009"),("Demšar, Statistical Comparisons of Classifiers over Multiple Data Sets","https://jmlr.org/papers/v7/demsar06a.html"))),
Chapter(222,"markov-chains","Markov Chains — When the Present Carries the Relevant Past",
"Statistical tests judge evidence gathered from repeated trials. Many intelligent systems instead inhabit a sequence: the next room, token, or state depends on what has already happened, and carrying the entire history soon becomes impossible.",
"A ranger moves among forest, river, and village. Tomorrow's location depends strongly on today's location. The station has years of paths, but planning one step ahead should not require rereading every footprint since the expedition began.",
"assign one fixed next-location distribution regardless of the current location",
"the river makes village likely while deep forest makes river likely. Erasing the present state destroys exactly the information that changes the next step.",
"choose a state description rich enough that, once the present state is known, earlier history adds no further information about the next-state distribution",
"Suppose that from forest the ranger moves to river with probability 0.7 and village with 0.3; from river the probabilities differ. If today's state is forest, the forest row supplies tomorrow's distribution. Yesterday may have been cave or village, but under this model it has already influenced the prediction by determining today's forest state.",
"**Xₜ** names the state at time t. The left side conditions tomorrow on the complete recorded history. The right side conditions only on today. Equality is the modelling promise that the chosen present state contains every historical detail relevant to one-step prediction.",
"[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) holds known history fixed while asking about the next state. [Equality](../../MATHEMATICAL_MOVES.md#equals) claims that discarding older conditions changes no next-step probability. Multiplying every transition probability here would answer the probability of a complete path, not the one-step memory question.",
r"P(X_{t+1}\mid X_t,X_{t-1},\ldots,X_0)=P(X_{t+1}\mid X_t)",
"A good travel diary can be compressed into your present location only when that location carries everything the next turn needs. If hunger or weather also matters, they must enter the state.",
"Autoregressive generation, hidden-state models, reinforcement learning, diffusion steps, and queueing systems all choose states intended to make the future conditionally manageable.",
"The Markov property does not say the physical world has no memory; it says our state representation has captured the relevant memory. Even with that representation, choosing actions for long-term reward still requires comparing branching futures.",
(("Bellman, On the Theory of Dynamic Programming","https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/"),("Mnih et al., Human-level Control through Deep Reinforcement Learning","https://doi.org/10.1038/nature14236"))),
Chapter(223,"dynamic-programming","Dynamic Programming — Remembering the Value of Futures Already Solved",
"A Markov state makes the next step depend on the present rather than the entire visible past. Planning remains expensive because every action opens more states, whose futures overlap and are recalculated along many paths.",
"From forest, the ranger can walk toward river or village. Both routes may later reach the same bridge. Drawing every complete journey separately solves the bridge's remaining journey again each time it is encountered.",
"enumerate every possible full action sequence and total its reward independently",
"the number of paths grows exponentially with horizon, and shared suffixes are recomputed. A ten-step tree may contain many copies of the same state with the same remaining problem.",
"give each state one stored value equal to the best immediate reward plus the discounted expected value of its possible next states, then reuse that value wherever the state reappears",
"At the bridge, suppose crossing now gives 2 and leads to home worth 8 next step; waiting gives 1 and leaves a future worth 6. With discount 0.9, crossing is worth `2 + 0.9×8 = 9.2`; waiting is worth `1 + 0.9×6 = 6.4`. Record 9.2 once. Every route arriving at the bridge can now reuse it.",
"**V(s)** is the best future value stored for state s. **a** is a candidate action. **r(s,a)** is immediate reward. **P(s′|s,a)** weighs possible next states. **γ** reduces the influence of distant reward. The maximum keeps the action with the best complete prospect.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) weights each future by both probability and discount. [Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive next-state possibilities; multiplying them would demand all next states occur together. [Maximum](../../MATHEMATICAL_MOVES.md#maximum) chooses among actions after each has been fully valued, while [addition](../../MATHEMATICAL_MOVES.md#addition) joins reward now with reward later.",
r"V(s)=\max_a\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right]",
"Instead of recounting every road to the sea, a cartographer writes the remaining distance on each crossroads. Every upstream route inherits the solved suffix.",
"Bellman backups power value iteration, Q-learning, tree search, decoding variants, and many ways of turning a long decision into reusable local subproblems.",
"Exact dynamic programming requires states and transitions that can be represented and revisited. Huge or continuous worlds need approximation, and a value function with arbitrary shape may still be difficult to optimize reliably.",
(("Bellman, On the Theory of Dynamic Programming","https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/"),("Mnih et al., Human-level Control through Deep Reinforcement Learning","https://doi.org/10.1038/nature14236"))),
Chapter(224,"convexity","Convexity — A Landscape Without Hidden Valleys",
"Dynamic programming replaces repeated futures with stored values, but learning those values or fitting a model still asks an optimizer to descend a landscape. Some landscapes conceal many valleys; others make every local descent globally trustworthy.",
"Stretch a string between two points on a bowl. Everywhere between the endpoints, the string floats on or above the bowl. Try the same across a rippled cave floor and the string can cut below a hill.",
"trust any small local minimum as the best possible solution",
"on a rippled landscape, a nearby valley may be higher than another valley beyond a ridge. Local slope alone cannot certify that no better point exists elsewhere.",
"require every chord between two points to lie on or above the function, preventing a hidden hump from separating a local minimum from a lower global one",
"For the bowl `f(x)=x²`, choose x=-2, y=2, and λ=1/2. Their midpoint is 0, where the bowl has height 0. The midpoint of endpoint heights is `(4+4)/2=4`; the bowl lies below its chord. Repeating this test for every pair and mixture weight is the geometric promise of convexity.",
"**x** and **y** are any two candidate points. **λ** lies between 0 and 1 and chooses a point along their segment. The left side evaluates the function at the mixed input. The right side mixes the two endpoint heights. The inequality demands that the function never rise above that chord.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) allocates complementary shares λ and 1-λ. [Addition](../../MATHEMATICAL_MOVES.md#addition) forms the mixtures. [Inequalities](../../MATHEMATICAL_MOVES.md#inequalities) compare the curved surface with its straight chord. Equality alone would describe only affine functions and exclude genuine bowls.",
r"f(\lambda x+(1-\lambda)y)\leq\lambda f(x)+(1-\lambda)f(y),\quad 0\leq\lambda\leq1",
"A valley shaped like a single bowl may be steep or shallow, but it contains no secret lower chamber behind a ridge.",
"Linear regression losses, logistic objectives, support-vector machines, and regularizers expose why some optimization guarantees are possible. Deep neural networks are generally nonconvex, so their success requires more delicate geometry.",
"Convexity is a powerful global promise, not a description of every useful model. It does not choose a stable numerical representation, prevent overflow, or make finite-precision arithmetic exact.",
(("Cortes and Vapnik, Support-Vector Networks","https://doi.org/10.1007/BF00994018"),("Dauphin et al., Identifying and Attacking the Saddle Point Problem","https://arxiv.org/abs/1406.2572"))),
Chapter(225,"numerical-stability","Numerical Stability — Preserving Mathematics Inside a Finite Machine",
"Convexity can make an exact mathematical landscape trustworthy. The machine that evaluates it has finite memory and finite precision, so an algebraically correct formula can still overflow, underflow, or erase a small but important difference.",
"Three logits are 1000, 999, and 998. Their exponentials should have sensible relative sizes, yet an ordinary floating-point calculator cannot store `e¹⁰⁰⁰`; the first operation becomes infinity before normalization can rescue it.",
"evaluate the written formula literally and assume algebraic equivalence guarantees computational equivalence",
"finite arithmetic has ceilings, floors, and rounding. Overflow turns meaningful ratios into `∞/∞`; subtracting nearly equal large numbers can discard the very digits carrying their difference.",
"rewrite the calculation so intermediate values remain in a safe range while the exact mathematical result stays unchanged",
"Let m be the largest logit, 1000. Subtract it first, producing `[0,-1,-2]`. Their exponentials are now `[1,e⁻¹,e⁻²]`, all representable. Because factoring out `eᵐ` from the original sum contributes m after the logarithm, the stable result is `1000 + log(1+e⁻¹+e⁻²)`—the same real number reached by a safer path.",
"**xᵢ** are the original scores. **m** is their maximum. **xᵢ-m** shifts every score without changing exponential ratios. The inner sum combines safe positive contributions. The outer logarithm returns from exponential scale, and adding m restores the factored scale.",
"[Maximum](../../MATHEMATICAL_MOVES.md#maximum) chooses a shift that makes every exponent nonpositive. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) creates that safe range. [The exponential](../../MATHEMATICAL_MOVES.md#exponential) recovers relative positive weights, [summation](../../MATHEMATICAL_MOVES.md#summation) combines alternatives, and [the logarithm](../../MATHEMATICAL_MOVES.md#logarithm) returns to log scale. Clipping would avoid overflow by changing the answer; this rearrangement preserves it.",
r"\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m},\quad m=\max_i x_i",
"A priceless melody can be played on a small instrument only if it is transposed into the instrument's range. The relationships survive although the absolute register temporarily changes.",
"Stable softmax, log-likelihoods, mixed precision, gradient scaling, normalization, and online attention all distinguish a mathematical identity from a safe computational route.",
"Stability cannot restore information already lost to poor data, an ill-conditioned problem, or insufficient precision. It asks a final engineering question: which equivalent path preserves the mathematical meaning on the machine we actually possess?",
(("Dao et al., FlashAttention","https://arxiv.org/abs/2205.14135"),("Micikevicius et al., Mixed Precision Training","https://arxiv.org/abs/1710.03740"))),
)


REALMS = (
    {
        "start": 201,
        "end": 203,
        "number": 1,
        "name": "The Hall of Boundaries",
        "question": "What belongs, what is connected, and what reliably becomes what?",
        "threshold": "A chalk circle opens in the floor. Before space can be measured or uncertainty counted, the world must first acquire boundaries, connections, and dependable transformations.",
        "sound": "chalk, thread, and one decisive click of brass",
        "path": "belonging → connection → dependable transformation",
    },
    {
        "start": 204,
        "end": 208,
        "number": 2,
        "name": "The Chamber of Directions",
        "question": "How can one space be described, and which directions genuinely matter?",
        "threshold": "The brass function opens a many-sided room. Rulers rotate in the walls, arrows cross the floor, and a high window turns every object into a shadow.",
        "sound": "sliding rulers, turning stone, and distant bells",
        "path": "language of space → new directions → persistent directions → honest shadows → strongest channels",
    },
    {
        "start": 209,
        "end": 215,
        "number": 3,
        "name": "The River of Change",
        "question": "How does something approach, change, bend, accumulate, and reveal hidden rhythm?",
        "threshold": "Beyond the chamber, the floor becomes a river. Nothing here stays still: distances shrink, slopes turn, water gathers, and tangled waves carry melodies no single moment can reveal.",
        "sound": "approaching footsteps, running water, and a buried chord",
        "path": "approach → local change → coupled change → bending → nearby prediction → accumulation → hidden rhythm",
    },
    {
        "start": 216,
        "end": 221,
        "number": 4,
        "name": "The Observatory of Possible Worlds",
        "question": "How can uncertain possibilities become quantities, beliefs, summaries, and evidence?",
        "threshold": "The river empties beneath a glass dome. Each lantern shows a different possible tomorrow; none may be extinguished merely because we do not yet know which world is real.",
        "sound": "turning lenses, weighted chains, and many quiet witnesses",
        "path": "possible worlds → evidence → centre and spread → settling averages → bell-shaped error → convincing claims",
    },
    {
        "start": 222,
        "end": 225,
        "number": 5,
        "name": "The Garden of Futures",
        "question": "How can the present remember enough, choose well, and preserve truth inside a finite machine?",
        "threshold": "A final door opens outdoors beneath a night sky. Paths branch through a garden of possible futures, cross a single bowl-shaped valley, and end at a small machine whose range is finite.",
        "sound": "footsteps at crossroads, a taut string, and a machine breathing safely",
        "path": "sufficient present → remembered futures → trustworthy landscape → safe computation",
    },
)


ROOT_MEMORY = {
    201: {
        "question": "Which animal cards truly belong inside this boundary?",
        "object": "three stone trays and one circle of chalk",
        "failure_image": "The tiger card appears twice, and moving it to the front changes the list although nothing about belonging changed.",
        "transformation": "Sweep away the numbered positions. Draw one chalk boundary around the admitted cards; let overlap appear where two circles share the same floor.",
        "sentence": "A set is a boundary that remembers only belonging.",
        "gesture": "Draw a circle in the air, then place one imagined object inside it.",
    },
    202: {
        "question": "How can the room remember that tiger is near river, not merely that both exist?",
        "object": "red and blue threads tied between named cards",
        "failure_image": "The cards collapse into one heap; the colour and direction of every connection disappear.",
        "transformation": "Separate the cards and tie an arrowed thread from the first object to the second. Different thread colours preserve different kinds of connection.",
        "sentence": "A relation is a thread that remembers who is connected to whom.",
        "gesture": "Point from one hand to the other; reversing your hands must reverse the claim.",
    },
    203: {
        "question": "What promise lets the next machine trust the answer of this one?",
        "object": "a brass slot with one input door and one output chute",
        "failure_image": "The same tiger card enters twice and the machine splits, returning two incompatible weights.",
        "transformation": "Lock one internal track from every allowed input to exactly one output. Other inputs may meet there, but one input can no longer fork.",
        "sentence": "A function is a machine that owes every allowed input one dependable answer.",
        "gesture": "Put an imaginary card into your left palm and close your right hand around its one promised result.",
    },
    204: {
        "question": "When the coordinate numbers change, what stayed the same?",
        "object": "two rotating ruler frames laid over one footprint",
        "failure_image": "The walk receives two different number pairs, and the record falsely declares that the ranger took two different journeys.",
        "transformation": "Keep the footprint fixed while rotating the rulers beneath it. Rebuild the same endpoint from new amounts of the new directions.",
        "sentence": "A basis is a chosen language for describing directions; the vector is the journey, not its coordinates.",
        "gesture": "Hold one finger still as a destination while rotating your other hand like a ruler frame.",
    },
    205: {
        "question": "Does this new arrow open genuinely new movement, or only rename movement already possible?",
        "object": "three floor arrows and a ring carrying one copied key",
        "failure_image": "The northeast arrow boasts of a third dimension even though east plus north already draws it exactly.",
        "transformation": "Try to cancel the arrows back to no movement. The nonzero recipe that succeeds exposes the copied direction; remove it and the reachable floor does not shrink.",
        "sentence": "Span is everywhere the arrows can reach; independence means each arrow opens a direction the others cannot.",
        "gesture": "Spread two fingers into independent directions, then lay a third finger along their combined diagonal.",
    },
    206: {
        "question": "Which direction can pass through the transformation without being turned?",
        "object": "a moving stone floor crossed by compass arrows",
        "failure_image": "Most arrows tumble differently at every repetition, burying the long-term pattern beneath changing coordinates.",
        "transformation": "Place arrows one by one until an eastward arrow emerges still pointing east—only longer. Mark that quiet direction and the scale impressed upon it.",
        "sentence": "An eigenvector is a direction a transformation cannot turn; its eigenvalue says how the direction is scaled.",
        "gesture": "Point forward and extend your arm without changing where your finger points.",
    },
    207: {
        "question": "What is the closest honest shadow of this track on the only rail our map allows?",
        "object": "a lantern, a tiger track, and one polished rail",
        "failure_image": "An arbitrary shadow leaves an error that still runs partly along the rail, proving that some allowed information was unnecessarily discarded.",
        "transformation": "Slide the shadow until the leftover error stands exactly perpendicular to the rail. No further allowed slide can make the disagreement smaller.",
        "sentence": "Projection is the closest honest shadow an allowed space can keep.",
        "gesture": "Drop one hand straight onto an imagined tabletop, forming a right angle with the discarded height.",
    },
    208: {
        "question": "Which coordinated channels carry most of this entire transformation?",
        "object": "a rectangular brass organ with input grooves and output bells",
        "failure_image": "Polishing the largest rivets changes little; the loudest bell is driven by a pattern spread across many modest parts.",
        "transformation": "Rotate the input wheel until each independent push rings one output direction, then order the bells from strongest to faintest.",
        "sentence": "SVD separates any matrix into its strongest input-to-output channels.",
        "gesture": "Turn two imaginary wheels, then lower your hands from the loudest channel to the quietest.",
    },
    209: {
        "question": "What must ‘closer and closer’ promise before we can build calculus upon it?",
        "object": "stepping stones approaching a sealed luminous door",
        "failure_image": "The words ‘very close’ move whenever the observer changes standards; no finite final step explains the destination.",
        "transformation": "Place any tiny ring around the door. Find a stage after which every remaining stone lies inside that ring, however small the ring was chosen.",
        "sentence": "A limit is a promise that every demanded closeness eventually becomes permanent.",
        "gesture": "Make a shrinking circle with your fingers, then point beyond an imagined threshold.",
    },
    210: {
        "question": "If every weight can move, which combined direction changes the loss fastest?",
        "object": "a compass resting on a many-dimensional hillside",
        "failure_image": "Separate one-weight trails cover the hill, but they never reveal what happens when several weights move together.",
        "transformation": "Gather every coordinate slope into one arrow. The compass turns until it points toward the steepest local rise; reverse it to descend.",
        "sentence": "A gradient is the compass of fastest local change.",
        "gesture": "Turn an imaginary compass, then step in the opposite direction to reduce the loss.",
    },
    211: {
        "question": "How does every output respond when every input is allowed to move?",
        "object": "a wall of levers facing a wall of bells",
        "failure_image": "A single slope follows one lever to one bell while the cross-effects among the rest remain invisible.",
        "transformation": "Pull each lever slightly and record every bell's response in one rectangular ledger: output rows, input columns.",
        "sentence": "A Jacobian is a ledger of every output's local sensitivity to every input.",
        "gesture": "Fan the fingers of one hand as inputs and the other as outputs; imagine a thread between every pair.",
    },
    212: {
        "question": "Two places have the same slope—why does one permit a bold step while the other punishes it?",
        "object": "two clay valleys and a pair of rolling marbles",
        "failure_image": "Both compasses show the same slope, yet one valley bends gently and the other turns into a narrow wall.",
        "transformation": "Press a curvature grid into the clay. It records how each component of the gradient changes as every direction moves.",
        "sentence": "A Hessian is a map of how the slope itself bends.",
        "gesture": "Curve one palm like a shallow bowl and the other like a narrow valley.",
    },
    213: {
        "question": "How much nearby terrain can be rebuilt from clues gathered at one point?",
        "object": "a torn map, a tangent ruler, and nested pieces of curved parchment",
        "failure_image": "The straight tangent predicts well for one step, then walks directly away from the bending road.",
        "transformation": "Begin with the current height, add the slope's straight correction, then add curvature and finer corrections only as distance makes them necessary.",
        "sentence": "A Taylor approximation rebuilds nearby shape from value, slope, curvature, and finer local clues.",
        "gesture": "Lay one flat hand as a tangent, then gradually bend the other around it.",
    },
    214: {
        "question": "How can a changing rate become the total water actually delivered?",
        "object": "a river gauge and thousands of increasingly thin glass cups",
        "failure_image": "One noon reading is multiplied across the whole day, granting dawn and dusk a rate they never had.",
        "transformation": "Let each tiny interval fill its own cup at its own rate, add the cups, and make them thinner until coarse partition error disappears.",
        "sentence": "An integral rebuilds a whole by accumulating locally honest pieces.",
        "gesture": "Cup both hands repeatedly, then gather the imagined pieces into one vessel.",
    },
    215: {
        "question": "Which simple rhythms are hidden inside this tangled signal?",
        "object": "a dark prism surrounded by rotating tuning forks",
        "failure_image": "The waveform is inspected moment by moment; overlapping notes remain one jagged line.",
        "transformation": "Turn a candidate rhythm against the signal. Matching rises and falls reinforce across time while mismatched turns cancel.",
        "sentence": "Fourier analysis is a prism that separates hidden rhythms.",
        "gesture": "Rotate one finger in a circle while the other traces a wave.",
    },
    216: {
        "question": "How can stories about possible tomorrows become quantities we can calculate with?",
        "object": "possible-world cards passing through a numbered brass sieve",
        "failure_image": "Names such as ‘empty photograph’ and ‘two tigers’ are added as though stories were already numbers.",
        "transformation": "Ask one numerical question of every world. Let different stories fall into the same numbered bowl when they give the same answer.",
        "sentence": "A random variable is a numerical question asked of every possible world.",
        "gesture": "Hold several imagined cards, then sort them into numbered bowls.",
    },
    217: {
        "question": "How should one paw print rearrange the brightness of competing hidden stories?",
        "object": "a ring of lanterns and one fresh track beneath a lens",
        "failure_image": "The brightest explanation of the print wins even if it was almost impossible before the print appeared.",
        "transformation": "Begin with each lantern's old brightness, scale it by how naturally that world makes the track, then renormalize the surviving light.",
        "sentence": "Bayes' rule lets evidence rearrange belief without erasing what was believed before.",
        "gesture": "Dim and brighten imaginary lanterns while keeping their total light fixed.",
    },
    218: {
        "question": "Where does uncertainty balance, how widely does it wander, and what moves together?",
        "object": "a hanging flock-mobile with a central spindle and paired threads",
        "failure_image": "Two flocks balance at the same centre, yet one is tightly gathered and the other spans the room; the mean calls them identical.",
        "transformation": "Mark the balance point, measure squared wingbeats away from it, then tie paired departures together to see whether they turn in concert.",
        "sentence": "Expectation finds the centre, variance the spread, and covariance the shared motion of uncertainty.",
        "gesture": "Balance one palm, spread both hands apart, then move them together or oppositely.",
    },
    219: {
        "question": "Why should many imperfect witnesses reveal a stable average?",
        "object": "a long procession of witnesses dropping stones onto a balance",
        "failure_image": "The first witness places one stone on one side and the station declares the population average to be an extreme.",
        "transformation": "Let every new witness contribute one stone, but divide by the growing crowd so headcount alone cannot inflate the answer.",
        "sentence": "The law of large numbers says many honest witnesses make an average settle.",
        "gesture": "Tap alternating fingers like arriving witnesses, then flatten your hand into a level balance.",
    },
    220: {
        "question": "What shape does the remaining error of a large average tend to take?",
        "object": "many transparent error sheets accumulating beneath a bell-shaped canopy",
        "failure_image": "The average is assumed to keep the strange shape of one individual disturbance, despite combining a hundred of them.",
        "transformation": "Repeat the entire averaging experiment, centre each error, and measure it in its natural shrinking units. The stacked silhouettes smooth toward a bell.",
        "sentence": "The central limit theorem gives normalized averaging error a familiar bell-shaped destination.",
        "gesture": "Stack imaginary transparent sheets, then trace a bell curve over their combined outline.",
    },
    221: {
        "question": "Is the new model's small victory a signal or an ordinary tremor of chance?",
        "object": "a distant tower bell beside a brass wind-and-noise meter",
        "failure_image": "One faint positive sound is celebrated without asking how loudly the empty night usually rattles the tower.",
        "transformation": "Subtract the no-improvement claim and measure the remaining sound in units of ordinary sample-mean wobble; keep an interval, not only a verdict.",
        "sentence": "A statistical test asks how large a signal is compared with the noise that could imitate it.",
        "gesture": "Cup one ear for the signal while the other hand marks the surrounding noise.",
    },
    222: {
        "question": "When can the present safely replace the entire remembered past?",
        "object": "a traveler's satchel beside an impossibly long scroll of footprints",
        "failure_image": "The ranger drags every footprint ever made, yet the next turn only needs information that could have been packed into today's state.",
        "transformation": "Put location, weather, and every genuinely predictive fact into the present satchel. Test whether older footprints change tomorrow once the satchel is known.",
        "sentence": "A Markov state is a present that carries all the past the next step still needs.",
        "gesture": "Sweep an imaginary history behind you into a small satchel held at your chest.",
    },
    223: {
        "question": "How can a future already solved stop being recomputed along every road?",
        "object": "a branching garden whose shared crossroads carry carved value stones",
        "failure_image": "Every route redraws the same journey from the bridge to home, and the tree of copies swallows the garden.",
        "transformation": "Solve the bridge once and carve its remaining value into the stone. Every upstream path may now reuse that future.",
        "sentence": "Dynamic programming remembers the value of futures already solved.",
        "gesture": "Trace two branching paths that meet, then tap the shared meeting point only once.",
    },
    224: {
        "question": "When can a nearby valley be trusted as the lowest valley anywhere?",
        "object": "a taut golden string stretched above a single clay bowl",
        "failure_image": "On a rippled floor, the traveler settles in a shallow pocket while a deeper valley hides beyond a ridge.",
        "transformation": "Stretch the string between any two points. If the landscape always remains below its chord, no hidden ridge can protect a better local valley.",
        "sentence": "Convexity is the promise that a landscape contains no secret lower valley.",
        "gesture": "Curve one palm into a bowl and stretch one finger of the other hand across it like a chord.",
    },
    225: {
        "question": "How can a finite machine travel to the same mathematical truth without overflowing on the way?",
        "object": "a small brass instrument facing three unbearably bright exponential flames",
        "failure_image": "The first flame becomes infinity before the machine can compare it with the others; a meaningful ratio collapses into infinity divided by infinity.",
        "transformation": "Transpose every score by the largest one. The flames shrink into the instrument's range while their relative brightness remains unchanged; restore the removed scale only at the end.",
        "sentence": "Numerical stability is a safer computational path to the same mathematical truth.",
        "gesture": "Lower both hands together without changing the distance between them, then raise the shared scale at the end.",
    },
}


def realm_for(number: int) -> dict:
    return next(realm for realm in REALMS if realm["start"] <= number <= realm["end"])


PURE = {
201: '''def overlap(observed, near_water):\n    return {animal for animal in observed if animal in near_water}\ndef demo():\n    shared=overlap({"tiger","deer","otter"},{"tiger","otter","frog"}); assert shared=={"tiger","otter"}; return shared''',
202: '''def related(relation,left,right): return (left,right) in relation\ndef demo():\n    near={("tiger","river"),("otter","river")}; assert related(near,"tiger","river") and not related(near,"river","tiger"); return near''',
203: '''def apply(mapping,item):\n    if item not in mapping: raise KeyError("input outside the function's domain")\n    return mapping[item]\ndef demo():\n    weights={"tiger":220,"deer":90,"otter":12}; assert apply(weights,"tiger")==220; return weights''',
204: '''def coordinates_in_diagonal_basis(vector):\n    x,y=vector; return ((x+y)/2,(y-x)/2)\ndef rebuild(coefficients):\n    first,second=coefficients; return (first-second,first+second)\ndef demo():\n    c=coordinates_in_diagonal_basis((3,2)); assert rebuild(c)==(3,2); return c''',
205: '''def combine(weights,vectors): return [sum(w*v[j] for w,v in zip(weights,vectors)) for j in range(len(vectors[0]))]\ndef demo():\n    directions=[(1,0),(0,1),(1,1)]; witness=(-1,-1,1); assert combine(witness,directions)==[0,0]; return {"independent":False,"witness":witness}''',
206: '''def transform(matrix,vector): return [sum(a*b for a,b in zip(row,vector)) for row in matrix]\ndef demo():\n    matrix=((2,0),(0,1)); east=(1,0); image=transform(matrix,east); assert image==[2,0]; return {"direction":east,"scale":2}''',
207: '''def dot(a,b): return sum(x*y for x,y in zip(a,b))\ndef project(vector,direction):\n    scale=dot(vector,direction)/dot(direction,direction); return [scale*x for x in direction]\ndef demo():\n    shadow=project((3,2),(1,0)); assert shadow==[3,0]; return shadow''',
208: '''def rank_one(matrix,steps=20):\n    v=[1.0 for _ in matrix[0]]\n    for _ in range(steps):\n        u=[sum(row[j]*v[j] for j in range(len(v))) for row in matrix]; un=sum(x*x for x in u)**.5; u=[x/un for x in u]\n        v=[sum(matrix[i][j]*u[i] for i in range(len(matrix))) for j in range(len(v))]; vn=sum(x*x for x in v)**.5; v=[x/vn for x in v]\n    sigma=sum(u[i]*matrix[i][j]*v[j] for i in range(len(u)) for j in range(len(v))); return u,sigma,v\ndef demo():\n    u,s,v=rank_one([[3.,0.],[0.,1.]]); assert abs(s-3)<1e-6; return {"singular_value":s}''',
209: '''def reciprocal_sequence(count): return [1/n for n in range(1,count+1)]\ndef demo():\n    values=reciprocal_sequence(1000); assert values[-1]<.002 and all(a>b for a,b in zip(values,values[1:])); return values[-5:]''',
210: '''def loss(tiger_weight,deer_weight): return (tiger_weight-220)**2+(deer_weight-90)**2\ndef finite_gradient(point,step=1e-5):\n    out=[]\n    for i in range(2):\n        left=list(point); right=list(point); left[i]-=step; right[i]+=step\n        out.append((loss(*right)-loss(*left))/(2*step))\n    return out\ndef demo():\n    g=finite_gradient((218.,94.)); assert abs(g[0]+4)<1e-4 and abs(g[1]-8)<1e-4; return g''',
211: '''def machine(height,weight): return (height+weight, height*weight)\ndef jacobian(height,weight): return [[1,1],[weight,height]]\ndef demo():\n    J=jacobian(2,3); assert J==[[1,1],[3,2]]; return J''',
212: '''def bowl(x,y): return x*x+3*y*y+x*y\ndef hessian(): return [[2,1],[1,6]]\ndef demo():\n    H=hessian(); assert H[0][1]==H[1][0] and H[1][1]>H[0][0]; return H''',
213: '''def exp_taylor(change,terms=5):\n    total=1.; factorial=1.; power=1.\n    for n in range(1,terms): factorial*=n; power*=change; total+=power/factorial\n    return total\ndef demo():\n    estimate=exp_taylor(.1); assert abs(estimate-1.105170)<1e-5; return estimate''',
214: '''def integrate(rate,start,end,slices):\n    width=(end-start)/slices; return sum(rate(start+i*width)*width for i in range(slices))\ndef demo():\n    total=integrate(lambda t:2*t,0,1,10000); assert abs(total-1)<.001; return total''',
215: '''import cmath\ndef dft(samples):\n    N=len(samples); return [sum(x*cmath.exp(-2j*cmath.pi*k*n/N) for n,x in enumerate(samples)) for k in range(N)]\ndef demo():\n    spectrum=dft([1,0,-1,0]); assert abs(spectrum[1]-2)<1e-9; return spectrum''',
216: '''def distribution(outcomes,probabilities,measure):\n    result={}\n    for outcome,p in zip(outcomes,probabilities): result[measure(outcome)]=result.get(measure(outcome),0)+p\n    return result\ndef demo():\n    histories=["none-a","none-b","one","two"]; d=distribution(histories,[.25]*4,lambda h:0 if h.startswith("none") else (1 if h=="one" else 2)); assert d[0]==.5; return d''',
217: '''def bayes(prior,likelihood):\n    evidence=sum(prior[h]*likelihood[h] for h in prior); return {h:prior[h]*likelihood[h]/evidence for h in prior}\ndef demo():\n    posterior=bayes({"tiger":.1,"deer":.9},{"tiger":.8,"deer":.1}); assert abs(posterior["tiger"]-8/17)<1e-12; return posterior''',
218: '''def summaries(xs,ys):\n    mx=sum(xs)/len(xs); my=sum(ys)/len(ys); variance=sum((x-mx)**2 for x in xs)/len(xs); covariance=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/len(xs); return mx,variance,covariance\ndef demo():\n    out=summaries([0,2],[0,2]); assert out==(1,1,1); return out''',
219: '''def running_means(values):\n    total=0.; out=[]\n    for count,value in enumerate(values,1): total+=value; out.append(total/count)\n    return out\ndef demo():\n    means=running_means([1,0]*500); assert means[-1]==.5; return means[-5:]''',
220: '''def standardized_mean(values,mean,deviation):\n    sample=sum(values)/len(values); return (sample-mean)/(deviation/(len(values)**.5))\ndef demo():\n    z=standardized_mean([10.2]*100,10,2); assert abs(z-1)<1e-12; return z''',
221: '''def paired_test(differences):\n    n=len(differences); mean=sum(differences)/n; variance=sum((d-mean)**2 for d in differences)/(n-1); se=(variance/n)**.5; return mean,se,mean/se,(mean-1.96*se,mean+1.96*se)\ndef demo():\n    differences=[-1.6,2.4]*50; mean,se,z,interval=paired_test(differences); assert abs(mean-.4)<1e-12 and interval[0]<mean<interval[1]; return mean,se,z,interval''',
222: '''def next_distribution(state,transitions): return transitions[state]\ndef demo():\n    transitions={"forest":{"river":.7,"village":.3},"river":{"forest":.4,"village":.6}}; out=next_distribution("forest",transitions); assert out["river"]==.7; return out''',
223: '''def backup(actions,discount=.9):\n    return max((reward+discount*future,name) for name,reward,future in actions)\ndef demo():\n    value,action=backup([("cross",2,8),("wait",1,6)]); assert action=="cross" and abs(value-9.2)<1e-12; return action,value''',
224: '''def convex_check(function,x,y,weight):\n    left=function(weight*x+(1-weight)*y); right=weight*function(x)+(1-weight)*function(y); return left,right,left<=right\ndef demo():\n    out=convex_check(lambda x:x*x,-2,2,.5); assert out==(0.,4.,True); return out''',
225: '''import math\ndef logsumexp(scores):\n    maximum=max(scores); return maximum+math.log(sum(math.exp(x-maximum) for x in scores))\ndef demo():\n    value=logsumexp([1000,999,998]); assert math.isfinite(value) and 1000<value<1001; return value''',
}


NUMPY = {
201: "a=np.array(['tiger','deer','otter']); b=np.array(['tiger','otter','frog']); out=np.intersect1d(a,b); assert set(out)=={'tiger','otter'}; print(out)",
202: "relation=np.array([['tiger','river'],['otter','river']]); assert np.any(np.all(relation==['tiger','river'],axis=1)); print(relation)",
203: "weights=np.array([220.,90.,12.]); indices={'tiger':0,'deer':1,'otter':2}; assert weights[indices['tiger']]==220; print(weights)",
204: "basis=np.array([[1.,-1.],[1.,1.]]); v=np.array([3.,2.]); c=np.linalg.solve(basis,v); assert np.allclose(basis@c,v); print(c)",
205: "directions=np.array([[1.,0.,1.],[0.,1.,1.]]); assert np.linalg.matrix_rank(directions)==2; print({'rank':np.linalg.matrix_rank(directions)})",
206: "A=np.diag([2.,1.]); values,vectors=np.linalg.eig(A); assert np.allclose(A@vectors,vectors@np.diag(values)); print(values)",
207: "v=np.array([3.,2.]); u=np.array([1.,0.]); shadow=(v@u)/(u@u)*u; assert np.allclose(shadow,[3,0]); print(shadow)",
208: "A=np.diag([3.,1.]); u,s,vt=np.linalg.svd(A); recovered=(u*s)@vt; assert np.allclose(recovered,A); print(s)",
209: "n=np.arange(1,1001); values=1/n; assert values[-1]<.002; print(values[-5:])",
210: "point=np.array([218.,94.]); gradient=2*(point-np.array([220.,90.])); assert np.allclose(gradient,[-4,8]); print(gradient)",
211: "J=np.array([[1.,1.],[3.,2.]]); change=np.array([.1,-.2]); print({'jacobian':J,'output_change':J@change})",
212: "H=np.array([[2.,1.],[1.,6.]]); values=np.linalg.eigvalsh(H); assert np.all(values>0); print(values)",
213: "h=.1; powers=np.arange(5); estimate=np.sum(h**powers/np.array([math.factorial(int(n)) for n in powers])); assert np.isclose(estimate,np.exp(h),atol=1e-5); print(estimate)",
214: "t=np.linspace(0,1,10001); total=np.trapezoid(2*t,t); assert np.isclose(total,1); print(total)",
215: "samples=np.array([1.,0.,-1.,0.]); spectrum=np.fft.fft(samples); assert np.isclose(spectrum[1],2); print(spectrum)",
216: "values=np.array([0,0,1,2]); probability=np.array([.25]*4); masses=np.bincount(values,weights=probability); assert np.allclose(masses,[.5,.25,.25]); print(masses)",
217: "prior=np.array([.1,.9]); likelihood=np.array([.8,.1]); posterior=prior*likelihood/(prior@likelihood); assert np.isclose(posterior[0],8/17); print(posterior)",
218: "x=np.array([0.,2.]); y=np.array([0.,2.]); assert np.isclose(x.var(),1) and np.isclose(np.cov(x,y,bias=True)[0,1],1); print({'mean':x.mean(),'variance':x.var(),'covariance':np.cov(x,y,bias=True)[0,1]})",
219: "values=np.tile([1.,0.],500); means=np.cumsum(values)/np.arange(1,len(values)+1); assert means[-1]==.5; print(means[-5:])",
220: "values=np.full(100,10.2); z=(values.mean()-10)/(2/np.sqrt(len(values))); assert np.isclose(z,1); print(z)",
221: "d=np.tile([-1.6,2.4],50); mean=d.mean(); se=d.std(ddof=1)/np.sqrt(len(d)); interval=mean+np.array([-1,1])*1.96*se; assert interval[0]<mean<interval[1]; print({'mean':mean,'se':se,'z':mean/se,'interval':interval})",
222: "P=np.array([[0.,.7,.3],[.4,0.,.6],[.2,.3,.5]]); state=np.array([1.,0.,0.]); tomorrow=state@P; assert np.isclose(tomorrow.sum(),1); print(tomorrow)",
223: "reward=np.array([2.,1.]); future=np.array([8.,6.]); values=reward+.9*future; assert values.argmax()==0; print(values)",
224: "f=lambda z:z*z; x,y,weight=-2.,2.,.5; left=f(weight*x+(1-weight)*y); right=weight*f(x)+(1-weight)*f(y); assert left<=right; print(left,right)",
225: "x=np.array([1000.,999.,998.]); maximum=x.max(); value=maximum+np.log(np.exp(x-maximum).sum()); assert np.isfinite(value); print(value)",
}


TORCH = {
201: "a={'tiger','deer','otter'}; b={'tiger','otter','frog'}; out=a&b; assert out=={'tiger','otter'}; print(out)",
202: "edges=torch.tensor([[0,0],[1,0]]); query=torch.tensor([0,0]); assert torch.any(torch.all(edges==query,dim=1)); print(edges)",
203: "weights=torch.tensor([220.,90.,12.]); assert weights[0]==220; print(weights)",
204: "basis=torch.tensor([[1.,-1.],[1.,1.]]); v=torch.tensor([3.,2.]); c=torch.linalg.solve(basis,v); assert torch.allclose(basis@c,v); print(c)",
205: "directions=torch.tensor([[1.,0.,1.],[0.,1.,1.]]); rank=torch.linalg.matrix_rank(directions); assert rank==2; print(rank)",
206: "A=torch.diag(torch.tensor([2.,1.])); values,vectors=torch.linalg.eig(A); assert torch.allclose((A@vectors.real),vectors.real@torch.diag(values.real)); print(values)",
207: "v=torch.tensor([3.,2.]); u=torch.tensor([1.,0.]); shadow=(v@u)/(u@u)*u; assert torch.allclose(shadow,torch.tensor([3.,0.])); print(shadow)",
208: "A=torch.diag(torch.tensor([3.,1.])); u,s,vh=torch.linalg.svd(A); assert torch.allclose((u*s)@vh,A); print(s)",
209: "n=torch.arange(1,1001,dtype=torch.float32); values=1/n; assert values[-1]<.002; print(values[-5:])",
210: "point=torch.tensor([218.,94.],requires_grad=True); loss=((point-torch.tensor([220.,90.]))**2).sum(); loss.backward(); assert torch.allclose(point.grad,torch.tensor([-4.,8.])); print(point.grad)",
211: "point=torch.tensor([2.,3.]); fn=lambda p:torch.stack((p[0]+p[1],p[0]*p[1])); J=torch.autograd.functional.jacobian(fn,point); assert torch.allclose(J,torch.tensor([[1.,1.],[3.,2.]])); print(J)",
212: "point=torch.tensor([0.,0.]); fn=lambda p:p[0]**2+3*p[1]**2+p[0]*p[1]; H=torch.autograd.functional.hessian(fn,point); assert torch.allclose(H,torch.tensor([[2.,1.],[1.,6.]])); print(H)",
213: "h=torch.tensor(.1); powers=torch.arange(5); factorial=torch.tensor([math.factorial(n) for n in range(5)]); estimate=(h**powers/factorial).sum(); assert torch.isclose(estimate,torch.exp(h),atol=1e-5); print(estimate)",
214: "t=torch.linspace(0,1,10001); total=torch.trapezoid(2*t,t); assert torch.isclose(total,torch.tensor(1.)); print(total)",
215: "samples=torch.tensor([1.,0.,-1.,0.]); spectrum=torch.fft.fft(samples); assert torch.isclose(spectrum[1].real,torch.tensor(2.)); print(spectrum)",
216: "values=torch.tensor([0,0,1,2]); probability=torch.full((4,),.25); masses=torch.zeros(3).scatter_add_(0,values,probability); assert torch.allclose(masses,torch.tensor([.5,.25,.25])); print(masses)",
217: "prior=torch.tensor([.1,.9]); likelihood=torch.tensor([.8,.1]); posterior=prior*likelihood/(prior@likelihood); assert torch.isclose(posterior[0],torch.tensor(8/17)); print(posterior)",
218: "x=torch.tensor([0.,2.]); y=torch.tensor([0.,2.]); covariance=((x-x.mean())*(y-y.mean())).mean(); assert x.var(correction=0)==1 and covariance==1; print(x.mean(),x.var(correction=0),covariance)",
219: "values=torch.tensor([1.,0.]).repeat(500); means=torch.cumsum(values,0)/torch.arange(1,len(values)+1); assert means[-1]==.5; print(means[-5:])",
220: "values=torch.full((100,),10.2); z=(values.mean()-10)/(2/torch.sqrt(torch.tensor(100.))); assert torch.isclose(z,torch.tensor(1.),atol=1e-5); print(z)",
221: "d=torch.tensor([-1.6,2.4]).repeat(50); mean=d.mean(); se=d.std()/torch.sqrt(torch.tensor(float(len(d)))); interval=mean+torch.tensor([-1.,1.])*1.96*se; assert interval[0]<mean<interval[1]; print(mean,se,mean/se,interval)",
222: "P=torch.tensor([[0.,.7,.3],[.4,0.,.6],[.2,.3,.5]]); state=torch.tensor([1.,0.,0.]); tomorrow=state@P; assert torch.isclose(tomorrow.sum(),torch.tensor(1.)); print(tomorrow)",
223: "reward=torch.tensor([2.,1.]); future=torch.tensor([8.,6.]); values=reward+.9*future; assert values.argmax()==0; print(values)",
224: "f=lambda z:z*z; x=torch.tensor(-2.); y=torch.tensor(2.); weight=.5; left=f(weight*x+(1-weight)*y); right=weight*f(x)+(1-weight)*f(y); assert left<=right; print(left,right)",
225: "x=torch.tensor([1000.,999.,998.]); value=torch.logsumexp(x,dim=0); assert torch.isfinite(value); print(value)",
}


def concept(row: Chapter) -> str:
    return row.title.split(" — ", 1)[0]


def chapter(row: Chapter) -> str:
    name = concept(row)
    memory = ROOT_MEMORY[row.number]
    realm = realm_for(row.number)
    index = (row.number - 201) % 6
    entries = (
        f"The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **{name}** has been covered so that only the unsolved situation remains.",
        f"In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **{name}**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.",
        f"The corridor bends beneath every model we have built. Here **{name}** is not presented as inherited knowledge. Its symbol is still buried, and the only lantern we carry is the failure left by the preceding excavation.",
        f"Another vault door opens. The carving that once named **{name}** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.",
        f"Far below the Transformer, the Undercroft stores no formula sheet. For **{name}**, it preserves a scene, a tempting tool, and the mark left where that tool broke.",
        f"At this depth, mathematics feels less like a catalogue and more like memory. We meet **{name}** first as an ordinary human need, before anyone has decided what marks should record it.",
    )
    attempts = (
        f"The first move is honest because it uses the nearest tool already in our hands: **{row.attempt}**.",
        f"Nothing yet suggests a new invention. We naturally {row.attempt}.",
        f"If we were the first people in this chamber, we would probably {row.attempt}.",
        f"The old machinery invites a plausible shortcut: {row.attempt}.",
        f"With no standard method to recite, the most economical proposal is to {row.attempt}.",
        f"We try to spend no new mathematics at all and simply {row.attempt}.",
    )
    failures = (
        "The proposal deserves a real trial, not a ceremonial rejection.",
        "For a moment the shortcut feels complete. Then the smallest contrary case arrives.",
        "We let the idea touch the evidence. The fracture appears exactly where information was lost.",
        "The stone does not object with terminology; it objects with a result we already know cannot be right.",
        "A useful wrong idea is one that leaves a clean fossil of its missing responsibility.",
        "The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity.",
    )
    repairs = (
        f"Now the reader can name the requirement before the textbook can name the method: we must {row.repair}.",
        f"What survives the failure is a precise demand. The repaired construction must {row.repair}.",
        f"The broken attempt has done its work. It tells us, in ordinary language, to {row.repair}.",
        f"We do not leap to a famous formula. We carry one missing responsibility forward: {row.repair}.",
        f"The next idea is forced only because the evidence asks us to {row.repair}.",
        f"At last there is something worth inventing. Whatever we build must {row.repair}.",
    )
    sketches = (
        f'```text\nknown tool ──tempts us──▶ first attempt\n                              │\n                         concrete failure\n                              │\n                              ▼\n                    missing responsibility\n                              │\n                              ▼\n                           {name}\n```',
        f'```text\nobservation\n    ↓\nour own proposal ──▶ test case ──▶ impossible answer\n                                      ↓\n                              preserve what vanished\n                                      ↓\n                                    {name}\n```',
        f'```text\n             what the world shows\n                      │\n         ┌────────────┴────────────┐\n         │                         │\n   old explanation           counterexample\n         │                         │\n         └──────── breaks ─────────┘\n                      │\n               repair the promise\n                      │\n                    {name}\n```',
        f'```text\nscene → guess → calculate → compare with reality\n          ▲                       │\n          └──── change the idea ──┘\n                       ↓\n                     {name}\n```',
        f'```text\nwhat we kept       what disappeared\n     │                     │\n     └──── first attempt ──┘\n               │\n          failure mark\n               │\n       one necessary repair\n               │\n             {name}\n```',
        f'```text\nno symbols yet\n      ↓\none named example\n      ↓\na rule we would naturally try\n      ↓\nthe case that refuses it\n      ↓\n{name} becomes necessary\n```',
    )
    part = ("> **PART XIV — THE MATHEMATICAL ROOTS BENEATH THE MACHINE**\n>\n"
            "> We have followed AI from observation to an accountable training factory. Now we descend beneath the finished engine and recover the older mathematical promises it was quietly using all along.\n>\n"
            "> A mathematical root is not a formula or a school subject. It is a reusable promise about belonging, connection, space, change, uncertainty, choice, or computation. The formula will arrive only after the human need has made that promise unavoidable. Begin with the [map of the Undercroft](../../MATHEMATICAL_ROOTS.md).\n\n") if row.number == 201 else ""
    realm_overture = ""
    if row.number == realm["start"]:
        realm_overture = f"""### Realm {realm["number"]} — {realm["name"]}

{realm["threshold"]}

Listen for {realm["sound"]}. The questions in this realm travel as one chain:

```text
{realm["path"]}
```

"""
    realm_position = (
        f'> **You are here:** Realm {realm["number"]} of 5 — [{realm["name"]}](../../MATHEMATICAL_ROOTS.md#realm-{realm["number"]})\n'
        f'>\n'
        f'> **Question waiting in this chamber:** {memory["question"]}\n'
        f'>\n'
        f'> **Do not take the answer yet:** first let the object fail.'
    )
    next_link = (
        f"[Continue to Excavation {row.number + 1:03d}: {ROWS[row.number - 200].title}](../{row.number + 1:03d}-{ROWS[row.number - 200].slug}/README.md)"
        if row.number < 225 else
        "[Return to the living Math Mandala](../../math-mandala/README.md), where every recovered idea remains connected to the chapters that needed it."
    )
    coda = ""
    if row.number == 225:
        coda = """
## The stair returns to daylight

The final carving is not an answer but a habit. We began with an observation, risked an idea of our own, listened when a small case broke it, and invented only the operation needed to preserve what had vanished. Symbols arrived as nicknames for things our hands and imagination already knew.

That rhythm now runs through the whole archive—from counting tigers to making models accountable. The mandala is not a wall of formulas to memorize. It is a map of human necessities. Touch any node and ask: *What failed so completely that someone had to invent this?* The mathematics will no longer feel borrowed. It will remember the path by which it became yours.
"""
    return f"""# Excavation {row.number:03d} — {row.title}

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

{part}{realm_overture}{realm_position}

{row.carry}

{entries[index]}

{row.scene}

The chamber has reduced the abstraction to one physical thing: **{memory["object"]}**. The question carved beside it asks: *{memory["question"]}*

{attempts[index]}

{failures[index]} {row.failure[0].upper() + row.failure[1:]}

{sketches[index]}

{repairs[index]}

This is the hinge of the {name} excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: {memory["failure_image"]}

Now let the scene move. {memory["transformation"]}

The transformation is the discovery of {name} made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press {name} into memory:

> **Memory seal — {name}**
>
> {memory["sentence"]}

Make the memory bodily, not merely verbal: {memory["gesture"]}

## {name} on the stone workbench

{row.worked}

The point of keeping the objects named while rebuilding {name} is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside {name.lower()}

Return to the named {name} scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

{row.terms}

### Why the melody needs these exact notes

{row.operations}

The operations inside {name} form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
{row.equation}
$$

Read the {name} line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

{row.analogy}

That echo helps {name} remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

{row.connection}

The older excavation and this {name} chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving {realm["name"]}, look back at its path—**{realm["path"]}**. {name} occupies one necessary step in that motion. Its object, **{memory["object"]}**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of {name.lower()} breaks

{row.limit}

The boundary belongs beside the discovery of {name} because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps {name} tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

{next_link}
{coda}"""


def diagram(row: Chapter) -> str:
    name = concept(row)
    memory = ROOT_MEMORY[row.number]
    realm = realm_for(row.number)
    return f"""# Diagram — Excavation {row.number:03d}: {row.title}

## The five-frame memory film

```mermaid
flowchart LR
  Q["1 · Human question"] --> O["2 · Physical object"]
  O --> F["3 · Visible failure"]
  F --> T["4 · Transformation"]
  T --> S["5 · Memory seal"]
  Q -.-> QD["{memory["question"]}"]
  O -.-> OD["{memory["object"]}"]
  S -.-> SD["{memory["sentence"]}"]
```

```text
FRAME 1 — QUESTION
{memory["question"]}

FRAME 2 — OBJECT
{memory["object"]}

FRAME 3 — FAILURE
{memory["failure_image"]}

FRAME 4 — TRANSFORMATION
{memory["transformation"]}

FRAME 5 — SEAL
{memory["sentence"]}
```

## Position inside the Undercroft

```text
Realm {realm["number"]} of 5 — {realm["name"]}
{realm["path"]}
current root: {name}
```

```text
temptation : {row.attempt}
break      : {row.failure}
repair     : {row.repair}
```

The film can be replayed without the equation. Once it is vivid, the symbols become a compact subtitle for a scene the reader already owns.
"""


def wrapped_python(source: str, number: int) -> str:
    return f'''"""Excavation {number:03d}: rebuild the chapter with no numerical library."""\n\n{source}\n\nif __name__ == "__main__":\n    print(demo())\n'''


def numpy_file(source: str, number: int) -> str:
    return f'''"""Excavation {number:03d}: array form of the same named experiment."""\nimport math\nfrom pathlib import Path\nimport sys\n\n_here = Path(__file__).resolve().parent\nsys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != _here]\nimport numpy as np\n\n{source}\n'''


def torch_file(source: str, number: int) -> str:
    return f'''"""Excavation {number:03d}: tensor form of the same named experiment."""\nimport math\ntry:\n    import torch\nexcept ImportError:\n    raise SystemExit("Install PyTorch to run this stage.")\n\n{source}\n'''


def roots_guide() -> str:
    out = [
        "# The Mathematical Roots — A Memory Palace Beneath AI",
        "",
        "A mathematical root is not a formula, a chapter label, or a school subject. "
        "It is a **reusable promise** humanity needed the world to keep: a promise "
        "about belonging, connection, direction, change, uncertainty, choice, or "
        "calculation. The equation is the final inscription on that promise.",
        "",
        "Use this palace during the retrieval passage in [How to Master AI "
        "Archaeology](HOW_TO_MASTER_THIS_BOOK.md), after first allowing the chapter "
        "to make the root necessary.",
        "",
        "The Undercroft is arranged as a movie because memory keeps transformations "
        "more naturally than definitions. In every chamber, watch the same five frames:",
        "",
        "```text",
        "human question",
        "      ↓",
        "physical object",
        "      ↓",
        "visible failure",
        "      ↓",
        "the object transforms",
        "      ↓",
        "one memory sentence",
        "      ↓",
        "equation becomes a subtitle for the remembered scene",
        "```",
        "",
        "Do not begin by memorizing the seals below. Enter a chapter, risk the wrong "
        "idea, and let the room change. Then return here and test whether the object "
        "can recover the promise.",
        "",
        "## The complete walk",
        "",
        "```text",
        "THE HALL OF BOUNDARIES",
        "belonging → connection → dependable transformation",
        "                 ↓",
        "THE CHAMBER OF DIRECTIONS",
        "language of space → new directions → persistent directions → honest shadows → strongest channels",
        "                 ↓",
        "THE RIVER OF CHANGE",
        "approach → local change → coupled change → bending → nearby prediction → accumulation → hidden rhythm",
        "                 ↓",
        "THE OBSERVATORY OF POSSIBLE WORLDS",
        "possible worlds → evidence → centre and spread → settling averages → bell-shaped error → convincing claims",
        "                 ↓",
        "THE GARDEN OF FUTURES",
        "sufficient present → remembered futures → trustworthy landscape → safe computation",
        "```",
        "",
        "[Open the living, clickable Undercroft →](mathematical-roots/README.md)",
    ]
    for realm in REALMS:
        out.extend([
            "",
            f'<a id="realm-{realm["number"]}"></a>',
            f'## Realm {realm["number"]} — {realm["name"]}',
            "",
            realm["threshold"],
            "",
            f'**The human question of this realm:** {realm["question"]}',
            "",
            f'**The sound that identifies it:** {realm["sound"]}.',
            "",
            "| # | Root chamber | Human question | Object carried in memory | Memory seal |",
            "|---:|---|---|---|---|",
        ])
        for row in ROWS:
            if not (realm["start"] <= row.number <= realm["end"]):
                continue
            memory = ROOT_MEMORY[row.number]
            link = f'excavations/{row.number:03d}-{row.slug}/README.md'
            out.append(
                f'| {row.number:03d} | [{concept(row)}]({link}) | '
                f'{memory["question"]} | {memory["object"]} | '
                f'**{memory["sentence"]}** |'
            )
        out.extend([
            "",
            f'Walk this realm aloud: **{realm["path"]}**.',
        ])
    out.extend([
        "",
        "## How to make the palace permanent",
        "",
        "After each chapter, close the page. See the physical object before saying the "
        "concept's name. Make the failure happen. Reverse it with the transformation. "
        "Only then speak the memory seal and reconstruct the equation's jobs.",
        "",
        "A useful test is bidirectional:",
        "",
        "- **From name to necessity:** “gradient” should summon the hillside, compass, "
        "missing combined direction, and descent.",
        "- **From necessity to name:** “I need the direction of fastest local change” "
        "should open the same chamber and recover gradient.",
        "- **From symbol to scene:** every sign in the equation should point to a visible "
        "action already performed in that room.",
        "",
        "When all three paths work, the mathematics is no longer a borrowed sentence. "
        "It has become an instrument the reader can reinvent.",
        "",
    ])
    return "\n".join(out)


def main() -> None:
    for row in ROWS:
        memory = ROOT_MEMORY[row.number]
        realm = realm_for(row.number)
        folder = ROOT / "excavations" / f"{row.number:03d}-{row.slug}"
        implementation = folder / "implementation"
        images = folder / "images"
        implementation.mkdir(parents=True, exist_ok=True)
        images.mkdir(exist_ok=True)
        (folder / "README.md").write_text(chapter(row))
        (folder / "diagram.md").write_text(diagram(row))
        (folder / "mistakes.md").write_text(f"""# Mistakes Worth Preserving — Excavation {row.number:03d}

## The tempting idea

We tried to {row.attempt}.

## The evidence that refused it

{row.failure}

## What the wreckage taught us

The next construction had to {row.repair}.

Keep this wrong idea. It is the negative space around {concept(row)}: it records why the accepted method has exactly the responsibilities it does.
""")
        (folder / "exercises.md").write_text(f"""# Invention Exercises — Excavation {row.number:03d}

1. Retell the opening scene without using the words **{concept(row)}** or any symbol from its equation. What can the people in the scene observe?
2. Build the smallest new example in which this attempt fails: {row.attempt}. Name the precise information lost.
3. Cover one operation in the displayed equation. What job becomes impossible? Replace it with addition, multiplication, or division and show the wrong result in human terms.
4. Change one number or object in the worked example. Predict every intermediate result, then verify it with `implementation/pure_python.py`.
5. Close the chapter and replay its five-frame film from memory: question → object → failure → transformation → seal. Use this gesture if the scene fades: {memory["gesture"]}
6. Design a new invention that addresses this boundary: {row.limit}

The goal is not recall. Each answer should recreate the pressure from which the mathematical object could be invented. When you can recover “{memory["sentence"]}” from the object **{memory["object"]}**, this root has begun to live in memory.
""")
        refs = "\n".join(f"- [{title}]({url}) — primary source for the history, mechanism, or modern use behind this excavation." for title, url in row.references)
        (folder / "references.md").write_text(f"""# Primary Research Trail — {row.title}

{refs}

Read the chapter first. These sources are not substitutes for the excavation; they let you inspect the historical formulation, assumptions, evidence, and modern consequences after the idea has become intuitive.
""")
        (images / "README.md").write_text(f"""# Visual Brief — {row.title}

Create a five-frame mathematical fantasy sequence inside **{realm["name"]}**.

1. **Question:** {memory["question"]}
2. **Object:** show {memory["object"]}.
3. **Failure:** {memory["failure_image"]}
4. **Transformation:** {memory["transformation"]}
5. **Memory seal:** reveal “{memory["sentence"]}”

Preserve the same named objects, camera direction, and visual landmarks across
all five frames so the viewer experiences one changing world rather than five
illustrations. The formula may appear only as a faint final engraving after the
transformation. The image succeeds when a reader can cover the caption and
reconstruct the mathematical promise from the scene alone.
""")
        (implementation / "README.md").write_text(f"""# Build {concept(row)} Three Times

All three files reproduce the named experiment from Excavation {row.number:03d}.

1. [`pure_python.py`](pure_python.py) uses ordinary values, sets, lists, and loops so every responsibility remains visible.
2. [`numpy.py`](numpy.py) expresses the same repair with arrays and numerical operations.
3. [`pytorch.py`](pytorch.py) carries it into tensor machinery used by modern AI.

Run them in order. Before each run, say what should remain invariant and which intermediate value would expose the original failure.
""")
        (implementation / "pure_python.py").write_text(wrapped_python(PURE[row.number], row.number))
        (implementation / "numpy.py").write_text(numpy_file(NUMPY[row.number], row.number))
        (implementation / "pytorch.py").write_text(torch_file(TORCH[row.number], row.number))
    (ROOT / "MATHEMATICAL_ROOTS.md").write_text(roots_guide())
    print("Built Excavations 201–225 as a connected book-and-laboratory volume.")


if __name__ == "__main__":
    main()
