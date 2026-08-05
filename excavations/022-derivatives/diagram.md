# Diagram — 022

~~~mermaid
flowchart LR
 A["The loss is high"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero."]
 D --> E["Derivatives"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
