# Excavation 072 — Linear Probes

<!-- book-prose-v2 -->

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

The least expensive next move is to train a powerful classifier on hidden states and call any success evidence.

The proposal deserves a fair hearing. For linear probes, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple.

The failure changes the question behind linear probes. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: use a deliberately limited probe and compare layers, controls, and baselines.

Only at this point does the inherited name **Linear Probes** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of linear probes by mentally removing the repair. We fall back to the proposal to train a powerful classifier on hidden states and call any success evidence; then the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. Restore only the ability to use a deliberately limited probe and compare layers, controls, and baselines, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to train a powerful classifier on hidden states and call any success evidence to requiring the system to use a deliberately limited probe and compare layers, controls, and baselines. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to linear probes.

## Understanding linear probes

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

Put the old procedure beside linear probes. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where linear probes runs out

Decodable information is not proof the model uses it.

The limit follows from the job assigned to linear probes. Its repair knows how to use a deliberately limited probe and compare layers, controls, and baselines. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take linear probes to the workbench

A claim about linear probes now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running linear probes, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the linear probes result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 073](../073-attribution/README.md)
