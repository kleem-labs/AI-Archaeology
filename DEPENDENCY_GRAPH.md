# Dependency Graph

~~~mermaid
flowchart TD
 O[Observations] --> F[Features] --> V[Vectors] --> D[Distance]
 V --> C[Change] --> M[Matrices] --> ME[Meaning] --> E[Embeddings]
 E --> A[Attention] --> S[Softmax] --> Q[Query Key Value]
 Q --> H[Multi Head Attention] --> N[Feed Forward Networks]
 N --> R[Residual Connections] --> L[Layer Normalization]
 L --> T[Learning] --> EM[Emergence]
 GD --> MB[Mini Batches] --> LR[Learning Rate] --> MO[Momentum]
 MO --> IN[Initialization] --> AF[Activation Functions] --> OV[Overfitting]
 OV --> RE[Regularization] --> VA[Validation] --> GE[Generalization]
 GE --> TN[Tiny Neural Network] --> TO[Tokenization] --> IE[Input Embeddings] --> PI[Positional Information]
 PI --> CM[Causal Masking] --> NT[Next Token Examples] --> LO[Logits]
 LO --> VP[Vocabulary Probabilities] --> SA[Sampling] --> CW[Context Window] --> GPT[Tiny GPT] --> PE[Perplexity]
 PE --> EV[Evaluation] --> HA[Hallucination] --> CA[Calibration]
 CA --> DQ[Data Quality] --> SL[Scaling Laws] --> IT[Instruction Tuning]
 IT --> PL[Preference Learning] --> RAG[Retrieval] --> AG[Tool Using Agents] --> AU[Authority]
 AU --> PI[Prompt Injection] --> PN[Planning] --> ME[Memory]
 ME --> ST[State Machines] --> VE[Verification] --> RI[Retries and Idempotency]
 RI --> MA[Multi Agent Coordination] --> OB[Observability] --> BA[Bounded Autonomy] --> FL[Feedback Loops]
 FL --> OL[Online Learning] --> DD[Distribution Drift] --> CE[Controlled Experiments] --> BD[Bandits]
 BD --> FI[Internal Features] --> LP[Linear Probes] --> AT[Attribution] --> SP[Superposition] --> CI[Causal Interventions]
 CI --> PX[Pixels] --> CO[Convolution] --> PO[Pooling] --> CNN[CNN Hierarchy] --> VT[Vision Transformers]
 VT --> AE[Autoencoders] --> LS[Latent Space] --> AR[Autoregressive Images] --> DI[Diffusion] --> DN[Denoising]
 DN --> RW[Rewards] --> SA[States and Actions] --> VA[Value] --> QL[Q Learning] --> PG[Policy Gradients]
 PG --> MM[Multimodal Alignment] --> CL[Contrastive Learning] --> AU[Audio] --> LR[LoRA] --> QU[Quantization]
 QU --> DT[Distributed Training] --> IS[Inference Serving] --> RT[Red Teaming] --> GO[Governance] --> CS[Complete AI System] --> UK[Two Kinds of Uncertainty]
 UK --> BY[Bayesian Updating] --> EN[Ensembles] --> AL[Active Learning] --> SE[Selective Prediction]
 SE --> CF[Catastrophic Forgetting] --> CT[Continual Learning] --> ML[Meta Learning] --> CU[Curriculum] --> SS[Self Supervision]
 SS --> WM[World Models] --> CA[Causality] --> CO[Counterfactuals] --> MP[Model Based Planning] --> TS[Tree Search]
 TS --> RV[Reasoning Verification] --> NS[Neuro Symbolic] --> KG[Knowledge Graphs] --> GN[Graph Networks] --> PS[Program Synthesis]
 PS --> FV[Formal Verification] --> DP[Differential Privacy] --> FE[Federated Learning] --> AR[Adversarial Robustness] --> OR[Open Ended Research]
~~~

Every arrow means the earlier idea creates or exposes the problem that forces the later one.
