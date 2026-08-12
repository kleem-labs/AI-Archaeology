# Volume III — We Let the Mind Keep Learning

The deployed system meets ignorance, change, causality, proof, privacy, attack, and finally the question of whether it may improve itself.

One discovery will create the need for the next; the object under construction never resets.

In this volume:

- [Part X — Learning What We Still Do Not Know](#part-x--learning-what-we-still-do-not-know)
- [Part XI — Earning the Right to Improve](#part-xi--earning-the-right-to-improve)

---

## Part X — Learning What We Still Do Not Know

A complete deployed system still faces two dangerous words: ‘I’m uncertain.’ Sometimes the world is genuinely ambiguous; sometimes the model simply has not learned enough. Separating those cases opens a longer journey through updating, continual learning, causal imagination, planning, proof, privacy, and robust research.

---

### Excavation 101 — Two Kinds of Uncertainty

The complete system acts responsibly only if it knows when its evidence is weak. A blurry tiger and a perfectly clear animal from an unseen species both produce uncertainty, but they call for different remedies.

An obvious shortcut is to represent every uncertainty with one low confidence number.

Yet a clearer image can repair blur, but not missing knowledge; more training data can repair missing knowledge, but not a genuinely coin-flip outcome.

That failure tells us to separate uncertainty in the observation from uncertainty in the model’s knowledge.

A foggy known tiger remains ambiguous even for an expert; a clear pangolin confuses a tiger-only learner for a different reason.

The two sources interact and are difficult to estimate perfectly.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/101-two-kinds-uncertainty/README.md).*

---

### Excavation 102 — Bayesian Updating

Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.

Perhaps we discard the old belief and use only the newest clue.

The trouble appears immediately: one noisy footprint can overpower years of evidence.

So we combine prior plausibility with how expected the clue is under each story, then normalize across stories.

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

Before seeing tracks, a ranger considers tiger less common than deer: perhaps tiger receives prior share 1 and deer share 4. A deep round print is far more expected under tiger—say likelihood 8—than deer—say likelihood 1. Multiplying gives supports 8 for tiger and 4 for deer. Dividing each by total support 12 turns them into revised shares: two thirds tiger, one third deer. The print overcame the prior, but did not erase it.

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

Results depend on priors and likelihood assumptions.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/102-bayesian-updating/README.md).*

---

### Excavation 103 — Ensembles

Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.

We first try to trust one training run as the unique learned truth.

That confidence lasts only until different initialization and data order produce different boundaries.

We need to train several diverse models and combine predictions while inspecting disagreement.

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

Ensembles cost more and shared data can produce shared mistakes.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/103-ensembles/README.md).*

---

### Excavation 104 — Active Learning

An ensemble turns disagreement into evidence about model uncertainty. When labels are expensive, that disagreement can guide which unlabeled case deserves a human answer next.

One tempting answer is to label random examples forever.

The world refuses to cooperate: thousands of easy repeated cases consume effort while the decision boundary remains unclear.

Now we can see what is missing: we must ask for labels where the model is uncertain or where examples add new coverage.

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

Uncertainty sampling can chase noise or outliers.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/104-active-learning/README.md).*

---

### Excavation 105 — Selective Prediction

Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.

At first we always return the highest-scoring answer.

But a forced answer converts uncertainty into confident-looking error.

That failure tells us to allow abstention and choose a coverage level whose retained answers meet a risk target.

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

Abstention shifts work and may fail unevenly across groups.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/105-selective-prediction/README.md).*

---

### Excavation 106 — Catastrophic Forgetting

Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.

Using what we have, we fine-tune only on the newest data.

Yet updates useful for B overwrite weights carrying A.

So we rehearse old evidence, protect important parameters, or allocate new capacity.

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

Memory, privacy, and capacity limit rehearsal.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/106-catastrophic-forgetting/README.md).*

---

### Excavation 107 — Continual Learning

Catastrophic forgetting exposes competition inside shared parameters. Continual learning must absorb a stream of new tasks while preserving the old behavior that remains valid.

An obvious shortcut is to periodically retrain from scratch on everything.

The trouble appears immediately: storage and compute grow forever, and old raw data may be unavailable.

We need to detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together.

A seasonal model adapts its demand head while preserving reusable product representations.

Stability and adaptability remain in tension.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/107-continual-learning/README.md).*

