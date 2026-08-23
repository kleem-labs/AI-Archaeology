# Volume II — We Let the Mind Enter the World

The model can speak. Now it must earn trust, use evidence and tools, survive deployment, gain new senses, act through consequences, and become an accountable system.

One discovery will create the need for the next; the object under construction never resets.

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

<!-- book-prose-v2 -->

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

We can postpone invention if we simply count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

If the proposal works on every relevant case, perplexity is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

Nothing magical creates perplexity. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

This boundary between the failed rule and its repair is the subject later work calls **Perplexity**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize perplexity; try to break it by subtraction. Remove the part that knows how to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale, leaving only the attempt to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree. What returns is not a vague weakness but the original contradiction: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree receives the same test as the rule to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. Their different outcomes reveal what perplexity contributes without asking the reader to trust historical convention.

#### The calculation hidden inside perplexity

Do not read the coming Perplexity line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

##### Names for pieces we have already used

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

##### Why no cheaper operation does the same job

[The log](../MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
[Summing](../MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](../MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
[The minus sign](../MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](../MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

Every symbol in Perplexity can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

#### Where perplexity runs out

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

This is where perplexity runs out for a causal reason. We gave it enough structure to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take perplexity to the workbench

A mathematical story about perplexity earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running perplexity, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the perplexity result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/046-perplexity/README.md).*

---

### Excavation 047 — Evaluation — What Does “Better” Actually Mean?

<!-- book-prose-v2 -->

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

The previous discovery seems almost sufficient: we could choose one benchmark score and call it intelligence.

The shortcut appears to retain everything evaluation needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter.

The counterexample teaches evaluation. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away.

Now—and not earlier—we may introduce **Evaluation**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to choose one benchmark score and call it intelligence, and the case answers that the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter. With the narrow repair—to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Evaluation returns to the same counterexample, replaces the attempt to choose one benchmark score and call it intelligence with the responsibility to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away, and must succeed where the shortcut failed.

#### What Does “Better” Actually Mean

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

A formula for evaluation is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### Where evaluation runs out

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

The boundary can be predicted from the construction itself. Evaluation performs the repair to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take evaluation to the workbench

Move evaluation from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running evaluation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the evaluation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/047-evaluation/README.md).*

---

### Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

<!-- book-prose-v2 -->

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

The least expensive next move is to trust fluent language because uncertainty should sound hesitant.

The proposal deserves a fair hearing. For hallucination, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”.

The failure changes the question behind hallucination. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

Only at this point does the inherited name **Hallucination** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of hallucination by mentally removing the repair. We fall back to the proposal to trust fluent language because uncertainty should sound hesitant; then training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. Restore only the ability to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to trust fluent language because uncertainty should sound hesitant to requiring the system to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to hallucination.

#### When Fluent Prediction Outruns Evidence

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

Put the old procedure beside hallucination. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where hallucination runs out

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

The limit follows from the job assigned to hallucination. Its repair knows how to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take hallucination to the workbench

A claim about hallucination now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running hallucination, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the hallucination result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/048-hallucination/README.md).*

---

### Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

<!-- book-prose-v2 -->

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

For a moment, remain loyal to the simplest proposal: treat the largest softmax probability as honest confidence.

Its appeal is not ignorance but economy. Calibration should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

Notice what the counterexample has accomplished for calibration. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

Humanity eventually gathered this problem and its repairs under the name **Calibration**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace calibration with the old instruction to treat the largest softmax probability as honest confidence. The result is again that collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. Put back only the requirement to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when calibration is introduced. The same evidence that defeated the attempt to treat the largest softmax probability as honest confidence is presented again. Only the ability to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### The calculation hidden inside calibration

Before Calibration receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

##### Names for pieces we have already used

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

##### Why no cheaper operation does the same job

[Confidence minus accuracy](../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
[Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
[Multiplying by |Bᵦ|/n](../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

Every symbol in Calibration can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

#### Where calibration runs out

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

Why does that boundary remain? Calibration was built for one responsibility: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take calibration to the workbench

The argument for calibration is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running calibration, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the calibration result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/049-calibration/README.md).*

---

### Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

<!-- book-prose-v2 -->

Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.

Nothing yet appears to demand a new invention. We can collect as much text as possible and assume scale washes out bad examples.

There is a real principle behind this restraint: the complexity of data quality must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

That distinction is the hinge on which data quality turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

We have earned the chapter's shorter name: **Data Quality**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that data quality is necessary rather than decorative. Delete its new responsibility and use the earlier plan to collect as much text as possible and assume scale washes out bad examples. Immediately, duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them. Reintroduce the single job to treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. Because the old plan to collect as much text as possible and assume scale washes out bad examples is the only displaced piece, the reader can locate exactly where data quality changes the outcome.

#### What Lessons Did the Model Actually Receive

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

The name data quality is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where data quality runs out

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

The weakness is not an accidental footnote. Every operation in data quality serves the narrower purpose to treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take data quality to the workbench

Understanding data quality now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data quality, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data quality result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/050-data-quality/README.md).*

---

### Excavation 051 — Scaling Laws — What Improves When We Add More?

<!-- book-prose-v2 -->

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

The machinery already in our hands suggests that we make the model as large as possible and assume capability follows parameter count.

This is how scaling laws ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

The wrong answer makes the need for scaling laws inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.

The usual name, **Scaling Laws**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to make the model as large as possible and assume capability follows parameter count produces the observed failure: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. Starting with the repaired demand to we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number preserves the information the shortcut lost. The subject of scaling laws lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number instead of merely trying to make the model as large as possible and assume capability follows parameter count. That controlled contrast is what turns a plausible explanation of scaling laws into an understandable derivation.

#### The calculation hidden inside scaling laws

Before Scaling Laws receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

##### Names for pieces we have already used

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

##### Why no cheaper operation does the same job

[The negative power](../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
[A scales that falling term](../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
[Adding B](../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

Every symbol in Scaling Laws can now be read back into an action already performed. The whole procedure fits in one line:

$$
L(N)=A N^{-\alpha}+B
$$

#### Where scaling laws runs out

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

Look back at what scaling laws actually preserves: it can we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take scaling laws to the workbench

The reader has reconstructed scaling laws in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running scaling laws, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the scaling laws result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/051-scaling-laws/README.md).*

---

### Excavation 052 — Instruction Tuning — From Continuation to Cooperation

<!-- book-prose-v2 -->

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

If the old idea can be stretched one step farther, we should prompt more forcefully and hope next-token prediction infers the desired interaction.

If the proposal works on every relevant case, instruction tuning is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

Nothing magical creates instruction tuning. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

This boundary between the failed rule and its repair is the subject later work calls **Instruction Tuning**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize instruction tuning; try to break it by subtraction. Remove the part that knows how to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern, leaving only the attempt to prompt more forcefully and hope next-token prediction infers the desired interaction. What returns is not a vague weakness but the original contradiction: the trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to prompt more forcefully and hope next-token prediction infers the desired interaction receives the same test as the rule to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern. Their different outcomes reveal what instruction tuning contributes without asking the reader to trust historical convention.

#### From Continuation to Cooperation

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

Hold the setting, evidence, and desired outcome fixed while testing instruction tuning. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where instruction tuning runs out

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

This is where instruction tuning runs out for a causal reason. We gave it enough structure to show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take instruction tuning to the workbench

A mathematical story about instruction tuning earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running instruction tuning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the instruction tuning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/052-instruction-tuning/README.md).*

---

### Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

<!-- book-prose-v2 -->

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

A careful builder would first avoid adding machinery and write one perfect target response for every prompt and train only to imitate it.

The shortcut appears to retain everything preference learning needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

The counterexample teaches preference learning. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

Now—and not earlier—we may introduce **Preference Learning**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to write one perfect target response for every prompt and train only to imitate it, and the case answers that many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. With the narrow repair—to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Preference Learning returns to the same counterexample, replaces the attempt to write one perfect target response for every prompt and train only to imitate it with the responsibility to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy, and must succeed where the shortcut failed.

#### The calculation hidden inside preference learning

Before Preference Learning receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

##### Names for pieces we have already used

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

##### Why no cheaper operation does the same job

[rA−rB](../MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
[The inner negative](../MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
[Exponentiation](../MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](../MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Every symbol in Preference Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

#### Where preference learning runs out

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

The boundary can be predicted from the construction itself. Preference Learning performs the repair to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take preference learning to the workbench

Move preference learning from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running preference learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the preference learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/053-preference-learning/README.md).*

---

### Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

<!-- book-prose-v2 -->

Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.

The obvious economy is to retrain the whole model whenever one document changes.

The proposal deserves a fair hearing. For retrieval-augmented generation, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

The failure changes the question behind retrieval-augmented generation. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

Only at this point does the inherited name **Retrieval-Augmented Generation** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of retrieval-augmented generation by mentally removing the repair. We fall back to the proposal to retrain the whole model whenever one document changes; then a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source. Restore only the ability to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to retrain the whole model whenever one document changes to requiring the system to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to retrieval-augmented generation.

#### Let the Model Look Before It Speaks

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

Put the old procedure beside retrieval-augmented generation. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where retrieval-augmented generation runs out

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

The limit follows from the job assigned to retrieval-augmented generation. Its repair knows how to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take retrieval-augmented generation to the workbench

A claim about retrieval-augmented generation now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running retrieval-augmented generation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the retrieval-augmented generation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/054-retrieval-augmented-generation/README.md).*

---

### Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

<!-- book-prose-v2 -->

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

Before naming anything new, try to ask the language model to simulate every tool from memory.

Its appeal is not ignorance but economy. Tool-Using Agents should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

Notice what the counterexample has accomplished for tool-using agents. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

Humanity eventually gathered this problem and its repairs under the name **Tool-Using Agents**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace tool-using agents with the old instruction to ask the language model to simulate every tool from memory. The result is again that it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. Put back only the requirement to we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when tool-using agents is introduced. The same evidence that defeated the attempt to ask the language model to simulate every tool from memory is presented again. Only the ability to we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### When Words Must Cause Verified Actions

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

Run the tool-using agents scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where tool-using agents runs out

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

Why does that boundary remain? Tool-Using Agents was built for one responsibility: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take tool-using agents to the workbench

The argument for tool-using agents is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tool-using agents, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tool-using agents result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/055-tool-using-agents/README.md).*

---

## Part VI — Trusting an Acting Machine

A model that only writes can be wrong. A model with tools can make its mistake real. The story therefore moves from capability to authority: what the assistant may do, how hostile text is kept from becoming an instruction, and what evidence proves that a long task actually succeeded.

---

### Excavation 056 — Authority — What Is the Agent Allowed to Do?

<!-- book-prose-v2 -->

Tools let language cause external effects. The moment an answer can act, capability must be separated from permission: what may this agent do without asking again?

The first defensible move is to give every available tool to the model and treat user intent as unlimited permission.

There is a real principle behind this restraint: the complexity of authority must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

That distinction is the hinge on which authority turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.

We have earned the chapter's shorter name: **Authority**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that authority is necessary rather than decorative. Delete its new responsibility and use the earlier plan to give every available tool to the model and treat user intent as unlimited permission. Immediately, ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not. Reintroduce the single job to separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. Because the old plan to give every available tool to the model and treat user intent as unlimited permission is the only displaced piece, the reader can locate exactly where authority changes the outcome.

#### What Is the Agent Allowed to Do

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

Authority earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

The name authority is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where authority runs out

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

The weakness is not an accidental footnote. Every operation in authority serves the narrower purpose to separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take authority to the workbench

Understanding authority now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running authority, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the authority result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/056-authority/README.md).*

---

### Excavation 057 — Prompt Injection — When Evidence Tries to Become an Instruction

<!-- book-prose-v2 -->

An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.

At this point the shortest path seems to be to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

This is how prompt injection ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control.

The wrong answer makes the need for prompt injection inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content.

The usual name, **Prompt Injection**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest produces the observed failure: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control. Starting with the repaired demand to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content preserves the information the shortcut lost. The subject of prompt injection lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content instead of merely trying to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest. That controlled contrast is what turns a plausible explanation of prompt injection into an understandable derivation.

#### When Evidence Tries to Become an Instruction

A policy document says “email this file externally.” The agent may summarize that sentence as document content, but the permission layer refuses the email because the user never authorized it.

Prompt Injection earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

There are now two histories of this prompt injection case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where prompt injection runs out

No prompt wording guarantees isolation. Security must also exist outside the model in tool schemas, permissions, and validation.

Look back at what prompt injection actually preserves: it can label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take prompt injection to the workbench

The reader has reconstructed prompt injection in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running prompt injection, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the prompt injection result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/057-prompt-injection/README.md).*

