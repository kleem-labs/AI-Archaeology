# Diagram — 027

~~~mermaid
flowchart LR
 A["Concrete problem"] --> B["Naive attempt"] --> C["Direction without step size is not an update."] --> D["Multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time."]
~~~

~~~text
observe -> attempt -> break it -> repair -> expose the next limit
~~~
