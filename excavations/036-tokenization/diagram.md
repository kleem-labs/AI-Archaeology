# Diagram — 036

~~~mermaid
flowchart LR
 A[Raw text] --> B[Whole words] --> C[Unknown vocabulary]
 C --> D[Characters] --> E[Sequences too long]
 E --> F[Merge repeated neighbors] --> G[Subword tokens]
~~~

~~~text
words: too large <- need -> characters: too small
                    |
                 subwords
~~~
