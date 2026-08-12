# Excavation 127 — Experimental Design — Changing One Cause at a Time

A testable hypothesis predicts a measurable difference. If several components change together, the result cannot reveal which intervention caused that difference.

We first try to ship both improvements and compare with the old system.

The trouble appears immediately: one score changed while two possible causes changed; the result cannot assign credit.

We need to hold everything fixed except the suspected cause, and include a control that receives no intervention.

## Let the case decide

Train four tiny models: old/new tokenizer crossed with small/large width; the four cells separate both effects and their interaction.

## The boundary of the discovery

Perfect control in a laboratory may not represent deployment.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Reproducibility — Can the Discovery Survive Another Run?](../128-reproducibility/README.md)
