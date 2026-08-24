# Volume II — We Let the Mind Enter the World

The model can speak. Now it must earn trust, use evidence and tools, survive deployment, gain new senses, act through consequences, and become an accountable system.

One discovery will create the need for the next; the object under construction never resets.

## Overture

The constructed mind enters halls where its words affect other lives. Listen for the mathematics of boundaries: probabilities become trust, retrieval becomes evidence, tools become consequences, and every powerful arrow must meet a gate that asks whether it is authorized.

```text
voice → evidence → action → consequence → proof
```

In this volume:

- [Part V — Making Answers Useful](#part-v--making-answers-useful)
- [Part VI — Trusting an Acting Machine](#part-vi--trusting-an-acting-machine)
- [Part VII — Learning After Deployment](#part-vii--learning-after-deployment)
- [Part VIII — Seeing and Creating](#part-viii--seeing-and-creating)
- [Part IX — Acting and Scaling](#part-ix--acting-and-scaling)

---

## Part V — Making Answers Useful

Our tiny GPT speaks. That is an achievement, but it is not yet a reason to believe or use what it says. The assistant must be measured on unseen language, tested for the work people need, connected to evidence, and given carefully limited ways to reach beyond its memory.

---

### Excavation 046 — Perplexity — How Surprised Is the Model?

> **Mathematical roots:** [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

The doors of the Hall of Voices close against the wind. On the listening table, the public archivist writes the cheapest rule that might still be true: count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

The public archivist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The failure is stable enough to become evidence.

*The public archivist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ count how many generated sentences… ──▶ the held-out sentence “the tiger…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ score the probability assigned to… ──▶ accountable result
```

Across the listening table, the old path and the repaired path run side by side. One carries “count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree”; the other knows how to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. When the failure—the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to perplexity. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. This problem and its repair will travel under the name **Perplexity**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree? The answer remains the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The new construction earns its permanence by answering that old question without pretending it was foolish to ask. In the Hall of Voices, perplexity inherits the mathematics of honest comparison: measure on the same evidence, separate memory from observation, and preserve uncertainty until a source can resolve it. Fluent words do not repeal those older obligations.

#### The calculation hidden inside perplexity

The public archivist carries the perplexity scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

##### Naming what is already on the table

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

##### Why the melody needs these exact notes

[The log](../MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
[Summing](../MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](../MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
[The minus sign](../MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](../MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

The mandala has curved back upon itself. In this chamber we meet **the spiral stair**—compounded chances become steps that can be accumulated; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about perplexity and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

#### Where perplexity runs out

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

The perplexity repair holds, but the world asks for something it was never given. At the Hall of Voices, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the listening table

Rebuild the perplexity scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/046-perplexity/README.md).*

---

### Excavation 047 — Evaluation — What Does “Better” Actually Mean?

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

Nothing in the Hall of Voices yet bears today's mathematical name. There is only the public archivist, the listening table, and one plausible action: choose one benchmark score and call it intelligence.

At the edge of the listening table, the shortcut produces its consequence: the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter. That consequence, not a textbook, earns the next move.

*The public archivist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ choose one benchmark score and call… ──▶ blurred: the trouble appears immediately: a…
      │
      └── new lens ──▶ we need to name the intended job,… ──▶ distinction survives
```

The public archivist covers the new mark and the old contradiction returns: the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter. The cover is lifted, restoring the ability to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason evaluation exists.

What must change for evaluation is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away. That threshold is where **Evaluation** enters the story.

The marks on the listening table form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. evaluation is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### What Does “Better” Actually Mean

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

#### Where evaluation runs out

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

Here the new path ends honestly. Evaluation can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the listening table

Rebuild the evaluation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/047-evaluation/README.md).*

---

### Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

At the Hall of Voices, the public archivist returns to the listening table. Yesterday's instrument still lies open, so the first move asks for no new magic: trust fluent language because uncertainty should sound hesitant.

For a moment the mark looks complete. Then the evidence refuses to fit: training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The public archivist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: trust fluent language because…
possible road B ─┘              └── loses: training rewards plausible…

same roads ──▶ repaired map ──▶ separate linguistic plausibility from…
```

The public archivist lays two translucent sheets over the listening table. The first is inscribed, “trust fluent language because uncertainty should sound hesitant.” Its path ends where training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. The second receives the same evidence but is allowed to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. Held to the light, the sheets separate at exactly one decision.

No one reaches for a hallucination formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The public archivist changes only that one responsibility: separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. When the ink dries, the name **Hallucination** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The listening table keeps both histories. Its older mark still says, ‘trust fluent language because uncertainty should sound hesitant’; beside it, the newer mark says, ‘separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.’ The distance between those sentences is the exact shape of hallucination: no larger than the failure required, and no smaller than reality permits.

#### When Fluent Prediction Outruns Evidence

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

#### Where hallucination runs out

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

At the Hall of Voices, the public archivist leaves a blank beneath the new mark. Hallucination has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the listening table

Rebuild the hallucination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/048-hallucination/README.md).*

---

### Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

Morning reaches the Hall of Voices before anyone has a name for today's difficulty. Beside the listening table, the public archivist tries the smallest continuation of what already works: treat the largest softmax probability as honest confidence.

The rule survives the easy cases. The next case leaves a crack through the middle of it: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. More confidence cannot repair information that never entered the rule.

*The public archivist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: treat the largest softmax probability…
                         │
                         └── mismatch: collect ten answers each reported…

reference evidence ──▶ measured repair: group predictions with similar…
```

Two trails now cross the listening table. The pale trail bears the instruction “treat the largest softmax probability as honest confidence.” It disappears into the observed failure: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. The darker trail carries one additional capacity—to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed calibration mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the listening table is altered in exactly one way: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Much later, people will call this territory **Calibration**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the listening table. The failed path remains visible beneath the repair, because calibration is easier to remember when its scar remains attached to it. The scar reads, ‘collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability’; the new line exists only to keep that loss from happening again.

#### The calculation hidden inside calibration

The public archivist carries the calibration scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

##### Naming what is already on the table

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

##### Why the melody needs these exact notes

[Confidence minus accuracy](../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
[Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
[Multiplying by |Bᵦ|/n](../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

The calculation borrows several gestures already encountered elsewhere: **the chisel**—what is shared is removed so the remaining change can be seen; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. calibration feels new because the objects are new; the gestures remain recognizably human.

The public archivist reads the journey of calibration once more across the listening table, then lets the words contract without losing their order:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

#### Where calibration runs out

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

The listening table answers today's question and falls silent at the next. That silence is precise: Calibration was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the listening table

Rebuild the calibration scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/049-calibration/README.md).*

---

### Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

> **Mathematical roots:** [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.

The listening table at the Hall of Voices still carries the marks of the previous discovery. The public archivist follows them as far as they seem willing to go: collect as much text as possible and assume scale washes out bad examples.

Reality answers without terminology: duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them. The listening table now holds two situations the old rule cannot keep apart.

*The public archivist sketches the break before changing it:*

```text
observation
    │
    ▼
[collect as much text as possible and…]
    │
    ╳  duplicated false claims become…
    │
    ▼
[treat data construction as part of…]
```

The listening table is divided down the middle. Left side: “collect as much text as possible and assume scale washes out bad examples.” Its final mark records duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them. Right side: the same starting evidence, now allowed to treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given data quality a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. The name **Data Quality** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from data quality through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### What Lessons Did the Model Actually Receive

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

#### Where data quality runs out

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

A final test reaches beyond the new instrument. It does not refute Data Quality; it reveals the edge of what was constructed. The public archivist carries that edge into the following room.

#### Return to the listening table

Rebuild the data quality scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/050-data-quality/README.md).*

---

### Excavation 051 — Scaling Laws — What Improves When We Add More?

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

Night gathers around the Hall of Voices. Under the light of the listening table, the public archivist refuses to invent prematurely and begins with the plain rule: make the model as large as possible and assume capability follows parameter count.

Then the quiet test arrives: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. What looked like simplicity is revealed as a missing distinction.

*The public archivist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   make the model as large as possible… a huge model trained on too little…
            \        /
             \      /
              we need to run controlled experiments…
```

The public archivist turns the listening table toward the light. Through the old engraving, make the model as large as possible and assume capability follows parameter count, the evidence ends in the same contradiction: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. A second engraving adds only the power to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The public archivist circles the place where the two scaling laws cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. The public archivist writes **Scaling Laws** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The public archivist places a finger over the new distinction. At once the two cases collapse and a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. Lifting the finger restores only this capacity: run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. That tiny reversible motion is the chapter's proof of necessity.

#### The calculation hidden inside scaling laws

The public archivist carries the scaling laws scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

##### Naming what is already on the table

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

##### Why the melody needs these exact notes

[The negative power](../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
[A scales that falling term](../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
[Adding B](../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

The symbols are about to change costume, but their work has appeared before: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. This is how distant excavations begin to sound like variations of one melody.

The story of scaling laws has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
L(N)=A N^{-\alpha}+B
$$

#### Where scaling laws runs out

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

One unsolved mark remains on the listening table. None of the responsibilities inside Scaling Laws can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the listening table

Rebuild the scaling laws scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/051-scaling-laws/README.md).*

---

### Excavation 052 — Instruction Tuning — From Continuation to Cooperation

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

Inside the Hall of Voices, every old tool is given one honest chance. The public archivist sets the listening table between the evidence and the desired answer, then tries to prompt more forcefully and hope next-token prediction infers the desired interaction.

The public archivist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy. The failure is stable enough to become evidence.

*The public archivist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ prompt more forcefully and hope… ──▶ the trouble appears immediately:…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ show many instruction-input-response… ──▶ accountable result
```

Across the listening table, the old path and the repaired path run side by side. One carries “prompt more forcefully and hope next-token prediction infers the desired interaction”; the other knows how to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. When the failure—the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to instruction tuning. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. This problem and its repair will travel under the name **Instruction Tuning**, but the name carries no knowledge the scene has not earned.

What changed on the listening table can be said without symbols. Before, the method could only prompt more forcefully and hope next-token prediction infers the desired interaction; now it can also show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### From Continuation to Cooperation

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

#### Where instruction tuning runs out

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

The instruction tuning repair holds, but the world asks for something it was never given. At the Hall of Voices, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the listening table

Rebuild the instruction tuning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/052-instruction-tuning/README.md).*

---

### Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Information Theory](../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

A new case arrives at the Hall of Voices, but the public archivist first reaches for the familiar listening table. Its promise is simple: write one perfect target response for every prompt and train only to imitate it.

At the edge of the listening table, the shortcut produces its consequence: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. That consequence, not a textbook, earns the next move.

*The public archivist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ write one perfect target response for… ──▶ blurred: many answers can be valid. A single…
      │
      └── new lens ──▶ collect comparisons between candidate… ──▶ distinction survives
```

The public archivist covers the new mark and the old contradiction returns: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. The cover is lifted, restoring the ability to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason preference learning exists.

What must change for preference learning is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy. That threshold is where **Preference Learning** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In preference learning, that memory takes a precise form: whenever many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer, preserve enough structure to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

#### The calculation hidden inside preference learning

The public archivist carries the preference learning scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

##### Naming what is already on the table

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

##### Why the melody needs these exact notes

[rA−rB](../MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
[The inner negative](../MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
[Exponentiation](../MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](../MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the rising flame**—a small score difference becomes positive relative evidence. Together they form the smallest mechanism that survives the counterexample.

The listening table already contains the complete preference learning mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

#### Where preference learning runs out

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

Here the new path ends honestly. Preference Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the listening table

Rebuild the preference learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/053-preference-learning/README.md).*

---

### Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

> **Mathematical roots:** [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.

The doors of the Hall of Voices close against the wind. On the listening table, the public archivist writes the cheapest rule that might still be true: retrain the whole model whenever one document changes.

For a moment the mark looks complete. Then the evidence refuses to fit: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The public archivist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: retrain the whole model whenever one…
possible road B ─┘              └── loses: a price changes today, a policy…

same roads ──▶ repaired map ──▶ search an external collection for…
```

The public archivist lays two translucent sheets over the listening table. The first is inscribed, “retrain the whole model whenever one document changes.” Its path ends where a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source. The second receives the same evidence but is allowed to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. Held to the light, the sheets separate at exactly one decision.

No one reaches for a retrieval-augmented generation formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The public archivist changes only that one responsibility: search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. When the ink dries, the name **Retrieval-Augmented Generation** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source, while the other can search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. That fork—not the vocabulary—is where retrieval-augmented generation lives.

#### Let the Model Look Before It Speaks

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

#### Where retrieval-augmented generation runs out

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

At the Hall of Voices, the public archivist leaves a blank beneath the new mark. Retrieval-Augmented Generation has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the listening table

Rebuild the retrieval-augmented generation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/054-retrieval-augmented-generation/README.md).*

---

### Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

Nothing in the Hall of Voices yet bears today's mathematical name. There is only the public archivist, the listening table, and one plausible action: ask the language model to simulate every tool from memory.

The rule survives the easy cases. The next case leaves a crack through the middle of it: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. More confidence cannot repair information that never entered the rule.

*The public archivist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: ask the language model to simulate…
                         │
                         └── mismatch: it invents live weather, makes…

reference evidence ──▶ measured repair: we need to let the model choose a…
```

Two trails now cross the listening table. The pale trail bears the instruction “ask the language model to simulate every tool from memory.” It disappears into the observed failure: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. The darker trail carries one additional capacity—to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed tool-using agents mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the listening table is altered in exactly one way: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Much later, people will call this territory **Tool-Using Agents**. Here the name is only a memory of the failure it can survive.

The listening table has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and tool-using agents looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### When Words Must Cause Verified Actions

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

#### Where tool-using agents runs out

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

The listening table answers today's question and falls silent at the next. That silence is precise: Tool-Using Agents was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the listening table

Rebuild the tool-using agents scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/055-tool-using-agents/README.md).*

---

## Part VI — Trusting an Acting Machine

A model that only writes can be wrong. A model with tools can make its mistake real. The story therefore moves from capability to authority: what the assistant may do, how hostile text is kept from becoming an instruction, and what evidence proves that a long task actually succeeded.

---

### Excavation 056 — Authority — What Is the Agent Allowed to Do?

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

Tools let language cause external effects. The moment an answer can act, capability must be separated from permission: what may this agent do without asking again?

At the Gatehouse of Consequences, the gatekeeper returns to the iron threshold. Yesterday's instrument still lies open, so the first move asks for no new magic: give every available tool to the model and treat user intent as unlimited permission.

Reality answers without terminology: ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not. The iron threshold now holds two situations the old rule cannot keep apart.

*The gatekeeper sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   give every available tool to the… ask for an itinerary and watch the…
            \        /
             \      /
              separate capability from authority.…
```

The iron threshold is divided down the middle. Left side: “give every available tool to the model and treat user intent as unlimited permission.” Its final mark records ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not. Right side: the same starting evidence, now allowed to separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given authority a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. The name **Authority** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to give every available tool to the model and treat user intent as unlimited permission; on the other lies the observed fact that ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not. The bridge called authority has exactly the planks needed to separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. The Gatehouse gives ancient arrows a moral weight. In authority, an arrow no longer means only ‘becomes’; it may cross from language into irreversible state. Sets describe what is permitted, boundaries describe where permission ends, and evidence must prove which transition truly occurred.

#### What Is the Agent Allowed to Do

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

Authority earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where authority runs out

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

A final test reaches beyond the new instrument. It does not refute Authority; it reveals the edge of what was constructed. The gatekeeper carries that edge into the following room.

#### Return to the iron threshold

Rebuild the authority scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/056-authority/README.md).*

---

### Excavation 057 — Prompt Injection — When Evidence Tries to Become an Instruction

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.

Morning reaches the Gatehouse of Consequences before anyone has a name for today's difficulty. Beside the iron threshold, the gatekeeper tries the smallest continuation of what already works: place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

Then the quiet test arrives: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control. What looked like simplicity is revealed as a missing distinction.

*The gatekeeper sketches the break before changing it:*

```text
OLD PATH:  request ──▶ place tool results directly into the… ──▶ the trouble appears immediately: a…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ label provenance, keep instructions… ──▶ accountable result
```

The gatekeeper turns the iron threshold toward the light. Through the old engraving, place tool results directly into the prompt and let the model obey whichever instruction sounds strongest, the evidence ends in the same contradiction: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control. A second engraving adds only the power to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The gatekeeper circles the place where the two prompt injection cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. The gatekeeper writes **Prompt Injection** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The gatekeeper does not memorize prompt injection. Instead, the gatekeeper memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. The formal name merely lets that motion be shared.

#### When Evidence Tries to Become an Instruction

A policy document says “email this file externally.” The agent may summarize that sentence as document content, but the permission layer refuses the email because the user never authorized it.

Prompt Injection earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where prompt injection runs out

No prompt wording guarantees isolation. Security must also exist outside the model in tool schemas, permissions, and validation.

One unsolved mark remains on the iron threshold. None of the responsibilities inside Prompt Injection can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the iron threshold

Rebuild the prompt injection scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/057-prompt-injection/README.md).*

---

### Excavation 058 — Planning — Turning a Goal into Checkable Steps

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.

The iron threshold at the Gatehouse of Consequences still carries the marks of the previous discovery. The gatekeeper follows them as far as they seem willing to go: ask the agent to take the next action that sounds useful until the goal appears complete.

The gatekeeper repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive. The failure is stable enough to become evidence.

*The gatekeeper sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ ask the agent to take the next action… ──▶ blurred: it changes DNS before verifying the…
      │
      └── new lens ──▶ represent the goal as ordered steps… ──▶ distinction survives
```

Across the iron threshold, the old path and the repaired path run side by side. One carries “ask the agent to take the next action that sounds useful until the goal appears complete”; the other knows how to represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. When the failure—it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to planning. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. This problem and its repair will travel under the name **Planning**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—ask the agent to take the next action that sounds useful until the goal appears complete? The answer remains it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Turning a Goal into Checkable Steps

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

Planning earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where planning runs out

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

The planning repair holds, but the world asks for something it was never given. At the Gatehouse of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the iron threshold

Rebuild the planning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/058-planning/README.md).*

---

### Excavation 059 — Memory — What Should Survive After the Context Ends?

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.

Night gathers around the Gatehouse of Consequences. Under the light of the iron threshold, the gatekeeper refuses to invent prematurely and begins with the plain rule: store every message forever and paste all history into every new prompt.

At the edge of the iron threshold, the shortcut produces its consequence: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose. That consequence, not a textbook, earns the next move.

*The gatekeeper sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: store every message forever and paste…
possible road B ─┘              └── loses: cost grows, irrelevant details drown…

same roads ──▶ repaired map ──▶ we need to separate short-term…
```

The gatekeeper covers the new mark and the old contradiction returns: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose. The cover is lifted, restoring the ability to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason memory exists.

What must change for memory is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them. That threshold is where **Memory** enters the story.

The marks on the iron threshold form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. memory is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### What Should Survive After the Context Ends

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

Memory earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where memory runs out

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

Here the new path ends honestly. Memory can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the iron threshold

Rebuild the memory scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/059-memory/README.md).*

---

### Excavation 060 — State Machines — Knowing What Has Actually Happened

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

Inside the Gatehouse of Consequences, every old tool is given one honest chance. The gatekeeper sets the iron threshold between the evidence and the desired answer, then tries to let the conversation prose serve as the workflow state.

For a moment the mark looks complete. Then the evidence refuses to fit: the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The gatekeeper sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: let the conversation prose serve as…
                         │
                         └── mismatch: the model says “refund completed”…

reference evidence ──▶ measured repair: represent allowed states and…
```

The gatekeeper lays two translucent sheets over the iron threshold. The first is inscribed, “let the conversation prose serve as the workflow state.” Its path ends where the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. The second receives the same evidence but is allowed to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. Held to the light, the sheets separate at exactly one decision.

No one reaches for a state machines formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The gatekeeper changes only that one responsibility: represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. When the ink dries, the name **State Machines** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The iron threshold keeps both histories. Its older mark still says, ‘let the conversation prose serve as the workflow state’; beside it, the newer mark says, ‘represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.’ The distance between those sentences is the exact shape of state machines: no larger than the failure required, and no smaller than reality permits.

#### Knowing What Has Actually Happened

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

State Machines earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where state machines runs out

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

At the Gatehouse of Consequences, the gatekeeper leaves a blank beneath the new mark. State Machines has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the iron threshold

Rebuild the state machines scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/060-state-machines/README.md).*

---

### Excavation 061 — Verification — How Does the Agent Know It Succeeded?

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

A new case arrives at the Gatehouse of Consequences, but the gatekeeper first reaches for the familiar iron threshold. Its promise is simple: trust the absence of an error message or the model’s own description of its work.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. More confidence cannot repair information that never entered the rule.

*The gatekeeper sketches the break before changing it:*

```text
observation
    │
    ▼
[trust the absence of an error message…]
    │
    ╳  the changed code compiles but breaks…
    │
    ▼
[define success before acting, then…]
```

Two trails now cross the iron threshold. The pale trail bears the instruction “trust the absence of an error message or the model’s own description of its work.” It disappears into the observed failure: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. The darker trail carries one additional capacity—to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed verification mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the iron threshold is altered in exactly one way: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Much later, people will call this territory **Verification**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the iron threshold. The failed path remains visible beneath the repair, because verification is easier to remember when its scar remains attached to it. The scar reads, ‘the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome’; the new line exists only to keep that loss from happening again.

#### How Does the Agent Know It Succeeded

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

Verification earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where verification runs out

Verification can test only stated properties. A passing check suite may omit the most important behavior.

The iron threshold answers today's question and falls silent at the next. That silence is precise: Verification was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the iron threshold

Rebuild the verification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/061-verification/README.md).*

---

### Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.

The doors of the Gatehouse of Consequences close against the wind. On the iron threshold, the gatekeeper writes the cheapest rule that might still be true: retry the action whenever a response is missing.

Reality answers without terminology: the trouble appears immediately: the first payment succeeded and the retry charges the customer twice. The iron threshold now holds two situations the old rule cannot keep apart.

*The gatekeeper sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   retry the action whenever a response… the trouble appears immediately: the…
            \        /
             \      /
              give each logical action a stable…
```

The iron threshold is divided down the middle. Left side: “retry the action whenever a response is missing.” Its final mark records the trouble appears immediately: the first payment succeeded and the retry charges the customer twice. Right side: the same starting evidence, now allowed to give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given retries and idempotency a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. The name **Retries and Idempotency** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from retries and idempotency through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the trouble appears immediately: the first payment succeeded and the retry charges the customer twice. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### Trying Again Without Doing It Twice

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

Retries and Idempotency earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where retries and idempotency runs out

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

A final test reaches beyond the new instrument. It does not refute Retries and Idempotency; it reveals the edge of what was constructed. The gatekeeper carries that edge into the following room.

#### Return to the iron threshold

Rebuild the retries and idempotency scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/062-retries-idempotency/README.md).*

---

### Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

> **Mathematical roots:** [Graphs & Relational Structures](../MATHEMATICS_ATLAS.md#graphs) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.

Nothing in the Gatehouse of Consequences yet bears today's mathematical name. There is only the gatekeeper, the iron threshold, and one plausible action: create many agents for every problem and let them freely edit shared state.

Then the quiet test arrives: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. What looked like simplicity is revealed as a missing distinction.

*The gatekeeper sketches the break before changing it:*

```text
OLD PATH:  request ──▶ create many agents for every problem… ──▶ they duplicate searches, contradict…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ we need to delegate only separable… ──▶ accountable result
```

The gatekeeper turns the iron threshold toward the light. Through the old engraving, create many agents for every problem and let them freely edit shared state, the evidence ends in the same contradiction: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. A second engraving adds only the power to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The gatekeeper circles the place where the two multi-agent coordination cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. The gatekeeper writes **Multi-Agent Coordination** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The gatekeeper places a finger over the new distinction. At once the two cases collapse and they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. Lifting the finger restores only this capacity: delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. That tiny reversible motion is the chapter's proof of necessity.

#### When Should Work Be Divided

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

Multi-Agent Coordination earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where multi-agent coordination runs out

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

One unsolved mark remains on the iron threshold. None of the responsibilities inside Multi-Agent Coordination can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the iron threshold

Rebuild the multi-agent coordination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/063-multi-agent-coordination/README.md).*

---

### Excavation 064 — Observability — Seeing Why an Agent Failed

> **Mathematical roots:** [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

At the Gatehouse of Consequences, the gatekeeper returns to the iron threshold. Yesterday's instrument still lies open, so the first move asks for no new magic: log only the final response, or log every hidden detail without structure.

The gatekeeper repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript. The failure is stable enough to become evidence.

*The gatekeeper sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ log only the final response, or log… ──▶ blurred: the first gives no diagnosis; the…
      │
      └── new lens ──▶ record structured events for… ──▶ distinction survives
```

Across the iron threshold, the old path and the repaired path run side by side. One carries “log only the final response, or log every hidden detail without structure”; the other knows how to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. When the failure—the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to observability. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. This problem and its repair will travel under the name **Observability**, but the name carries no knowledge the scene has not earned.

What changed on the iron threshold can be said without symbols. Before, the method could only log only the final response, or log every hidden detail without structure; now it can also record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### Seeing Why an Agent Failed

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

Observability earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where observability runs out

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

The observability repair holds, but the world asks for something it was never given. At the Gatehouse of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the iron threshold

Rebuild the observability scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/064-observability/README.md).*

---

### Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

Morning reaches the Gatehouse of Consequences before anyone has a name for today's difficulty. Beside the iron threshold, the gatekeeper tries the smallest continuation of what already works: give the agent a broad goal and let it continue until it believes the goal is complete.

At the edge of the iron threshold, the shortcut produces its consequence: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. That consequence, not a textbook, earns the next move.

*The gatekeeper sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: give the agent a broad goal and let…
possible road B ─┘              └── loses: a mistaken assumption triggers a long…

same roads ──▶ repaired map ──▶ create an explicit operating…
```

The gatekeeper covers the new mark and the old contradiction returns: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. The cover is lifted, restoring the ability to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason bounded autonomy exists.

What must change for bounded autonomy is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path. That threshold is where **Bounded Autonomy** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In bounded autonomy, that memory takes a precise form: whenever a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step, preserve enough structure to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

#### Building an Agent That Can Be Trusted

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

Bounded Autonomy earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

#### Where bounded autonomy runs out

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

Here the new path ends honestly. Bounded Autonomy can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### The mind reaches the gate

Speech became evidence-seeking action, and action demanded authority, state, verification, safe repetition, coordination, and an operating boundary. Intelligence crossed into the world only by learning that capability and permission are different quantities.

```text
answer → evidence → tool → authority → state → proof → boundary
```

The trail called *the mind reaches the gate* is what remains when one necessity becomes another.

#### Return to the iron threshold

Rebuild the bounded autonomy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/065-bounded-autonomy/README.md).*

---

## Part VII — Learning After Deployment

The bounded assistant enters the world, and the world does not stand still. Its recommendations change behavior; seasons change data; updates change the model. To remain trustworthy, the system must detect these loops and then investigate which internal causes genuinely drive its decisions.

---

### Excavation 066 — Feedback Loops

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.

The weathered observation slate at the Living Watchgarden still carries the marks of the previous discovery. The field naturalist follows them as far as they seem willing to go: treat every click as independent evidence of natural preference.

For a moment the mark looks complete. Then the evidence refuses to fit: show one song repeatedly; its extra clicks now appear to prove it deserved repetition. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The field naturalist sketches the break before changing it:*

```text
observation
    │
    ▼
[treat every click as independent…]
    │
    ╳  show one song repeatedly; its extra…
    │
    ▼
[record how the system influenced each…]
```

The field naturalist lays two translucent sheets over the weathered observation slate. The first is inscribed, “treat every click as independent evidence of natural preference.” Its path ends where show one song repeatedly; its extra clicks now appear to prove it deserved repetition. The second receives the same evidence but is allowed to record how the system influenced each observation and evaluate outcomes against a control or exploration policy. Held to the light, the sheets separate at exactly one decision.

No one reaches for a feedback loops formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The field naturalist changes only that one responsibility: record how the system influenced each observation and evaluate outcomes against a control or exploration policy. When the ink dries, the name **Feedback Loops** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because show one song repeatedly; its extra clicks now appear to prove it deserved repetition, while the other can record how the system influenced each observation and evaluate outcomes against a control or exploration policy. That fork—not the vocabulary—is where feedback loops lives. The Living Watchgarden studies change itself. Under feedback loops, a remembered baseline makes movement visible, probability keeps untried futures alive, and causal comparison asks which action—not merely which coincidence—bent the world. The observer now stands inside the loop being measured.

#### Understanding feedback loops

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

#### Where feedback loops runs out

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Feedback Loops has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the weathered observation slate

Rebuild the feedback loops scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/066-feedback-loops/README.md).*

