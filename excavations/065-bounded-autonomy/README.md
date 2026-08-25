# Excavation 065 — Bounded Autonomy — Building an Agent That Can Be Trusted

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

Observability makes a failure inspectable after it occurs. Trust requires more than postmortems: the agent's possible actions must remain inside an explicit operating envelope before anything goes wrong.

The previous discovery reaches the Gatehouse of Consequences carrying one unfinished problem. Beside the iron threshold, the gatekeeper first tries to give the agent a broad goal and let it continue until it believes the goal is complete.

There is good reason to begin this way. If we give the agent a broad goal and let it continue until it believes the goal is complete, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

This failure cannot be repaired by performing the instruction to give the agent a broad goal and let it continue until it believes the goal is complete more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the iron threshold; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Bounded Autonomy**. The name is simply a handle for the distinction already reconstructed.

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
