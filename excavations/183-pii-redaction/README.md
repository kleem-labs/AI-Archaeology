# Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Data and pretraining operations

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to remove any entire document containing a sequence that resembles personal information.

Nothing about this first move is careless. To remove any entire document containing a sequence that resembles personal information is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

The important discovery is not merely that trying to remove any entire document containing a sequence that resembles personal information failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **PII Redaction**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Do Not Turn Accidental Secrets into Lessons

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

## Where pii redaction runs out

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside PII Redaction can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the chain-of-custody ledger

Rebuild the pii redaction scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Data Mixtures — Decide Which Worlds Receive a Voice](../184-data-mixtures/README.md)
