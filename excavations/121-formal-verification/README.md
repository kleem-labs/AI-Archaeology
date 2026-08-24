# Excavation 121 — Formal Verification

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.

Morning reaches the Hall of Possible Worlds before anyone has a name for today's difficulty. Beside the table of mirrored maps, the keeper of unfinished questions tries the smallest continuation of what already works: add more random tests and call the property proven.

The rule survives the easy cases. The next case leaves a crack through the middle of it: an untested edge case can remain. More confidence cannot repair information that never entered the rule.

*The keeper of unfinished questions sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: add more random tests and call the…
possible road B ─┘              └── loses: an untested edge case can remain

same roads ──▶ repaired map ──▶ state assumptions and desired…
```

Two trails now cross the table of mirrored maps. The pale trail bears the instruction “add more random tests and call the property proven.” It disappears into the observed failure: an untested edge case can remain. The darker trail carries one additional capacity—to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed formal verification mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the table of mirrored maps is altered in exactly one way: state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. Much later, people will call this territory **Formal Verification**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the table of mirrored maps. The failed path remains visible beneath the repair, because formal verification is easier to remember when its scar remains attached to it. The scar reads, ‘an untested edge case can remain’; the new line exists only to keep that loss from happening again.

## Understanding formal verification

Prove a refund state machine can issue at most one payment per idempotency key.

## Where formal verification runs out

Proof covers the formal model, which may omit real-world behavior.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Formal Verification was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the formal verification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 122](../122-differential-privacy/README.md)
