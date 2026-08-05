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
 RI --> MA[Multi Agent Coordination] --> OB[Observability] --> BA[Bounded Autonomy]
~~~

Every arrow means the earlier idea creates or exposes the problem that forces the later one.
