# Excavation 124 — Adversarial Robustness

<!-- book-prose-v2 -->

Federated learning moves computation to distributed data. Model updates and inputs remain vulnerable to malicious or tiny perturbations that preserve human meaning while flipping machine behavior.

If the old idea can be stretched one step farther, we should test only natural clean examples.

If the proposal works on every relevant case, adversarial robustness is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: an attacker follows the model’s sensitivity into a brittle direction.

Nothing magical creates adversarial robustness. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: search for worst-case permitted perturbations, train against them, and bound behavior where possible.

This boundary between the failed rule and its repair is the subject later work calls **Adversarial Robustness**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize adversarial robustness; try to break it by subtraction. Remove the part that knows how to search for worst-case permitted perturbations, train against them, and bound behavior where possible, leaving only the attempt to test only natural clean examples. What returns is not a vague weakness but the original contradiction: an attacker follows the model’s sensitivity into a brittle direction. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to test only natural clean examples receives the same test as the rule to search for worst-case permitted perturbations, train against them, and bound behavior where possible. Their different outcomes reveal what adversarial robustness contributes without asking the reader to trust historical convention.

## Understanding adversarial robustness

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

Hold the setting, evidence, and desired outcome fixed while testing adversarial robustness. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## Where adversarial robustness runs out

Robustness to one threat model does not imply robustness to others.

This is where adversarial robustness runs out for a causal reason. We gave it enough structure to search for worst-case permitted perturbations, train against them, and bound behavior where possible, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take adversarial robustness to the workbench

A mathematical story about adversarial robustness earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running adversarial robustness, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the adversarial robustness result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 125](../125-open-ended-research-system/README.md)