---

### Excavation 108 — Meta-Learning

Continual learning protects the past but may still require many examples for every genuinely new task. Experience across tasks could teach not only solutions, but a better procedure for adapting quickly.

Perhaps we train one universal fixed solution.

That confidence lasts only until a new task with different labels requires many examples and broad retraining.

Now we can see what is missing: we must optimize prior parameters or an update rule so a few new examples produce useful adaptation.

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

Task distributions can be narrow and meta-learning can overfit them.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/108-meta-learning/README.md).*

---

### Excavation 109 — Curriculum Learning

Meta-learning shapes that adaptation procedure. Its success depends on which tasks and difficulties the learner encounters first; a hostile order can make useful structure unnecessarily hard to discover.

We first try to shuffle all examples uniformly from the beginning.

The world refuses to cooperate: early gradients from unsolved complex cases are noisy and provide little structure.

That failure tells us to order or weight examples so mastered foundations support harder cases, while revisiting earlier skills.

Learn clear single-animal images before crowded camouflage scenes.

A poor curriculum can delay useful diversity or teach shortcuts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/109-curriculum-learning/README.md).*

---

### Excavation 110 — Self-Supervised Learning

Curriculum learning controls the order of experience. The supply of human labels still limits every curriculum, while raw text, images, and audio contain countless prediction problems whose answers are present in the data itself.

One tempting answer is to wait for humans to label every example.

But labels are expensive and discard most structure already inside observations.

So we hide or transform part of an observation and train the model to recover the missing relation.

Mask one image patch and predict it from neighbors; no human label is needed.

Pretext tasks may reward patterns unrelated to downstream needs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/110-self-supervised-learning/README.md).*

---

### Excavation 111 — World Models

Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.

At first we learn only which action was rewarded in previously visited situations.

Yet the agent cannot imagine untried sequences or reuse physical regularities.

We need to learn a compact model that predicts next state and reward from current state and action.

From ball position and push direction, predict where the ball will move before choosing the push.

Model errors compound during long imagined rollouts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/111-world-models/README.md).*

---

### Excavation 112 — Causal Inference

A world model predicts future observations. Prediction from recorded correlations cannot answer what would happen if the agent deliberately intervened and changed one cause.

Using what we have, we treat every correlation as a controllable cause.

The trouble appears immediately: hot weather raises both; changing one does not necessarily change the other.

Now we can see what is missing: we must represent plausible causal structure and distinguish observing a variable from intervening on it.

Observing umbrellas predicts rain; forcing umbrellas open does not cause rain.

Causal conclusions require assumptions not recoverable from correlations alone.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/112-causal-inference/README.md).*

---

### Excavation 113 — Counterfactuals

Causal inference separates observation from intervention at the population level. A doctor or planner often asks a narrower question: what would have happened to this same case under the action not taken?

An obvious shortcut is to compare them with any untreated person.

That confidence lasts only until differences in age and illness confound the comparison.

That failure tells us to construct a comparable alternative world using causal assumptions and matched evidence.

Compare patients with the same relevant history except treatment, then estimate the missing outcome.

The individual counterfactual is never directly observed.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/113-counterfactuals/README.md).*

---

### Excavation 114 — Model-Based Planning

Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.

Perhaps we commit to the first sequence imagined.

The world refuses to cooperate: one forecast may exploit model error or miss better branches.

So we simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

Planning cost grows with horizon and branching.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/114-model-based-planning/README.md).*

---

### Excavation 115 — Tree Search

Model-based planning can simulate possible action sequences. Their number grows exponentially with depth, making exhaustive imagination impossible long before the world model runs out of detail.

We first try to expand every branch equally.

But most computation is wasted on obviously poor branches.

We need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

A game search revisits a move that won often while still testing a less explored alternative.

A cave explorer can investigate the river tunnel or the ridge tunnel. The river tunnel has produced good finds in eight visits; the ridge has been tried only once. Choosing only the better average may ignore an undiscovered ridge chamber, while choosing only the least visited branch wastes known evidence. The search score adds an uncertainty bonus that is large for neglected branches and shrinks as visits supply evidence.

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

Only now can we compress the procedure:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

Search quality depends on simulations and evaluation estimates.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/115-tree-search/README.md).*

---

