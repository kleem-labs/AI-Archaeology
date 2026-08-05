# Diagram — 028

~~~mermaid
flowchart LR
 A["Concrete problem"] --> B["Naive attempt"] --> C["Useful direction persists across batches while much of the noise changes sign."] --> D["Keep a fading memory of past gradients and combine it with the new one."]
~~~

~~~text
observe -> attempt -> break it -> repair -> expose the next limit
~~~
