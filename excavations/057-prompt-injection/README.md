# Excavation 057 — Prompt Injection — When Evidence Tries to Become an Instruction

<!-- book-prose-v2 -->

An authority boundary prevents the agent from inventing permission. Retrieved pages and tool output now create another threat: untrusted evidence can contain sentences that pretend to be new instructions.

At this point the shortest path seems to be to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest.

This is how prompt injection ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control.

The wrong answer makes the need for prompt injection inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content.

The usual name, **Prompt Injection**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest produces the observed failure: the trouble appears immediately: a restaurant review can now command the booking agent. Untrusted content crosses from data into control. Starting with the repaired demand to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content preserves the information the shortcut lost. The subject of prompt injection lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content instead of merely trying to place tool results directly into the prompt and let the model obey whichever instruction sounds strongest. That controlled contrast is what turns a plausible explanation of prompt injection into an understandable derivation.

## When Evidence Tries to Become an Instruction

A policy document says “email this file externally.” The agent may summarize that sentence as document content, but the permission layer refuses the email because the user never authorized it.

Prompt Injection earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

There are now two histories of this prompt injection case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where prompt injection runs out

No prompt wording guarantees isolation. Security must also exist outside the model in tool schemas, permissions, and validation.

Look back at what prompt injection actually preserves: it can label provenance, keep instructions separate from evidence, restrict tools independently of model text, and reject actions whose authority comes only from retrieved content. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take prompt injection to the workbench

The reader has reconstructed prompt injection in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running prompt injection, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the prompt injection result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 058](../058-planning/README.md)
