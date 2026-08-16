# Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

We first try to remove any entire document containing a sequence that resembles personal information.

That confidence lasts only until the first measurement. One phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

What broke tells us what the next design must preserve. Detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.

## Let one run decide

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

## What this repair cannot do

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Data Mixtures — Decide Which Worlds Receive a Voice](../184-data-mixtures/README.md)