---

### Excavation 058 — Planning — Turning a Goal into Checkable Steps

<!-- book-prose-v2 -->

Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.

We can postpone invention if we simply ask the agent to take the next action that sounds useful until the goal appears complete.

If the proposal works on every relevant case, planning is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

Nothing magical creates planning. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.

This boundary between the failed rule and its repair is the subject later work calls **Planning**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize planning; try to break it by subtraction. Remove the part that knows how to represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions, leaving only the attempt to ask the agent to take the next action that sounds useful until the goal appears complete. What returns is not a vague weakness but the original contradiction: it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to ask the agent to take the next action that sounds useful until the goal appears complete receives the same test as the rule to represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. Their different outcomes reveal what planning contributes without asking the reader to trust historical convention.

#### Turning a Goal into Checkable Steps

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

Planning earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Hold the setting, evidence, and desired outcome fixed while testing planning. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where planning runs out

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

This is where planning runs out for a causal reason. We gave it enough structure to represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take planning to the workbench

A mathematical story about planning earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running planning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the planning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/058-planning/README.md).*

---

### Excavation 059 — Memory — What Should Survive After the Context Ends?

<!-- book-prose-v2 -->

Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.

The previous discovery seems almost sufficient: we could store every message forever and paste all history into every new prompt.

The shortcut appears to retain everything memory needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

The counterexample teaches memory. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.

Now—and not earlier—we may introduce **Memory**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to store every message forever and paste all history into every new prompt, and the case answers that cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose. With the narrow repair—to we need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Memory returns to the same counterexample, replaces the attempt to store every message forever and paste all history into every new prompt with the responsibility to we need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them, and must succeed where the shortcut failed.

#### What Should Survive After the Context Ends

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

Memory earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

A formula for memory is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### Where memory runs out

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

The boundary can be predicted from the construction itself. Memory performs the repair to we need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take memory to the workbench

Move memory from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running memory, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the memory result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/059-memory/README.md).*

---

### Excavation 060 — State Machines — Knowing What Has Actually Happened

<!-- book-prose-v2 -->

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

The least expensive next move is to let the conversation prose serve as the workflow state.

The proposal deserves a fair hearing. For state machines, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

The failure changes the question behind state machines. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

Only at this point does the inherited name **State Machines** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of state machines by mentally removing the repair. We fall back to the proposal to let the conversation prose serve as the workflow state; then the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. Restore only the ability to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let the conversation prose serve as the workflow state to requiring the system to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to state machines.

#### Knowing What Has Actually Happened

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

State Machines earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Put the old procedure beside state machines. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where state machines runs out

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

The limit follows from the job assigned to state machines. Its repair knows how to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take state machines to the workbench

A claim about state machines now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running state machines, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the state machines result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/060-state-machines/README.md).*

---

### Excavation 061 — Verification — How Does the Agent Know It Succeeded?

<!-- book-prose-v2 -->

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

For a moment, remain loyal to the simplest proposal: trust the absence of an error message or the model’s own description of its work.

Its appeal is not ignorance but economy. Verification should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

Notice what the counterexample has accomplished for verification. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

Humanity eventually gathered this problem and its repairs under the name **Verification**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace verification with the old instruction to trust the absence of an error message or the model’s own description of its work. The result is again that the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. Put back only the requirement to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when verification is introduced. The same evidence that defeated the attempt to trust the absence of an error message or the model’s own description of its work is presented again. Only the ability to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### How Does the Agent Know It Succeeded

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

Verification earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Run the verification scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where verification runs out

Verification can test only stated properties. A passing check suite may omit the most important behavior.

Why does that boundary remain? Verification was built for one responsibility: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take verification to the workbench

The argument for verification is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running verification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the verification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/061-verification/README.md).*

---

### Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

<!-- book-prose-v2 -->

Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.

Nothing yet appears to demand a new invention. We can retry the action whenever a response is missing.

There is a real principle behind this restraint: the complexity of retries and idempotency must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: the trouble appears immediately: the first payment succeeded and the retry charges the customer twice.

That distinction is the hinge on which retries and idempotency turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

We have earned the chapter's shorter name: **Retries and Idempotency**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that retries and idempotency is necessary rather than decorative. Delete its new responsibility and use the earlier plan to retry the action whenever a response is missing. Immediately, the trouble appears immediately: the first payment succeeded and the retry charges the customer twice. Reintroduce the single job to give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. Because the old plan to retry the action whenever a response is missing is the only displaced piece, the reader can locate exactly where retries and idempotency changes the outcome.

#### Trying Again Without Doing It Twice

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

Retries and Idempotency earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

The name retries and idempotency is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where retries and idempotency runs out

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

The weakness is not an accidental footnote. Every operation in retries and idempotency serves the narrower purpose to give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take retries and idempotency to the workbench

Understanding retries and idempotency now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running retries and idempotency, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the retries and idempotency result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/062-retries-idempotency/README.md).*

---

### Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

<!-- book-prose-v2 -->

Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.

