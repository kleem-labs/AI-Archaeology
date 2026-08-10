# Excavation 127 — Experimental Design — Changing One Cause at a Time

[Previous excavation](../126-hypothesis-generation/README.md)

A new tokenizer and a larger model improve accuracy together. Which change helped?

Without knowing the inherited method, we might try this: Ship both improvements and compare with the old system.

Its hidden assumption appears in the following case: One score changed while two possible causes changed; the result cannot assign credit.

Remove that assumption and the needed repair becomes clear: Hold everything fixed except the suspected cause, and include a control that receives no intervention.

Only here do we name the idea: **Experimental Design**.

## Follow one case all the way through

Train four tiny models: old/new tokenizer crossed with small/large width; the four cells separate both effects and their interaction.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Perfect control in a laboratory may not represent deployment.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Reproducibility — Can the Discovery Survive Another Run?](../128-reproducibility/README.md)