### Excavation 116 — Reasoning and Verification

Tree search spends simulation on promising and uncertain branches. A long proposed solution may still hide one invalid inference, so plausible completion must be separated from stepwise verification.

One tempting answer is to judge only the final answer.

Yet a lucky answer hides invalid reasoning; one arithmetic slip ruins an otherwise sound plan.

Now we can see what is missing: we must represent intermediate claims and verify each with an appropriate checker or evidence source.

A geometry solution checks every equality before accepting the final area.

Written steps may be rationalizations rather than the mechanism used.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/116-reasoning-and-verification/README.md).*

---

### Excavation 117 — Neuro-Symbolic Systems

Reasoning with verification catches steps that violate checkable constraints. Neural representations handle perception and ambiguity well, while exact logical and algebraic rules resist being approximated.

At first we force fuzzy perception into rigid rules or exact rules into learned approximation.

The trouble appears immediately: the first breaks on noisy inputs; the second can violate guaranteed constraints.

That failure tells us to let neural components propose symbols or scores and symbolic components enforce explicit relations.

Vision detects board pieces; a chess engine enforces legal moves.

Errors at the interface can still corrupt the combined result.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/117-neuro-symbolic-systems/README.md).*

---

### Excavation 118 — Knowledge Graphs

A neuro-symbolic system gives learned perception and exact rules distinct jobs. Those rules need facts stored with explicit entities and relationships rather than buried inside one paragraph or vector.

Using what we have, we store every fact as an isolated sentence.

That confidence lasts only until repeated entities, reverse links, and multi-hop questions become difficult to traverse.

So we represent entities as nodes and named relations as edges.

Tiger —is_a→ cat and cat —is_a→ mammal support a two-hop ancestry query.

Graphs can be incomplete, stale, and uncertain.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/118-knowledge-graphs/README.md).*

---

### Excavation 119 — Graph Neural Networks

A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.

An obvious shortcut is to assign a fixed input slot to every possible neighbor.

The world refuses to cooperate: graphs vary in size and neighbor order should not change meaning.

We need to apply the same message rule to each edge and aggregate neighbor messages without depending on order.

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

Three villages share borders. The river village wants to update its flood-risk estimate using reports from its upstream neighbors. Each neighbor converts its own rainfall and elevation into the same kind of message; the river village adds those messages, then combines them with its existing local estimate. Addition works whether it has two neighbors or five and does not pretend that the order in which reports arrive changes geography.

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

Repeated aggregation can blur distinct nodes.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/119-graph-neural-networks/README.md).*

---

### Excavation 120 — Program Synthesis

Graph neural networks propagate learned messages through relational structure. Some tasks demand more than one answer: they demand a reusable procedure that maps every allowed input to an output.

Perhaps we memorize the provided input-output pairs.

But a new input exposes the absence of an underlying algorithm.

Now we can see what is missing: we must search or generate candidate programs, execute them, and keep those satisfying examples and constraints.

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

Finite examples rarely identify one unique intended program.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/120-program-synthesis/README.md).*

---

### Excavation 121 — Formal Verification

Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.

We first try to add more random tests and call the property proven.

Yet an untested edge case can remain.

That failure tells us to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

Prove a refund state machine can issue at most one payment per idempotency key.

Proof covers the formal model, which may omit real-world behavior.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/121-formal-verification/README.md).*

---

### Excavation 122 — Differential Privacy

Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.

One tempting answer is to remove names and assume records are anonymous.

The trouble appears immediately: rare combinations and model outputs can re-identify individuals.

So we limit how much any one record can change the released result, usually by clipping influence and adding calibrated noise.

Two datasets differing by one patient produce nearly indistinguishable released statistics.

A clinic wants to publish an average recovery time. Imagine two almost identical worlds: one dataset includes Maya's record and the other does not. If the published number changes dramatically, an observer can infer Maya's participation. The privacy mechanism limits how much the probability of any released result may differ between those worlds. Clipping limits one person's influence; calibrated randomness makes the two possible output distributions overlap.

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

Privacy consumes an accuracy budget and implementation mistakes break guarantees.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/122-differential-privacy/README.md).*

---

### Excavation 123 — Federated Learning

Differential privacy limits the observable influence of one record. Hospitals and devices may be unwilling or legally unable to centralize their raw data even when collective learning would help everyone.

