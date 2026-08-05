# Diagram — 021

~~~mermaid
flowchart LR
 A["A model predicts tiger 90% and deer 10%, but a deer appears"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Charge the information cost assigned by the predicted distribution to the outcome that actually occurred."]
 D --> E["Cross-Entropy"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
