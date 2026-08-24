# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

Morning reaches the Gatehouse of Consequences before anyone has a name for today's difficulty. Beside the iron threshold, the gatekeeper tries the smallest continuation of what already works: give the agent a broad goal and let it continue until it believes the goal is complete.

At the edge of the iron threshold, the shortcut produces its consequence: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. That consequence, not a textbook, earns the next move.

*The gatekeeper sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: give the agent a broad goal and let…
possible road B ─┘              └── loses: a mistaken assumption triggers a long…

same roads ──▶ repaired map ──▶ create an explicit operating…
```

The gatekeeper covers the new mark and the old contradiction returns: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step. The cover is lifted, restoring the ability to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason bounded autonomy exists.

What must change for bounded autonomy is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path. That threshold is where **Bounded Autonomy** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In bounded autonomy, that memory takes a precise form: whenever a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step, preserve enough structure to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.

## Building an Agent That Can Be Trusted

A deployment agent may modify staging for thirty minutes, spend at most a fixed budget, run required tests, and prepare a production change. Production execution remains behind human approval.

Bounded Autonomy earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where bounded autonomy runs out

Bounded autonomy reduces blast radius; it does not make the model infallible. Responsibility remains with the people and systems granting authority.

Here the new path ends honestly. Bounded Autonomy can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## The mind reaches the gate

Speech became evidence-seeking action, and action demanded authority, state, verification, safe repetition, coordination, and an operating boundary. Intelligence crossed into the world only by learning that capability and permission are different quantities.

```text
answer → evidence → tool → authority → state → proof → boundary
```

The trail called *the mind reaches the gate* is what remains when one necessity becomes another.

## Return to the iron threshold

Rebuild the bounded autonomy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Feedback Loops](../066-feedback-loops/README.md)
