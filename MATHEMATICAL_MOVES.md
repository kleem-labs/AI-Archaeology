# Mathematical Moves — Why This Sign, Here?

Mathematics has a small collection of moves. The symbols are only their short
names.

Imagine three rangers reporting on one tiger. One reports its weight, one its
speed, and one its distance from camp. Before writing any formula, decide what
job you are trying to perform:

- keep the reports separate;
- find a change between two reports;
- combine independent contributions;
- make a fair share or average;
- make repeated evidence easier to accumulate;
- choose the strongest candidate;
- or measure how one quantity responds when another changes.

Different jobs force different operations. **Addition is not “better” than
multiplication. A logarithm is not mathematical decoration.** Each preserves a
different relationship. The question to ask whenever you meet a sign is:

> What relationship would be lost if I replaced this operation with another?

Use the links below from any excavation. Return to the concrete chapter after
the move makes sense; this guide explains the tool, while the excavation
explains why that tool became necessary there.

## Map of the moves

| Job | Moves |
|---|---|
| Name and organize | [equals](#equals), [brackets](#brackets), [indices](#indices), [membership](#membership), [arrows](#arrows), [function application](#function-application) |
| Compare and measure change | [subtraction](#subtraction), [absolute value](#absolute-value), [powers](#powers), [square root](#square-root), [difference and delta](#difference-and-delta) |
| Combine evidence | [addition](#addition), [summation](#summation), [multiplication](#multiplication), [dot product](#dot-product), [concatenation](#concatenation) |
| Share and normalize | [division](#division), [mean](#mean), [normalization](#normalization), [norm](#norm) |
| Reshape scale | [exponential](#exponential), [logarithm](#logarithm), [negative sign](#negative-sign) |
| Choose or constrain | [maximum](#maximum), [arg-max](#arg-max), [cases](#cases), [inequalities](#inequalities), [union](#union), [rounding](#rounding) |
| Describe sensitivity | [limit](#limit), [derivative](#derivative), [partial derivative](#partial-derivative), [gradient](#gradient), [proportionality](#proportionality) |
| Reason under uncertainty | [probability](#probability), [conditional bar](#conditional-bar), [expectation](#expectation), [variance](#variance) |

## Quick sign index

| Sign | Read it as | Detailed mental model |
|---|---|---|
| $=$ | “is the same result as” | [equals](#equals) |
| $+$, $\sum$ | combine same-role contributions | [addition](#addition), [summation](#summation) |
| $-$ | find a gap or reverse a direction | [subtraction](#subtraction), [negative sign](#negative-sign) |
| $ab$, $a\times b$, $a\cdot b$ | scale, interact, or combine aligned factors | [multiplication](#multiplication), [dot product](#dot-product) |
| $a/b$, $\frac{a}{b}$ | amount per unit, share, or normalization | [division](#division) |
| $a^2$, $a^{-b}$ | repeated multiplication or power-law scaling | [powers](#powers) |
| $\sqrt{a}$ | return from squared scale | [square root](#square-root) |
| $e^a$, $\exp(a)$ | positive multiplicative weight from an additive score | [exponential](#exponential) |
| $\log a$ | convert multiplication into addition | [logarithm](#logarithm) |
| $\lvert a\rvert$, $\lVert a\rVert$ | magnitude after discarding selected direction information | [absolute value](#absolute-value), [norm](#norm) |
| $\to$, $\leftarrow$ | flows into, becomes, or is updated by | [arrows](#arrows) |
| $\in$, $\cup$ | belongs to a set; joins set members | [membership](#membership), [union](#union) |
| $<$, $>$, $\le$ | order or bound without claiming equality | [inequalities](#inequalities) |
| $\approx$, $\propto$ | approximately equal; scales like | [approximation](#approximation), [proportionality](#proportionality) |
| $\lim$, $d/du$, $\partial$, $\nabla$ | approaching value; local sensitivity | [limit](#limit), [derivative](#derivative), [partial derivative](#partial-derivative), [gradient](#gradient) |
| $P(\cdot)$, $\mid$, $\mathbb{E}$ | probability, conditioning, probability-weighted average | [probability](#probability), [conditional bar](#conditional-bar), [expectation](#expectation) |
| $\max$, $\underset{x}{\text{arg max}}$ | winning value; candidate that wins | [maximum](#maximum), [arg max](#arg-max) |
| $\lvert B\rvert$ | number of members in B | [cardinality](#cardinality) |
| $x_i$, $x^*$, $x'$, $\widehat{x}$, $\bar{x}$ | addressed or specially marked version of x | [indices](#indices), [symbol decorations](#symbol-decorations) |

---

<a id="equals"></a>
## Equals: two descriptions of the same result

Suppose the ranger counts two adult tigers and one cub. “Three tigers” and
“two adults plus one cub” are different descriptions of the same total:

$$
3=2+1
$$

The equals sign does not mean “and then.” It makes a claim that the expression
on the left and the expression on the right produce the same object or value.

Use it when defining a quantity, recording an equivalent recipe, or stating a
relationship that should remain true. Do not use it merely to connect successive
thoughts whose values differ.

<a id="brackets"></a>
## Brackets: keep related observations together

Tiger weight, speed, and age answer different questions, so adding them would
destroy their identities. Brackets let us carry them as one ordered object
without combining them:

$$
[220,65,6]
$$

Use brackets for vectors, lists, matrix rows, intervals, or indexing. Brackets
organize; by themselves they do not add, average, or compare anything.

<a id="indices"></a>
## Indices and subscripts: point to one member without giving it a new name

If a report has a thousand features, inventing a separate name for each one is
clumsy. A subscript says which member we mean: $x_1$ is the first feature,
$x_i$ is whichever feature is currently being considered, and $x_{ij}$ can
identify row $i$, column $j$.

Use indices for ordered sequences, coordinates, tokens, examples, time steps,
or matrix locations. An index is an address, not multiplication.

<a id="symbol-decorations"></a>
## Stars, primes, hats, and bars: mark a related version without inventing a new alphabet

A decoration changes which version of an object we mean:

- $x^*$ often marks a selected or best candidate;
- $x'$ often marks a changed, next, or comparison version;
- $\widehat{x}$ often marks an estimate, prediction, reconstruction, or normalized version;
- $\bar{x}$ often marks an average or an accumulated reverse-mode sensitivity.

These are conventions, not universal laws. The chapter must define the job
each mark performs. None of these marks means multiplication merely because it
is written above or beside a symbol.

<a id="cardinality"></a>
## Vertical bars around a set: count its members

If B is a mini-batch containing three examples, $|B|=3$. Here the bars ask “how
many members?” rather than “how large is a signed number?” Context distinguishes
cardinality from [absolute value](#absolute-value).

Use cardinality when a total must be divided by the number of participating
objects or when comparing set sizes.

<a id="membership"></a>
## Membership: say what kind of object is allowed

The statement $x\in\mathbb{R}$ says “x is one real number.” The statement
$\mathbf{x}\in\mathbb{R}^d$ says “x is an ordered collection of d real
numbers.” The symbol $\in$ means “belongs to.”

Use membership when the allowed type or set matters. It prevents nonsense such
as feeding a word where a three-number vector is required.

<a id="arrows"></a>
## Arrows: show movement, mapping, or process order

An arrow can mean “becomes,” “is represented as,” or “flows into,” depending on
the sentence around it:

```text
observation → features → prediction
```

Use arrows when order or transformation matters more than equality. Do not read
an arrow as an equals sign: the observation and prediction are not the same
object.

<a id="function-application"></a>
## Parentheses and function application: feed an input into a named machine

In $F(x)$, $F$ is a reusable procedure and $x$ is what we give it. Parentheses
keep the input attached to the procedure. Nested parentheses such as $F(G(x))$
say that G acts first and F receives its result.

Use function notation when one rule should work for many inputs. It exposes
composition without spelling out every internal step each time.

---

<a id="subtraction"></a>
## Subtraction: ask what must change

A tiger was 12 metres away and is now 7 metres away. The change is “new minus
old”: $7-12=-5$. The negative answer preserves direction—it moved five metres
closer.

Use subtraction for displacement, error, residuals, centered values, and gaps.
Addition would answer “how much altogether?” rather than “what changed?”

<a id="absolute-value"></a>
## Absolute value: keep size and deliberately discard direction

One confidence estimate is 0.8 and observed accuracy is 0.4. Their signed gap
is $0.4-0.8=-0.4$, but calibration error needs the size of the mismatch, 0.4.
Absolute value turns both $-0.4$ and $+0.4$ into the same magnitude.

Use it when direction truly does not matter. Do not use it when “too high” and
“too low” require different actions.

<a id="powers"></a>
## Powers and squaring: repeated multiplication with a purpose

Squaring a mismatch multiplies it by itself. A difference of 2 contributes 4;
a difference of 5 contributes 25. This does two useful jobs: negative and
positive differences no longer cancel, and large misses matter more.

Use powers for area-like magnitude, nonlinear penalties, repeated growth, and
scaling laws. Do not square automatically: it changes the relative importance
of large and small values.

<a id="square-root"></a>
## Square root: return from squared scale

After squared centimetre differences have been combined, the result is in
“squared centimetres.” A square root asks which ordinary length would produce
that square, returning the answer to the original scale.

Use a root when an earlier power was useful internally but the final answer
should return to an interpretable scale. It is not needed if squared scale is
already the quantity you want to optimize.

<a id="difference-and-delta"></a>
## Delta: name a change so it can be reused

$\Delta$ is the Greek letter delta, conventionally used to name a change. If a
ranger moves from position $a$ to position $b$, then $\Delta=b-a$. Naming the
change lets us later write $a+\Delta=b$.

Use delta for finite changes. For an infinitesimally small sensitivity, the
[derivative](#derivative) is the more precise move.

---

<a id="addition"></a>
## Addition: combine contributions measured in the same role

Three scouts report 2, 3, and 1 tigers in non-overlapping regions. If the job is
the total number of tigers, their contributions accumulate: $2+3+1=6$.

Addition is forced when contributions should retain their ordinary size and
each extra contribution should increase the total by that amount. Multiplying
would claim interaction: one zero report would erase every other region and
doubling one report would scale the whole result. That is not what “total
across regions” means.

Use addition for totals, residual paths, votes, evidence already placed on a
common scale, and independent effects in linear models.

<a id="summation"></a>
## Summation: repeat addition over an indexed collection

$\sum_i x_i$ is not a new operation. It says: take every allowed $i$, retrieve
$x_i$, and add those contributions. We use the large sigma because writing
$x_1+x_2+\cdots+x_n$ becomes unreadable when the collection is large.

Use a sum when every member contributes to one total in the same role. Do not
use it when members must remain separate, when order matters, or when the
relationship is compound growth—those jobs need brackets, sequences, or
multiplication.

<a id="multiplication"></a>
## Multiplication: scale one quantity or require factors to act together

A danger clue of 4 given importance 3 contributes $3\times4=12$. The clue
would contribute nothing if its importance were zero, reverse direction if the
importance were negative, and double if the importance doubled.

Multiplication is forced when one quantity controls the strength of another, or
when independent factors jointly determine a result. Addition would let a zero
importance still add the clue and would not express scaling.

Use multiplication for weights, rates, probabilities of independent joint
events, unit conversion, areas, and passing sensitivity through several stages.

<a id="dot-product"></a>
## Dot product: multiply matching features, then add their agreements

A query asking for “large, striped, nearby” must compare its “large” need with
the key's “large” offer—not with its “nearby” offer. The dot product first
multiplies aligned features, then adds the resulting agreements and
disagreements into one relevance score.

Multiplication alone would leave one score per feature. Addition alone would
mix unpaired features and lose whether the same attribute agreed. The two-step
job forces “multiply matches, then sum contributions.”

Use dot products for alignment, weighted totals, projections, similarity-like
scores, and linear layers.

<a id="concatenation"></a>
## Concatenation: preserve several answers side by side

If one attention head follows grammar and another follows reference, adding
their outputs immediately would blur which evidence came from which expert.
Concatenation places the outputs side by side so a later learned transformation
can decide how to mix them.

Use concatenation when identities must survive combination. Use addition when
the pieces already play the same role and should become one total.

---

<a id="division"></a>
## Division: make a rate, share, or comparison independent of scale

Six tiger sightings among twenty comparable observations becomes $6/20$. The
division asks, “for each one observation, what share belonged to tiger?” If we
kept the count 6, a longer observation period would look more likely merely
because it contained more opportunities.

Use division for probabilities, averages, rates, normalization, and unit
conversion. Multiplication answers the opposite kind of question: “how much
after scaling by this factor?”

<a id="mean"></a>
## Mean: add comparable witnesses, then divide by how many spoke

Three thermometers read 18, 20, and 22 degrees. Their total, 60, grows if we add
more thermometers. Dividing by three returns the typical contribution per
thermometer: 20.

Use a mean when each observation should receive equal influence and the answer
should remain on the original scale. Do not average incomparable units or cases
whose unequal reliability should be preserved.

<a id="normalization"></a>
## Normalization: preserve relative pattern while removing irrelevant scale

Scores 2, 4, and 8 and scores 20, 40, and 80 have the same ratios but different
volumes. Normalization divides by an appropriate total or spread so downstream
work responds to the pattern rather than arbitrary scale.

Use it when relative shares or comparable scale matter. Do not normalize away
absolute magnitude when that magnitude itself carries meaning.

<a id="norm"></a>
## Norm: turn many coordinate magnitudes into one size

A vector can be large in several directions. A norm combines those coordinate
contributions into one nonnegative magnitude. The squared L2 norm adds squared
coordinates, making large weights increasingly expensive.

Use norms for distance, regularization, error magnitude, and constraints. The
choice of norm encodes what kinds of deviations should matter most.

---

<a id="exponential"></a>
## Exponential: turn additive score gaps into positive multiplicative weight

Suppose one candidate's score exceeds another by 2. After exponentiation their
positive weights differ by the fixed ratio $e^2$, no matter whether the raw
scores were 1 and 3 or 101 and 103. A larger additive score gap becomes a larger
multiplicative preference, and no weight can become negative.

Why not square the scores? Squaring makes $-3$ outrank $2$ and treats a common
shift as meaningful. Why not use absolute value? It also destroys which score
was higher. Exponentiation preserves order, stays positive, and converts score
differences into ratios. That is precisely what softmax needs.

Use exponentials for positive growth, decays, unnormalized probability weights,
odds, and processes whose current amount controls their rate of change.

<a id="logarithm"></a>
## Logarithm: turn multiplication into addition

Two independent observations with probabilities 1/2 and 1/8 occur together
with probability $1/2\times1/8=1/16$. Their surprises should accumulate as one
bit plus three bits, not remain an awkward product. The logarithm performs that
conversion: $\log(ab)=\log a+\log b$.

Why not use $1/p$ as surprise? It grows for rare events, but independent
surprises multiply, making long sequences hard to accumulate and compare. The
log is forced when underlying probabilities multiply but the quantity we want
to total should add.

Use logs for information, likelihoods, multiplicative growth, ratios spanning
large scales, and turning products into numerically stable sums.

<a id="negative-sign"></a>
## Negative sign: reverse direction or reverse ranking

Probabilities below one have negative logarithms. Surprise should be
nonnegative and should grow when probability shrinks, so $-\log p$ reverses the
sign and ranking. In gradient descent, subtracting the gradient reverses the
direction of increasing loss.

Use a negative sign only when the desired direction is the opposite of the
quantity already computed. It is not a cosmetic way to make an answer positive;
the reversal must have a real job.

---

<a id="maximum"></a>
## Maximum: keep the largest value

If several actions have estimated future returns, $\max$ returns the largest
return. It discards the identity of the action and every losing value.

Use maximum when only the winning value matters. It is brittle when uncertainty,
diversity, or near-ties matter; then averaging, sampling, or preserving the full
distribution may be more honest.

<a id="arg-max"></a>
## Arg max: keep the candidate that produced the largest value

If pair `lo` occurs 30 times and pair `ow` 12 times, max returns 30 while arg
max returns `lo`. Tokenization needs the pair to merge, not merely its count.

Use arg max when the identity of the winner matters. Use max when only the
winning score matters.

<a id="cases"></a>
## Cases: let different conditions invoke different rules

A causal attention mask assigns zero cost to visible earlier positions and an
impossible cost to future positions. One smooth rule would hide this deliberate
boundary. Cases say exactly which rule applies under each condition.

Use cases for thresholds, piecewise policies, masks, and boundary behavior.

<a id="inequalities"></a>
## Inequalities: state a bound instead of exact equality

Privacy does not claim that two output probabilities are equal. It limits how
far apart they may be, so $\le$ is the honest relationship.

Use inequalities for guarantees, budgets, ordering, feasible regions, and
approximate control. Equality would make a stronger claim that may be false and
unnecessary.

<a id="union"></a>
## Union: combine sets while preserving membership

Training, validation, and test sets together form the complete dataset. Union
combines their members; it does not add their numeric values.

Use union when joining collections of objects. If overlap is forbidden, state
that separately—the union sign alone does not guarantee disjoint sets.

<a id="rounding"></a>
## Rounding: choose the nearest allowed discrete value

Quantization cannot store every real-valued weight. After scaling, rounding
selects the nearest available integer level. The move deliberately loses small
differences in exchange for cheaper storage and arithmetic.

Use rounding when the allowed representation is discrete and the resulting
error has been measured. Do not treat it as exact equality.

---

<a id="limit"></a>
## Limit: ask what a procedure approaches as the probe shrinks

A finite nudge can leap across curvature. Rather than pretending the nudge is
already zero—which would cause division by zero—we watch the change ratio as
the nudge becomes arbitrarily small. The limit names the value approached.

Use limits for instantaneous rates, continuity, and asymptotic behavior.

<a id="derivative"></a>
## Derivative: change in output per tiny change in one input

Move one weight slightly, observe how loss changes, and divide output change by
input change. Shrinking the probe isolates local sensitivity. The derivative is
a rate, which is why division is essential.

Use derivatives for slopes, sensitivities, optimization, motion, and marginal
effects. A derivative describes the neighborhood of the present point, not the
entire landscape.

<a id="partial-derivative"></a>
## Partial derivative: question one input while holding the others fixed

A network node may depend on many inputs. $\partial y/\partial x$ asks how y
responds to x locally while the other inputs are held fixed. The curled symbol
warns us that this is one route through a multi-input system.

Use partial derivatives in multivariable functions, networks, physical fields,
and any system where several causes meet.

<a id="gradient"></a>
## Gradient: collect every parameter's local uphill direction

One derivative advises one weight. A model has many weights, so the gradient
collects all those local sensitivities in parameter order. It points toward
increasing loss; the negative gradient points locally downhill.

Use gradients when many adjustable quantities jointly affect one result.

<a id="proportionality"></a>
## Proportionality: state how something scales without claiming an exact constant

Attention cost grows like the square of context length, but hardware and
implementation determine the exact constant. $\propto n^2$ records the scaling
relationship without inventing a universal equality.

Use proportionality when relative growth is known but the fixed multiplier is
irrelevant or context-dependent.

<a id="approximation"></a>
## Approximately equal: state a useful target without claiming exact identity

Randomly initialized weights can be designed so their population variance is
near $1/n$, but one finite sample will not land on that number exactly. The sign
$\approx$ keeps the intended scale while refusing a false equality.

Use approximation for measured values, numerical estimates, asymptotic rules,
and design targets whose small deviations do not change the argument. State the
tolerance when a decision depends on how close is close enough.

---

<a id="probability"></a>
## Probability: give plausible outcomes shares of one whole

Probability does not declare which story is true. It allocates nonnegative
shares that total one, preserving uncertainty while making comparison and
decision possible.

Use probability when several outcomes remain possible and evidence supports
different degrees of belief or long-run frequency.

<a id="conditional-bar"></a>
## Conditional bar: change the question after evidence is known

$P(E\mid H)$ reads “the probability of evidence E if hypothesis H were true.”
The bar prevents us from confusing that with $P(H\mid E)$, the probability of
the hypothesis after seeing evidence.

Use conditioning whenever the information assumed known changes the
distribution being discussed.

<a id="expectation"></a>
## Expectation: probability-weighted averaging over possible cases

If a loss of 10 occurs 10% of the time and a loss of 1 occurs 90% of the time,
the long-run average is not their unweighted mean. Expectation multiplies each
outcome by how often it matters, then sums the contributions.

Use expectation for average loss, reward, risk, and uncertainty when outcomes
do not occur equally often.

<a id="variance"></a>
## Variance: measure spread around the mean without cancellation

Values one below and one above the mean should both count as variation. Their
signed differences cancel, so variance squares the centered differences before
averaging them.

Use variance for noise, uncertainty, initialization scale, and dispersion. It
measures spread, not the original unit; standard deviation takes the square
root to return to that unit.

---

## A five-question habit for every future equation

Before accepting any operation, ask:

1. What are the concrete objects entering it?
2. What relationship must survive: total, scale, direction, identity, order, or
   uncertainty?
3. What would addition mean here? What would multiplication mean?
4. Which wrong result appears if the chosen operation is removed or replaced?
5. Can I perform the move on one tiny example before reading the symbols?

When those questions have answers, the equation stops looking like authority.
It becomes your own compressed decision.