The machinery already in our hands suggests that we create many agents for every problem and let them freely edit shared state.

This is how multi-agent coordination ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving.

The wrong answer makes the need for multi-agent coordination inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result.

The usual name, **Multi-Agent Coordination**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to create many agents for every problem and let them freely edit shared state produces the observed failure: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. Starting with the repaired demand to we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result preserves the information the shortcut lost. The subject of multi-agent coordination lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result instead of merely trying to create many agents for every problem and let them freely edit shared state. That controlled contrast is what turns a plausible explanation of multi-agent coordination into an understandable derivation.

#### When Should Work Be Divided

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

Multi-Agent Coordination earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

There are now two histories of this multi-agent coordination case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where multi-agent coordination runs out

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

Look back at what multi-agent coordination actually preserves: it can we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take multi-agent coordination to the workbench

The reader has reconstructed multi-agent coordination in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running multi-agent coordination, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the multi-agent coordination result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/063-multi-agent-coordination/README.md).*

---

### Excavation 064 — Observability — Seeing Why an Agent Failed

<!-- book-prose-v2 -->

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

If the old idea can be stretched one step farther, we should log only the final response, or log every hidden detail without structure.

If the proposal works on every relevant case, observability is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Nothing magical creates observability. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

This boundary between the failed rule and its repair is the subject later work calls **Observability**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize observability; try to break it by subtraction. Remove the part that knows how to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content, leaving only the attempt to log only the final response, or log every hidden detail without structure. What returns is not a vague weakness but the original contradiction: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to log only the final response, or log every hidden detail without structure receives the same test as the rule to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. Their different outcomes reveal what observability contributes without asking the reader to trust historical convention.

#### Seeing Why an Agent Failed

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

Observability earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Hold the setting, evidence, and desired outcome fixed while testing observability. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where observability runs out

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

This is where observability runs out for a causal reason. We gave it enough structure to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take observability to the workbench

A mathematical story about observability earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running observability, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the observability result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/064-observability/README.md).*

---

### Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

<!-- book-prose-v2 -->

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

A careful builder would first avoid adding machinery and give the agent a broad goal and let it continue until it believes the goal is complete.

The shortcut appears to retain everything bounded autonomy needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

The counterexample teaches bounded autonomy. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

Now—and not earlier—we may introduce **Bounded Autonomy**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to give the agent a broad goal and let it continue until it believes the goal is complete, and the case answers that a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. With the narrow repair—to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Bounded Autonomy returns to the same counterexample, replaces the attempt to give the agent a broad goal and let it continue until it believes the goal is complete with the responsibility to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path, and must succeed where the shortcut failed.

#### Building an Agent That Can Be Trusted

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

Bounded Autonomy earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

A formula for bounded autonomy is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### Where bounded autonomy runs out

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

The boundary can be predicted from the construction itself. Bounded Autonomy performs the repair to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take bounded autonomy to the workbench

Move bounded autonomy from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running bounded autonomy, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the bounded autonomy result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/065-bounded-autonomy/README.md).*

---

## Part VII — Learning After Deployment

The bounded assistant enters the world, and the world does not stand still. Its recommendations change behavior; seasons change data; updates change the model. To remain trustworthy, the system must detect these loops and then investigate which internal causes genuinely drive its decisions.

---

### Excavation 066 — Feedback Loops

<!-- book-prose-v2 -->

The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.

The obvious economy is to treat every click as independent evidence of natural preference.

The proposal deserves a fair hearing. For feedback loops, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that show one song repeatedly; its extra clicks now appear to prove it deserved repetition.

The failure changes the question behind feedback loops. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: record how the system influenced each observation and evaluate outcomes against a control or exploration policy.

Only at this point does the inherited name **Feedback Loops** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of feedback loops by mentally removing the repair. We fall back to the proposal to treat every click as independent evidence of natural preference; then show one song repeatedly; its extra clicks now appear to prove it deserved repetition. Restore only the ability to record how the system influenced each observation and evaluate outcomes against a control or exploration policy, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to treat every click as independent evidence of natural preference to requiring the system to record how the system influenced each observation and evaluate outcomes against a control or exploration policy. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to feedback loops.

#### Understanding feedback loops

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

Put the old procedure beside feedback loops. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where feedback loops runs out

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

The limit follows from the job assigned to feedback loops. Its repair knows how to record how the system influenced each observation and evaluate outcomes against a control or exploration policy. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take feedback loops to the workbench

A claim about feedback loops now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running feedback loops, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the feedback loops result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/066-feedback-loops/README.md).*

---

### Excavation 067 — Online Learning

<!-- book-prose-v2 -->

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

Before naming anything new, try to retrain immediately on every new labeled event.

Its appeal is not ignorance but economy. Online Learning should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices.

Notice what the counterexample has accomplished for online learning. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

Humanity eventually gathered this problem and its repairs under the name **Online Learning**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace online learning with the old instruction to retrain immediately on every new labeled event. The result is again that the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. Put back only the requirement to we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when online learning is introduced. The same evidence that defeated the attempt to retrain immediately on every new labeled event is presented again. Only the ability to we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Understanding online learning

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

Run the online learning scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where online learning runs out

Fast adaptation also creates fast corruption.

Why does that boundary remain? Online Learning was built for one responsibility: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take online learning to the workbench

The argument for online learning is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running online learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the online learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/067-online-learning/README.md).*

---

### Excavation 068 — Distribution Drift

<!-- book-prose-v2 -->

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

The first defensible move is to assume training accuracy remains valid forever.

There is a real principle behind this restraint: the complexity of distribution drift must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: a winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

That distinction is the hinge on which distribution drift turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

We have earned the chapter's shorter name: **Distribution Drift**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that distribution drift is necessary rather than decorative. Delete its new responsibility and use the earlier plan to assume training accuracy remains valid forever. Immediately, a winter-trained demand model meets summer behavior and keeps reporting confident old patterns. Reintroduce the single job to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. Because the old plan to assume training accuracy remains valid forever is the only displaced piece, the reader can locate exactly where distribution drift changes the outcome.

#### Understanding distribution drift

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

The name distribution drift is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where distribution drift runs out

Not every statistical shift changes the decision that matters.

The weakness is not an accidental footnote. Every operation in distribution drift serves the narrower purpose to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take distribution drift to the workbench

Understanding distribution drift now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running distribution drift, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the distribution drift result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/068-distribution-drift/README.md).*

---

### Excavation 069 — Controlled Experiments

<!-- book-prose-v2 -->

Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.

At this point the shortest path seems to be to compare this week with last week.

This is how controlled experiments ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: a holiday raises sales for both systems and receives credit as a model improvement.

The wrong answer makes the need for controlled experiments inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: randomly assign comparable cases to old and new behavior and compare predefined outcomes.

The usual name, **Controlled Experiments**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to compare this week with last week produces the observed failure: a holiday raises sales for both systems and receives credit as a model improvement. Starting with the repaired demand to randomly assign comparable cases to old and new behavior and compare predefined outcomes preserves the information the shortcut lost. The subject of controlled experiments lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to randomly assign comparable cases to old and new behavior and compare predefined outcomes instead of merely trying to compare this week with last week. That controlled contrast is what turns a plausible explanation of controlled experiments into an understandable derivation.

#### Understanding controlled experiments

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

There are now two histories of this controlled experiments case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where controlled experiments runs out

Experiments require sufficient samples, ethical limits, and careful metrics.

Look back at what controlled experiments actually preserves: it can randomly assign comparable cases to old and new behavior and compare predefined outcomes. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take controlled experiments to the workbench

The reader has reconstructed controlled experiments in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running controlled experiments, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the controlled experiments result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/069-controlled-experiments/README.md).*

---

### Excavation 070 — Bandits — Learning While Choosing

<!-- book-prose-v2 -->

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

We can postpone invention if we simply always choose the currently best option.

If the proposal works on every relevant case, bandits is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: an unlucky first result permanently hides a better alternative.

Nothing magical creates bandits. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: reserve some choices for exploration while exploiting accumulated evidence.

This boundary between the failed rule and its repair is the subject later work calls **Bandits**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize bandits; try to break it by subtraction. Remove the part that knows how to reserve some choices for exploration while exploiting accumulated evidence, leaving only the attempt to always choose the currently best option. What returns is not a vague weakness but the original contradiction: an unlucky first result permanently hides a better alternative. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to always choose the currently best option receives the same test as the rule to reserve some choices for exploration while exploiting accumulated evidence. Their different outcomes reveal what bandits contributes without asking the reader to trust historical convention.

#### Learning While Choosing

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

Hold the setting, evidence, and desired outcome fixed while testing bandits. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where bandits runs out

Exploration has real cost and can be unacceptable for high-risk actions.

This is where bandits runs out for a causal reason. We gave it enough structure to reserve some choices for exploration while exploiting accumulated evidence, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take bandits to the workbench

