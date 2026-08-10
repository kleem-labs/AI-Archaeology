# Diagram — Excavation 121 — Formal Verification

The picture carries this excavation's particular counterexample and repair.

```mermaid
flowchart TD
    A["Add more random tests and call the property proven."] --> B["Reality: An untested edge case can remain."]
    B -. "missing requirement" .-> C["State assumptions and desired properties formally, then prove or mechanically check that…"]
```

```text
TRY     Add more random tests and call the property proven.
BREAK   An untested edge case can remain.
REPAIR  State assumptions and desired properties formally, then prove or mechanically check that…
```