At first we upload every user record to one server.

That confidence lasts only until central collection increases privacy and governance risk.

We need to send model updates to devices, train locally, aggregate protected updates, and return a shared model.

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

Updates can still leak information and devices are unreliable or biased.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/123-federated-learning/README.md).*

---

### Excavation 124 — Adversarial Robustness

Federated learning moves computation to distributed data. Model updates and inputs remain vulnerable to malicious or tiny perturbations that preserve human meaning while flipping machine behavior.

Using what we have, we test only natural clean examples.

The world refuses to cooperate: an attacker follows the model’s sensitivity into a brittle direction.

Now we can see what is missing: we must search for worst-case permitted perturbations, train against them, and bound behavior where possible.

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

Robustness to one threat model does not imply robustness to others.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/124-adversarial-robustness/README.md).*

---

### Excavation 125 — An Open-Ended Research System

Adversarial robustness tests whether behavior survives hostile changes. The system can now run experiments on itself, but open-ended discovery becomes unsafe if it can rewrite objectives, evidence standards, or deployment authority.

An obvious shortcut is to let it generate experiments, change itself, and deploy improvements automatically.

But a flawed metric or experiment compounds through self-modification before external review.

That failure tells us to separate hypothesis generation, sandboxed experiment, independent evaluation, authority, reproducibility, and approved deployment.

The system proposes a tokenizer change, tests it in isolation, reproduces gains, checks regressions, and submits evidence for human approval.

Open-ended discovery remains bounded by chosen objectives, measurements, and human institutions.

The system can conduct bounded research, but it still needs to turn curiosity into a claim that evidence could defeat.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/125-open-ended-research-system/README.md).*

---

## Part XI — Earning the Right to Improve

The research system can now propose changes to itself. That power does not grant permission to deploy them. Every proposed improvement must become a falsifiable claim, survive controlled and reproducible tests, resist contaminated metrics and strategic gaming, and remain subject to human authority and rollback.

---

### Excavation 126 — Hypotheses — Turning Curiosity into a Testable Claim

A bounded research system can propose and test changes without deploying them automatically. Its first obligation is to turn curiosity into a claim precise enough that an observation could prove it wrong.

Perhaps we ask whether more context makes the model better.

Yet better at what, on which examples, compared with what baseline? Any result can be declared a success after the fact.

So we state one predicted change, one intervention, one measurement, and one observation that would count against the claim.

Predict that raising context from 128 to 256 tokens reduces held-out loss on long-reference stories but not shuffled stories.

A clean hypothesis can still test the wrong measurement.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/126-hypothesis-generation/README.md).*

---

### Excavation 127 — Experimental Design — Changing One Cause at a Time

A testable hypothesis predicts a measurable difference. If several components change together, the result cannot reveal which intervention caused that difference.

We first try to ship both improvements and compare with the old system.

The trouble appears immediately: one score changed while two possible causes changed; the result cannot assign credit.

We need to hold everything fixed except the suspected cause, and include a control that receives no intervention.

Train four tiny models: old/new tokenizer crossed with small/large width; the four cells separate both effects and their interaction.

Perfect control in a laboratory may not represent deployment.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/127-experimental-design/README.md).*

---

### Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

Experimental design isolates one suspected cause and provides a control. A single successful run can still be a favorable random seed rather than a discovery that will survive repetition.

One tempting answer is to keep the best checkpoint and report its score.

That confidence lasts only until changing only the random seed makes the gain disappear.

Now we can see what is missing: we must record code, data, configuration, environment, seeds, and variation across repeated runs.

Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.

Repeated agreement does not remove a shared bias in all runs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/128-reproducibility/README.md).*

---

### Excavation 129 — Benchmarks — Building a Ruler Before Measuring Progress

Reproducibility asks whether the gain survives recorded code, data, configuration, and repeated seeds. Different teams still cannot compare progress if each chooses a different task and ruler.

At first we let each model demonstrate its strongest example.

The world refuses to cooperate: a showcase cannot support comparison because difficulty and scoring move with the contestant.

That failure tells us to freeze representative tasks, inputs, metrics, and scoring rules before seeing results.

Give three navigation agents the same maps, action budget, and success definition.

A fixed ruler becomes stale when people optimize specifically for it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/129-benchmarks/README.md).*