A mathematical story about bandits earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running bandits, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the bandits result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/070-bandits/README.md).*

---

### Excavation 071 — Features Inside Networks

<!-- book-prose-v2 -->

Bandit strategies balance present reward with the value of exploring uncertain choices. Once deployed, their decisions still emerge from internal representations whose meaning and failure modes remain hidden.

The previous discovery seems almost sufficient: we could search for one neuron dedicated to each human concept.

The shortcut appears to retain everything features inside networks needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: the concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons.

The counterexample teaches features inside networks. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to treat representations as distributed directions and test them across varied examples.

Now—and not earlier—we may introduce **Features Inside Networks**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to search for one neuron dedicated to each human concept, and the case answers that the concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons. With the narrow repair—to we need to treat representations as distributed directions and test them across varied examples—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Features Inside Networks returns to the same counterexample, replaces the attempt to search for one neuron dedicated to each human concept with the responsibility to we need to treat representations as distributed directions and test them across varied examples, and must succeed where the shortcut failed.

#### Understanding features inside networks

Tiger and zebra activate overlapping patterns; subtracting ordinary cats isolates a stripe-related direction better than one cell.

A formula for features inside networks is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### Where features inside networks runs out

Human labels may not match the model’s internal abstractions.

The boundary can be predicted from the construction itself. Features Inside Networks performs the repair to we need to treat representations as distributed directions and test them across varied examples; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take features inside networks to the workbench

Move features inside networks from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running features inside networks, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the features inside networks result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/071-features-inside-networks/README.md).*

---

### Excavation 072 — Linear Probes

<!-- book-prose-v2 -->

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

The least expensive next move is to train a powerful classifier on hidden states and call any success evidence.

The proposal deserves a fair hearing. For linear probes, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple.

The failure changes the question behind linear probes. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: use a deliberately limited probe and compare layers, controls, and baselines.

Only at this point does the inherited name **Linear Probes** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of linear probes by mentally removing the repair. We fall back to the proposal to train a powerful classifier on hidden states and call any success evidence; then the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. Restore only the ability to use a deliberately limited probe and compare layers, controls, and baselines, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to train a powerful classifier on hidden states and call any success evidence to requiring the system to use a deliberately limited probe and compare layers, controls, and baselines. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to linear probes.

#### Understanding linear probes

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

Put the old procedure beside linear probes. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where linear probes runs out

Decodable information is not proof the model uses it.

The limit follows from the job assigned to linear probes. Its repair knows how to use a deliberately limited probe and compare layers, controls, and baselines. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take linear probes to the workbench

A claim about linear probes now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running linear probes, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the linear probes result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/072-linear-probes/README.md).*

---

### Excavation 073 — Attribution

<!-- book-prose-v2 -->

Linear probes reveal information available to a simple reader. To understand one prediction, we must trace which input evidence actually influenced the output rather than merely existing somewhere inside.

For a moment, remain loyal to the simplest proposal: remove each word and treat output change as complete explanation.

Its appeal is not ignorance but economy. Attribution should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: removing a word changes grammar and creates an unnatural new input.

Notice what the counterexample has accomplished for attribution. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions.

Humanity eventually gathered this problem and its repairs under the name **Attribution**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace attribution with the old instruction to remove each word and treat output change as complete explanation. The result is again that removing a word changes grammar and creates an unnatural new input. Put back only the requirement to measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when attribution is introduced. The same evidence that defeated the attempt to remove each word and treat output change as complete explanation is presented again. Only the ability to measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Understanding attribution

For “not dangerous,” attribution highlights not; replacing it with very changes the class as predicted.

Run the attribution scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where attribution runs out

Attribution can be unstable and method-dependent.

Why does that boundary remain? Attribution was built for one responsibility: measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take attribution to the workbench

The argument for attribution is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running attribution, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the attribution result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/073-attribution/README.md).*

---

### Excavation 074 — Superposition

<!-- book-prose-v2 -->

Attribution assigns influence to inputs or internal components. The investigation soon finds that one neuron can participate in many features and one feature can be distributed across many neurons.

Nothing yet appears to demand a new invention. We can demand one feature per coordinate.

There is a real principle behind this restraint: the complexity of superposition must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that limited width forces useful patterns to share neurons, producing confusing mixed activations.

That distinction is the hinge on which superposition turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: represent features as directions that can overlap when they rarely need to be active together.

We have earned the chapter's shorter name: **Superposition**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that superposition is necessary rather than decorative. Delete its new responsibility and use the earlier plan to demand one feature per coordinate. Immediately, limited width forces useful patterns to share neurons, producing confusing mixed activations. Reintroduce the single job to represent features as directions that can overlap when they rarely need to be active together. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can represent features as directions that can overlap when they rarely need to be active together. Because the old plan to demand one feature per coordinate is the only displaced piece, the reader can locate exactly where superposition changes the outcome.

#### Understanding superposition

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

The name superposition is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where superposition runs out

Separating superposed features is difficult and may not yield unique answers.

The weakness is not an accidental footnote. Every operation in superposition serves the narrower purpose to represent features as directions that can overlap when they rarely need to be active together; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take superposition to the workbench

Understanding superposition now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running superposition, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the superposition result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/074-superposition/README.md).*

---

### Excavation 075 — Causal Interventions

<!-- book-prose-v2 -->

Superposition explains how limited dimensions can carry more features than individual neurons. A readable direction may still be a bystander; only changing it and observing behavior can test whether it is causally used.

The machinery already in our hands suggests that we assume correlation with output proves causation.

This is how causal interventions ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: the direction predicts answers but changing it leaves behavior unchanged.

The wrong answer makes the need for causal interventions inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to intervene on the representation and measure the specific downstream change against controls.

The usual name, **Causal Interventions**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to assume correlation with output proves causation produces the observed failure: the direction predicts answers but changing it leaves behavior unchanged. Starting with the repaired demand to we need to intervene on the representation and measure the specific downstream change against controls preserves the information the shortcut lost. The subject of causal interventions lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to intervene on the representation and measure the specific downstream change against controls instead of merely trying to assume correlation with output proves causation. That controlled contrast is what turns a plausible explanation of causal interventions into an understandable derivation.

#### Understanding causal interventions

Adding the candidate direction raises tiger probability only in relevant contexts; random directions do not.

There are now two histories of this causal interventions case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where causal interventions runs out

Interventions can create unnatural internal states.

Look back at what causal interventions actually preserves: it can we need to intervene on the representation and measure the specific downstream change against controls. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take causal interventions to the workbench

The reader has reconstructed causal interventions in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running causal interventions, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the causal interventions result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/075-causal-interventions/README.md).*

---

## Part VIII — Seeing and Creating

Language is only one trace of the valley. Cameras bring grids of colored light, and the assistant cannot understand them by pretending they are sentences. We begin again from the observation itself, then reuse the deeper principles already earned: locality, hierarchy, attention, compression, and gradual generation.

---

### Excavation 076 — Pixels — Turning Light into Numbers

<!-- book-prose-v2 -->

Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.

If the old idea can be stretched one step farther, we should assign one label to the entire raw byte sequence.

If the proposal works on every relevant case, pixels is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: a one-pixel shift changes thousands of byte positions although the same tiger remains.

Nothing magical creates pixels. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: preserve local spatial arrangement and compare nearby color measurements.

This boundary between the failed rule and its repair is the subject later work calls **Pixels**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize pixels; try to break it by subtraction. Remove the part that knows how to preserve local spatial arrangement and compare nearby color measurements, leaving only the attempt to assign one label to the entire raw byte sequence. What returns is not a vague weakness but the original contradiction: a one-pixel shift changes thousands of byte positions although the same tiger remains. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to assign one label to the entire raw byte sequence receives the same test as the rule to preserve local spatial arrangement and compare nearby color measurements. Their different outcomes reveal what pixels contributes without asking the reader to trust historical convention.

#### Turning Light into Numbers

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

Hold the setting, evidence, and desired outcome fixed while testing pixels. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where pixels runs out

Pixels depend on lighting, sensor, scale, and viewpoint.

This is where pixels runs out for a causal reason. We gave it enough structure to preserve local spatial arrangement and compare nearby color measurements, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take pixels to the workbench

A mathematical story about pixels earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pixels, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pixels result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/076-pixels/README.md).*

---

### Excavation 077 — Convolution — Reusing the Same Local Detector

<!-- book-prose-v2 -->

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

A careful builder would first avoid adding machinery and learn a separate edge detector for every location.

The shortcut appears to retain everything convolution needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves.

The counterexample teaches convolution. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: slide one small learned filter across all positions and reuse its weights.

