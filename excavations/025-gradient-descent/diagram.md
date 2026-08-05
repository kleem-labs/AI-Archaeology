# Diagram — 025

~~~mermaid
flowchart LR
 A["We can now assign blame to every weight"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress."]
 D --> E["Gradient Descent"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