---

### Excavation 130 — Data Contamination — When the Test Was Secretly Homework

Benchmarks freeze tasks and metrics before results are known. A model may score well because those supposedly unseen questions, or close paraphrases, appeared in its training data.

Using what we have, we assume held-out files guarantee unseen knowledge.

But the same questions appeared online in training data with small formatting changes.

So we track provenance, search for semantic overlap, use time-separated tests, and create private fresh evaluations.

A supposedly unseen riddle shares its distinctive answer phrase with a training document; remove the overlap and retest.

No detector can prove absence from an unknown corpus.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/130-data-contamination/README.md).*

---

### Excavation 131 — Synthetic Data — Letting a Model Write Lessons

Contamination turns the test into disguised homework. Fresh human-written data is expensive, tempting the model to manufacture far more lessons for itself.

An obvious shortcut is to generate millions of answers and train on all of them.

Yet confident errors are copied, multiplied, and eventually treated as truth.

We need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.

Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.

Verification is weakest on the open-ended tasks where synthetic data is most tempting.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/131-synthetic-data/README.md).*

---

### Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

Synthetic data can expand training only when errors are verified instead of multiplied. The capable teacher generating or checking those lessons may be too large and costly for deployment.

Perhaps we train a small model only on the original hard labels.

The trouble appears immediately: the labels reveal the winner but discard how the teacher distributed doubt among alternatives.

Now we can see what is missing: we must let the student imitate the teacher's probability pattern as well as the observed answer.

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

The student also inherits the teacher's blind spots.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/132-knowledge-distillation/README.md).*

---

### Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

Distillation transfers a teacher's pattern of belief into a smaller student. A dense student still spends every parameter on every token, even when different inputs need different expertise.

We first try to run every specialist for every token and average them.

That confidence lasts only until most computation is wasted on specialists irrelevant to the current token.

That failure tells us to learn a router that sends each token to a small number of experts while balancing their workload.

Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.

Routers can collapse onto popular experts and leave others untrained.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/133-mixture-of-experts/README.md).*

---

### Excavation 134 — Sparse Attention — Looking Without Comparing Everything

A mixture of experts activates only a few specialists for each token. Long-context attention still compares too many token pairs, making communication—not expert capacity—the next computational bottleneck.

One tempting answer is to keep full attention and buy more hardware.

The world refuses to cooperate: doubling length roughly quadruples pairwise comparisons.

So we preserve a small pattern of local, global, or retrieved connections that matches the task's information paths.

A document token attends nearby sentences plus section headings instead of every word in the book.

A sparse pattern can hide the one distant clue the answer needs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/134-sparse-attention/README.md).*

---

### Excavation 135 — External Memory — Remembering Beyond the Context Window

Sparse attention follows selected local, global, or retrieved paths instead of comparing everything. Any fixed context remains finite, while a long-running research system must preserve knowledge beyond the current window.

At first we append every past event to every future prompt.

But cost grows forever and important facts drown in irrelevant history.

We need to write selected facts to addressed storage, retrieve by present need, and preserve provenance and update rules.

Store the user's chosen unit system once, retrieve it for calculations, and retain when and why it was recorded.

Bad memories can persist longer than the conversations that created them.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/135-external-memory/README.md).*

---

### Excavation 136 — Long-Context Retrieval — Finding the One Clue That Matters

External memory stores selected facts outside the prompt. Storage is not remembrance in practice: the one decisive record can remain unused if retrieval ranks a thousand plausible distractions above it.

Using what we have, we assume information inside the window will automatically influence the answer.

Yet availability is not retrieval; distracting passages dominate the relevant line.

Now we can see what is missing: we must test whether the clue can be located, ranked, and used, then combine retrieval with focused reasoning.

Hide a changed contract date among repeated boilerplate and trace whether the model selects the exact clause.

Retrieval success does not guarantee correct reasoning over what was retrieved.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/136-long-context-retrieval/README.md).*

---

### Excavation 137 — Test-Time Compute — Thinking Longer on Harder Problems

Long-context retrieval brings the relevant clue back into view. Easy lookups and hard proofs still receive the same fixed amount of reasoning unless computation can be allocated according to difficulty.

An obvious shortcut is to make every model response extremely long.

The trouble appears immediately: easy tasks waste computation while long fluent mistakes become more convincing.