Now—and not earlier—we may introduce **Convolution**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to learn a separate edge detector for every location, and the case answers that the trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves. With the narrow repair—to slide one small learned filter across all positions and reuse its weights—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Convolution returns to the same counterexample, replaces the attempt to learn a separate edge detector for every location with the responsibility to slide one small learned filter across all positions and reuse its weights, and must succeed where the shortcut failed.

#### Reusing the Same Local Detector

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

A formula for convolution is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside convolution

Before Convolution receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

The signal values are neighboring brightness measurements.
The kernel values are the same small detector reused at every location.
Multiplication measures how each local measurement agrees with its detector weight.
Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

##### Why no cheaper operation does the same job

[Each multiplication](../MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
[The sum](../MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
[i+j](../MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Every symbol in Convolution can now be read back into an action already performed. The whole procedure fits in one line:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

#### Where convolution runs out

Convolution assumes useful locality and translation reuse.

The boundary can be predicted from the construction itself. Convolution performs the repair to slide one small learned filter across all positions and reuse its weights; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take convolution to the workbench

Move convolution from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running convolution, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the convolution result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/077-convolution/README.md).*

---

### Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

<!-- book-prose-v2 -->

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

The obvious economy is to keep every activation at full resolution through every layer.

The proposal deserves a fair hearing. For pooling, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: memory explodes and tiny shifts move evidence to neighboring cells.

The failure changes the question behind pooling. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: summarize small neighborhoods while retaining the strongest or average evidence.

Only at this point does the inherited name **Pooling** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pooling by mentally removing the repair. We fall back to the proposal to keep every activation at full resolution through every layer; then memory explodes and tiny shifts move evidence to neighboring cells. Restore only the ability to summarize small neighborhoods while retaining the strongest or average evidence, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to keep every activation at full resolution through every layer to requiring the system to summarize small neighborhoods while retaining the strongest or average evidence. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pooling.

#### Keeping Evidence While Shrinking the Map

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

Put the old procedure beside pooling. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where pooling runs out

Pooling discards exact location and can erase subtle patterns.

The limit follows from the job assigned to pooling. Its repair knows how to summarize small neighborhoods while retaining the strongest or average evidence. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take pooling to the workbench

A claim about pooling now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pooling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pooling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/078-pooling/README.md).*

---

### Excavation 079 — CNN Hierarchies

<!-- book-prose-v2 -->

Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.

Before naming anything new, try to classify directly from isolated edge responses.

Its appeal is not ignorance but economy. CNN Hierarchies should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: one edge has no object-level meaning.

Notice what the counterexample has accomplished for cnn hierarchies. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to stack local detectors so later layers combine earlier patterns over wider regions.

Humanity eventually gathered this problem and its repairs under the name **CNN Hierarchies**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace cnn hierarchies with the old instruction to classify directly from isolated edge responses. The result is again that one edge has no object-level meaning. Put back only the requirement to we need to stack local detectors so later layers combine earlier patterns over wider regions. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when cnn hierarchies is introduced. The same evidence that defeated the attempt to classify directly from isolated edge responses is presented again. Only the ability to we need to stack local detectors so later layers combine earlier patterns over wider regions changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Understanding cnn hierarchies

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

Run the cnn hierarchies scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where cnn hierarchies runs out

The hierarchy is learned, not guaranteed to match human parts.

Why does that boundary remain? CNN Hierarchies was built for one responsibility: we need to stack local detectors so later layers combine earlier patterns over wider regions. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take cnn hierarchies to the workbench

The argument for cnn hierarchies is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running cnn hierarchies, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the cnn hierarchies result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/079-cnn-hierarchy/README.md).*

---

### Excavation 080 — Vision Transformers

<!-- book-prose-v2 -->

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

The first defensible move is to treat every pixel as a token.

There is a real principle behind this restraint: the complexity of vision transformers must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: the sequence becomes enormous and individual pixels carry little stable structure.

That distinction is the hinge on which vision transformers turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: group pixels into patches, embed them as tokens, add position, and apply attention.

We have earned the chapter's shorter name: **Vision Transformers**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that vision transformers is necessary rather than decorative. Delete its new responsibility and use the earlier plan to treat every pixel as a token. Immediately, the sequence becomes enormous and individual pixels carry little stable structure. Reintroduce the single job to group pixels into patches, embed them as tokens, add position, and apply attention. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can group pixels into patches, embed them as tokens, add position, and apply attention. Because the old plan to treat every pixel as a token is the only displaced piece, the reader can locate exactly where vision transformers changes the outcome.

#### Understanding vision transformers

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

The name vision transformers is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where vision transformers runs out

Patch size trades detail for cost and needs substantial data.

The weakness is not an accidental footnote. Every operation in vision transformers serves the narrower purpose to group pixels into patches, embed them as tokens, add position, and apply attention; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take vision transformers to the workbench

Understanding vision transformers now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running vision transformers, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the vision transformers result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/080-vision-transformers/README.md).*

---

### Excavation 081 — Autoencoders — Compressing and Rebuilding

<!-- book-prose-v2 -->

Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.

At this point the shortest path seems to be to copy the input through an unrestricted hidden layer.

This is how autoencoders ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: a wide hidden layer learns identity without compression.

The wrong answer makes the need for autoencoders inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: force information through a bottleneck and train reconstruction.

The usual name, **Autoencoders**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to copy the input through an unrestricted hidden layer produces the observed failure: a wide hidden layer learns identity without compression. Starting with the repaired demand to force information through a bottleneck and train reconstruction preserves the information the shortcut lost. The subject of autoencoders lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to force information through a bottleneck and train reconstruction instead of merely trying to copy the input through an unrestricted hidden layer. That controlled contrast is what turns a plausible explanation of autoencoders into an understandable derivation.

#### Compressing and Rebuilding

Four correlated measurements compress to two codes that still rebuild the originals approximately.

There are now two histories of this autoencoders case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where autoencoders runs out

Good reconstruction may preserve details irrelevant to downstream meaning.

Look back at what autoencoders actually preserves: it can force information through a bottleneck and train reconstruction. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take autoencoders to the workbench

The reader has reconstructed autoencoders in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running autoencoders, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the autoencoders result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/081-autoencoders/README.md).*

---

### Excavation 082 — Latent Space — Coordinates for Hidden Causes

<!-- book-prose-v2 -->

An autoencoder learns to compress and reconstruct. Its bottleneck is only a list of numbers until changes in those coordinates correspond to useful hidden causes such as pose, lighting, or identity.

We can postpone invention if we simply assume any compressed coordinates form a smooth useful space.

If the proposal works on every relevant case, latent space is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that the trouble appears immediately: tiny code changes can cause abrupt unrelated outputs.

Nothing magical creates latent space. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: shape the latent distribution and train nearby codes to decode coherently.

This boundary between the failed rule and its repair is the subject later work calls **Latent Space**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize latent space; try to break it by subtraction. Remove the part that knows how to shape the latent distribution and train nearby codes to decode coherently, leaving only the attempt to assume any compressed coordinates form a smooth useful space. What returns is not a vague weakness but the original contradiction: the trouble appears immediately: tiny code changes can cause abrupt unrelated outputs. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to assume any compressed coordinates form a smooth useful space receives the same test as the rule to shape the latent distribution and train nearby codes to decode coherently. Their different outcomes reveal what latent space contributes without asking the reader to trust historical convention.

#### Coordinates for Hidden Causes

Moving one latent coordinate gradually changes image brightness while another changes pose.

Hold the setting, evidence, and desired outcome fixed while testing latent space. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where latent space runs out

Latent directions need not be independent or human-readable.

This is where latent space runs out for a causal reason. We gave it enough structure to shape the latent distribution and train nearby codes to decode coherently, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take latent space to the workbench

A mathematical story about latent space earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running latent space, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the latent space result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/082-latent-space/README.md).*

---

### Excavation 083 — Autoregressive Generation Beyond Text

<!-- book-prose-v2 -->

A meaningful latent space gives images coordinates we can navigate. To create a new image, the system still needs a procedure that turns an uncertain starting state into a complete arrangement of pixels.

The previous discovery seems almost sufficient: we could predict all pixels independently.

The shortcut appears to retain everything autoregressive generation beyond text needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: independent pixels produce noise because neighboring colors and shapes constrain one another.

The counterexample teaches autoregressive generation beyond text. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to choose an order and predict each piece from previously generated pieces.

Now—and not earlier—we may introduce **Autoregressive Generation Beyond Text**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to predict all pixels independently, and the case answers that independent pixels produce noise because neighboring colors and shapes constrain one another. With the narrow repair—to we need to choose an order and predict each piece from previously generated pieces—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Autoregressive Generation Beyond Text returns to the same counterexample, replaces the attempt to predict all pixels independently with the responsibility to we need to choose an order and predict each piece from previously generated pieces, and must succeed where the shortcut failed.

#### Understanding autoregressive generation beyond text

After generating sky pixels, the model gives blue neighbors higher probability.

A formula for autoregressive generation beyond text is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### Where autoregressive generation beyond text runs out

