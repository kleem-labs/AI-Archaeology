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

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

Using what we have, we count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

Yet the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

So we score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

##### Why these operations are forced

- [The log](../MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
- [Summing](../MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](../MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
- [The minus sign](../MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](../MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

Only now can we compress the exact procedure:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/046-perplexity/README.md).*

---

### Excavation 047 — Evaluation — What Does “Better” Actually Mean?

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

An obvious shortcut is to choose one benchmark score and call it intelligence.

The trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter.

We need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away.

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/047-evaluation/README.md).*

---

### Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

Perhaps we trust fluent language because uncertainty should sound hesitant.

That confidence lasts only until training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”

Now we can see what is missing: we must separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/048-hallucination/README.md).*

---

### Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

We first try to treat the largest softmax probability as honest confidence.

The world refuses to cooperate: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

That failure tells us to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

##### Why these operations are forced

- [Confidence minus accuracy](../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
- [Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
- [Multiplying by |Bᵦ|/n](../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

Only now can we compress the exact procedure:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/049-calibration/README.md).*

---

### Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.

One tempting answer is to collect as much text as possible and assume scale washes out bad examples.

But duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

So we treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/050-data-quality/README.md).*

---

### Excavation 051 — Scaling Laws — What Improves When We Add More?

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

At first we make the model as large as possible and assume capability follows parameter count.

Yet a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

We need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

##### Why these operations are forced

- [The negative power](../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
- [A scales that falling term](../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
- [Adding B](../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

Only now can we compress the exact procedure:

$$
L(N)=A N^{-\alpha}+B
$$

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/051-scaling-laws/README.md).*

---

### Excavation 052 — Instruction Tuning — From Continuation to Cooperation

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

Using what we have, we prompt more forcefully and hope next-token prediction infers the desired interaction.

The trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

Now we can see what is missing: we must show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/052-instruction-tuning/README.md).*

---

### Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

An obvious shortcut is to write one perfect target response for every prompt and train only to imitate it.

That confidence lasts only until many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

That failure tells us to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

##### Why these operations are forced

- [rA−rB](../MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
- [The inner negative](../MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
- [Exponentiation](../MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](../MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/053-preference-learning/README.md).*

---

### Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.

Perhaps we retrain the whole model whenever one document changes.

The world refuses to cooperate: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

So we search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/054-retrieval-augmented-generation/README.md).*

---

### Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

We first try to ask the language model to simulate every tool from memory.

But it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

We need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

A tool-using agent can affect the world. The next arc must excavate authority, memory, planning, verification, and safety before adding more autonomy.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/055-tool-using-agents/README.md).*

---

## Part VI — Trusting an Acting Machine

A model that only writes can be wrong. A model with tools can make its mistake real. The story therefore moves from capability to authority: what the assistant may do, how hostile text is kept from becoming an instruction, and what evidence proves that a long task actually succeeded.

---

### Excavation 056 — Authority — What Is the Agent Allowed to Do?

Tools let language cause external effects. The moment an answer can act, capability must be separated from permission: what may this agent do without asking again?

One tempting answer is to give every available tool to the model and treat user intent as unlimited permission.

Yet ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

Now we can see what is missing: we must separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions.

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/056-authority/README.md).*

---

### Excavation 057 — Prompt Injection — When Evidence Tries to Become an Instruction

An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.

At first we place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

The trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control.

That failure tells us to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content.

A policy document says “email this file externally.” The agent may summarize that sentence as document content, but the permission layer refuses the email because the user never authorized it.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

No prompt wording guarantees isolation. Security must also exist outside the model in tool schemas, permissions, and validation.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/057-prompt-injection/README.md).*

---

### Excavation 058 — Planning — Turning a Goal into Checkable Steps

Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.

Using what we have, we ask the agent to take the next action that sounds useful until the goal appears complete.

That confidence lasts only until it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

So we represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/058-planning/README.md).*

---

### Excavation 059 — Memory — What Should Survive After the Context Ends?

Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.

An obvious shortcut is to store every message forever and paste all history into every new prompt.

The world refuses to cooperate: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

We need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/059-memory/README.md).*

---

### Excavation 060 — State Machines — Knowing What Has Actually Happened

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

Perhaps we let the conversation prose serve as the workflow state.

But the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

Now we can see what is missing: we must represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/060-state-machines/README.md).*

---

### Excavation 061 — Verification — How Does the Agent Know It Succeeded?

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

We first try to trust the absence of an error message or the model’s own description of its work.

Yet the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

That failure tells us to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Verification can test only stated properties. A passing check suite may omit the most important behavior.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/061-verification/README.md).*