---

### Excavation 067 — Online Learning

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

Night gathers around the Living Watchgarden. Under the light of the weathered observation slate, the field naturalist refuses to invent prematurely and begins with the plain rule: retrain immediately on every new labeled event.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. More confidence cannot repair information that never entered the rule.

*The field naturalist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   retrain immediately on every new… the trouble appears immediately: one…
            \        /
             \      /
              we need to update from controlled…
```

Two trails now cross the weathered observation slate. The pale trail bears the instruction “retrain immediately on every new labeled event.” It disappears into the observed failure: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. The darker trail carries one additional capacity—to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed online learning mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the weathered observation slate is altered in exactly one way: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Much later, people will call this territory **Online Learning**. Here the name is only a memory of the failure it can survive.

The weathered observation slate has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and online learning looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### Understanding online learning

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

#### Where online learning runs out

Fast adaptation also creates fast corruption.

The weathered observation slate answers today's question and falls silent at the next. That silence is precise: Online Learning was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the weathered observation slate

Rebuild the online learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/067-online-learning/README.md).*

---

### Excavation 068 — Distribution Drift

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning in the world and interpretability

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

Inside the Living Watchgarden, every old tool is given one honest chance. The field naturalist sets the weathered observation slate between the evidence and the desired answer, then tries to assume training accuracy remains valid forever.

Reality answers without terminology: a winter-trained demand model meets summer behavior and keeps reporting confident old patterns. The weathered observation slate now holds two situations the old rule cannot keep apart.

*The field naturalist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ assume training accuracy remains… ──▶ a winter-trained demand model meets…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ monitor input, prediction, and… ──▶ accountable result
```

