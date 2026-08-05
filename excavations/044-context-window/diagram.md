# Diagram — 044

~~~mermaid
flowchart LR
 A[Concrete problem] --> B[Naive attempt] --> C[Visible failure] --> D["Choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past."]
~~~