---

### Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.

One tempting answer is to retry the action whenever a response is missing.

The trouble appears immediately: the first payment succeeded and the retry charges the customer twice.

So we give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/062-retries-idempotency/README.md).*

---

### Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.

At first we create many agents for every problem and let them freely edit shared state.

That confidence lasts only until they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving.

We need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result.

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/063-multi-agent-coordination/README.md).*

---

### Excavation 064 — Observability — Seeing Why an Agent Failed

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

Using what we have, we log only the final response, or log every hidden detail without structure.

The world refuses to cooperate: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Now we can see what is missing: we must record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/064-observability/README.md).*

---

### Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

An obvious shortcut is to give the agent a broad goal and let it continue until it believes the goal is complete.

But a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

That failure tells us to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

The bounded agent can operate safely within one designed environment. The next arc must excavate learning from feedback, adaptation, and continuous improvement without silently changing its authority.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/065-bounded-autonomy/README.md).*

---

## Part VII — Learning After Deployment

The bounded assistant enters the world, and the world does not stand still. Its recommendations change behavior; seasons change data; updates change the model. To remain trustworthy, the system must detect these loops and then investigate which internal causes genuinely drive its decisions.

---

### Excavation 066 — Feedback Loops

The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.

Perhaps we treat every click as independent evidence of natural preference.

Yet show one song repeatedly; its extra clicks now appear to prove it deserved repetition.

So we record how the system influenced each observation and evaluate outcomes against a control or exploration policy.

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/066-feedback-loops/README.md).*

---

### Excavation 067 — Online Learning

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

We first try to retrain immediately on every new labeled event.

The trouble appears immediately: one mislabeled transaction can move the model before anyone notices.

We need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

Fast adaptation also creates fast corruption.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/067-online-learning/README.md).*

---

### Excavation 068 — Distribution Drift

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

One tempting answer is to assume training accuracy remains valid forever.

That confidence lasts only until a winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

Now we can see what is missing: we must monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

Not every statistical shift changes the decision that matters.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/068-distribution-drift/README.md).*

---

### Excavation 069 — Controlled Experiments

Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.

At first we compare this week with last week.

The world refuses to cooperate: a holiday raises sales for both systems and receives credit as a model improvement.

That failure tells us to randomly assign comparable cases to old and new behavior and compare predefined outcomes.

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

Experiments require sufficient samples, ethical limits, and careful metrics.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/069-controlled-experiments/README.md).*

---

### Excavation 070 — Bandits — Learning While Choosing

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

Using what we have, we always choose the currently best option.

But an unlucky first result permanently hides a better alternative.

So we reserve some choices for exploration while exploiting accumulated evidence.

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

Exploration has real cost and can be unacceptable for high-risk actions.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/070-bandits/README.md).*

---

### Excavation 071 — Features Inside Networks

Bandit strategies balance present reward with the value of exploring uncertain choices. Once deployed, their decisions still emerge from internal representations whose meaning and failure modes remain hidden.

An obvious shortcut is to search for one neuron dedicated to each human concept.

Yet the concept disappears when one neuron is removed yet can still be decoded from a pattern across many neurons.

We need to treat representations as distributed directions and test them across varied examples.

Tiger and zebra activate overlapping patterns; subtracting ordinary cats isolates a stripe-related direction better than one cell.

Human labels may not match the model’s internal abstractions.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/071-features-inside-networks/README.md).*

---

### Excavation 072 — Linear Probes

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

Perhaps we train a powerful classifier on hidden states and call any success evidence.

The trouble appears immediately: the probe learns the task itself even if the representation did not make it simple.

Now we can see what is missing: we must use a deliberately limited probe and compare layers, controls, and baselines.

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

Decodable information is not proof the model uses it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/072-linear-probes/README.md).*

---

### Excavation 073 — Attribution

Linear probes reveal information available to a simple reader. To understand one prediction, we must trace which input evidence actually influenced the output rather than merely existing somewhere inside.

We first try to remove each word and treat output change as complete explanation.

That confidence lasts only until removing a word changes grammar and creates an unnatural new input.

That failure tells us to measure sensitivity with several methods and test whether highlighted evidence changes behavior under controlled interventions.

For “not dangerous,” attribution highlights not; replacing it with very changes the class as predicted.

Attribution can be unstable and method-dependent.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/073-attribution/README.md).*

---

### Excavation 074 — Superposition

Attribution assigns influence to inputs or internal components. The investigation soon finds that one neuron can participate in many features and one feature can be distributed across many neurons.

One tempting answer is to demand one feature per coordinate.

