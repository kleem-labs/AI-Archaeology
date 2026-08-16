# AI Archaeology

**Rediscover the ideas behind modern AI from the problems that forced them to exist.**

This repository is both a book and a laboratory. Read the excavation first,
then break and rebuild the idea in the [Laboratory](LABORATORY.md). The
[completion standard](BOOK_AND_LAB_STANDARD.md) defines what “finished” means;
file presence alone is not completion.

For uninterrupted reading, begin with the
[three-volume book edition](book/README.md). The excavation directories remain
the working dig sites where code, diagrams, mistakes, exercises, and references
live beside the idea that produced them.

Read it as a book through the [thirteen-part reading path](PARTS.md). Work with it
as a laboratory through the [field-lab protocol](labs/README.md). The
[completion status](COMPLETION_STATUS.md) distinguishes finished depth from
scaffolding still waiting to be excavated.

After deriving an idea in its chapter, revisit it in the
[Mathematical Gist](MATHEMATICAL_GIST.md): one ordered mathematical spine that
keeps the concrete explanation of every term beside the equation it produced.

When an operation itself is unfamiliar, follow its chapter link into
[Mathematical Moves](MATHEMATICAL_MOVES.md). It explains what addition,
multiplication, division, powers, roots, exponentials, logarithms, derivatives,
expectations, and notation preserve; why a different move would answer a
different question; and where each move is useful elsewhere.

This book does not begin with formulas. It begins with a person facing reality without inherited mathematics.

Every excavation follows the same discipline:

```text
reality → question → naive attempt → failure → discovery → equation
```

The reader should want the mathematics before seeing it. Symbols are compressed records of reasoning, not substitutes for reasoning.

## Excavations

