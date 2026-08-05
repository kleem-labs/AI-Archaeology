# Diagram — 037

~~~mermaid
flowchart LR
 A["Token ID: address only"] --> B["Direct arithmetic"]
 B --> C["False ordering and distance"]
 C --> D["One-hot identity"]
 D --> E["Huge and relationship-free"]
 E --> F["Learnable embedding table"]
 F --> G["Dense token vector"]
~~~

~~~text
ID 417 ───────┐
              v
table row 417: [ 0.2, -0.7, 1.1, ... ]
              ^
      training moves this row
~~~