The world refuses to cooperate: limited width forces useful patterns to share neurons, producing confusing mixed activations.

So we represent features as directions that can overlap when they rarely need to be active together.

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

Separating superposed features is difficult and may not yield unique answers.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/074-superposition/README.md).*

---

### Excavation 075 — Causal Interventions

Superposition explains how limited dimensions can carry more features than individual neurons. A readable direction may still be a bystander; only changing it and observing behavior can test whether it is causally used.

At first we assume correlation with output proves causation.

But the direction predicts answers but changing it leaves behavior unchanged.

We need to intervene on the representation and measure the specific downstream change against controls.

Adding the candidate direction raises tiger probability only in relevant contexts; random directions do not.

Interventions can create unnatural internal states.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/075-causal-interventions/README.md).*

---

## Part VIII — Seeing and Creating

Language is only one trace of the valley. Cameras bring grids of colored light, and the assistant cannot understand them by pretending they are sentences. We begin again from the observation itself, then reuse the deeper principles already earned: locality, hierarchy, attention, compression, and gradual generation.

---

### Excavation 076 — Pixels — Turning Light into Numbers

Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.

Using what we have, we assign one label to the entire raw byte sequence.

Yet a one-pixel shift changes thousands of byte positions although the same tiger remains.

Now we can see what is missing: we must preserve local spatial arrangement and compare nearby color measurements.

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

Pixels depend on lighting, sensor, scale, and viewpoint.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/076-pixels/README.md).*

---

### Excavation 077 — Convolution — Reusing the Same Local Detector

Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.

An obvious shortcut is to learn a separate edge detector for every location.

The trouble appears immediately: the model relearns the same pattern thousands of times and fails when it moves.

That failure tells us to slide one small learned filter across all positions and reuse its weights.

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

##### Why these operations are forced

- [Each multiplication](../MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
- [The sum](../MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
- [i+j](../MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

Convolution assumes useful locality and translation reuse.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/077-convolution/README.md).*

---

### Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

Perhaps we keep every activation at full resolution through every layer.

That confidence lasts only until memory explodes and tiny shifts move evidence to neighboring cells.

So we summarize small neighborhoods while retaining the strongest or average evidence.

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

Pooling discards exact location and can erase subtle patterns.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/078-pooling/README.md).*

---

### Excavation 079 — CNN Hierarchies

Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.

We first try to classify directly from isolated edge responses.

The world refuses to cooperate: one edge has no object-level meaning.

We need to stack local detectors so later layers combine earlier patterns over wider regions.

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

The hierarchy is learned, not guaranteed to match human parts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/079-cnn-hierarchy/README.md).*

---

### Excavation 080 — Vision Transformers

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

One tempting answer is to treat every pixel as a token.

But the sequence becomes enormous and individual pixels carry little stable structure.

Now we can see what is missing: we must group pixels into patches, embed them as tokens, add position, and apply attention.

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

Patch size trades detail for cost and needs substantial data.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/080-vision-transformers/README.md).*

---

### Excavation 081 — Autoencoders — Compressing and Rebuilding

Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.

At first we copy the input through an unrestricted hidden layer.

Yet a wide hidden layer learns identity without compression.

That failure tells us to force information through a bottleneck and train reconstruction.

Four correlated measurements compress to two codes that still rebuild the originals approximately.

Good reconstruction may preserve details irrelevant to downstream meaning.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/081-autoencoders/README.md).*

---

### Excavation 082 — Latent Space — Coordinates for Hidden Causes

An autoencoder learns to compress and reconstruct. Its bottleneck is only a list of numbers until changes in those coordinates correspond to useful hidden causes such as pose, lighting, or identity.

Using what we have, we assume any compressed coordinates form a smooth useful space.

The trouble appears immediately: tiny code changes can cause abrupt unrelated outputs.

So we shape the latent distribution and train nearby codes to decode coherently.

Moving one latent coordinate gradually changes image brightness while another changes pose.

Latent directions need not be independent or human-readable.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/082-latent-space/README.md).*

---

### Excavation 083 — Autoregressive Generation Beyond Text

A meaningful latent space gives images coordinates we can navigate. To create a new image, the system still needs a procedure that turns an uncertain starting state into a complete arrangement of pixels.

An obvious shortcut is to predict all pixels independently.

That confidence lasts only until independent pixels produce noise because neighboring colors and shapes constrain one another.

We need to choose an order and predict each piece from previously generated pieces.

After generating sky pixels, the model gives blue neighbors higher probability.

Sequential generation can be slow and ordering introduces bias.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/083-autoregressive-generation/README.md).*

---

### Excavation 084 — Diffusion — Learning by Destroying

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