| # | Excavation | The question that opens it |
|---:|---|---|
| 000 | [Before Mathematics Existed](excavations/000-before-mathematics-existed/README.md) | Why can experience teach us anything? |
| 001 | [Why Features Exist](excavations/001-why-features-exist/README.md) | Which details should survive compression? |
| 002 | [Vectors](excavations/002-vectors/README.md) | How can related measurements travel as one object? |
| 003 | [Distance](excavations/003-distance/README.md) | How can many differences become one comparison? |
| 004 | [Vectors as Change](excavations/004-vectors-as-change/README.md) | How do we describe direction as well as amount? |
| 005 | [Matrices](excavations/005-matrices/README.md) | How can one machine transform any input vector? |
| 006 | [Meaning Without a Dictionary](excavations/006-meaning/README.md) | How can symbols constrain one another without a dictionary? |
| 007 | [Embeddings](excavations/007-embeddings/README.md) | How can those constraints become geometry? |
| 008 | [Why Attention Had to Exist](excavations/008-attention/README.md) | How can a token retrieve what matters now? |
| 009 | [From Scores to Attention](excavations/009-softmax/README.md) | How do unstable scores become usable weights? |
| 010 | [Query, Key, and Value](excavations/010-query-key-value/README.md) | Who is relevant, and what should they contribute? |
| 011 | [Multi-Head Attention](excavations/011-multi-head-attention/README.md) | How can several relationships be followed at once? |
| 012 | [Feed-Forward Networks](excavations/012-feed-forward-networks/README.md) | After communication, how does each token process what it heard? |
| 013 | [Residual Connections](excavations/013-residual-connections/README.md) | How can depth improve a message without repeatedly erasing it? |
| 014 | [Layer Normalization](excavations/014-layer-normalization/README.md) | How can representations work at a stable numerical volume? |
| 015 | [How a Dead Brain Learns](excavations/015-learning/README.md) | How does a random machine turn mistakes into improvement? |
| 016 | [The Hidden World Behind Words](excavations/016-emergence/README.md) | What hidden world must be inferred to predict its linguistic traces? |
| 017 | [Probability — Counting What We Do Not Know](excavations/017-probability/README.md) | How can we act without pretending to be certain? |
| 018 | [Likelihood — Which Hidden Story Produced This Evidence?](excavations/018-likelihood/README.md) | Which hidden story best explains the evidence? |
| 019 | [Information — Why Surprise Needs a Number](excavations/019-information/README.md) | Why does a rare message teach us more? |
| 020 | [Entropy — Measuring the Uncertainty of a Whole Situation](excavations/020-entropy/README.md) | How uncertain is an entire situation? |
| 021 | [Cross-Entropy — Paying for Confidently Wrong Predictions](excavations/021-cross-entropy/README.md) | How should confident mistakes be penalized? |
| 022 | [Derivatives — Asking One Weight What It Changed](excavations/022-derivatives/README.md) | Which way should one weight move? |
| 023 | [The Chain Rule — Following One Change Through Many Machines](excavations/023-chain-rule/README.md) | How does one change travel through many machines? |
| 024 | [Backpropagation — Reusing Blame Instead of Recomputing It](excavations/024-backpropagation/README.md) | How can shared blame be calculated once and reused? |
| 025 | [Gradient Descent — Teaching a Tiny Network](excavations/025-gradient-descent/README.md) | How do local sensitivities become repeated learning? |
| 026 | [Mini-Batches — Learning from More Than One Example](excavations/026-mini-batches/README.md) | How can we learn without trusting one noisy example? |
| 027 | [Learning Rate — How Large Should the Next Step Be?](excavations/027-learning-rate/README.md) | How far should we move downhill? |
| 028 | [Momentum — Remembering Which Way Downhill Persists](excavations/028-momentum/README.md) | How can persistent direction survive noisy gradients? |
| 029 | [Initialization — Where Should Learning Begin?](excavations/029-initialization/README.md) | Where should learning begin? |
| 030 | [Activation Functions — Why a Network Must Bend](excavations/030-activation-functions/README.md) | Why must a deep network bend? |
| 031 | [Overfitting — When Perfect Memory Pretends to Be Intelligence](excavations/031-overfitting/README.md) | When does perfect memory stop being intelligence? |
| 032 | [Regularization — Making Memorization More Expensive](excavations/032-regularization/README.md) | How can brittle memorization become expensive? |
| 033 | [Validation — Testing Without Peeking at the Final Exam](excavations/033-validation/README.md) | How can we test without leaking the answers? |
| 034 | [Generalization — What Should Survive Beyond the Dataset?](excavations/034-generalization/README.md) | What should survive beyond the dataset? |
| 035 | [A Tiny Neural Network — Assemble the Entire Learning Loop](excavations/035-tiny-neural-network/README.md) | How do all the learning pieces become one working machine? |
| 036 | [Tokenization: What Can a Language Model See?](excavations/036-tokenization/README.md) | What pieces can a language model actually see? |
| 037 | [Input Embeddings: Giving Tokens Learnable Coordinates](excavations/037-input-embeddings/README.md) | How can arbitrary token IDs become learnable coordinates? |
| 038 | [Position — Why Order Must Enter the Model](excavations/038-position/README.md) | How can the model see order? |
| 039 | [Causal Masking — Preventing the Future from Leaking Backward](excavations/039-causal-mask/README.md) | How can future answers remain hidden? |
| 040 | [Next-Token Examples — One Sentence Becomes Many Lessons](excavations/040-next-token-examples/README.md) | How can one sentence create many lessons? |
| 041 | [Logits — Let Every Vocabulary Token Compete](excavations/041-logits/README.md) | How does context score every token? |
| 042 | [Vocabulary Probabilities — Turning Scores into a Prediction](excavations/042-vocabulary-probabilities/README.md) | How do scores become probabilities? |
| 043 | [Sampling — Choosing Without Always Taking the Maximum](excavations/043-sampling/README.md) | How should generation choose? |
| 044 | [Context Windows — How Much Past Can the Model Carry?](excavations/044-context-window/README.md) | How much past can the model carry? |
| 045 | [A Tiny GPT — Close the Prediction Loop](excavations/045-tiny-gpt/README.md) | How do all parts form a tiny GPT? |
| 046 | [Perplexity — How Surprised Is the Model?](excavations/046-perplexity/README.md) | How surprised is the model by real held-out text? |
| 047 | [Evaluation — What Does “Better” Actually Mean?](excavations/047-evaluation/README.md) | What does better mean for the intended job? |
| 048 | [Hallucination — When Fluent Prediction Outruns Evidence](excavations/048-hallucination/README.md) | When does fluent prediction outrun evidence? |
| 049 | [Calibration — Does 80% Confidence Mean Eight Out of Ten?](excavations/049-calibration/README.md) | Does stated confidence match observed reliability? |
| 050 | [Data Quality — What Lessons Did the Model Actually Receive?](excavations/050-data-quality/README.md) | What lessons did the training data actually repeat? |
| 051 | [Scaling Laws — What Improves When We Add More?](excavations/051-scaling-laws/README.md) | Should resources buy model size, data, or computation? |
| 052 | [Instruction Tuning — From Continuation to Cooperation](excavations/052-instruction-tuning/README.md) | How does continuation become cooperation? |
| 053 | [Preference Learning — When Several Answers Are Correct but Not Equally Helpful](excavations/053-preference-learning/README.md) | How can several valid answers still differ in helpfulness? |
| 054 | [Retrieval-Augmented Generation — Let the Model Look Before It Speaks](excavations/054-retrieval-augmented-generation/README.md) | How can the model consult current evidence before answering? |
| 055 | [Tool-Using Agents — When Words Must Cause Verified Actions](excavations/055-tool-using-agents/README.md) | When should words invoke a real, permissioned action? |
| 056 | [Authority — What Is the Agent Allowed to Do?](excavations/056-authority/README.md) | What may the agent do without new approval? |
| 057 | [Prompt Injection — When Evidence Tries to Become an Instruction](excavations/057-prompt-injection/README.md) | When is retrieved text evidence rather than authority? |
| 058 | [Planning — Turning a Goal into Checkable Steps](excavations/058-planning/README.md) | How can a goal become ordered, checkable steps? |
| 059 | [Memory — What Should Survive After the Context Ends?](excavations/059-memory/README.md) | What deserves to survive beyond the current context? |
| 060 | [State Machines — Knowing What Has Actually Happened](excavations/060-state-machines/README.md) | Which events may change real workflow state? |
| 061 | [Verification — How Does the Agent Know It Succeeded?](excavations/061-verification/README.md) | What evidence proves the requested outcome occurred? |
| 062 | [Retries and Idempotency — Trying Again Without Doing It Twice](excavations/062-retries-idempotency/README.md) | How can a retry avoid repeating the effect? |
| 063 | [Multi-Agent Coordination — When Should Work Be Divided?](excavations/063-multi-agent-coordination/README.md) | When does delegation help instead of adding coordination failure? |
| 064 | [Observability — Seeing Why an Agent Failed](excavations/064-observability/README.md) | Which trace reveals where an agent failed? |
| 065 | [Bounded Autonomy — Building an Agent That Can Be Trusted](excavations/065-bounded-autonomy/README.md) | How can autonomy remain inside an explicit safety envelope? |
| 066 | [Feedback Loops](excavations/066-feedback-loops/README.md) | Recommendations change what users see, and those changed choices become tomorrow’s training data. |
| 067 | [Online Learning](excavations/067-online-learning/README.md) | A fraud pattern changes today, but the deployed model learned only from last year. |
| 068 | [Distribution Drift](excavations/068-distribution-drift/README.md) | The world producing inputs changes after deployment. |
| 069 | [Controlled Experiments](excavations/069-controlled-experiments/README.md) | A new model performs better after launch, but traffic and season also changed. |
| 070 | [Bandits — Learning While Choosing](excavations/070-bandits/README.md) | An agent must choose recommendations while still learning which are useful. |
| 071 | [Features Inside Networks](excavations/071-features-inside-networks/README.md) | A trained network works, but where is “striped animal” represented? |
| 072 | [Linear Probes](excavations/072-linear-probes/README.md) | Can a hidden layer already separate animal species? |
| 073 | [Attribution](excavations/073-attribution/README.md) | Which input words influenced one prediction? |
| 074 | [Superposition](excavations/074-superposition/README.md) | A network stores more useful features than it has individual neurons. |
| 075 | [Causal Interventions](excavations/075-causal-interventions/README.md) | A probe finds a “tiger” direction. Does the model actually use it? |
| 076 | [Pixels — Turning Light into Numbers](excavations/076-pixels/README.md) | A camera gives a grid of colored light, not objects. |
| 077 | [Convolution — Reusing the Same Local Detector](excavations/077-convolution/README.md) | An edge can appear anywhere in an image. |
| 078 | [Pooling — Keeping Evidence While Shrinking the Map](excavations/078-pooling/README.md) | Local detectors create large activation maps. |
| 079 | [CNN Hierarchies](excavations/079-cnn-hierarchy/README.md) | Edges are not yet eyes, stripes, or tigers. |
| 080 | [Vision Transformers](excavations/080-vision-transformers/README.md) | Convolutions bake in locality, but distant image regions may need direct comparison. |
| 081 | [Autoencoders — Compressing and Rebuilding](excavations/081-autoencoders/README.md) | Can a model preserve what matters using fewer numbers? |
| 082 | [Latent Space — Coordinates for Hidden Causes](excavations/082-latent-space/README.md) | The bottleneck contains numbers, but do nearby codes vary meaningfully? |
| 083 | [Autoregressive Generation Beyond Text](excavations/083-autoregressive-generation/README.md) | How can a model generate an image one piece at a time? |
| 084 | [Diffusion — Learning by Destroying](excavations/084-diffusion/README.md) | How can generation begin without choosing a first meaningful pixel? |
| 085 | [Denoising — Predicting What the Noise Hid](excavations/085-denoising/README.md) | At one diffusion step, what should the network predict? |
| 086 | [Rewards — Learning Without Correct Answers](excavations/086-rewards/README.md) | An agent acts over time and receives only eventual success or failure. |
| 087 | [States, Actions, and Transitions](excavations/087-states-actions-transitions/README.md) | To learn from reward, what must one experience record? |
| 088 | [Value — Estimating Future Consequences](excavations/088-value-functions/README.md) | Immediate reward cannot distinguish a step toward a distant goal from a dead end. |
| 089 | [Q-Learning — Improving Values from Experience](excavations/089-q-learning/README.md) | How should one experience update the value of an action? |
| 090 | [Policy Gradients — Improving the Choices Directly](excavations/090-policy-gradients/README.md) | Value learning still needs a rule converting estimates into action probabilities. |
| 091 | [Multimodal Alignment](excavations/091-multimodal-alignment/README.md) | How can an image and its caption meet in one representation? |
| 092 | [Contrastive Learning](excavations/092-contrastive-learning/README.md) | Paired examples should be close, but close relative to what? |
| 093 | [Speech and Audio](excavations/093-speech-audio/README.md) | Audio is a long pressure waveform whose meaning survives small time shifts. |
| 094 | [Low-Rank Adaptation](excavations/094-lora/README.md) | How can a huge pretrained model learn a new task without changing every weight? |
| 095 | [Quantization](excavations/095-quantization/README.md) | How can a model use less memory and faster arithmetic at inference? |
| 096 | [Distributed Training](excavations/096-distributed-training/README.md) | One machine cannot hold the model, data, and optimizer state. |
| 097 | [Inference Serving](excavations/097-inference-serving/README.md) | A trained model must answer many users with low latency and bounded cost. |
| 098 | [Red Teaming](excavations/098-red-teaming/README.md) | Ordinary tests miss adversarial and unusual failures. |
| 099 | [Governance — Who Decides and Who Is Accountable?](excavations/099-governance/README.md) | A technically safe model still affects people through deployment choices. |
| 100 | [The Complete AI System — From Observation to Responsible Action](excavations/100-complete-ai-system/README.md) | We have excavated models, data, learning, tools, and controls. How do they become one coherent system? |
| 101 | [Two Kinds of Uncertainty](excavations/101-two-kinds-uncertainty/README.md) | The model is unsure whether a blurry animal is a tiger. Is the image ambiguous, or has the model never seen this species? |
| 102 | [Bayesian Updating](excavations/102-bayesian-updating/README.md) | A tracker begins with prior beliefs about tiger, deer, and wind, then observes a deep paw print. |
| 103 | [Ensembles](excavations/103-ensembles/README.md) | One trained model gives a confident answer. Would another equally trained model agree? |
| 104 | [Active Learning](excavations/104-active-learning/README.md) | Labeling one example is expensive. Which unlabeled case should a human inspect next? |
| 105 | [Selective Prediction](excavations/105-selective-prediction/README.md) | Must the model answer every question, even when evidence is weak? |
| 106 | [Catastrophic Forgetting](excavations/106-catastrophic-forgetting/README.md) | After learning task B, the model suddenly fails task A. |
| 107 | [Continual Learning](excavations/107-continual-learning/README.md) | A deployed learner faces a stream of changing tasks without clear boundaries. |
| 108 | [Meta-Learning](excavations/108-meta-learning/README.md) | Can experience across many tasks teach the model how to learn a new task quickly? |
| 109 | [Curriculum Learning](excavations/109-curriculum-learning/README.md) | Should a learner face the hardest examples first? |
| 110 | [Self-Supervised Learning](excavations/110-self-supervised-learning/README.md) | How can enormous unlabeled data teach useful representations? |
| 111 | [World Models](excavations/111-world-models/README.md) | An agent needs to predict consequences before acting. |
| 112 | [Causal Inference](excavations/112-causal-inference/README.md) | Ice-cream sales and drownings rise together. Would banning ice cream reduce drownings? |
| 113 | [Counterfactuals](excavations/113-counterfactuals/README.md) | What would have happened to this same patient under a treatment they did not receive? |
| 114 | [Model-Based Planning](excavations/114-model-based-planning/README.md) | A world model can predict one step. How should the agent choose a long action sequence? |
| 115 | [Tree Search](excavations/115-tree-search/README.md) | Exploring every future action sequence becomes impossible. |
| 116 | [Reasoning and Verification](excavations/116-reasoning-and-verification/README.md) | A model produces a plausible multi-step answer. Which step failed? |
| 117 | [Neuro-Symbolic Systems](excavations/117-neuro-symbolic-systems/README.md) | Neural models handle perception; symbolic rules handle exact constraints. Must one system do both? |
| 118 | [Knowledge Graphs](excavations/118-knowledge-graphs/README.md) | How can facts preserve who relates to whom instead of becoming one text paragraph? |
| 119 | [Graph Neural Networks](excavations/119-graph-neural-networks/README.md) | How can each node learn from a variable number of neighbors? |
| 120 | [Program Synthesis](excavations/120-program-synthesis/README.md) | Can examples specify a reusable procedure rather than one output? |
| 121 | [Formal Verification](excavations/121-formal-verification/README.md) | Tests sample cases. How can we guarantee a property for all allowed inputs? |
| 122 | [Differential Privacy](excavations/122-differential-privacy/README.md) | Can aggregate learning reveal whether one person’s record was included? |
| 123 | [Federated Learning](excavations/123-federated-learning/README.md) | Can many devices train together without centralizing raw data? |
| 124 | [Adversarial Robustness](excavations/124-adversarial-robustness/README.md) | A tiny input change invisible to a person flips the model’s decision. |
| 125 | [An Open-Ended Research System](excavations/125-open-ended-research-system/README.md) | How can a system keep discovering without silently rewriting its goals or safety boundaries? |
| 126 | [Hypotheses — Turning Curiosity into a Testable Claim](excavations/126-hypothesis-generation/README.md) | The research system notices that longer context sometimes helps. What exactly should it test? |
| 127 | [Experimental Design — Changing One Cause at a Time](excavations/127-experimental-design/README.md) | A new tokenizer and a larger model improve accuracy together. Which change helped? |
| 128 | [Reproducibility — Can the Discovery Survive Another Run?](excavations/128-reproducibility/README.md) | One training run beats the baseline. Has the system discovered an improvement? |
| 129 | [Benchmarks — Building a Ruler Before Measuring Progress](excavations/129-benchmarks/README.md) | Every team says its model is better, but each chooses different tasks. |
| 130 | [Data Contamination — When the Test Was Secretly Homework](excavations/130-data-contamination/README.md) | A model scores perfectly on a benchmark. Did it generalize? |
| 131 | [Synthetic Data — Letting a Model Write Lessons](excavations/131-synthetic-data/README.md) | Human examples are scarce. Can a model manufacture training data? |
| 132 | [Knowledge Distillation — Teaching a Smaller Student](excavations/132-knowledge-distillation/README.md) | A capable model is too expensive to deploy on a phone. |
| 133 | [Mixture of Experts — Spending Computation Where It Helps](excavations/133-mixture-of-experts/README.md) | Making every layer wider improves capacity but charges every token the full cost. |
| 134 | [Sparse Attention — Looking Without Comparing Everything](excavations/134-sparse-attention/README.md) | Long context makes every token compare with every other token. |
| 135 | [External Memory — Remembering Beyond the Context Window](excavations/135-external-memory/README.md) | An agent must remember a project after the current prompt disappears. |
| 136 | [Long-Context Retrieval — Finding the One Clue That Matters](excavations/136-long-context-retrieval/README.md) | A million-token archive fits, but the model still overlooks one decisive sentence. |
| 137 | [Test-Time Compute — Thinking Longer on Harder Problems](excavations/137-test-time-compute/README.md) | One fixed forward pass treats an easy lookup and a hard proof as equal work. |
| 138 | [Search and Verification — Separate Proposing from Checking](excavations/138-search-and-verification/README.md) | The first proposed solution to a puzzle is plausible but wrong. |
| 139 | [Process Supervision — Rewarding the Path, Not Only the Answer](excavations/139-process-supervision/README.md) | Two solutions reach the correct number; one used invalid reasoning by luck. |
| 140 | [Reward Hacking — When the Score Replaces the Goal](excavations/140-reward-hacking/README.md) | An agent receives points for keeping a room clean. |
| 141 | [Specification Gaming — Obeying the Words While Betraying the Purpose](excavations/141-specification-gaming/README.md) | A delivery agent is told to minimize average arrival time. |
| 142 | [Corrigibility — Remaining Willing to Be Corrected](excavations/142-corrigibility/README.md) | A capable agent expects an operator to stop its current plan. |
| 143 | [Uncertainty-Aware Planning — Choosing While Admitting Ignorance](excavations/143-uncertainty-aware-planning/README.md) | The shortest route crosses a bridge whose condition is unknown. |
| 144 | [Impact Measures — Notice What Changed Besides the Goal](excavations/144-impact-measures/README.md) | A cleaning robot succeeds but rearranges the entire house. |
| 145 | [Human Oversight — Put Judgment at the Irreversible Edge](excavations/145-human-oversight/README.md) | An agent can draft and send a legal filing in seconds. |
| 146 | [Scalable Oversight — Reviewing Work Too Large for One Person](excavations/146-scalable-oversight/README.md) | A model produces a million-line migration no reviewer can inspect completely. |
| 147 | [Debate — Let Claims Meet an Adversary](excavations/147-debate/README.md) | A persuasive answer hides one weak assumption in a long argument. |
| 148 | [Constitutional Guidance — Rules That Can Critique Answers](excavations/148-constitutional-guidance/README.md) | Thousands of preferences cannot cover every new situation. |
| 149 | [Pre-Deployment Evaluations — Fail Before the World Pays](excavations/149-predeployment-evaluations/README.md) | A model passes ordinary tests and is about to receive real tools. |
| 150 | [A Bounded Self-Improving System — Close the Research Loop](excavations/150-bounded-self-improvement/README.md) | Can a system improve its own components without quietly expanding its power or rewriting success? |
| 151 | [A Reproducible Baseline — Improve Something That Actually Exists](excavations/151-reproducible-baseline/README.md) | What exactly must remain fixed before an improvement can be measured? |
| 152 | [Profiling — Measure Where the Time Went](excavations/152-profiling/README.md) | The baseline is slow. Which operation actually consumes the time? |
| 153 | [The Input Pipeline — Stop Making the Accelerator Wait](excavations/153-input-pipeline/README.md) | How can loading overlap computation without changing the lessons? |
| 154 | [Sequence Packing — Stop Training on Empty Space](excavations/154-sequence-packing/README.md) | The pipeline is full, but why is much of each batch padding? |
| 155 | [Rotary Position Embeddings — Let Distance Enter the Match](excavations/155-rotary-position/README.md) | Packed tokens use the device efficiently. How should attention recognize relative separation? |
| 156 | [Relative Position Bias — What Should Happen Beyond the Seen Window?](excavations/156-relative-position-bias/README.md) | RoPE exposes relative distance, but how should attention treat distances never seen in training? |
| 157 | [The KV Cache — Stop Re-reading the Entire Past](excavations/157-kv-cache/README.md) | Why recompute old keys and values for every generated token? |
| 158 | [Multi-Query Attention — Why Cache Separate Copies for Every Head?](excavations/158-multi-query-attention/README.md) | The cache avoids recomputation. Why store one complete history per query head? |
| 159 | [Grouped-Query Attention — Recover Some Specialist Memory](excavations/159-grouped-query-attention/README.md) | Can specialist key-value views return without restoring every copy? |
| 160 | [FlashAttention — The Arithmetic Was Not the Bottleneck](excavations/160-flash-attention/README.md) | Why does exact long-sequence attention spend so much time moving its score matrix? |
| 161 | [RMSNorm — Do We Need to Subtract the Centre?](excavations/161-rmsnorm/README.md) | Can normalization preserve useful scale control with less work? |
| 162 | [Pre-Normalization — Protect the Residual Highway](excavations/162-pre-normalization/README.md) | Where should normalization sit so gradients can cross a deep stack? |
| 163 | [SwiGLU — Let One Learned Path Gate Another](excavations/163-swiglu/README.md) | Can the feed-forward block choose which candidate features pass? |
| 164 | [Weight Tying — Use One Word Geometry Twice](excavations/164-weight-tying/README.md) | Why learn unrelated token geometry at the entrance and exit? |
| 165 | [Adam — Give Each Parameter Its Own Step Scale](excavations/165-adam/README.md) | Why does one global learning rate train some weights poorly? |
| 166 | [AdamW — Keep Shrinkage Separate from Adaptation](excavations/166-adamw/README.md) | What goes wrong when weight decay passes through Adam's adaptive scaling? |
| 167 | [Gradient Clipping — Stop One Shock from Becoming a Catastrophe](excavations/167-gradient-clipping/README.md) | How should training react to one enormous gradient spike? |
| 168 | [Mixed Precision — Stop Storing Every Number with Unneeded Detail](excavations/168-mixed-precision/README.md) | Why pay full precision for operations that do not need it? |
| 169 | [Loss Scaling — Rescue Gradients Too Small to Represent](excavations/169-loss-scaling/README.md) | How can tiny gradients survive reduced precision? |
| 170 | [Gradient Accumulation — Build a Large Batch That Does Not Fit](excavations/170-gradient-accumulation/README.md) | How can several micro-batches become one honest optimizer step? |
| 171 | [Activation Checkpointing — Remember Less, Recompute Exactly](excavations/171-activation-checkpointing/README.md) | Why store every intermediate value when some can be rebuilt? |
| 172 | [ZeRO — Stop Replicating the Same Training State](excavations/172-zero-sharding/README.md) | Why does every data-parallel device hold the same optimizer state? |
| 173 | [Tensor Parallelism — Split One Matrix That No Device Can Hold](excavations/173-tensor-parallelism/README.md) | What if one layer is too large even when training state is sharded? |
| 174 | [Speculative Decoding — Let a Small Model Propose, Never Decide](excavations/174-speculative-decoding/README.md) | Can a cheap draft accelerate generation without replacing the trusted distribution? |
| 175 | [A Modern Tiny Language Model — Assemble the Measured Engine](excavations/175-modern-tiny-llm/README.md) | Can every earned repair cooperate while preserving evidence and a reference path? |
| 176 | [A Corpus Manifest — Know What Entered the Run](excavations/176-corpus-manifest/README.md) | Which exact body of evidence will shape the model? |
| 177 | [Document Boundaries — Keep One Story from Leaking into Another](excavations/177-document-boundaries/README.md) | How can packed documents avoid inventing false continuations? |
| 178 | [Language Identification — Do Not Confuse Familiar Script with Familiar Language](excavations/178-language-identification/README.md) | Which language evidence does the corpus actually contain? |
| 179 | [Exact Deduplication — Stop Paying Twice for the Same Document](excavations/179-exact-deduplication/README.md) | Why should a mirrored document receive more votes? |
| 180 | [Near Deduplication — When a Copy Changes a Few Words](excavations/180-near-deduplication/README.md) | How can edited copies be recognized without demanding equality? |
| 181 | [Quality Filtering — Remove Noise Without Defining Humanity Away](excavations/181-quality-filtering/README.md) | How can noise be reduced without hiding whose language was excluded? |
| 182 | [Data Provenance — Keep the Path Back to Every Source](excavations/182-data-provenance/README.md) | Can every final token be traced through the decisions that retained it? |
| 183 | [PII Redaction — Do Not Turn Accidental Secrets into Lessons](excavations/183-pii-redaction/README.md) | How can risky spans be removed without erasing the entire document? |
| 184 | [Data Mixtures — Decide Which Worlds Receive a Voice](excavations/184-data-mixtures/README.md) | Should raw source size silently choose the model's curriculum? |
| 185 | [Mixture Sampling — Turn Planned Shares into a Reproducible Stream](excavations/185-mixture-sampling/README.md) | How do domain proportions become a finite ordered stream? |
| 186 | [The Token Budget — Convert a Training Plan into a Count of Lessons](excavations/186-token-budget/README.md) | How much language will the run actually expose? |
| 187 | [Compute-Optimal Allocation — Buy a Larger Memory or More Experience?](excavations/187-compute-optimal-allocation/README.md) | Should fixed compute buy more parameters or more tokens? |
| 188 | [Learning-Rate Warmup — Let Adam Learn the Terrain Before Running](excavations/188-learning-rate-warmup/README.md) | Why are the optimizer's first steps unusually fragile? |
| 189 | [Cosine Decay — Make Late Corrections Smaller Without a Cliff](excavations/189-cosine-decay/README.md) | How should broad early learning become careful late correction? |
| 190 | [Gradient Noise Scale — When More Examples Stop Buying More Direction](excavations/190-gradient-noise-scale/README.md) | When does a larger batch mostly repeat existing advice? |
| 191 | [Data Parallelism — Let Several Workers Observe Different Evidence](excavations/191-data-parallelism/README.md) | How can several devices form one honest global batch? |
| 192 | [Pipeline Parallelism — Keep Layer Stages Working Together](excavations/192-pipeline-parallelism/README.md) | How can model stages avoid waiting for a whole batch? |
| 193 | [Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis](excavations/193-three-dimensional-parallelism/README.md) | How can tensor, pipeline, and data parallelism cooperate? |
| 194 | [Sharded Checkpoints — Save One Recoverable State Without Gathering It](excavations/194-sharded-checkpoints/README.md) | When is a directory of shards truly one checkpoint? |
| 195 | [Deterministic Resume — Continue the Same Experiment, Not a Similar One](excavations/195-deterministic-resume/README.md) | What must be restored so the next update remains the same? |
| 196 | [Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road](excavations/196-loss-spike-recovery/README.md) | When should a loss jump trigger recovery? |
| 197 | [A Validation Stream — Test Learning Outside the Current Batch](excavations/197-validation-stream/README.md) | Is the model improving beyond the data presently updating it? |
| 198 | [A Memorization Audit — Pattern or Stored Passage?](excavations/198-memorization-audit/README.md) | Can authorized probes reveal extractable training memory? |
| 199 | [The Training Report — Preserve the Decisions, Not Only the Weights](excavations/199-training-report/README.md) | What evidence must accompany the final tensors? |
| 200 | [A Tiny Pretraining Factory — Close the Accountable Training Loop](excavations/200-tiny-pretraining-factory/README.md) | Can one run remain traceable from source documents to reversible release? |

## A note on style

The questions and discoveries that shaped the original conversation are part of the argument, not side anecdotes: “How many tigers?”, “Where are they?”, comparing like attributes, squaring and rooting differences, distinguishing relevance from similarity, multiplying aligned features, and letting each expert contribute knowledge from its domain.

Each excavation is one coherent Markdown chapter. Diagrams and challenges appear only when they advance the reasoning.

## Build what you discover

The narrative is the spine, but this is not a notes-only project. Every excavation directory keeps its chapter, diagram, exercises, and relevant implementation together. Start with the chapter; open its companions only after the problem has made them meaningful.

## Project standard

The repository is periodically checked against the original teaching agreement in [AUDIT.md](AUDIT.md). Contributions must preserve the observation → failure → discovery sequence; see [CONTRIBUTING.md](CONTRIBUTING.md).