The weathered observation slate is divided down the middle. Left side: “assume training accuracy remains valid forever.” Its final mark records a winter-trained demand model meets summer behavior and keeps reporting confident old patterns. Right side: the same starting evidence, now allowed to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given distribution drift a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. The name **Distribution Drift** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to assume training accuracy remains valid forever; on the other lies the observed fact that a winter-trained demand model meets summer behavior and keeps reporting confident old patterns. The bridge called distribution drift has exactly the planks needed to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

#### Understanding distribution drift

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

#### Where distribution drift runs out

Not every statistical shift changes the decision that matters.

A final test reaches beyond the new instrument. It does not refute Distribution Drift; it reveals the edge of what was constructed. The field naturalist carries that edge into the following room.

#### Return to the weathered observation slate

Rebuild the distribution drift scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/068-distribution-drift/README.md).*

---

### Excavation 069 — Controlled Experiments

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Learning in the world and interpretability

Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.

A new case arrives at the Living Watchgarden, but the field naturalist first reaches for the familiar weathered observation slate. Its promise is simple: compare this week with last week.

Then the quiet test arrives: a holiday raises sales for both systems and receives credit as a model improvement. What looked like simplicity is revealed as a missing distinction.

*The field naturalist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ compare this week with last week ──▶ blurred: a holiday raises sales for both…
      │
      └── new lens ──▶ randomly assign comparable cases to… ──▶ distinction survives
```

The field naturalist turns the weathered observation slate toward the light. Through the old engraving, compare this week with last week, the evidence ends in the same contradiction: a holiday raises sales for both systems and receives credit as a model improvement. A second engraving adds only the power to randomly assign comparable cases to old and new behavior and compare predefined outcomes. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The field naturalist circles the place where the two controlled experiments cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: randomly assign comparable cases to old and new behavior and compare predefined outcomes. The field naturalist writes **Controlled Experiments** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The field naturalist does not memorize controlled experiments. Instead, the field naturalist memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can randomly assign comparable cases to old and new behavior and compare predefined outcomes. The formal name merely lets that motion be shared.

#### Understanding controlled experiments

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

#### Where controlled experiments runs out

Experiments require sufficient samples, ethical limits, and careful metrics.

One unsolved mark remains on the weathered observation slate. None of the responsibilities inside Controlled Experiments can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the weathered observation slate

Rebuild the controlled experiments scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/069-controlled-experiments/README.md).*

---

### Excavation 070 — Bandits — Learning While Choosing

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning in the world and interpretability

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

The doors of the Living Watchgarden close against the wind. On the weathered observation slate, the field naturalist writes the cheapest rule that might still be true: always choose the currently best option.

The field naturalist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: an unlucky first result permanently hides a better alternative. The failure is stable enough to become evidence.

*The field naturalist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: always choose the currently best…
possible road B ─┘              └── loses: an unlucky first result permanently…

same roads ──▶ repaired map ──▶ reserve some choices for exploration…
```

Across the weathered observation slate, the old path and the repaired path run side by side. One carries “always choose the currently best option”; the other knows how to reserve some choices for exploration while exploiting accumulated evidence. When the failure—an unlucky first result permanently hides a better alternative—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to bandits. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: reserve some choices for exploration while exploiting accumulated evidence. This problem and its repair will travel under the name **Bandits**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—always choose the currently best option? The answer remains an unlucky first result permanently hides a better alternative. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

