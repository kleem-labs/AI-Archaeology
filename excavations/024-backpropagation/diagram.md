# Diagram — 024

~~~mermaid
flowchart LR
 A["A network has millions of weights and shared intermediate results"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream."]
 D --> E["Backpropagation"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
