# Dependency Graph

~~~mermaid
flowchart TD
 O[Observations] --> F[Features] --> V[Vectors] --> D[Distance]
 V --> C[Change] --> M[Matrices] --> ME[Meaning] --> E[Embeddings]
 E --> A[Attention] --> S[Softmax] --> Q[Query Key Value]
 Q --> H[Multi Head Attention] --> N[Feed Forward Networks]
 N --> R[Residual Connections] --> L[Layer Normalization]
 L --> T[Learning] --> EM[Emergence]
~~~

Every arrow means the earlier idea creates or exposes the problem that forces the later one.
