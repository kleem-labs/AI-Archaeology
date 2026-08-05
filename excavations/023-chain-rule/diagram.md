# Diagram — 023

~~~mermaid
flowchart LR
 A["A weight changes a hidden signal, which changes a score, which changes a probability, which changes the loss"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward."]
 D --> E["The Chain Rule"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
