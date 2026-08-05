# Diagram — 020

~~~mermaid
flowchart LR
 A["One bag contains ten red stones"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Average the information of every possible outcome, weighted by how often that outcome occurs."]
 D --> E["Entropy"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
