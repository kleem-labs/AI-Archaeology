# Diagram — 019

~~~mermaid
flowchart LR
 A["A messenger can report either “the sun rose” or “a tiger entered camp"] --> B["Naive attempt"]
 B --> C["Failure becomes visible"]
 C --> D["Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs."]
 D --> E["Information"]
~~~

~~~text
problem -> attempt -> failure -> need -> discovery
~~~