Sequential generation can be slow and ordering introduces bias.

The boundary can be predicted from the construction itself. Autoregressive Generation Beyond Text performs the repair to we need to choose an order and predict each piece from previously generated pieces; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take autoregressive generation beyond text to the workbench

Move autoregressive generation beyond text from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running autoregressive generation beyond text, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the autoregressive generation beyond text result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/083-autoregressive-generation/README.md).*

---

### Excavation 084 — Diffusion — Learning by Destroying

<!-- book-prose-v2 -->

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

The least expensive next move is to map one random vector directly to a finished image in one jump.

The proposal deserves a fair hearing. For diffusion, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: one enormous jump is difficult to learn and unstable across diverse images.

The failure changes the question behind diffusion. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: gradually add noise to real images, then learn the smaller reverse step at every noise level.

Only at this point does the inherited name **Diffusion** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of diffusion by mentally removing the repair. We fall back to the proposal to map one random vector directly to a finished image in one jump; then one enormous jump is difficult to learn and unstable across diverse images. Restore only the ability to gradually add noise to real images, then learn the smaller reverse step at every noise level, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to map one random vector directly to a finished image in one jump to requiring the system to gradually add noise to real images, then learn the smaller reverse step at every noise level. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to diffusion.

#### Learning by Destroying

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

Put the old procedure beside diffusion. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside diffusion

Do not read the coming Diffusion line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

The clean image is the named tiger image x0.
Noise ε is the random corruption added during the forward process.
The retained clean fraction and noise fraction change with step t.
Square roots scale amplitudes so their variances combine as intended.

##### Why no cheaper operation does the same job

