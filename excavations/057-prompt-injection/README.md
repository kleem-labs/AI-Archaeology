# Excavation 057 — Prompt Injection — When Evidence Tries to Become an Instruction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.

The previous discovery reaches the Gatehouse of Consequences carrying one unfinished problem. Beside the iron threshold, the gatekeeper first tries to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

There is good reason to begin this way. If we place tool results directly into the prompt and let the model obey whichever instruction sounds strongest, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control.

This failure cannot be repaired by performing the instruction to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the iron threshold; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Prompt Injection**. The name is simply a handle for the distinction already reconstructed.

## When Evidence Tries to Become an Instruction

A policy document says “email this file externally.” The agent may summarize that sentence as document content, but the permission layer refuses the email because the user never authorized it.

Prompt Injection earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where prompt injection runs out

No prompt wording guarantees isolation. Security must also exist outside the model in tool schemas, permissions, and validation.

One unsolved mark remains on the iron threshold. None of the responsibilities inside Prompt Injection can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the iron threshold

Rebuild the prompt injection scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 058](../058-planning/README.md)
