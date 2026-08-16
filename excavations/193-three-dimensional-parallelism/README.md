# Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

An obvious shortcut is to increase whichever parallel technique was introduced most recently until the model fits.

Then the hidden cost becomes visible. More pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

Crossing that boundary requires one additional guarantee. Compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

## Let one run decide

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

## The arithmetic we have earned

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

Only now can we compress the procedure:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

## What this repair cannot do

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Sharded Checkpoints — Save One Recoverable State Without Gathering It](../194-sharded-checkpoints/README.md)