[The two multiplications](../MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
[Addition](../MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
[Square roots of the variance shares](../MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Every symbol in Diffusion can now be read back into an action already performed. The whole procedure fits in one line:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

#### Where diffusion runs out

Many denoising steps make sampling expensive.

The limit follows from the job assigned to diffusion. Its repair knows how to gradually add noise to real images, then learn the smaller reverse step at every noise level. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take diffusion to the workbench

A claim about diffusion now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running diffusion, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the diffusion result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/084-diffusion/README.md).*

---

### Excavation 085 — Denoising — Predicting What the Noise Hid

<!-- book-prose-v2 -->

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

For a moment, remain loyal to the simplest proposal: ask it to recreate the entire clean image directly from every noise level.

Its appeal is not ignorance but economy. Denoising should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: the task changes dramatically across noise strengths.

Notice what the counterexample has accomplished for denoising. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: tell the model the noise level and predict the added noise or equivalent clean direction.

Humanity eventually gathered this problem and its repairs under the name **Denoising**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace denoising with the old instruction to ask it to recreate the entire clean image directly from every noise level. The result is again that the task changes dramatically across noise strengths. Put back only the requirement to tell the model the noise level and predict the added noise or equivalent clean direction. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when denoising is introduced. The same evidence that defeated the attempt to ask it to recreate the entire clean image directly from every noise level is presented again. Only the ability to tell the model the noise level and predict the added noise or equivalent clean direction changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Predicting What the Noise Hid

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

Run the denoising scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside denoising

Before Denoising receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

xt is the noisy image already constructed in the example.
t tells the network how much corruption it faces.
The network predicts the exact noise ε that hid the clean image.
Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

##### Why no cheaper operation does the same job

[Subtracting predicted noise from actual noise](../MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
[The squared norm](../MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
[Expectation](../MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Every symbol in Denoising can now be read back into an action already performed. The whole procedure fits in one line:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

#### Where denoising runs out

Prediction parameterization and schedule affect stability and quality.

Why does that boundary remain? Denoising was built for one responsibility: tell the model the noise level and predict the added noise or equivalent clean direction. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take denoising to the workbench

The argument for denoising is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running denoising, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the denoising result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/085-denoising/README.md).*

---

## Part IX — Acting and Scaling

The system can describe and create, but action supplies no correct next token. It supplies consequences. We follow that new kind of evidence from rewards and future value through multimodal alignment, efficient adaptation, large-scale training, live service, adversarial testing, and governance.

---

### Excavation 086 — Rewards — Learning Without Correct Answers

<!-- book-prose-v2 -->

Denoising closes the image-generation loop. The field system can predict words and images, but an acting agent often receives no correct action label—only eventual success, damage, or failure.

Nothing yet appears to demand a new invention. We can label the correct action at every moment.

There is a real principle behind this restraint: the complexity of rewards must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: for exploration or games, nobody knows every correct intermediate move.

That distinction is the hinge on which rewards turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: provide outcome feedback and let experience connect actions with later consequences.

We have earned the chapter's shorter name: **Rewards**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that rewards is necessary rather than decorative. Delete its new responsibility and use the earlier plan to label the correct action at every moment. Immediately, for exploration or games, nobody knows every correct intermediate move. Reintroduce the single job to provide outcome feedback and let experience connect actions with later consequences. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can provide outcome feedback and let experience connect actions with later consequences. Because the old plan to label the correct action at every moment is the only displaced piece, the reader can locate exactly where rewards changes the outcome.

#### Learning Without Correct Answers

A maze gives +1 only at the exit; repeated trials reveal which earlier turns tend to reach it.

The name rewards is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where rewards runs out

Poor rewards create unintended shortcuts.

The weakness is not an accidental footnote. Every operation in rewards serves the narrower purpose to provide outcome feedback and let experience connect actions with later consequences; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take rewards to the workbench

Understanding rewards now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running rewards, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the rewards result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/086-rewards/README.md).*

---

### Excavation 087 — States, Actions, and Transitions

<!-- book-prose-v2 -->

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

The machinery already in our hands suggests that we store only action and final reward.

This is how states, actions, and transitions ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: the trouble appears immediately: the same action helps in one situation and harms in another.

The wrong answer makes the need for states, actions, and transitions inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to record current state, chosen action, reward, and resulting state.

The usual name, **States, Actions, and Transitions**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to store only action and final reward produces the observed failure: the trouble appears immediately: the same action helps in one situation and harms in another. Starting with the repaired demand to we need to record current state, chosen action, reward, and resulting state preserves the information the shortcut lost. The subject of states, actions, and transitions lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to record current state, chosen action, reward, and resulting state instead of merely trying to store only action and final reward. That controlled contrast is what turns a plausible explanation of states, actions, and transitions into an understandable derivation.

#### Understanding states, actions, and transitions

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

There are now two histories of this states, actions, and transitions case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where states, actions, and transitions runs out

A state representation may omit information needed for future decisions.

Look back at what states, actions, and transitions actually preserves: it can we need to record current state, chosen action, reward, and resulting state. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take states, actions, and transitions to the workbench

The reader has reconstructed states, actions, and transitions in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running states, actions, and transitions, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the states, actions, and transitions result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/087-states-actions-transitions/README.md).*

---

### Excavation 088 — Value — Estimating Future Consequences

<!-- book-prose-v2 -->

State–action–transition records make experience explicit. Immediate reward still cannot distinguish a move toward a distant rescue from a move into a dead end when neither pays off yet.

If the old idea can be stretched one step farther, we should choose the action with the largest reward right now.

If the proposal works on every relevant case, value is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: a small immediate treat can prevent reaching a larger later reward.

Nothing magical creates value. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: estimate the future reward expected from a state or state-action pair.

This boundary between the failed rule and its repair is the subject later work calls **Value**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize value; try to break it by subtraction. Remove the part that knows how to estimate the future reward expected from a state or state-action pair, leaving only the attempt to choose the action with the largest reward right now. What returns is not a vague weakness but the original contradiction: a small immediate treat can prevent reaching a larger later reward. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to choose the action with the largest reward right now receives the same test as the rule to estimate the future reward expected from a state or state-action pair. Their different outcomes reveal what value contributes without asking the reader to trust historical convention.

#### Estimating Future Consequences

One path gives 1 now; another gives 0 now and 10 next. Future value makes the second preferable.

Hold the setting, evidence, and desired outcome fixed while testing value. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### Where value runs out

Value estimates inherit errors from limited experience.

This is where value runs out for a causal reason. We gave it enough structure to estimate the future reward expected from a state or state-action pair, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take value to the workbench

A mathematical story about value earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running value, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the value result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/088-value-functions/README.md).*

---

### Excavation 089 — Q-Learning — Improving Values from Experience

<!-- book-prose-v2 -->

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

A careful builder would first avoid adding machinery and replace its value with the immediate reward.

The shortcut appears to retain everything q-learning needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: the update ignores the valuable state reached afterward.

The counterexample teaches q-learning. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: move the estimate toward reward plus the best discounted value available next.

Now—and not earlier—we may introduce **Q-Learning**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to replace its value with the immediate reward, and the case answers that the update ignores the valuable state reached afterward. With the narrow repair—to move the estimate toward reward plus the best discounted value available next—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Q-Learning returns to the same counterexample, replaces the attempt to replace its value with the immediate reward with the responsibility to move the estimate toward reward plus the best discounted value available next, and must succeed where the shortcut failed.

#### Improving Values from Experience

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

A formula for q-learning is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside q-learning

Before Q-Learning receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

The immediate reward is what happened now.
The largest next-state Q value represents the best continuation currently known.
Discount γ reduces distant evidence and keeps unending sums bounded.
Adding immediate and discounted future reward creates the target the old estimate moves toward.

##### Why no cheaper operation does the same job

[Addition](../MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
[γ scales future value](../MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
[Max](../MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

Every symbol in Q-Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

#### Where q-learning runs out

Maximization can overestimate noisy actions and offline data limits safe exploration.

The boundary can be predicted from the construction itself. Q-Learning performs the repair to move the estimate toward reward plus the best discounted value available next; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take q-learning to the workbench

Move q-learning from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running q-learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the q-learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/089-q-learning/README.md).*

---

### Excavation 090 — Policy Gradients — Improving the Choices Directly

<!-- book-prose-v2 -->

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

The obvious economy is to always choose the highest estimated action.

The proposal deserves a fair hearing. For policy gradients, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that early errors remove exploration and discrete choice blocks ordinary differentiation.

The failure changes the question behind policy gradients. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: sample from a policy and increase probability of actions followed by better-than-expected returns.

Only at this point does the inherited name **Policy Gradients** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of policy gradients by mentally removing the repair. We fall back to the proposal to always choose the highest estimated action; then early errors remove exploration and discrete choice blocks ordinary differentiation. Restore only the ability to sample from a policy and increase probability of actions followed by better-than-expected returns, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to always choose the highest estimated action to requiring the system to sample from a policy and increase probability of actions followed by better-than-expected returns. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to policy gradients.

#### Improving the Choices Directly

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

Put the old procedure beside policy gradients. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside policy gradients

Do not read the coming Policy Gradients line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

The sampled action probability comes from policy πθ.
Its log converts repeated action probabilities into additive learning signals.
Return G says how the chosen action eventually turned out.
The gradient changes θ in the direction that makes above-average rewarded actions more likely.

##### Why no cheaper operation does the same job

[The policy log](../MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
[Multiplying by return G](../MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
[Expectation](../MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Every symbol in Policy Gradients can now be read back into an action already performed. The whole procedure fits in one line:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

#### Where policy gradients runs out

Policy gradients are noisy and can exploit reward flaws.

The limit follows from the job assigned to policy gradients. Its repair knows how to sample from a policy and increase probability of actions followed by better-than-expected returns. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take policy gradients to the workbench

A claim about policy gradients now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running policy gradients, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the policy gradients result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/090-policy-gradients/README.md).*

---

### Excavation 091 — Multimodal Alignment

<!-- book-prose-v2 -->

Policy gradients let consequences reshape action probabilities. The field system's words, images, and actions still live in separate representational worlds unless paired observations can teach them to meet.

Before naming anything new, try to compare raw pixels directly with token IDs.

Its appeal is not ignorance but economy. Multimodal Alignment should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: their coordinates have unrelated meanings and shapes.

Notice what the counterexample has accomplished for multimodal alignment. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to use separate encoders and train paired image-text examples to become nearby.

Humanity eventually gathered this problem and its repairs under the name **Multimodal Alignment**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace multimodal alignment with the old instruction to compare raw pixels directly with token IDs. The result is again that their coordinates have unrelated meanings and shapes. Put back only the requirement to we need to use separate encoders and train paired image-text examples to become nearby. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when multimodal alignment is introduced. The same evidence that defeated the attempt to compare raw pixels directly with token IDs is presented again. Only the ability to we need to use separate encoders and train paired image-text examples to become nearby changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Understanding multimodal alignment

A tiger photo and “striped big cat” move together; mismatched captions move apart.

Run the multimodal alignment scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where multimodal alignment runs out

Pairs can contain weak, biased, or incomplete descriptions.

Why does that boundary remain? Multimodal Alignment was built for one responsibility: we need to use separate encoders and train paired image-text examples to become nearby. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take multimodal alignment to the workbench

The argument for multimodal alignment is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running multimodal alignment, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the multimodal alignment result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/091-multimodal-alignment/README.md).*

---

### Excavation 092 — Contrastive Learning

<!-- book-prose-v2 -->

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

The first defensible move is to pull every observed pair together without negatives.

There is a real principle behind this restraint: the complexity of contrastive learning must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the trouble appears immediately: all representations can collapse to one point.

That distinction is the hinge on which contrastive learning turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: compare each true pair against mismatched alternatives in the same batch.

We have earned the chapter's shorter name: **Contrastive Learning**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that contrastive learning is necessary rather than decorative. Delete its new responsibility and use the earlier plan to pull every observed pair together without negatives. Immediately, the trouble appears immediately: all representations can collapse to one point. Reintroduce the single job to compare each true pair against mismatched alternatives in the same batch. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can compare each true pair against mismatched alternatives in the same batch. Because the old plan to pull every observed pair together without negatives is the only displaced piece, the reader can locate exactly where contrastive learning changes the outcome.

#### Understanding contrastive learning

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

The name contrastive learning is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside contrastive learning

Do not read the coming Contrastive Learning line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

zi and ti are the matched image and text vectors.
Their dot product is the named alignment score.
Temperature T controls how sharply alternatives compete.
The denominator includes every candidate caption, preventing all examples from collapsing to one point.
The negative log penalizes the true pair when mismatches receive comparable scores.

##### Why no cheaper operation does the same job

[Each dot product](../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
[Dividing by temperature](../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
[The denominator sum](../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
[Negative log](../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Every symbol in Contrastive Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

#### Where contrastive learning runs out

False negatives may actually describe the same concept.

The weakness is not an accidental footnote. Every operation in contrastive learning serves the narrower purpose to compare each true pair against mismatched alternatives in the same batch; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take contrastive learning to the workbench

Understanding contrastive learning now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running contrastive learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the contrastive learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/092-contrastive-learning/README.md).*

---

### Excavation 093 — Speech and Audio

<!-- book-prose-v2 -->

Contrastive learning creates that relative competition. Sound introduces another modality whose pressure waveform is long, continuous, and shifted in time even when a listener hears the same event.

At this point the shortest path seems to be to treat every raw sample as an independent token.

This is how speech and audio ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: sequences are huge and local frequency structure is hidden.

The wrong answer makes the need for speech and audio inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: transform short windows into time-frequency features, then model their sequence.

The usual name, **Speech and Audio**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to treat every raw sample as an independent token produces the observed failure: sequences are huge and local frequency structure is hidden. Starting with the repaired demand to transform short windows into time-frequency features, then model their sequence preserves the information the shortcut lost. The subject of speech and audio lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to transform short windows into time-frequency features, then model their sequence instead of merely trying to treat every raw sample as an independent token. That controlled contrast is what turns a plausible explanation of speech and audio into an understandable derivation.

#### Understanding speech and audio

A whistle appears as sustained energy in one frequency band across several time windows.

There are now two histories of this speech and audio case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where speech and audio runs out

Spectrogram choices discard phase or fine timing.

Look back at what speech and audio actually preserves: it can transform short windows into time-frequency features, then model their sequence. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take speech and audio to the workbench

The reader has reconstructed speech and audio in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running speech and audio, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the speech and audio result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/093-speech-audio/README.md).*

---

### Excavation 094 — Low-Rank Adaptation

<!-- book-prose-v2 -->

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

We can postpone invention if we simply copy and fine-tune all parameters for every task.

If the proposal works on every relevant case, low-rank adaptation is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: storage and training cost multiply, and the base model is harder to preserve.

Nothing magical creates low-rank adaptation. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: freeze the base and learn a small low-rank correction to selected matrices.

This boundary between the failed rule and its repair is the subject later work calls **Low-Rank Adaptation**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize low-rank adaptation; try to break it by subtraction. Remove the part that knows how to freeze the base and learn a small low-rank correction to selected matrices, leaving only the attempt to copy and fine-tune all parameters for every task. What returns is not a vague weakness but the original contradiction: storage and training cost multiply, and the base model is harder to preserve. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to copy and fine-tune all parameters for every task receives the same test as the rule to freeze the base and learn a small low-rank correction to selected matrices. Their different outcomes reveal what low-rank adaptation contributes without asking the reader to trust historical convention.

#### Understanding low-rank adaptation

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

Hold the setting, evidence, and desired outcome fixed while testing low-rank adaptation. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside low-rank adaptation

Do not read the coming Low-Rank Adaptation line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

W is the frozen large matrix we refuse to duplicate.
A and B are the two narrow trainable matrices.
Their product BA creates a full-shaped correction while using far fewer values.
Addition preserves the base behavior and applies only the learned adaptation.

##### Why no cheaper operation does the same job

[BA](../MATHEMATICAL_MOVES.md#multiplication) composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.
[Adding that correction to W](../MATHEMATICAL_MOVES.md#addition) preserves the pretrained base and treats adaptation as a change. [The prime on W](../MATHEMATICAL_MOVES.md#symbol-decorations) marks the adapted version; replacing W would discard the knowledge we intended to keep.

Every symbol in Low-Rank Adaptation can now be read back into an action already performed. The whole procedure fits in one line:

$$
W^\prime=W+BA
$$

#### Where low-rank adaptation runs out

Low rank may be insufficient for large behavioral changes.

This is where low-rank adaptation runs out for a causal reason. We gave it enough structure to freeze the base and learn a small low-rank correction to selected matrices, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take low-rank adaptation to the workbench

A mathematical story about low-rank adaptation earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running low-rank adaptation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the low-rank adaptation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/094-lora/README.md).*

---

### Excavation 095 — Quantization

<!-- book-prose-v2 -->

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

The previous discovery seems almost sufficient: we could round every weight aggressively without measuring effect.

The shortcut appears to retain everything quantization needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: small but important distinctions disappear and outputs degrade.

The counterexample teaches quantization. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to map values to a limited set of levels using calibrated scale and test sensitive layers.

Now—and not earlier—we may introduce **Quantization**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to round every weight aggressively without measuring effect, and the case answers that small but important distinctions disappear and outputs degrade. With the narrow repair—to we need to map values to a limited set of levels using calibrated scale and test sensitive layers—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Quantization returns to the same counterexample, replaces the attempt to round every weight aggressively without measuring effect with the responsibility to we need to map values to a limited set of levels using calibrated scale and test sensitive layers, and must succeed where the shortcut failed.

#### Understanding quantization

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

A formula for quantization is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside quantization

Before Quantization receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

Real weight w is divided by scale s to express it in integer-sized steps.
Rounding chooses the nearest allowed integer q.
Multiplying q by s reconstructs the approximate weight used in computation.
The scale is calibrated so important values fit the available integer range.

##### Why no cheaper operation does the same job

[Dividing by scale s](../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
[Rounding](../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
[Multiplying q by s](../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Every symbol in Quantization can now be read back into an action already performed. The whole procedure fits in one line:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

#### Where quantization runs out

Lower precision trades accuracy for efficiency and hardware support varies.

The boundary can be predicted from the construction itself. Quantization performs the repair to we need to map values to a limited set of levels using calibrated scale and test sensitive layers; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take quantization to the workbench

Move quantization from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running quantization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the quantization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/095-quantization/README.md).*

---

### Excavation 096 — Distributed Training

<!-- book-prose-v2 -->

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

The least expensive next move is to let many machines train independent copies and combine them occasionally.

The proposal deserves a fair hearing. For distributed training, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: their parameters drift and duplicated work wastes computation.

The failure changes the question behind distributed training. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: partition data or model work, synchronize required results, and preserve one coherent update.

Only at this point does the inherited name **Distributed Training** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of distributed training by mentally removing the repair. We fall back to the proposal to let many machines train independent copies and combine them occasionally; then their parameters drift and duplicated work wastes computation. Restore only the ability to partition data or model work, synchronize required results, and preserve one coherent update, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let many machines train independent copies and combine them occasionally to requiring the system to partition data or model work, synchronize required results, and preserve one coherent update. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to distributed training.

#### Understanding distributed training

Two workers compute gradients on different batches, average them, then apply the same update.

Put the old procedure beside distributed training. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### Where distributed training runs out

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

The limit follows from the job assigned to distributed training. Its repair knows how to partition data or model work, synchronize required results, and preserve one coherent update. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take distributed training to the workbench

A claim about distributed training now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running distributed training, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the distributed training result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/096-distributed-training/README.md).*

---

### Excavation 097 — Inference Serving

<!-- book-prose-v2 -->

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

For a moment, remain loyal to the simplest proposal: run one request at a time on one full model.

Its appeal is not ignorance but economy. Inference Serving should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

Notice what the counterexample has accomplished for inference serving. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

Humanity eventually gathered this problem and its repairs under the name **Inference Serving**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace inference serving with the old instruction to run one request at a time on one full model. The result is again that the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. Put back only the requirement to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when inference serving is introduced. The same evidence that defeated the attempt to run one request at a time on one full model is presented again. Only the ability to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Understanding inference serving

Four prompts share one matrix operation while each retains separate token state.

Run the inference serving scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where inference serving runs out

Batching improves throughput but can worsen individual latency.

Why does that boundary remain? Inference Serving was built for one responsibility: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take inference serving to the workbench

The argument for inference serving is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running inference serving, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the inference serving result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/097-inference-serving/README.md).*

---

### Excavation 098 — Red Teaming

<!-- book-prose-v2 -->

Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.

Nothing yet appears to demand a new invention. We can evaluate only expected well-formed requests.

There is a real principle behind this restraint: the complexity of red teaming must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that real users, attackers, and accidents find paths designers never listed.

That distinction is the hinge on which red teaming turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations.

We have earned the chapter's shorter name: **Red Teaming**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that red teaming is necessary rather than decorative. Delete its new responsibility and use the earlier plan to evaluate only expected well-formed requests. Immediately, real users, attackers, and accidents find paths designers never listed. Reintroduce the single job to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. Because the old plan to evaluate only expected well-formed requests is the only displaced piece, the reader can locate exactly where red teaming changes the outcome.

#### Understanding red teaming

A hidden instruction in a retrieved page bypasses a normal demo; the case becomes a permanent injection test.

The name red teaming is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where red teaming runs out

No finite red team proves universal safety.

The weakness is not an accidental footnote. Every operation in red teaming serves the narrower purpose to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take red teaming to the workbench

Understanding red teaming now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running red teaming, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the red teaming result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/098-red-teaming/README.md).*

---

### Excavation 099 — Governance — Who Decides and Who Is Accountable?

<!-- book-prose-v2 -->

Red teaming discovers failures before ordinary traffic does. Deciding which risks are acceptable, who may approve deployment, and who is accountable cannot be delegated to the model being evaluated.

The machinery already in our hands suggests that we let builders decide every acceptable use because they understand the system.

This is how governance ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: affected users carry risks without authority, appeal, or visibility.

The wrong answer makes the need for governance inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries.

The usual name, **Governance**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to let builders decide every acceptable use because they understand the system produces the observed failure: affected users carry risks without authority, appeal, or visibility. Starting with the repaired demand to we need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries preserves the information the shortcut lost. The subject of governance lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries instead of merely trying to let builders decide every acceptable use because they understand the system. That controlled contrast is what turns a plausible explanation of governance into an understandable derivation.

#### Who Decides and Who Is Accountable

A lending model requires documented data, subgroup evaluation, human appeal, and a named owner before launch.

There are now two histories of this governance case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where governance runs out

Governance can become paperwork unless tied to real authority and enforcement.

Look back at what governance actually preserves: it can we need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take governance to the workbench

The reader has reconstructed governance in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running governance, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the governance result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/099-governance/README.md).*

---

### Excavation 100 — The Complete AI System — From Observation to Responsible Action

<!-- book-prose-v2 -->

Governance assigns legitimate decisions and responsibility around the technology. We can finally assemble data, models, tools, evaluation, operations, and authority into one complete AI system rather than treating the model as the whole product.

If the old idea can be stretched one step farther, we should connect every powerful component and call the result intelligent.

If the proposal works on every relevant case, the complete ai system is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: an accurate model with stale data, excessive authority, weak verification, or no accountability still fails.

Nothing magical creates the complete ai system. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another.

This boundary between the failed rule and its repair is the subject later work calls **The Complete AI System**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize the complete ai system; try to break it by subtraction. Remove the part that knows how to build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another, leaving only the attempt to connect every powerful component and call the result intelligent. What returns is not a vague weakness but the original contradiction: an accurate model with stale data, excessive authority, weak verification, or no accountability still fails. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to connect every powerful component and call the result intelligent receives the same test as the rule to build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another. Their different outcomes reveal what the complete ai system contributes without asking the reader to trust historical convention.

#### From Observation to Responsible Action

A support system retrieves current policy, drafts an answer, cites evidence, requests approval for refunds, verifies transactions, logs outcomes, and learns only through reviewed updates.

Hold the setting, evidence, and desired outcome fixed while testing the complete ai system. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The Expedition Continues

Excavation 100 closes this map, not discovery. New observations must be allowed to break the system and force the next invention.

#### Where the complete ai system runs out

No architecture completes intelligence forever; every deployment creates new observations and new responsibilities.

This is where the complete ai system runs out for a causal reason. We gave it enough structure to build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take the complete ai system to the workbench

A mathematical story about the complete ai system earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the complete ai system, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the complete ai system result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/100-complete-ai-system/README.md).*
