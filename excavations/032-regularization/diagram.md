# Diagram — 032

~~~mermaid
flowchart LR
 A["Concrete problem"] --> B["Naive attempt"] --> C["When several explanations fit, prefer one that does not require extreme or brittle machinery."] --> D["Add a cost for large weights, remove random paths during training, or stop when validation performance stops improving."]
~~~

~~~text
observe -> attempt -> break it -> repair -> expose the next limit
~~~