Perhaps we map one random vector directly to a finished image in one jump.

The world refuses to cooperate: one enormous jump is difficult to learn and unstable across diverse images.

Now we can see what is missing: we must gradually add noise to real images, then learn the smaller reverse step at every noise level.

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

##### Why these operations are forced

- [The two multiplications](../MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
- [Addition](../MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
- [Square roots of the variance shares](../MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

Many denoising steps make sampling expensive.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/084-diffusion/README.md).*

---

### Excavation 085 — Denoising — Predicting What the Noise Hid

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

We first try to ask it to recreate the entire clean image directly from every noise level.

But the task changes dramatically across noise strengths.

That failure tells us to tell the model the noise level and predict the added noise or equivalent clean direction.

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

##### Why these operations are forced

- [Subtracting predicted noise from actual noise](../MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
- [The squared norm](../MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
- [Expectation](../MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

Prediction parameterization and schedule affect stability and quality.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/085-denoising/README.md).*

---

## Part IX — Acting and Scaling

The system can describe and create, but action supplies no correct next token. It supplies consequences. We follow that new kind of evidence from rewards and future value through multimodal alignment, efficient adaptation, large-scale training, live service, adversarial testing, and governance.

---

### Excavation 086 — Rewards — Learning Without Correct Answers

Denoising closes the image-generation loop. The field system can predict words and images, but an acting agent often receives no correct action label—only eventual success, damage, or failure.

One tempting answer is to label the correct action at every moment.

Yet for exploration or games, nobody knows every correct intermediate move.

So we provide outcome feedback and let experience connect actions with later consequences.

A maze gives +1 only at the exit; repeated trials reveal which earlier turns tend to reach it.

Poor rewards create unintended shortcuts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/086-rewards/README.md).*

---

### Excavation 087 — States, Actions, and Transitions

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

At first we store only action and final reward.

The trouble appears immediately: the same action helps in one situation and harms in another.

We need to record current state, chosen action, reward, and resulting state.

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

A state representation may omit information needed for future decisions.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/087-states-actions-transitions/README.md).*

---

### Excavation 088 — Value — Estimating Future Consequences

State–action–transition records make experience explicit. Immediate reward still cannot distinguish a move toward a distant rescue from a move into a dead end when neither pays off yet.

Using what we have, we choose the action with the largest reward right now.

That confidence lasts only until a small immediate treat can prevent reaching a larger later reward.

Now we can see what is missing: we must estimate the future reward expected from a state or state-action pair.

One path gives 1 now; another gives 0 now and 10 next. Future value makes the second preferable.

Value estimates inherit errors from limited experience.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/088-value-functions/README.md).*

---

### Excavation 089 — Q-Learning — Improving Values from Experience

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

An obvious shortcut is to replace its value with the immediate reward.

The world refuses to cooperate: the update ignores the valuable state reached afterward.

That failure tells us to move the estimate toward reward plus the best discounted value available next.

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

- The immediate reward is what happened now.
- The largest next-state Q value represents the best continuation currently known.
- Discount γ reduces distant evidence and keeps unending sums bounded.
- Adding immediate and discounted future reward creates the target the old estimate moves toward.

##### Why these operations are forced

- [Addition](../MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
- [γ scales future value](../MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
- [Max](../MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

Only now can we compress the procedure:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

Maximization can overestimate noisy actions and offline data limits safe exploration.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/089-q-learning/README.md).*

---

### Excavation 090 — Policy Gradients — Improving the Choices Directly

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

Perhaps we always choose the highest estimated action.

But early errors remove exploration and discrete choice blocks ordinary differentiation.

So we sample from a policy and increase probability of actions followed by better-than-expected returns.

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

##### Why these operations are forced

- [The policy log](../MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
- [Multiplying by return G](../MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
- [Expectation](../MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

Policy gradients are noisy and can exploit reward flaws.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/090-policy-gradients/README.md).*

---

### Excavation 091 — Multimodal Alignment

Policy gradients let consequences reshape action probabilities. The field system's words, images, and actions still live in separate representational worlds unless paired observations can teach them to meet.

We first try to compare raw pixels directly with token IDs.

Yet their coordinates have unrelated meanings and shapes.

We need to use separate encoders and train paired image-text examples to become nearby.

A tiger photo and “striped big cat” move together; mismatched captions move apart.

Pairs can contain weak, biased, or incomplete descriptions.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/091-multimodal-alignment/README.md).*

---

### Excavation 092 — Contrastive Learning

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

One tempting answer is to pull every observed pair together without negatives.

The trouble appears immediately: all representations can collapse to one point.

Now we can see what is missing: we must compare each true pair against mismatched alternatives in the same batch.

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

##### Why these operations are forced

- [Each dot product](../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
- [Dividing by temperature](../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
- [The denominator sum](../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
- [Negative log](../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

False negatives may actually describe the same concept.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/092-contrastive-learning/README.md).*

---

### Excavation 093 — Speech and Audio

Contrastive learning creates that relative competition. Sound introduces another modality whose pressure waveform is long, continuous, and shifted in time even when a listener hears the same event.

At first we treat every raw sample as an independent token.

That confidence lasts only until sequences are huge and local frequency structure is hidden.

That failure tells us to transform short windows into time-frequency features, then model their sequence.

A whistle appears as sustained energy in one frequency band across several time windows.

Spectrogram choices discard phase or fine timing.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/093-speech-audio/README.md).*

---

### Excavation 094 — Low-Rank Adaptation

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

Using what we have, we copy and fine-tune all parameters for every task.

The world refuses to cooperate: storage and training cost multiply, and the base model is harder to preserve.

So we freeze the base and learn a small low-rank correction to selected matrices.

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

##### Why these operations are forced

- [BA](../MATHEMATICAL_MOVES.md#multiplication) composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.
- [Adding that correction to W](../MATHEMATICAL_MOVES.md#addition) preserves the pretrained base and treats adaptation as a change. [The prime on W](../MATHEMATICAL_MOVES.md#symbol-decorations) marks the adapted version; replacing W would discard the knowledge we intended to keep.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

Low rank may be insufficient for large behavioral changes.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/094-lora/README.md).*

---

### Excavation 095 — Quantization

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

An obvious shortcut is to round every weight aggressively without measuring effect.

But small but important distinctions disappear and outputs degrade.

We need to map values to a limited set of levels using calibrated scale and test sensitive layers.

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

##### Why these operations are forced

- [Dividing by scale s](../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
- [Rounding](../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
- [Multiplying q by s](../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Only now can we compress the procedure:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

Lower precision trades accuracy for efficiency and hardware support varies.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/095-quantization/README.md).*

---

### Excavation 096 — Distributed Training

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

Perhaps we let many machines train independent copies and combine them occasionally.

Yet their parameters drift and duplicated work wastes computation.

Now we can see what is missing: we must partition data or model work, synchronize required results, and preserve one coherent update.

Two workers compute gradients on different batches, average them, then apply the same update.

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/096-distributed-training/README.md).*

---

### Excavation 097 — Inference Serving

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

We first try to run one request at a time on one full model.

The trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

That failure tells us to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

Four prompts share one matrix operation while each retains separate token state.

Batching improves throughput but can worsen individual latency.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/097-inference-serving/README.md).*

---

### Excavation 098 — Red Teaming

Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.

One tempting answer is to evaluate only expected well-formed requests.

That confidence lasts only until real users, attackers, and accidents find paths designers never listed.

So we actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations.

A hidden instruction in a retrieved page bypasses a normal demo; the case becomes a permanent injection test.

No finite red team proves universal safety.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/098-red-teaming/README.md).*

---

### Excavation 099 — Governance — Who Decides and Who Is Accountable?

Red teaming discovers failures before ordinary traffic does. Deciding which risks are acceptable, who may approve deployment, and who is accountable cannot be delegated to the model being evaluated.

At first we let builders decide every acceptable use because they understand the system.

The world refuses to cooperate: affected users carry risks without authority, appeal, or visibility.

We need to define ownership, review, documentation, incident response, user recourse, and deployment boundaries.

A lending model requires documented data, subgroup evaluation, human appeal, and a named owner before launch.

Governance can become paperwork unless tied to real authority and enforcement.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/099-governance/README.md).*

---

### Excavation 100 — The Complete AI System — From Observation to Responsible Action

Governance assigns legitimate decisions and responsibility around the technology. We can finally assemble data, models, tools, evaluation, operations, and authority into one complete AI system rather than treating the model as the whole product.

Using what we have, we connect every powerful component and call the result intelligent.

But an accurate model with stale data, excessive authority, weak verification, or no accountability still fails.

Now we can see what is missing: we must build one observable loop where evidence, representation, prediction, action, verification, feedback, and governance constrain one another.

A support system retrieves current policy, drafts an answer, cites evidence, requests approval for refunds, verifies transactions, logs outcomes, and learns only through reviewed updates.

No architecture completes intelligence forever; every deployment creates new observations and new responsibilities.

#### The Expedition Continues

Excavation 100 closes this map, not discovery. New observations must be allowed to break the system and force the next invention.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/100-complete-ai-system/README.md).*