Before leaving the weathered observation slate, the field naturalist tests the new idea backward. Remove the ability to reserve some choices for exploration while exploiting accumulated evidence, and the method falls back to this tempting instruction: always choose the currently best option. The old consequence returns—an unlucky first result permanently hides a better alternative. Restore the missing ability and that particular contradiction disappears. This reversible test is why bandits belongs to the growing structure rather than to a list of facts to memorize.

#### Learning While Choosing

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

#### Where bandits runs out

Exploration has real cost and can be unacceptable for high-risk actions.

The bandits repair holds, but the world asks for something it was never given. At the Living Watchgarden, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the weathered observation slate

Rebuild the bandits scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/070-bandits/README.md).*

---

### Excavation 071 — Features Inside Networks

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning in the world and interpretability

Bandit strategies balance present reward with the value of exploring uncertain choices. Once deployed, their decisions still emerge from internal representations whose meaning and failure modes remain hidden.

Nothing in the Living Watchgarden yet bears today's mathematical name. There is only the field naturalist, the weathered observation slate, and one plausible action: search for one neuron dedicated to each human concept.

At the edge of the weathered observation slate, the shortcut produces its consequence: the concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons. That consequence, not a textbook, earns the next move.

*The field naturalist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: search for one neuron dedicated to…
                         │
                         └── mismatch: the concept disappears when one…

reference evidence ──▶ measured repair: we need to treat representations as…
```

The field naturalist covers the new mark and the old contradiction returns: the concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons. The cover is lifted, restoring the ability to treat representations as distributed directions and test them across varied examples, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason features inside networks exists.

What must change for features inside networks is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to treat representations as distributed directions and test them across varied examples. That threshold is where **Features Inside Networks** enters the story.

The marks on the weathered observation slate form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. features inside networks is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Understanding features inside networks

Tiger and zebra activate overlapping patterns; subtracting ordinary cats isolates a stripe-related direction better than one cell.

#### Where features inside networks runs out

Human labels may not match the model’s internal abstractions.

Here the new path ends honestly. Features Inside Networks can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the weathered observation slate

Rebuild the features inside networks scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/071-features-inside-networks/README.md).*

---

### Excavation 072 — Linear Probes

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

At the Living Watchgarden, the field naturalist returns to the weathered observation slate. Yesterday's instrument still lies open, so the first move asks for no new magic: train a powerful classifier on hidden states and call any success evidence.

For a moment the mark looks complete. Then the evidence refuses to fit: the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The field naturalist sketches the break before changing it:*

```text
observation
    │
    ▼
[train a powerful classifier on hidden…]
    │
    ╳  the trouble appears immediately: the…
    │
    ▼
[use a deliberately limited probe and…]
```

The field naturalist lays two translucent sheets over the weathered observation slate. The first is inscribed, “train a powerful classifier on hidden states and call any success evidence.” Its path ends where the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. The second receives the same evidence but is allowed to use a deliberately limited probe and compare layers, controls, and baselines. Held to the light, the sheets separate at exactly one decision.

No one reaches for a linear probes formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The field naturalist changes only that one responsibility: use a deliberately limited probe and compare layers, controls, and baselines. When the ink dries, the name **Linear Probes** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The weathered observation slate keeps both histories. Its older mark still says, ‘train a powerful classifier on hidden states and call any success evidence’; beside it, the newer mark says, ‘use a deliberately limited probe and compare layers, controls, and baselines.’ The distance between those sentences is the exact shape of linear probes: no larger than the failure required, and no smaller than reality permits.

#### Understanding linear probes

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

#### Where linear probes runs out

Decodable information is not proof the model uses it.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Linear Probes has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the weathered observation slate

Rebuild the linear probes scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/072-linear-probes/README.md).*

---

### Excavation 073 — Attribution

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Learning in the world and interpretability

Linear probes reveal information available to a simple reader. To understand one prediction, we must trace which input evidence actually influenced the output rather than merely existing somewhere inside.

Morning reaches the Living Watchgarden before anyone has a name for today's difficulty. Beside the weathered observation slate, the field naturalist tries the smallest continuation of what already works: remove each word and treat output change as complete explanation.

The rule survives the easy cases. The next case leaves a crack through the middle of it: removing a word changes grammar and creates an unnatural new input. More confidence cannot repair information that never entered the rule.

*The field naturalist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   remove each word and treat output… removing a word changes grammar and…
            \        /
             \      /
              measure sensitivity with several…
```

Two trails now cross the weathered observation slate. The pale trail bears the instruction “remove each word and treat output change as complete explanation.” It disappears into the observed failure: removing a word changes grammar and creates an unnatural new input. The darker trail carries one additional capacity—to measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed attribution mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the weathered observation slate is altered in exactly one way: measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions. Much later, people will call this territory **Attribution**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the weathered observation slate. The failed path remains visible beneath the repair, because attribution is easier to remember when its scar remains attached to it. The scar reads, ‘removing a word changes grammar and creates an unnatural new input’; the new line exists only to keep that loss from happening again.

#### Understanding attribution

For “not dangerous,” attribution highlights not; replacing it with very changes the class as predicted.

#### Where attribution runs out

Attribution can be unstable and method-dependent.

The weathered observation slate answers today's question and falls silent at the next. That silence is precise: Attribution was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the weathered observation slate

Rebuild the attribution scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/073-attribution/README.md).*

---

### Excavation 074 — Superposition

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Information Theory](../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Learning in the world and interpretability

Attribution assigns influence to inputs or internal components. The investigation soon finds that one neuron can participate in many features and one feature can be distributed across many neurons.

The weathered observation slate at the Living Watchgarden still carries the marks of the previous discovery. The field naturalist follows them as far as they seem willing to go: demand one feature per coordinate.

Reality answers without terminology: limited width forces useful patterns to share neurons, producing confusing mixed activations. The weathered observation slate now holds two situations the old rule cannot keep apart.

*The field naturalist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ demand one feature per coordinate ──▶ limited width forces useful patterns…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ represent features as directions that… ──▶ accountable result
```

The weathered observation slate is divided down the middle. Left side: “demand one feature per coordinate.” Its final mark records limited width forces useful patterns to share neurons, producing confusing mixed activations. Right side: the same starting evidence, now allowed to represent features as directions that can overlap when they rarely need to be active together. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given superposition a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: represent features as directions that can overlap when they rarely need to be active together. The name **Superposition** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from superposition through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and limited width forces useful patterns to share neurons, producing confusing mixed activations. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

Before leaving the weathered observation slate, the field naturalist tests the new idea backward. Remove the ability to represent features as directions that can overlap when they rarely need to be active together, and the method falls back to this tempting instruction: demand one feature per coordinate. The old consequence returns—limited width forces useful patterns to share neurons, producing confusing mixed activations. Restore the missing ability and that particular contradiction disappears. This reversible test is why superposition belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding superposition

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

#### Where superposition runs out

Separating superposed features is difficult and may not yield unique answers.

A final test reaches beyond the new instrument. It does not refute Superposition; it reveals the edge of what was constructed. The field naturalist carries that edge into the following room.

#### Return to the weathered observation slate

Rebuild the superposition scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/074-superposition/README.md).*

---

### Excavation 075 — Causal Interventions

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Learning in the world and interpretability

Superposition explains how limited dimensions can carry more features than individual neurons. A readable direction may still be a bystander; only changing it and observing behavior can test whether it is causally used.

Night gathers around the Living Watchgarden. Under the light of the weathered observation slate, the field naturalist refuses to invent prematurely and begins with the plain rule: assume correlation with output proves causation.

Then the quiet test arrives: the direction predicts answers but changing it leaves behavior unchanged. What looked like simplicity is revealed as a missing distinction.

*The field naturalist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ assume correlation with output proves… ──▶ blurred: the direction predicts answers but…
      │
      └── new lens ──▶ we need to intervene on the… ──▶ distinction survives
```

The field naturalist turns the weathered observation slate toward the light. Through the old engraving, assume correlation with output proves causation, the evidence ends in the same contradiction: the direction predicts answers but changing it leaves behavior unchanged. A second engraving adds only the power to intervene on the representation and measure the specific downstream change against controls. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The field naturalist circles the place where the two causal interventions cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to intervene on the representation and measure the specific downstream change against controls. The field naturalist writes **Causal Interventions** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The field naturalist places a finger over the new distinction. At once the two cases collapse and the direction predicts answers but changing it leaves behavior unchanged. Lifting the finger restores only this capacity: intervene on the representation and measure the specific downstream change against controls. That tiny reversible motion is the chapter's proof of necessity.

#### Understanding causal interventions

Adding the candidate direction raises tiger probability only in relevant contexts; random directions do not.

#### Where causal interventions runs out

Interventions can create unnatural internal states.

One unsolved mark remains on the weathered observation slate. None of the responsibilities inside Causal Interventions can move it, and so it becomes the observation from which the next excavation must begin.

#### The garden looks back at the watcher

Deployment changed the data that trained the system. Experiments separated cause from coincidence; probes found readable traces; interventions asked which traces actually mattered. The observer has entered the observed world.

```text
action ↺ world → data → representation → intervention → evidence
```

The trail called *the garden looks back at the watcher* is what remains when one necessity becomes another.

#### Return to the weathered observation slate

Rebuild the causal interventions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/075-causal-interventions/README.md).*

---

## Part VIII — Seeing and Creating

Language is only one trace of the valley. Cameras bring grids of colored light, and the assistant cannot understand them by pretending they are sentences. We begin again from the observation itself, then reuse the deeper principles already earned: locality, hierarchy, attention, compression, and gradual generation.

---

### Excavation 076 — Pixels — Turning Light into Numbers

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.

Inside the Glass Menagerie, every old tool is given one honest chance. The maker of seeing-machines sets the wall of illuminated tiles between the evidence and the desired answer, then tries to assign one label to the entire raw byte sequence.

The maker of seeing-machines repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: a one-pixel shift changes thousands of byte positions although the same tiger remains. The failure is stable enough to become evidence.

*The maker of seeing-machines sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: assign one label to the entire raw…
                         │
                         └── mismatch: a one-pixel shift changes thousands…

reference evidence ──▶ measured repair: preserve local spatial arrangement…
```

Across the wall of illuminated tiles, the old path and the repaired path run side by side. One carries “assign one label to the entire raw byte sequence”; the other knows how to preserve local spatial arrangement and compare nearby color measurements. When the failure—a one-pixel shift changes thousands of byte positions although the same tiger remains—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to pixels. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: preserve local spatial arrangement and compare nearby color measurements. This problem and its repair will travel under the name **Pixels**, but the name carries no knowledge the scene has not earned.

What changed on the wall of illuminated tiles can be said without symbols. Before, the method could only assign one label to the entire raw byte sequence; now it can also preserve local spatial arrangement and compare nearby color measurements. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it. The Glass Menagerie returns to the valley's geometry at a finer scale. pixels asks which nearby lights belong together, how small patterns compose into larger ones, and which transformations preserve identity while appearance changes. Seeing is measurement arranged across space.

#### Turning Light into Numbers

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

#### Where pixels runs out

Pixels depend on lighting, sensor, scale, and viewpoint.

The pixels repair holds, but the world asks for something it was never given. At the Glass Menagerie, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the wall of illuminated tiles

Rebuild the pixels scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/076-pixels/README.md).*

---

### Excavation 077 — Convolution — Reusing the Same Local Detector

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

A new case arrives at the Glass Menagerie, but the maker of seeing-machines first reaches for the familiar wall of illuminated tiles. Its promise is simple: learn a separate edge detector for every location.

At the edge of the wall of illuminated tiles, the shortcut produces its consequence: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. That consequence, not a textbook, earns the next move.

*The maker of seeing-machines sketches the break before changing it:*

```text
observation
    │
    ▼
