# Diagram — 033

~~~mermaid
flowchart LR
 A["Concrete problem"] --> B["Naive attempt"] --> C["One unseen set must guide choices, while another remains untouched for the final estimate."] --> D["Split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end."]
~~~

~~~text
observe -> attempt -> break it -> repair -> expose the next limit
~~~