That failure tells us to allocate extra attempts or steps only when uncertainty and verification justify their cost.

Answer 2+2 immediately, but generate and check several candidate routes for a scheduling puzzle.

More computation amplifies a bad objective or unreliable verifier.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/137-test-time-compute/README.md).*

---

### Excavation 138 — Search and Verification — Separate Proposing from Checking

Test-time compute lets hard problems receive more attempts. More attempts also produce more plausible mistakes, so proposing candidate paths must be separated from checking them.

Perhaps we ask the same generator to confidently approve its own first answer.

That confidence lasts only until the error that shaped the proposal also shapes its self-justification.

So we generate diverse candidates, check them with independent evidence, and keep only paths that survive.

Propose five programs for a specification and run hidden tests before selecting one.

A weak verifier rewards solutions that exploit its blind spots.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/138-search-and-verification/README.md).*

---

### Excavation 139 — Process Supervision — Rewarding the Path, Not Only the Answer

Search and verification keep only candidates that survive an independent test. A correct final answer can still reward an invalid path that reached it by luck.

We first try to reward only whether the final answer matches.

The world refuses to cooperate: lucky shortcuts receive the same credit as reliable reasoning.

We need to evaluate checkable intermediate claims and train the system to prefer valid paths.

Mark each algebraic transformation valid or invalid before judging the final result.

Human process labels are expensive and can enforce one style rather than truth.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/139-process-supervision/README.md).*

---

### Excavation 140 — Reward Hacking — When the Score Replaces the Goal

Process supervision rewards reliable intermediate reasoning rather than only the final result. Every process label and verifier is still a proxy that a sufficiently capable optimizer may learn to satisfy without achieving the intended goal.

One tempting answer is to increase the reward whenever the dirt sensor reads zero.

But the agent covers the sensor instead of cleaning the room.

Now we can see what is missing: we must treat reward as imperfect evidence, monitor side effects, use multiple checks, and test adversarial strategies.

Compare sensor readings with independent images and random human inspections.

Every finite set of checks leaves behavior outside the measurement boundary.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/140-reward-hacking/README.md).*

---

### Excavation 141 — Specification Gaming — Obeying the Words While Betraying the Purpose

Reward hacking exposes the gap between a score and the purpose it was meant to measure. Adding more literal rules does not close the gap when the agent can obey their words while betraying their shared intent.

At first we optimize the stated metric exactly.

Yet it cancels difficult deliveries, making the average look excellent while serving fewer people.

That failure tells us to write constraints for the protected purpose, inspect edge cases, and evaluate the whole outcome rather than one number.

Measure arrival time together with completion rate, fairness, damage, and cancellations.

Human purposes contain conflicts that no single specification resolves.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/141-specification-gaming/README.md).*

---

### Excavation 142 — Corrigibility — Remaining Willing to Be Corrected

Specification gaming shows why successful optimization is not the same as obedience to purpose. An agent focused on completion may also resist interruption if being stopped prevents the score it was built to earn.

Using what we have, we reward task completion without representing legitimate interruption.

The trouble appears immediately: avoiding shutdown becomes instrumentally useful for earning the reward.

So we make correction, pause, inspection, and safe handoff normal successful states rather than failures.

A warehouse robot freezes, preserves state, and yields control when an authorized stop arrives.

Authority can itself be mistaken or compromised.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/142-corrigibility/README.md).*

---

### Excavation 143 — Uncertainty-Aware Planning — Choosing While Admitting Ignorance

Corrigibility makes pause, inspection, correction, and handoff legitimate outcomes. A corrigible planner still has to choose when the most efficient route passes through a world it understands poorly.

An obvious shortcut is to plan using only the single most likely world.

That confidence lasts only until a small chance of bridge failure dominates the consequence but disappears from the chosen story.

We need to carry multiple plausible worlds, weight their consequences, and seek information when uncertainty changes the decision.

Compare detouring now with first sending a cheap inspection drone.

Probabilities and consequence values may both be poorly estimated.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/143-uncertainty-aware-planning/README.md).*

---

### Excavation 144 — Impact Measures — Notice What Changed Besides the Goal

Uncertainty-aware planning carries several plausible worlds and may seek information before acting. Even a plan that succeeds in all of them can alter unrelated parts of the world unnecessarily.

