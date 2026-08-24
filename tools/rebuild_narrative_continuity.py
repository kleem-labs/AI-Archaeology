"""Rebuild chapter openings as one causal book-length argument."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]

CARRY = {
17:"The Transformer has begun to infer hidden causes from the footprints of language. But inference without certainty is dangerous: the same rustle may have been made by a tiger, a deer, or only the wind.",
18:"Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.",
19:"Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.",
20:"Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.",
21:"Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.",
22:"Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.",
23:"A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.",
24:"The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.",
25:"Backpropagation can now return one local sensitivity to every adjustable weight. Sensitivity is advice, not learning: the network still needs a rule that turns millions of local directions into a new parameter state.",
26:"Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.",
27:"A mini-batch replaces one noisy witness with the average advice of a small council. The council can point downhill, but its vote still says nothing about how far the network should move.",
28:"The learning rate controls the size of each step. Mini-batches nevertheless disagree sideways from one update to the next, hiding the direction that persists across their noise.",
29:"Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.",
30:"Careful initialization keeps early signals alive and breaks symmetry. But a tower made only from linear transformations still collapses algebraically into one linear transformation, no matter how many layers we stack.",
31:"Activation gates let the network bend and build conditional internal paths. That flexibility also makes a new deception possible: the machine can reproduce every training example without learning what should survive beyond them.",
32:"Overfitting reveals that low training error can be perfect memory wearing the costume of intelligence. The learner therefore needs pressure against fragile, unnecessarily extreme explanations.",
33:"Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.",
34:"Validation lets us choose among models without opening the sealed test set. Even an honest test can come from yesterday's hospital, dialect, season, or camera while tomorrow arrives from somewhere else.",
35:"Generalization is the property we actually wanted: useful structure that survives new cases. We have derived its pieces separately; now they must become one visible machine whose prediction, loss, blame, and update form a complete loop.",
36:"The tiny neural network now learns from numbered examples. People do not speak in fixed numerical columns; they produce an open stream of words, punctuation, names, code, and writing systems.",
37:"Tokenization gives the machine repeatable pieces and assigns each piece an address. An address distinguishes tokens but says nothing about how their meanings should begin.",
38:"An embedding table gives every token a learned starting description. The sentences “dog bites man” and “man bites dog” still contain the same three descriptions, so the machine cannot tell who did what.",
39:"Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.",
40:"Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.",
41:"Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.",
42:"The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; neither the reader nor the loss can treat them as comparable beliefs yet.",
43:"Softmax turns vocabulary scores into a distribution. Generation now faces a choice that training did not settle: should the machine always take the winner or sometimes follow another plausible continuation?",
44:"Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.",
45:"A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.",
46:"The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.",
47:"Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.",
48:"Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.",
49:"Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.",
50:"Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.",
51:"Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.",
52:"Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.",
53:"Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.",
54:"Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.",
55:"Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.",
56:"Tools let language cause external effects. The moment an answer can act, capability must be separated from permission: what may this agent do without asking again?",
57:"An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.",
58:"Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.",
59:"Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.",
60:"Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.",
61:"A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.",
62:"Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.",
63:"Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.",
64:"Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.",
65:"Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.",
66:"The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.",
67:"A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.",
68:"Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.",
69:"Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.",
70:"Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.",
71:"Bandit strategies balance present reward with the value of exploring uncertain choices. Once deployed, their decisions still emerge from internal representations whose meaning and failure modes remain hidden.",
72:"Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.",
73:"Linear probes reveal information available to a simple reader. To understand one prediction, we must trace which input evidence actually influenced the output rather than merely existing somewhere inside.",
74:"Attribution assigns influence to inputs or internal components. The investigation soon finds that one neuron can participate in many features and one feature can be distributed across many neurons.",
75:"Superposition explains how limited dimensions can carry more features than individual neurons. A readable direction may still be a bystander; only changing it and observing behavior can test whether it is causally used.",
76:"Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.",
77:"Pixels preserve local color and position without yet revealing edges, stripes, or animals. The same small visual pattern may appear anywhere in the image, so relearning a detector at every location wastes both data and parameters.",
78:"Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.",
79:"Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.",
80:"A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.",
81:"Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.",
82:"An autoencoder learns to compress and reconstruct. Its bottleneck is only a list of numbers until changes in those coordinates correspond to useful hidden causes such as pose, lighting, or identity.",
83:"A meaningful latent space gives images coordinates we can navigate. To create a new image, the system still needs a procedure that turns an uncertain starting state into a complete arrangement of pixels.",
84:"Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.",
85:"The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.",
86:"Denoising closes the image-generation loop. The field system can predict words and images, but an acting agent often receives no correct action label—only eventual success, damage, or failure.",
87:"A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.",
88:"State–action–transition records make experience explicit. Immediate reward still cannot distinguish a move toward a distant rescue from a move into a dead end when neither pays off yet.",
89:"A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.",
90:"Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.",
91:"Policy gradients let consequences reshape action probabilities. The field system's words, images, and actions still live in separate representational worlds unless paired observations can teach them to meet.",
92:"Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.",
93:"Contrastive learning creates that relative competition. Sound introduces another modality whose pressure waveform is long, continuous, and shifted in time even when a listener hears the same event.",
94:"Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.",
95:"Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.",
96:"Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.",
97:"Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.",
98:"Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.",
99:"Red teaming discovers failures before ordinary traffic does. Deciding which risks are acceptable, who may approve deployment, and who is accountable cannot be delegated to the model being evaluated.",
100:"Governance assigns legitimate decisions and responsibility around the technology. We can finally assemble data, models, tools, evaluation, operations, and authority into one complete AI system rather than treating the model as the whole product.",
101:"The complete system acts responsibly only if it knows when its evidence is weak. A blurry tiger and a perfectly clear animal from an unseen species both produce uncertainty, but they call for different remedies.",
102:"Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.",
103:"Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.",
104:"An ensemble turns disagreement into evidence about model uncertainty. When labels are expensive, that disagreement can guide which unlabeled case deserves a human answer next.",
105:"Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.",
106:"Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.",
107:"Catastrophic forgetting exposes competition inside shared parameters. Continual learning must absorb a stream of new tasks while preserving the old behavior that remains valid.",
108:"Continual learning protects the past but may still require many examples for every genuinely new task. Experience across tasks could teach not only solutions, but a better procedure for adapting quickly.",
109:"Meta-learning shapes that adaptation procedure. Its success depends on which tasks and difficulties the learner encounters first; a hostile order can make useful structure unnecessarily hard to discover.",
110:"Curriculum learning controls the order of experience. The supply of human labels still limits every curriculum, while raw text, images, and audio contain countless prediction problems whose answers are present in the data itself.",
111:"Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.",
112:"A world model predicts future observations. Prediction from recorded correlations cannot answer what would happen if the agent deliberately intervened and changed one cause.",
113:"Causal inference separates observation from intervention at the population level. A doctor or planner often asks a narrower question: what would have happened to this same case under the action not taken?",
114:"Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.",
115:"Model-based planning can simulate possible action sequences. Their number grows exponentially with depth, making exhaustive imagination impossible long before the world model runs out of detail.",
116:"Tree search spends simulation on promising and uncertain branches. A long proposed solution may still hide one invalid inference, so plausible completion must be separated from stepwise verification.",
117:"Reasoning with verification catches steps that violate checkable constraints. Neural representations handle perception and ambiguity well, while exact logical and algebraic rules resist being approximated.",
118:"A neuro-symbolic system gives learned perception and exact rules distinct jobs. Those rules need facts stored with explicit entities and relationships rather than buried inside one paragraph or vector.",
119:"A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.",
120:"Graph neural networks propagate learned messages through relational structure. Some tasks demand more than one answer: they demand a reusable procedure that maps every allowed input to an output.",
121:"Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.",
122:"Formal verification can prove universal properties of a program. Training and evaluating the wider system may still expose whether one person's sensitive record participated in the data.",
123:"Differential privacy limits the observable influence of one record. Hospitals and devices may be unwilling or legally unable to centralize their raw data even when collective learning would help everyone.",
124:"Federated learning moves computation to distributed data. Model updates and inputs remain vulnerable to malicious or tiny perturbations that preserve human meaning while flipping machine behavior.",
125:"Adversarial robustness tests whether behavior survives hostile changes. The system can now run experiments on itself, but open-ended discovery becomes unsafe if it can rewrite objectives, evidence standards, or deployment authority.",
126:"A bounded research system can propose and test changes without deploying them automatically. Its first obligation is to turn curiosity into a claim precise enough that an observation could prove it wrong.",
127:"A testable hypothesis predicts a measurable difference. If several components change together, the result cannot reveal which intervention caused that difference.",
128:"Experimental design isolates one suspected cause and provides a control. A single successful run can still be a favorable random seed rather than a discovery that will survive repetition.",
129:"Reproducibility asks whether the gain survives recorded code, data, configuration, and repeated seeds. Different teams still cannot compare progress if each chooses a different task and ruler.",
130:"Benchmarks freeze tasks and metrics before results are known. A model may score well because those supposedly unseen questions, or close paraphrases, appeared in its training data.",
131:"Contamination turns the test into disguised homework. Fresh human-written data is expensive, tempting the model to manufacture far more lessons for itself.",
132:"Synthetic data can expand training only when errors are verified instead of multiplied. The capable teacher generating or checking those lessons may be too large and costly for deployment.",
133:"Distillation transfers a teacher's pattern of belief into a smaller student. A dense student still spends every parameter on every token, even when different inputs need different expertise.",
134:"A mixture of experts activates only a few specialists for each token. Long-context attention still compares too many token pairs, making communication—not expert capacity—the next computational bottleneck.",
135:"Sparse attention follows selected local, global, or retrieved paths instead of comparing everything. Any fixed context remains finite, while a long-running research system must preserve knowledge beyond the current window.",
136:"External memory stores selected facts outside the prompt. Storage is not remembrance in practice: the one decisive record can remain unused if retrieval ranks a thousand plausible distractions above it.",
137:"Long-context retrieval brings the relevant clue back into view. Easy lookups and hard proofs still receive the same fixed amount of reasoning unless computation can be allocated according to difficulty.",
138:"Test-time compute lets hard problems receive more attempts. More attempts also produce more plausible mistakes, so proposing candidate paths must be separated from checking them.",
139:"Search and verification keep only candidates that survive an independent test. A correct final answer can still reward an invalid path that reached it by luck.",
140:"Process supervision rewards reliable intermediate reasoning rather than only the final result. Every process label and verifier is still a proxy that a sufficiently capable optimizer may learn to satisfy without achieving the intended goal.",
141:"Reward hacking exposes the gap between a score and the purpose it was meant to measure. Adding more literal rules does not close the gap when the agent can obey their words while betraying their shared intent.",
142:"Specification gaming shows why successful optimization is not the same as obedience to purpose. An agent focused on completion may also resist interruption if being stopped prevents the score it was built to earn.",
143:"Corrigibility makes pause, inspection, correction, and handoff legitimate outcomes. A corrigible planner still has to choose when the most efficient route passes through a world it understands poorly.",
144:"Uncertainty-aware planning carries several plausible worlds and may seek information before acting. Even a plan that succeeds in all of them can alter unrelated parts of the world unnecessarily.",
145:"Impact measures make avoidable side effects visible against a baseline. No formula can settle every conflict among values, so consequential or irreversible boundaries still require informed human judgment.",
146:"Human oversight places judgment where an action becomes difficult to reverse. The artifacts produced by a powerful system can exceed any one reviewer's time and attention.",
147:"Scalable oversight decomposes work, attaches local evidence, samples risk, and escalates anomalies. A polished argument can still hide one weak assumption unless an equally capable opponent is rewarded for finding it.",
148:"Debate exposes checkable disagreement instead of letting one persuasive answer control the evidence. Novel cases still need stable principles by which a judge can criticize both sides.",
149:"Constitutional guidance turns inspectable principles into critique and revision. Before real tools and users are exposed, the complete system must face staged tests of capabilities, misuse, safeguards, and operating limits.",
150:"Pre-deployment evaluation can reject a dangerous candidate before the world pays for the experiment. A measured improvement must still pass reproducibility, impact review, authorization, staged release, monitoring, and rollback before it may replace the system that proposed it.",
}

# Part XII is authored as one measured experiment by its dedicated builder. Use
# those exact openings here so continuity checks cannot drift away from the
# chapter sources.
from build_excavations_151_175 import ROWS as PART_XII_ROWS
CARRY.update({row[0]: row[4] for row in PART_XII_ROWS})
from build_excavations_176_200 import ROWS as PART_XIII_ROWS
CARRY.update({row[0]: row[3] for row in PART_XIII_ROWS})
from build_excavations_201_225 import ROWS as PART_XIV_ROWS
CARRY.update({row.number: row.carry for row in PART_XIV_ROWS})

ATTEMPT_MARKERS = (
    "The first solution that suggests itself is this:",
    "A reasonable place to begin is:",
    "Without knowing the inherited method, we might try this:",
    "At first, the simplest answer is tempting:",
    "Our first construction is deliberately modest:",
    "The first repair that suggests itself is simple:",
)
FAILURE_MARKERS = (
    "The idea survives only until we test it against reality:",
    "Now place that proposal under pressure:",
    "Its hidden assumption appears in the following case:",
    "But the simplicity has discarded something important:",
    "It works—right up to this boundary:",
)
REPAIR_MARKERS = (
    "The failure gives us a precise requirement:",
    "What broke tells us what the replacement must preserve:",
    "Remove that assumption and the needed repair becomes clear:",
    "The missing information determines the next move:",
    "Crossing that boundary requires one additional idea:",
    "The cost of that attempt points to the missing operation:",
)


def extract(paragraphs, markers):
    for paragraph in paragraphs:
        for marker in markers:
            if paragraph.startswith(marker):
                return paragraph[len(marker):].strip()
    return ""


def lower_first(value):
    if not value:
        return value
    return value[0].lower() + value[1:]


def sentence(prefix, value):
    return prefix + lower_first(value)


ATTEMPT_LEADS = (
    "Perhaps we ", "We first try to ", "One tempting answer is to ",
    "At first we ", "Using what we have, we ", "An obvious shortcut is to ",
)
FAILURE_LEADS = (
    "But ", "Yet ", "The trouble appears immediately: ",
    "That confidence lasts only until ", "The world refuses to cooperate: ",
)
REPAIR_LEADS = (
    "Now we can see what is missing: we must ",
    "That failure tells us to ",
    "So we ",
    "We need to ",
)


LEGACY_ATTEMPT_LEADS = ATTEMPT_MARKERS + (
    "One possibility is to ", "The obvious shortcut is to ", "Our first instinct is to ",
    "A direct approach is to ", "The machine could ", "Suppose we ",
    "It is tempting to ", "The cheapest-looking move is to ",
    "A straightforward design would ", "We begin by trying to ",
    "The existing machinery suggests that we ", "Nothing stops us from trying to ",
    "The first answer seems obvious: ", "At first we try to ",
    "A shortcut offers itself: ", "The simplest move is to ",
    "Using what we already have, we could ", "Our first design would ",
)
LEGACY_FAILURE_LEADS = FAILURE_MARKERS + (
    "That breaks because ", "In practice, ", "Then ", "Reality objects: ",
    "The trouble appears immediately: ", "That confidence lasts only until ",
    "The world refuses to cooperate: ",
)
LEGACY_REPAIR_LEADS = REPAIR_MARKERS + (
    "So we ", "What we need instead is to ", "The failure forces us to ",
    "The missing operation is to ", "The repair is to ",
    "We can escape the failure only if we ",
    "Now the missing requirement is visible: ",
    "That failure tells us what must come next: ",
    "The broken attempt leaves one useful clue: ", "So the next invention must ",
    "The requirement is that ", "We need ",
)

CUSTOM_REPAIR_LEADS = {19: "We need "}


def remove_leads(value, leads):
    """Unwrap any number of old authoring prefixes, regardless of case."""
    changed = True
    while changed:
        changed = False
        for lead in sorted(leads, key=len, reverse=True):
            if value.lower().startswith(lead.lower()):
                value = value[len(lead):]
                changed = True
                break
    return value


def integrate(number, text):
    first_h2 = text.find("\n## ")
    if first_h2 < 0:
        return text
    prefix, remainder = text[:first_h2], text[first_h2:]
    paragraphs = [p.strip() for p in prefix.split("\n\n") if p.strip()]
    attempt = extract(paragraphs, ATTEMPT_MARKERS)
    failure = extract(paragraphs, FAILURE_MARKERS)
    repair = extract(paragraphs, REPAIR_MARKERS)
    if not attempt and CARRY[number] in paragraphs:
        carry_index = paragraphs.index(CARRY[number])
        raw = paragraphs[carry_index + 1:]
        if len(raw) == 2:
            attempt, repair = raw
        elif len(raw) >= 3:
            attempt, failure, repair = raw[:3]
    if not attempt or not repair:
        return text

    # Preserve the title and optional part/volume epigraph; move file
    # navigation to the end where it cannot interrupt the opening scene.
    kept = []
    for paragraph in paragraphs:
        if paragraph.startswith("# ") or paragraph.startswith("> **PART") or (kept and kept[-1].startswith("> **PART") and paragraph.startswith(">")):
            kept.append(paragraph)
    attempt = remove_leads(attempt, ("We could ",) + ATTEMPT_LEADS + LEGACY_ATTEMPT_LEADS)
    failure = remove_leads(failure, FAILURE_LEADS + LEGACY_FAILURE_LEADS)
    repair = remove_leads(repair, REPAIR_LEADS + LEGACY_REPAIR_LEADS)
    failure = failure.replace(
        " What information did the attempt lose? Write that requirement before continuing.", ""
    )
    opening = [CARRY[number], sentence(ATTEMPT_LEADS[number % len(ATTEMPT_LEADS)], attempt)]
    if failure:
        opening.append(sentence(FAILURE_LEADS[number % len(FAILURE_LEADS)], failure))
    repair_lead = CUSTOM_REPAIR_LEADS.get(number, REPAIR_LEADS[number % len(REPAIR_LEADS)])
    opening.append(sentence(repair_lead, repair))
    return "\n\n".join(kept + opening) + "\n" + remainder


def clean_editorial_scaffolding(text):
    """Remove sentences that describe the lesson instead of telling the story."""
    text = re.sub(
        r"\nThe repair is explicit: .*? Its power is also its boundary; anything not represented in those operations remains undecided\.\n",
        "\n",
        text,
    )
    text = text.replace(
        " What information did the attempt lose? Write that requirement before continuing.", ""
    )
    text = text.replace(" Name the missing guarantee before continuing.", "")
    text = text.replace(
        "We need to rare events should carry more information, certain events none, and independent messages should add.",
        "We need rare events to carry more information, certain events to carry none, and independent messages to add.",
    )
    text = text.replace(
        "Yet use the held-out sentence “the tiger sleeps.”",
        "But the held-out sentence “the tiger sleeps” reveals the weakness.",
    )
    text = re.sub(
        r"\nThis is not an unrelated warning\. The construction can .*? It cannot infer or control information that never enters that construction\.\n",
        "\n",
        text,
    )
    text = re.sub(
        r"\nNo new equation is needed here\. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it\.\n",
        "\n",
        text,
    )
    text = text.replace(
        "\nThe named objects come first. We add notation only when it shortens a procedure the reader has already performed.\n",
        "\n",
    )
    text = text.replace(
        "\nThe equation is not the discovery. It is the shortest record of the discovery already reconstructed above.\n",
        "\n",
    )
    text = text.replace(
        "\nEvery operation records a need established above; the equation is the fossil, not the living discovery.\n",
        "\n",
    )
    text = text.replace(
        "\nThat limit is not a footnote. It is the pressure that forces the next excavation.\n",
        "\n",
    )
    text = re.sub(
        r"\nThe reason is visible in the procedure\. It knows how to .*? The limitation above asks for another judgment, and no part of the procedure makes that judgment\.\n",
        "\n",
        text,
    )
    text = re.sub(
        r"\nWhy does the boundary remain\? Our new machinery only knows how to .*? Solving that problem does not automatically solve every decision built on top of it\.\n",
        "\n",
        text,
    )
    text = re.sub(
        r"\nThe boundary follows from the mechanism itself\. We designed it to .*? That operation solves the failure we had reached, but it contains no step that answers the additional problem above\.\n",
        "\n",
        text,
    )
    text = re.sub(
        r"\nThe named objects(?: and arithmetic)? come first\. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated\.\n",
        "\n",
        text,
    )
    text = re.sub(
        r"\nWrite down what changed, what remained fixed, and which observation could have contradicted your belief\. The method lives in those jobs; its name is only shorthand\.\n",
        "\n",
        text,
    )
    text = text.replace("## Now work a case you can see", "## Let the case decide")
    text = text.replace("## Follow one case all the way through", "## Let the case decide")
    text = text.replace("## Build each piece from what just happened", "## The arithmetic we have earned")
    text = text.replace("## Build Every Piece from the Concrete Example", "## The arithmetic we have earned")
    text = text.replace("### Give Short Names Only After We Know the Pieces", "### Only now do the symbols earn names")
    text = text.replace("## Where your new idea still breaks", "## The boundary of the discovery")
    text = text.replace("## Where the discovery still breaks", "## The boundary of the discovery")
    return re.sub(r"\n{3,}", "\n\n", text)


def main():
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        number = int(path.parent.name[:3])
        text = path.read_text()
        # Top-of-chapter file navigation is useful on GitHub but damages book
        # rhythm. Every chapter already links forward at its end.
        text = re.sub(r"^\[Previous[^\n]*\]\([^\n]+\)\n*", "", text, flags=re.M)
        if number in CARRY:
            text = integrate(number, text)
        text = clean_editorial_scaffolding(text)
        path.write_text(text.rstrip() + "\n")
    print("Rebuilt causal openings and removed editorial scaffolding from Excavations 000–225.")


if __name__ == "__main__":
    main()
