# Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: keep documents containing mostly familiar Latin characters and discard the rest.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: keep documents containing mostly…
possible road B ─┘              └── loses: spanish and Vietnamese are mistaken…

same roads ──▶ repaired map ──▶ use a calibrated language classifier,…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “keep documents containing mostly familiar Latin characters and discard the rest”; the other knows how to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. When the failure—spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to language identification. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. This problem and its repair will travel under the name **Language Identification**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—keep documents containing mostly familiar Latin characters and discard the rest? The answer remains spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

## Do Not Confuse Familiar Script with Familiar Language

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

## The calculation hidden inside language identification

The archivist-engineer carries the language identification scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

### Why the melody needs these exact notes

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Cover the prose about language identification and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

## Where language identification runs out

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

The language identification repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the chain-of-custody ledger

Rebuild the language identification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Exact Deduplication — Stop Paying Twice for the Same Document](../179-exact-deduplication/README.md)
