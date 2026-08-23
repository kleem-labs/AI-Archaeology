# Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

<!-- book-prose-v2 -->

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

The machinery already in our hands suggests that we remove any entire document containing a sequence that resembles personal information.

This is how pii redaction ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

The wrong answer makes the need for pii redaction inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.

The usual name, **PII Redaction**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to remove any entire document containing a sequence that resembles personal information produces the observed failure: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span. Starting with the repaired demand to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision preserves the information the shortcut lost. The subject of pii redaction lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision instead of merely trying to remove any entire document containing a sequence that resembles personal information. That controlled contrast is what turns a plausible explanation of pii redaction into an understandable derivation.

## Do Not Turn Accidental Secrets into Lessons

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

There are now two histories of this pii redaction case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where pii redaction runs out

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

Look back at what pii redaction actually preserves: it can detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take pii redaction to the workbench

The reader has reconstructed pii redaction in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pii redaction, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pii redaction result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Data Mixtures — Decide Which Worlds Receive a Voice](../184-data-mixtures/README.md)