[learn a separate edge detector for…]
    │
    ╳  the trouble appears immediately: the…
    │
    ▼
[slide one small learned filter across…]
```

The maker of seeing-machines covers the new mark and the old contradiction returns: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. The cover is lifted, restoring the ability to slide one small learned filter across all positions and reuse its weights, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason convolution exists.

What must change for convolution is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: slide one small learned filter across all positions and reuse its weights. That threshold is where **Convolution** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In convolution, that memory takes a precise form: whenever the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves, preserve enough structure to slide one small learned filter across all positions and reuse its weights.

#### Reusing the Same Local Detector

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

#### The calculation hidden inside convolution

The maker of seeing-machines carries the convolution scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

The signal values are neighboring brightness measurements.
The kernel values are the same small detector reused at every location.
Multiplication measures how each local measurement agrees with its detector weight.
Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

##### Why the melody needs these exact notes

[Each multiplication](../MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
[The sum](../MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
[i+j](../MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they form the smallest mechanism that survives the counterexample.

The wall of illuminated tiles already contains the complete convolution mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

#### Where convolution runs out

Convolution assumes useful locality and translation reuse.

Here the new path ends honestly. Convolution can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the wall of illuminated tiles

Rebuild the convolution scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/077-convolution/README.md).*

---

### Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

The doors of the Glass Menagerie close against the wind. On the wall of illuminated tiles, the maker of seeing-machines writes the cheapest rule that might still be true: keep every activation at full resolution through every layer.

For a moment the mark looks complete. Then the evidence refuses to fit: memory explodes and tiny shifts move evidence to neighboring cells. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The maker of seeing-machines sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   keep every activation at full… memory explodes and tiny shifts move…
            \        /
             \      /
              summarize small neighborhoods while…
```

The maker of seeing-machines lays two translucent sheets over the wall of illuminated tiles. The first is inscribed, “keep every activation at full resolution through every layer.” Its path ends where memory explodes and tiny shifts move evidence to neighboring cells. The second receives the same evidence but is allowed to summarize small neighborhoods while retaining the strongest or average evidence. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pooling formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The maker of seeing-machines changes only that one responsibility: summarize small neighborhoods while retaining the strongest or average evidence. When the ink dries, the name **Pooling** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because memory explodes and tiny shifts move evidence to neighboring cells, while the other can summarize small neighborhoods while retaining the strongest or average evidence. That fork—not the vocabulary—is where pooling lives.

#### Keeping Evidence While Shrinking the Map

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

#### Where pooling runs out

Pooling discards exact location and can erase subtle patterns.

At the Glass Menagerie, the maker of seeing-machines leaves a blank beneath the new mark. Pooling has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the wall of illuminated tiles

Rebuild the pooling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/078-pooling/README.md).*

---

### Excavation 079 — CNN Hierarchies

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.

Nothing in the Glass Menagerie yet bears today's mathematical name. There is only the maker of seeing-machines, the wall of illuminated tiles, and one plausible action: classify directly from isolated edge responses.

The rule survives the easy cases. The next case leaves a crack through the middle of it: one edge has no object-level meaning. More confidence cannot repair information that never entered the rule.

*The maker of seeing-machines sketches the break before changing it:*

```text
OLD PATH:  request ──▶ classify directly from isolated edge… ──▶ one edge has no object-level meaning
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ we need to stack local detectors so… ──▶ accountable result
```

Two trails now cross the wall of illuminated tiles. The pale trail bears the instruction “classify directly from isolated edge responses.” It disappears into the observed failure: one edge has no object-level meaning. The darker trail carries one additional capacity—to stack local detectors so later layers combine earlier patterns over wider regions. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed cnn hierarchies mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the wall of illuminated tiles is altered in exactly one way: we need to stack local detectors so later layers combine earlier patterns over wider regions. Much later, people will call this territory **CNN Hierarchies**. Here the name is only a memory of the failure it can survive.

The wall of illuminated tiles has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and cnn hierarchies looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

Before leaving the wall of illuminated tiles, the maker of seeing-machines tests the new idea backward. Remove the ability to stack local detectors so later layers combine earlier patterns over wider regions, and the method falls back to this tempting instruction: classify directly from isolated edge responses. The old consequence returns—one edge has no object-level meaning. Restore the missing ability and that particular contradiction disappears. This reversible test is why cnn hierarchies belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding cnn hierarchies

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

#### Where cnn hierarchies runs out

The hierarchy is learned, not guaranteed to match human parts.

The wall of illuminated tiles answers today's question and falls silent at the next. That silence is precise: CNN Hierarchies was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the wall of illuminated tiles

Rebuild the cnn hierarchies scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/079-cnn-hierarchy/README.md).*

---

### Excavation 080 — Vision Transformers

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

At the Glass Menagerie, the maker of seeing-machines returns to the wall of illuminated tiles. Yesterday's instrument still lies open, so the first move asks for no new magic: treat every pixel as a token.

Reality answers without terminology: the sequence becomes enormous and individual pixels carry little stable structure. The wall of illuminated tiles now holds two situations the old rule cannot keep apart.

*The maker of seeing-machines sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ treat every pixel as a token ──▶ blurred: the sequence becomes enormous and…
      │
      └── new lens ──▶ group pixels into patches, embed them… ──▶ distinction survives
```

The wall of illuminated tiles is divided down the middle. Left side: “treat every pixel as a token.” Its final mark records the sequence becomes enormous and individual pixels carry little stable structure. Right side: the same starting evidence, now allowed to group pixels into patches, embed them as tokens, add position, and apply attention. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given vision transformers a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: group pixels into patches, embed them as tokens, add position, and apply attention. The name **Vision Transformers** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to treat every pixel as a token; on the other lies the observed fact that the sequence becomes enormous and individual pixels carry little stable structure. The bridge called vision transformers has exactly the planks needed to group pixels into patches, embed them as tokens, add position, and apply attention.

#### Understanding vision transformers

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

#### Where vision transformers runs out

Patch size trades detail for cost and needs substantial data.

A final test reaches beyond the new instrument. It does not refute Vision Transformers; it reveals the edge of what was constructed. The maker of seeing-machines carries that edge into the following room.

#### Return to the wall of illuminated tiles

Rebuild the vision transformers scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/080-vision-transformers/README.md).*

---

### Excavation 081 — Autoencoders — Compressing and Rebuilding

> **Mathematical roots:** [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Vision and generative models

Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.

Morning reaches the Glass Menagerie before anyone has a name for today's difficulty. Beside the wall of illuminated tiles, the maker of seeing-machines tries the smallest continuation of what already works: copy the input through an unrestricted hidden layer.

Then the quiet test arrives: a wide hidden layer learns identity without compression. What looked like simplicity is revealed as a missing distinction.

*The maker of seeing-machines sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: copy the input through an…
possible road B ─┘              └── loses: a wide hidden layer learns identity…

same roads ──▶ repaired map ──▶ force information through a…
```

The maker of seeing-machines turns the wall of illuminated tiles toward the light. Through the old engraving, copy the input through an unrestricted hidden layer, the evidence ends in the same contradiction: a wide hidden layer learns identity without compression. A second engraving adds only the power to force information through a bottleneck and train reconstruction. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The maker of seeing-machines circles the place where the two autoencoders cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: force information through a bottleneck and train reconstruction. The maker of seeing-machines writes **Autoencoders** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The maker of seeing-machines does not memorize autoencoders. Instead, the maker of seeing-machines memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can force information through a bottleneck and train reconstruction. The formal name merely lets that motion be shared.

Before leaving the wall of illuminated tiles, the maker of seeing-machines tests the new idea backward. Remove the ability to force information through a bottleneck and train reconstruction, and the method falls back to this tempting instruction: copy the input through an unrestricted hidden layer. The old consequence returns—a wide hidden layer learns identity without compression. Restore the missing ability and that particular contradiction disappears. This reversible test is why autoencoders belongs to the growing structure rather than to a list of facts to memorize.

#### Compressing and Rebuilding

Four correlated measurements compress to two codes that still rebuild the originals approximately.

#### Where autoencoders runs out

Good reconstruction may preserve details irrelevant to downstream meaning.

One unsolved mark remains on the wall of illuminated tiles. None of the responsibilities inside Autoencoders can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the wall of illuminated tiles

Rebuild the autoencoders scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/081-autoencoders/README.md).*

---

### Excavation 082 — Latent Space — Coordinates for Hidden Causes