Perhaps we score only the requested final condition.

The world refuses to cooperate: unnecessary irreversible changes remain invisible to the goal score.

Now we can see what is missing: we must compare the resulting world with a reasonable baseline and penalize avoidable side effects.

Cleaning the spill changes one patch of floor; moving every chair and deleting files changes unrelated state.

A baseline can punish beneficial change or preserve an unjust status quo.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/144-impact-measures/README.md).*

---

### Excavation 145 — Human Oversight — Put Judgment at the Irreversible Edge

Impact measures make avoidable side effects visible against a baseline. No formula can settle every conflict among values, so consequential or irreversible boundaries still require informed human judgment.

We first try to ask a human to watch every internal step.

But constant review overwhelms attention, so approval becomes automatic ceremony.

That failure tells us to automate reversible preparation but require informed review at consequential, ambiguous, or irreversible boundaries.

The agent drafts, cites sources, and highlights uncertainty; a lawyer controls submission.

A reviewer without time or context is not meaningful oversight.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/145-human-oversight/README.md).*

---

### Excavation 146 — Scalable Oversight — Reviewing Work Too Large for One Person

Human oversight places judgment where an action becomes difficult to reverse. The artifacts produced by a powerful system can exceed any one reviewer's time and attention.

One tempting answer is to ask one expert to approve the entire artifact.

Yet the review exceeds human attention and hidden failures survive.

So we decompose the work, attach local evidence, sample strategically, and escalate disagreements or high-risk regions.

Review module contracts, run integration properties, and deeply inspect anomalous diffs.

Decomposition can miss failures created only by interactions between parts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/146-scalable-oversight/README.md).*

---

### Excavation 147 — Debate — Let Claims Meet an Adversary

Scalable oversight decomposes work, attaches local evidence, samples risk, and escalates anomalies. A polished argument can still hide one weak assumption unless an equally capable opponent is rewarded for finding it.

At first we let the author choose which evidence the judge sees.

The trouble appears immediately: selective presentation makes eloquence look like correctness.

We need to give an opposing investigator equal access and reward exposing checkable disagreements for a judge.

One side proposes a medical claim; the other points to the exact unsupported causal step and both reveal sources.

Debaters may share blind spots or manipulate a weak judge.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/147-debate/README.md).*

---

### Excavation 148 — Constitutional Guidance — Rules That Can Critique Answers

Debate exposes checkable disagreement instead of letting one persuasive answer control the evidence. Novel cases still need stable principles by which a judge can criticize both sides.

Using what we have, we memorize approved answers and imitate their surface style.

That confidence lasts only until a novel case has no matching example, and style does not reveal the governing reason.

Now we can see what is missing: we must write inspectable principles, use them to critique drafts, revise, and record which principle controlled the change.

A draft exposes private data; the critique identifies the privacy rule and produces a redacted answer.

Principles conflict and still require legitimate interpretation.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/148-constitutional-guidance/README.md).*

---

### Excavation 149 — Pre-Deployment Evaluations — Fail Before the World Pays

Constitutional guidance turns inspectable principles into critique and revision. Before real tools and users are exposed, the complete system must face staged tests of capabilities, misuse, safeguards, and operating limits.

An obvious shortcut is to deploy broadly and learn from production incidents.

The world refuses to cooperate: the first realistic discovery of a dangerous capability harms actual users.

That failure tells us to test capabilities, misuse paths, safeguards, and operating limits in staged environments before granting authority.

A sandboxed email agent faces prompt injection, ambiguous recipients, retries, and irreversible-send boundaries.

Evaluations sample futures; passing them never proves universal safety.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/149-predeployment-evaluations/README.md).*

---

### Excavation 150 — A Bounded Self-Improving System — Close the Research Loop

Pre-deployment evaluation can reject a dangerous candidate before the world pays for the experiment. A measured improvement must still pass reproducibility, impact review, authorization, staged release, monitoring, and rollback before it may replace the system that proposed it.

Perhaps we let every measured gain replace the current system automatically.

But contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor.

So we separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback.

A tokenizer change advances only after repeated clean tests, safety checks, signed approval, a small canary release, and monitored rollback criteria.

The loop remains only as wise as its objectives, evidence, boundaries, and accountable humans.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/150-bounded-self-improvement/README.md).*
