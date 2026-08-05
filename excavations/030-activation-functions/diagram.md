# Diagram — 030

~~~mermaid
flowchart LR
 A["Concrete problem"] --> B["Naive attempt"] --> C["A deep learner needs a simple nonlinearity that changes which paths respond while remaining trainable."] --> D["Place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually."]
~~~

~~~text
observe -> attempt -> break it -> repair -> expose the next limit
~~~