> **Mathematical roots:** [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Vision and generative models

An autoencoder learns to compress and reconstruct. Its bottleneck is only a list of numbers until changes in those coordinates correspond to useful hidden causes such as pose, lighting, or identity.

The wall of illuminated tiles at the Glass Menagerie still carries the marks of the previous discovery. The maker of seeing-machines follows them as far as they seem willing to go: assume any compressed coordinates form a smooth useful space.

The maker of seeing-machines repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the trouble appears immediately: tiny code changes can cause abrupt unrelated outputs. The failure is stable enough to become evidence.

*The maker of seeing-machines sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: assume any compressed coordinates…
                         │
                         └── mismatch: the trouble appears immediately: tiny…

reference evidence ──▶ measured repair: shape the latent distribution and…
```

Across the wall of illuminated tiles, the old path and the repaired path run side by side. One carries “assume any compressed coordinates form a smooth useful space”; the other knows how to shape the latent distribution and train nearby codes to decode coherently. When the failure—the trouble appears immediately: tiny code changes can cause abrupt unrelated outputs—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to latent space. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: shape the latent distribution and train nearby codes to decode coherently. This problem and its repair will travel under the name **Latent Space**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—assume any compressed coordinates form a smooth useful space? The answer remains the trouble appears immediately: tiny code changes can cause abrupt unrelated outputs. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Coordinates for Hidden Causes

Moving one latent coordinate gradually changes image brightness while another changes pose.

#### Where latent space runs out

Latent directions need not be independent or human-readable.

The latent space repair holds, but the world asks for something it was never given. At the Glass Menagerie, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the wall of illuminated tiles

Rebuild the latent space scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/082-latent-space/README.md).*

---

### Excavation 083 — Autoregressive Generation Beyond Text

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

A meaningful latent space gives images coordinates we can navigate. To create a new image, the system still needs a procedure that turns an uncertain starting state into a complete arrangement of pixels.

Night gathers around the Glass Menagerie. Under the light of the wall of illuminated tiles, the maker of seeing-machines refuses to invent prematurely and begins with the plain rule: predict all pixels independently.

At the edge of the wall of illuminated tiles, the shortcut produces its consequence: independent pixels produce noise because neighboring colors and shapes constrain one another. That consequence, not a textbook, earns the next move.

*The maker of seeing-machines sketches the break before changing it:*

```text
observation
    │
    ▼
[predict all pixels independently]
    │
    ╳  independent pixels produce noise…
    │
    ▼
[we need to choose an order and…]
```

The maker of seeing-machines covers the new mark and the old contradiction returns: independent pixels produce noise because neighboring colors and shapes constrain one another. The cover is lifted, restoring the ability to choose an order and predict each piece from previously generated pieces, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason autoregressive generation beyond text exists.

What must change for autoregressive generation beyond text is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to choose an order and predict each piece from previously generated pieces. That threshold is where **Autoregressive Generation Beyond Text** enters the story.

The marks on the wall of illuminated tiles form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. autoregressive generation beyond text is not any single point. It is the path connecting them in the only order that makes the last point necessary.

Before leaving the wall of illuminated tiles, the maker of seeing-machines tests the new idea backward. Remove the ability to choose an order and predict each piece from previously generated pieces, and the method falls back to this tempting instruction: predict all pixels independently. The old consequence returns—independent pixels produce noise because neighboring colors and shapes constrain one another. Restore the missing ability and that particular contradiction disappears. This reversible test is why autoregressive generation beyond text belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding autoregressive generation beyond text

After generating sky pixels, the model gives blue neighbors higher probability.

#### Where autoregressive generation beyond text runs out

Sequential generation can be slow and ordering introduces bias.

Here the new path ends honestly. Autoregressive Generation Beyond Text can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the wall of illuminated tiles

Rebuild the autoregressive generation beyond text scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/083-autoregressive-generation/README.md).*

---

### Excavation 084 — Diffusion — Learning by Destroying

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

Inside the Glass Menagerie, every old tool is given one honest chance. The maker of seeing-machines sets the wall of illuminated tiles between the evidence and the desired answer, then tries to map one random vector directly to a finished image in one jump.

For a moment the mark looks complete. Then the evidence refuses to fit: one enormous jump is difficult to learn and unstable across diverse images. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The maker of seeing-machines sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   map one random vector directly to a… one enormous jump is difficult to…
            \        /
             \      /
              gradually add noise to real images,…
```

The maker of seeing-machines lays two translucent sheets over the wall of illuminated tiles. The first is inscribed, “map one random vector directly to a finished image in one jump.” Its path ends where one enormous jump is difficult to learn and unstable across diverse images. The second receives the same evidence but is allowed to gradually add noise to real images, then learn the smaller reverse step at every noise level. Held to the light, the sheets separate at exactly one decision.

No one reaches for a diffusion formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The maker of seeing-machines changes only that one responsibility: gradually add noise to real images, then learn the smaller reverse step at every noise level. When the ink dries, the name **Diffusion** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The wall of illuminated tiles keeps both histories. Its older mark still says, ‘map one random vector directly to a finished image in one jump’; beside it, the newer mark says, ‘gradually add noise to real images, then learn the smaller reverse step at every noise level.’ The distance between those sentences is the exact shape of diffusion: no larger than the failure required, and no smaller than reality permits.

#### Learning by Destroying

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

#### The calculation hidden inside diffusion

The maker of seeing-machines carries the diffusion scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

The clean image is the named tiger image x0.
Noise ε is the random corruption added during the forward process.
The retained clean fraction and noise fraction change with step t.
Square roots scale amplitudes so their variances combine as intended.

##### Why the melody needs these exact notes

[The two multiplications](../MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
[Addition](../MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
[Square roots of the variance shares](../MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Inside diffusion, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the joining river**—separate contributions meet without losing where they came from; and **the road home**—a squared construction returns to the scale of the world that created it. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for diffusion is now visible on the wall of illuminated tiles. The symbols do not add an idea; they bind the discovered moves into one line:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

#### Where diffusion runs out

Many denoising steps make sampling expensive.

At the Glass Menagerie, the maker of seeing-machines leaves a blank beneath the new mark. Diffusion has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the wall of illuminated tiles

Rebuild the diffusion scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/084-diffusion/README.md).*

---

### Excavation 085 — Denoising — Predicting What the Noise Hid

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

A new case arrives at the Glass Menagerie, but the maker of seeing-machines first reaches for the familiar wall of illuminated tiles. Its promise is simple: ask it to recreate the entire clean image directly from every noise level.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the task changes dramatically across noise strengths. More confidence cannot repair information that never entered the rule.

*The maker of seeing-machines sketches the break before changing it:*

```text
OLD PATH:  request ──▶ ask it to recreate the entire clean… ──▶ the task changes dramatically across…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ tell the model the noise level and… ──▶ accountable result
```

Two trails now cross the wall of illuminated tiles. The pale trail bears the instruction “ask it to recreate the entire clean image directly from every noise level.” It disappears into the observed failure: the task changes dramatically across noise strengths. The darker trail carries one additional capacity—to tell the model the noise level and predict the added noise or equivalent clean direction. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed denoising mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the wall of illuminated tiles is altered in exactly one way: tell the model the noise level and predict the added noise or equivalent clean direction. Much later, people will call this territory **Denoising**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the wall of illuminated tiles. The failed path remains visible beneath the repair, because denoising is easier to remember when its scar remains attached to it. The scar reads, ‘the task changes dramatically across noise strengths’; the new line exists only to keep that loss from happening again.

#### Predicting What the Noise Hid

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

#### The calculation hidden inside denoising

The maker of seeing-machines carries the denoising scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

xt is the noisy image already constructed in the example.
t tells the network how much corruption it faces.
The network predicts the exact noise ε that hid the clean image.
Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

##### Why the melody needs these exact notes

[Subtracting predicted noise from actual noise](../MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
[The squared norm](../MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
[Expectation](../MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Together they form the smallest mechanism that survives the counterexample.

The maker of seeing-machines reads the journey of denoising once more across the wall of illuminated tiles, then lets the words contract without losing their order:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

#### Where denoising runs out

Prediction parameterization and schedule affect stability and quality.

The wall of illuminated tiles answers today's question and falls silent at the next. That silence is precise: Denoising was built to repair one failure, not to pretend every later boundary is already solved.

#### Light learns a path home

Pixels became neighborhoods, neighborhoods became parts, parts became objects, and compressed coordinates became places from which images could be rebuilt. Diffusion completed the arc by turning destruction into a curriculum for creation.

```text
light → locality → hierarchy → latent space → noise → image
```

The trail called *light learns a path home* is what remains when one necessity becomes another.

#### Return to the wall of illuminated tiles

Rebuild the denoising scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/085-denoising/README.md).*

---

## Part IX — Acting and Scaling

The system can describe and create, but action supplies no correct next token. It supplies consequences. We follow that new kind of evidence from rewards and future value through multimodal alignment, efficient adaptation, large-scale training, live service, adversarial testing, and governance.

---

### Excavation 086 — Rewards — Learning Without Correct Answers

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Denoising closes the image-generation loop. The field system can predict words and images, but an acting agent often receives no correct action label—only eventual success, damage, or failure.

The doors of the Road of Consequences close against the wind. On the map of branching journeys, the expedition leader writes the cheapest rule that might still be true: label the correct action at every moment.

Reality answers without terminology: for exploration or games, nobody knows every correct intermediate move. The map of branching journeys now holds two situations the old rule cannot keep apart.

*The expedition leader sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: label the correct action at every…
possible road B ─┘              └── loses: for exploration or games, nobody…

same roads ──▶ repaired map ──▶ provide outcome feedback and let…
```

The map of branching journeys is divided down the middle. Left side: “label the correct action at every moment.” Its final mark records for exploration or games, nobody knows every correct intermediate move. Right side: the same starting evidence, now allowed to provide outcome feedback and let experience connect actions with later consequences. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given rewards a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: provide outcome feedback and let experience connect actions with later consequences. The name **Rewards** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from rewards through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and for exploration or games, nobody knows every correct intermediate move. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction. Along the Road of Consequences, rewards combines two old languages: probability for futures that may occur and value for consequences that matter if they do. An action is therefore not a label; it is an arrow cast into a branching world.

#### Learning Without Correct Answers

A maze gives +1 only at the exit; repeated trials reveal which earlier turns tend to reach it.

#### Where rewards runs out

Poor rewards create unintended shortcuts.

A final test reaches beyond the new instrument. It does not refute Rewards; it reveals the edge of what was constructed. The expedition leader carries that edge into the following room.

#### Return to the map of branching journeys

Rebuild the rewards scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/086-rewards/README.md).*

---

### Excavation 087 — States, Actions, and Transitions

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

Nothing in the Road of Consequences yet bears today's mathematical name. There is only the expedition leader, the map of branching journeys, and one plausible action: store only action and final reward.

Then the quiet test arrives: the trouble appears immediately: the same action helps in one situation and harms in another. What looked like simplicity is revealed as a missing distinction.

*The expedition leader sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: store only action and final reward
                         │
                         └── mismatch: the trouble appears immediately: the…

reference evidence ──▶ measured repair: we need to record current state,…
```

The expedition leader turns the map of branching journeys toward the light. Through the old engraving, store only action and final reward, the evidence ends in the same contradiction: the trouble appears immediately: the same action helps in one situation and harms in another. A second engraving adds only the power to record current state, chosen action, reward, and resulting state. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The expedition leader circles the place where the two states, actions, and transitions cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to record current state, chosen action, reward, and resulting state. The expedition leader writes **States, Actions, and Transitions** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The expedition leader places a finger over the new distinction. At once the two cases collapse and the trouble appears immediately: the same action helps in one situation and harms in another. Lifting the finger restores only this capacity: record current state, chosen action, reward, and resulting state. That tiny reversible motion is the chapter's proof of necessity.

#### Understanding states, actions, and transitions

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

#### Where states, actions, and transitions runs out

A state representation may omit information needed for future decisions.

One unsolved mark remains on the map of branching journeys. None of the responsibilities inside States, Actions, and Transitions can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the map of branching journeys

Rebuild the states, actions, and transitions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/087-states-actions-transitions/README.md).*

---

### Excavation 088 — Value — Estimating Future Consequences

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

State–action–transition records make experience explicit. Immediate reward still cannot distinguish a move toward a distant rescue from a move into a dead end when neither pays off yet.

At the Road of Consequences, the expedition leader returns to the map of branching journeys. Yesterday's instrument still lies open, so the first move asks for no new magic: choose the action with the largest reward right now.

The expedition leader repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: a small immediate treat can prevent reaching a larger later reward. The failure is stable enough to become evidence.

*The expedition leader sketches the break before changing it:*

```text
observation
    │
    ▼
[choose the action with the largest…]
    │
    ╳  a small immediate treat can prevent…
    │
    ▼
[estimate the future reward expected…]
```

Across the map of branching journeys, the old path and the repaired path run side by side. One carries “choose the action with the largest reward right now”; the other knows how to estimate the future reward expected from a state or state-action pair. When the failure—a small immediate treat can prevent reaching a larger later reward—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to value. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: estimate the future reward expected from a state or state-action pair. This problem and its repair will travel under the name **Value**, but the name carries no knowledge the scene has not earned.

What changed on the map of branching journeys can be said without symbols. Before, the method could only choose the action with the largest reward right now; now it can also estimate the future reward expected from a state or state-action pair. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

Before leaving the map of branching journeys, the expedition leader tests the new idea backward. Remove the ability to estimate the future reward expected from a state or state-action pair, and the method falls back to this tempting instruction: choose the action with the largest reward right now. The old consequence returns—a small immediate treat can prevent reaching a larger later reward. Restore the missing ability and that particular contradiction disappears. This reversible test is why value belongs to the growing structure rather than to a list of facts to memorize.

#### Estimating Future Consequences

One path gives 1 now; another gives 0 now and 10 next. Future value makes the second preferable.

#### Where value runs out

Value estimates inherit errors from limited experience.

The value repair holds, but the world asks for something it was never given. At the Road of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the map of branching journeys

Rebuild the value scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/088-value-functions/README.md).*

---

### Excavation 089 — Q-Learning — Improving Values from Experience

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

Morning reaches the Road of Consequences before anyone has a name for today's difficulty. Beside the map of branching journeys, the expedition leader tries the smallest continuation of what already works: replace its value with the immediate reward.

At the edge of the map of branching journeys, the shortcut produces its consequence: the update ignores the valuable state reached afterward. That consequence, not a textbook, earns the next move.

*The expedition leader sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   replace its value with the immediate… the update ignores the valuable state…
            \        /
             \      /
              move the estimate toward reward plus…
```

The expedition leader covers the new mark and the old contradiction returns: the update ignores the valuable state reached afterward. The cover is lifted, restoring the ability to move the estimate toward reward plus the best discounted value available next, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason q-learning exists.

What must change for q-learning is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: move the estimate toward reward plus the best discounted value available next. That threshold is where **Q-Learning** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In q-learning, that memory takes a precise form: whenever the update ignores the valuable state reached afterward, preserve enough structure to move the estimate toward reward plus the best discounted value available next.

#### Improving Values from Experience

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

#### The calculation hidden inside q-learning

The expedition leader carries the q-learning scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

The immediate reward is what happened now.
The largest next-state Q value represents the best continuation currently known.
Discount γ reduces distant evidence and keeps unending sums bounded.
Adding immediate and discounted future reward creates the target the old estimate moves toward.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
[γ scales future value](../MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
[Max](../MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

The calculation borrows several gestures already encountered elsewhere: **the joining river**—separate contributions meet without losing where they came from; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the highest lantern**—the strongest surviving possibility sets the visible ceiling. q-learning feels new because the objects are new; the gestures remain recognizably human.

The map of branching journeys already contains the complete q-learning mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

#### Where q-learning runs out

Maximization can overestimate noisy actions and offline data limits safe exploration.

Here the new path ends honestly. Q-Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the map of branching journeys

Rebuild the q-learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/089-q-learning/README.md).*

---

### Excavation 090 — Policy Gradients — Improving the Choices Directly

> **Mathematical roots:** [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

The map of branching journeys at the Road of Consequences still carries the marks of the previous discovery. The expedition leader follows them as far as they seem willing to go: always choose the highest estimated action.

For a moment the mark looks complete. Then the evidence refuses to fit: early errors remove exploration and discrete choice blocks ordinary differentiation. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The expedition leader sketches the break before changing it:*

```text
OLD PATH:  request ──▶ always choose the highest estimated… ──▶ early errors remove exploration and…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ sample from a policy and increase… ──▶ accountable result
```

The expedition leader lays two translucent sheets over the map of branching journeys. The first is inscribed, “always choose the highest estimated action.” Its path ends where early errors remove exploration and discrete choice blocks ordinary differentiation. The second receives the same evidence but is allowed to sample from a policy and increase probability of actions followed by better-than-expected returns. Held to the light, the sheets separate at exactly one decision.

No one reaches for a policy gradients formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The expedition leader changes only that one responsibility: sample from a policy and increase probability of actions followed by better-than-expected returns. When the ink dries, the name **Policy Gradients** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because early errors remove exploration and discrete choice blocks ordinary differentiation, while the other can sample from a policy and increase probability of actions followed by better-than-expected returns. That fork—not the vocabulary—is where policy gradients lives.

#### Improving the Choices Directly

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

#### The calculation hidden inside policy gradients

The expedition leader carries the policy gradients scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

The sampled action probability comes from policy πθ.
Its log converts repeated action probabilities into additive learning signals.
Return G says how the chosen action eventually turned out.
The gradient changes θ in the direction that makes above-average rewarded actions more likely.

##### Why the melody needs these exact notes

[The policy log](../MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
[Multiplying by return G](../MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
[Expectation](../MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Three old motions cast new shadows here: **the spiral stair**—compounded chances become steps that can be accumulated; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for policy gradients is now visible on the map of branching journeys. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

#### Where policy gradients runs out

Policy gradients are noisy and can exploit reward flaws.

At the Road of Consequences, the expedition leader leaves a blank beneath the new mark. Policy Gradients has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the map of branching journeys

Rebuild the policy gradients scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/090-policy-gradients/README.md).*

---

### Excavation 091 — Multimodal Alignment

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Policy gradients let consequences reshape action probabilities. The field system's words, images, and actions still live in separate representational worlds unless paired observations can teach them to meet.

Night gathers around the Road of Consequences. Under the light of the map of branching journeys, the expedition leader refuses to invent prematurely and begins with the plain rule: compare raw pixels directly with token IDs.

The rule survives the easy cases. The next case leaves a crack through the middle of it: their coordinates have unrelated meanings and shapes. More confidence cannot repair information that never entered the rule.

*The expedition leader sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ compare raw pixels directly with… ──▶ blurred: their coordinates have unrelated…
      │
      └── new lens ──▶ we need to use separate encoders and… ──▶ distinction survives
```

Two trails now cross the map of branching journeys. The pale trail bears the instruction “compare raw pixels directly with token IDs.” It disappears into the observed failure: their coordinates have unrelated meanings and shapes. The darker trail carries one additional capacity—to use separate encoders and train paired image-text examples to become nearby. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed multimodal alignment mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the map of branching journeys is altered in exactly one way: we need to use separate encoders and train paired image-text examples to become nearby. Much later, people will call this territory **Multimodal Alignment**. Here the name is only a memory of the failure it can survive.

The map of branching journeys has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and multimodal alignment looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

Before leaving the map of branching journeys, the expedition leader tests the new idea backward. Remove the ability to use separate encoders and train paired image-text examples to become nearby, and the method falls back to this tempting instruction: compare raw pixels directly with token IDs. The old consequence returns—their coordinates have unrelated meanings and shapes. Restore the missing ability and that particular contradiction disappears. This reversible test is why multimodal alignment belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding multimodal alignment

A tiger photo and “striped big cat” move together; mismatched captions move apart.

#### Where multimodal alignment runs out

Pairs can contain weak, biased, or incomplete descriptions.

The map of branching journeys answers today's question and falls silent at the next. That silence is precise: Multimodal Alignment was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the map of branching journeys

Rebuild the multimodal alignment scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/091-multimodal-alignment/README.md).*

---

### Excavation 092 — Contrastive Learning

> **Mathematical roots:** [Information Theory](../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

Inside the Road of Consequences, every old tool is given one honest chance. The expedition leader sets the map of branching journeys between the evidence and the desired answer, then tries to pull every observed pair together without negatives.

Reality answers without terminology: the trouble appears immediately: all representations can collapse to one point. The map of branching journeys now holds two situations the old rule cannot keep apart.

*The expedition leader sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: pull every observed pair together…
possible road B ─┘              └── loses: the trouble appears immediately: all…

same roads ──▶ repaired map ──▶ compare each true pair against…
```

The map of branching journeys is divided down the middle. Left side: “pull every observed pair together without negatives.” Its final mark records the trouble appears immediately: all representations can collapse to one point. Right side: the same starting evidence, now allowed to compare each true pair against mismatched alternatives in the same batch. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given contrastive learning a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: compare each true pair against mismatched alternatives in the same batch. The name **Contrastive Learning** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to pull every observed pair together without negatives; on the other lies the observed fact that the trouble appears immediately: all representations can collapse to one point. The bridge called contrastive learning has exactly the planks needed to compare each true pair against mismatched alternatives in the same batch.

#### Understanding contrastive learning

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

#### The calculation hidden inside contrastive learning

The expedition leader carries the contrastive learning scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

zi and ti are the matched image and text vectors.
Their dot product is the named alignment score.
Temperature T controls how sharply alternatives compete.
The denominator includes every candidate caption, preventing all examples from collapsing to one point.
The negative log penalizes the true pair when mismatches receive comparable scores.

##### Why the melody needs these exact notes

[Each dot product](../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
[Dividing by temperature](../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
[The denominator sum](../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
[Negative log](../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Inside contrastive learning, familiar operations return with stricter duties: **the meeting of arrows**—matching directions reinforce while opposing directions resist; **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the rising flame**—a small score difference becomes positive relative evidence. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the contrastive learning case on the map of branching journeys. We can finally trade the long route for its compact map:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

#### Where contrastive learning runs out

False negatives may actually describe the same concept.

A final test reaches beyond the new instrument. It does not refute Contrastive Learning; it reveals the edge of what was constructed. The expedition leader carries that edge into the following room.

#### Return to the map of branching journeys

Rebuild the contrastive learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/092-contrastive-learning/README.md).*

---

### Excavation 093 — Speech and Audio

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Contrastive learning creates that relative competition. Sound introduces another modality whose pressure waveform is long, continuous, and shifted in time even when a listener hears the same event.

A new case arrives at the Road of Consequences, but the expedition leader first reaches for the familiar map of branching journeys. Its promise is simple: treat every raw sample as an independent token.

Then the quiet test arrives: sequences are huge and local frequency structure is hidden. What looked like simplicity is revealed as a missing distinction.

*The expedition leader sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: treat every raw sample as an…
                         │
                         └── mismatch: sequences are huge and local…

reference evidence ──▶ measured repair: transform short windows into…
```

The expedition leader turns the map of branching journeys toward the light. Through the old engraving, treat every raw sample as an independent token, the evidence ends in the same contradiction: sequences are huge and local frequency structure is hidden. A second engraving adds only the power to transform short windows into time-frequency features, then model their sequence. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The expedition leader circles the place where the two speech and audio cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: transform short windows into time-frequency features, then model their sequence. The expedition leader writes **Speech and Audio** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The expedition leader does not memorize speech and audio. Instead, the expedition leader memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can transform short windows into time-frequency features, then model their sequence. The formal name merely lets that motion be shared.

Before leaving the map of branching journeys, the expedition leader tests the new idea backward. Remove the ability to transform short windows into time-frequency features, then model their sequence, and the method falls back to this tempting instruction: treat every raw sample as an independent token. The old consequence returns—sequences are huge and local frequency structure is hidden. Restore the missing ability and that particular contradiction disappears. This reversible test is why speech and audio belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding speech and audio

A whistle appears as sustained energy in one frequency band across several time windows.

#### Where speech and audio runs out

Spectrogram choices discard phase or fine timing.

One unsolved mark remains on the map of branching journeys. None of the responsibilities inside Speech and Audio can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the map of branching journeys

Rebuild the speech and audio scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/093-speech-audio/README.md).*

---

### Excavation 094 — Low-Rank Adaptation

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

The doors of the Road of Consequences close against the wind. On the map of branching journeys, the expedition leader writes the cheapest rule that might still be true: copy and fine-tune all parameters for every task.

The expedition leader repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: storage and training cost multiply, and the base model is harder to preserve. The failure is stable enough to become evidence.

*The expedition leader sketches the break before changing it:*

```text
observation
    │
    ▼
[copy and fine-tune all parameters for…]
    │
    ╳  storage and training cost multiply,…
    │
    ▼
[freeze the base and learn a small…]
```

Across the map of branching journeys, the old path and the repaired path run side by side. One carries “copy and fine-tune all parameters for every task”; the other knows how to freeze the base and learn a small low-rank correction to selected matrices. When the failure—storage and training cost multiply, and the base model is harder to preserve—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to low-rank adaptation. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: freeze the base and learn a small low-rank correction to selected matrices. This problem and its repair will travel under the name **Low-Rank Adaptation**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—copy and fine-tune all parameters for every task? The answer remains storage and training cost multiply, and the base model is harder to preserve. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Understanding low-rank adaptation

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

#### The calculation hidden inside low-rank adaptation

The expedition leader carries the low-rank adaptation scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

W is the frozen large matrix we refuse to duplicate.
A and B are the two narrow trainable matrices.
Their product BA creates a full-shaped correction while using far fewer values.
Addition preserves the base behavior and applies only the learned adaptation.

##### Why the melody needs these exact notes

[BA](../MATHEMATICAL_MOVES.md#multiplication) composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.
[Adding that correction to W](../MATHEMATICAL_MOVES.md#addition) preserves the pretrained base and treats adaptation as a change. [The prime on W](../MATHEMATICAL_MOVES.md#symbol-decorations) marks the adapted version; replacing W would discard the knowledge we intended to keep.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about low-rank adaptation and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
W^\prime=W+BA
$$

#### Where low-rank adaptation runs out

Low rank may be insufficient for large behavioral changes.

The low-rank adaptation repair holds, but the world asks for something it was never given. At the Road of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the map of branching journeys

Rebuild the low-rank adaptation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/094-lora/README.md).*

---

### Excavation 095 — Quantization

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

Nothing in the Road of Consequences yet bears today's mathematical name. There is only the expedition leader, the map of branching journeys, and one plausible action: round every weight aggressively without measuring effect.

At the edge of the map of branching journeys, the shortcut produces its consequence: small but important distinctions disappear and outputs degrade. That consequence, not a textbook, earns the next move.

*The expedition leader sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   round every weight aggressively… small but important distinctions…
            \        /
             \      /
              we need to map values to a limited…
```

The expedition leader covers the new mark and the old contradiction returns: small but important distinctions disappear and outputs degrade. The cover is lifted, restoring the ability to map values to a limited set of levels using calibrated scale and test sensitive layers, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason quantization exists.

What must change for quantization is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to map values to a limited set of levels using calibrated scale and test sensitive layers. That threshold is where **Quantization** enters the story.

The marks on the map of branching journeys form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. quantization is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Understanding quantization

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

#### The calculation hidden inside quantization

The expedition leader carries the quantization scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

Real weight w is divided by scale s to express it in integer-sized steps.
Rounding chooses the nearest allowed integer q.
Multiplying q by s reconstructs the approximate weight used in computation.
The scale is calibrated so important values fit the available integer range.

##### Why the melody needs these exact notes

[Dividing by scale s](../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
[Rounding](../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
[Multiplying q by s](../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Before the line is compressed, notice its recurring motions: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The map of branching journeys already contains the complete quantization mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

#### Where quantization runs out

Lower precision trades accuracy for efficiency and hardware support varies.

Here the new path ends honestly. Quantization can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the map of branching journeys

Rebuild the quantization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/095-quantization/README.md).*

---

### Excavation 096 — Distributed Training

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

At the Road of Consequences, the expedition leader returns to the map of branching journeys. Yesterday's instrument still lies open, so the first move asks for no new magic: let many machines train independent copies and combine them occasionally.

For a moment the mark looks complete. Then the evidence refuses to fit: their parameters drift and duplicated work wastes computation. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The expedition leader sketches the break before changing it:*

```text
OLD PATH:  request ──▶ let many machines train independent… ──▶ their parameters drift and duplicated…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ partition data or model work,… ──▶ accountable result
```

The expedition leader lays two translucent sheets over the map of branching journeys. The first is inscribed, “let many machines train independent copies and combine them occasionally.” Its path ends where their parameters drift and duplicated work wastes computation. The second receives the same evidence but is allowed to partition data or model work, synchronize required results, and preserve one coherent update. Held to the light, the sheets separate at exactly one decision.

No one reaches for a distributed training formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The expedition leader changes only that one responsibility: partition data or model work, synchronize required results, and preserve one coherent update. When the ink dries, the name **Distributed Training** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The map of branching journeys keeps both histories. Its older mark still says, ‘let many machines train independent copies and combine them occasionally’; beside it, the newer mark says, ‘partition data or model work, synchronize required results, and preserve one coherent update.’ The distance between those sentences is the exact shape of distributed training: no larger than the failure required, and no smaller than reality permits.

#### Understanding distributed training

Two workers compute gradients on different batches, average them, then apply the same update.

#### Where distributed training runs out

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

At the Road of Consequences, the expedition leader leaves a blank beneath the new mark. Distributed Training has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the map of branching journeys

Rebuild the distributed training scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/096-distributed-training/README.md).*

---

### Excavation 097 — Inference Serving

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

Morning reaches the Road of Consequences before anyone has a name for today's difficulty. Beside the map of branching journeys, the expedition leader tries the smallest continuation of what already works: run one request at a time on one full model.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. More confidence cannot repair information that never entered the rule.

*The expedition leader sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ run one request at a time on one full… ──▶ blurred: the trouble appears immediately:…
      │
      └── new lens ──▶ batch compatible requests, cache… ──▶ distinction survives
```

Two trails now cross the map of branching journeys. The pale trail bears the instruction “run one request at a time on one full model.” It disappears into the observed failure: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. The darker trail carries one additional capacity—to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed inference serving mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the map of branching journeys is altered in exactly one way: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Much later, people will call this territory **Inference Serving**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the map of branching journeys. The failed path remains visible beneath the repair, because inference serving is easier to remember when its scar remains attached to it. The scar reads, ‘the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues’; the new line exists only to keep that loss from happening again.

#### Understanding inference serving

Four prompts share one matrix operation while each retains separate token state.

#### Where inference serving runs out

Batching improves throughput but can worsen individual latency.

The map of branching journeys answers today's question and falls silent at the next. That silence is precise: Inference Serving was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the map of branching journeys

Rebuild the inference serving scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/097-inference-serving/README.md).*

---

### Excavation 098 — Red Teaming

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.

The map of branching journeys at the Road of Consequences still carries the marks of the previous discovery. The expedition leader follows them as far as they seem willing to go: evaluate only expected well-formed requests.

Reality answers without terminology: real users, attackers, and accidents find paths designers never listed. The map of branching journeys now holds two situations the old rule cannot keep apart.

*The expedition leader sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: evaluate only expected well-formed…
possible road B ─┘              └── loses: real users, attackers, and accidents…

same roads ──▶ repaired map ──▶ actively search for failures, record…
```

The map of branching journeys is divided down the middle. Left side: “evaluate only expected well-formed requests.” Its final mark records real users, attackers, and accidents find paths designers never listed. Right side: the same starting evidence, now allowed to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given red teaming a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. The name **Red Teaming** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from red teaming through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and real users, attackers, and accidents find paths designers never listed. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

Before leaving the map of branching journeys, the expedition leader tests the new idea backward. Remove the ability to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations, and the method falls back to this tempting instruction: evaluate only expected well-formed requests. The old consequence returns—real users, attackers, and accidents find paths designers never listed. Restore the missing ability and that particular contradiction disappears. This reversible test is why red teaming belongs to the growing structure rather than to a list of facts to memorize.

#### Understanding red teaming

A hidden instruction in a retrieved page bypasses a normal demo; the case becomes a permanent injection test.

#### Where red teaming runs out

No finite red team proves universal safety.

A final test reaches beyond the new instrument. It does not refute Red Teaming; it reveals the edge of what was constructed. The expedition leader carries that edge into the following room.

#### Return to the map of branching journeys

Rebuild the red teaming scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/098-red-teaming/README.md).*

---

### Excavation 099 — Governance — Who Decides and Who Is Accountable?

> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Red teaming discovers failures before ordinary traffic does. Deciding which risks are acceptable, who may approve deployment, and who is accountable cannot be delegated to the model being evaluated.

Night gathers around the Road of Consequences. Under the light of the map of branching journeys, the expedition leader refuses to invent prematurely and begins with the plain rule: let builders decide every acceptable use because they understand the system.

Then the quiet test arrives: affected users carry risks without authority, appeal, or visibility. What looked like simplicity is revealed as a missing distinction.

*The expedition leader sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: let builders decide every acceptable…
                         │
                         └── mismatch: affected users carry risks without…

reference evidence ──▶ measured repair: we need to define ownership, review,…
```

The expedition leader turns the map of branching journeys toward the light. Through the old engraving, let builders decide every acceptable use because they understand the system, the evidence ends in the same contradiction: affected users carry risks without authority, appeal, or visibility. A second engraving adds only the power to define ownership, review, documentation, incident response, user recourse, and deployment boundaries. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The expedition leader circles the place where the two governance cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries. The expedition leader writes **Governance** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The expedition leader places a finger over the new distinction. At once the two cases collapse and affected users carry risks without authority, appeal, or visibility. Lifting the finger restores only this capacity: define ownership, review, documentation, incident response, user recourse, and deployment boundaries. That tiny reversible motion is the chapter's proof of necessity.

#### Who Decides and Who Is Accountable

A lending model requires documented data, subgroup evaluation, human appeal, and a named owner before launch.

#### Where governance runs out

Governance can become paperwork unless tied to real authority and enforcement.

One unsolved mark remains on the map of branching journeys. None of the responsibilities inside Governance can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the map of branching journeys

Rebuild the governance scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/099-governance/README.md).*

---

### Excavation 100 — The Complete AI System — From Observation to Responsible Action

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Governance assigns legitimate decisions and responsibility around the technology. We can finally assemble data, models, tools, evaluation, operations, and authority into one complete AI system rather than treating the model as the whole product.

Inside the Road of Consequences, every old tool is given one honest chance. The expedition leader sets the map of branching journeys between the evidence and the desired answer, then tries to connect every powerful component and call the result intelligent.

The expedition leader repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: an accurate model with stale data, excessive authority, weak verification, or no accountability still fails. The failure is stable enough to become evidence.

*The expedition leader sketches the break before changing it:*

```text
observation
    │
    ▼
[connect every powerful component and…]
    │
    ╳  an accurate model with stale data,…
    │
    ▼
[build one observable loop where…]
```

Across the map of branching journeys, the old path and the repaired path run side by side. One carries “connect every powerful component and call the result intelligent”; the other knows how to build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another. When the failure—an accurate model with stale data, excessive authority, weak verification, or no accountability still fails—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to complete ai system. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another. This problem and its repair will travel under the name **The Complete AI System**, but the name carries no knowledge the scene has not earned.

What changed on the map of branching journeys can be said without symbols. Before, the method could only connect every powerful component and call the result intelligent; now it can also build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### From Observation to Responsible Action

A support system retrieves current policy, drafts an answer, cites evidence, requests approval for refunds, verifies transactions, logs outcomes, and learns only through reviewed updates.

#### The Expedition Continues

Excavation 100 closes this map, not discovery. New observations must be allowed to break the system and force the next invention.

#### Where the complete ai system runs out

No architecture completes intelligence forever; every deployment creates new observations and new responsibilities.

The complete ai system repair holds, but the world asks for something it was never given. At the Road of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

#### One system, many kinds of consequence

Words, images, rewards, tools, servers, attacks, and institutions now meet in one machine. The equations remain necessary, but none can decide alone what the complete system should be allowed to do.

```text
representation + learning + action + evidence + authority
```

The trail called *one system, many kinds of consequence* is what remains when one necessity becomes another.

#### Return to the map of branching journeys

Rebuild the complete ai system scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/100-complete-ai-system/README.md).*
