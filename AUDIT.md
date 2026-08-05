# Repository Audit — 2026-08-04

## Verdict before this revision

**The repository partially matched the teaching standard, but did not match the promised project standard.**

The chapters already followed much of the correct narrative method. They began with tigers, movement, experts, messages, and footprints rather than definitions. The strongest chapters preserved the learner's actual discoveries:

- compare like attributes before calculating a difference;
- square, add, and take the root when signed differences cancel;
- distance measures similarity, while attention needs directional relevance;
- multiply aligned query/key features and add them to obtain one score;
- let each expert contribute knowledge from their own domain.

Equations usually appeared after these arguments. That material was worth preserving.

The project nevertheless failed the stated scope. It contained seventeen short chapter files plus three indexes, but no runnable code, tests, substantial exercise sets, or dedicated diagrams. The roadmap even postponed those elements. A reader could read a compact narrative but could not yet build, test, alter, or inspect the ideas. That is a notes repository, not the promised book-and-laboratory.

## Rubric

| Standard | Before revision | Evidence | Required correction |
|---|---|---|---|
| Begin with observation and a concrete problem | Strong | Every chapter opens in a physical or linguistic situation | Preserve |
| Show plausible attempts and their failure | Strong but brief | Named failed attempts throughout 000–016 | Preserve; exercises extend them |
| Preserve the learner's reasoning | Strong in 001, 003, 004, 010, 011 | Directly attributed discoveries | Preserve as the spine, not decoration |
| Make mathematics inevitable | Mostly strong | Equations generally occur after prose derivations | Keep equations downstream of need |
| Explain simply without becoming inaccurate | Strong | Short sentences, concrete examples, explicit limitations | Preserve caveats |
| Code and implementations | Missing | No source files | Add plain Python, NumPy, and PyTorch stages |
| Exercises | Inadequate | One challenge per chapter | Add staged observation, failure, derivation, and building tasks |
| Diagrams | Inadequate | A few inline text sketches | Add a visual path for the full arc |
| Verification | Missing | No tests or project configuration | Add deterministic tests |
| Full professional project scope | Failed | Roadmap deferred core deliverables | Restore milestones and contribution rules |

## What this revision changes

This revision keeps the narrative chapters and adds three companion paths: diagrams, invention exercises, and runnable implementations. The code is deliberately staged: plain Python exposes every operation; NumPy reveals the matrix form; PyTorch shows the recognizable Transformer structure. Tests verify the executable claims.

## Ongoing acceptance test

A new excavation is incomplete unless a reviewer can answer yes to all seven questions:

1. Does it begin with something observable?
2. Is there a concrete decision or problem?
3. Does a reasonable first attempt fail for a visible reason?
4. Does the discovery respond exactly to that failure?
5. Can the reader explain every operation before seeing notation?
6. Do the diagram, exercise, and code reveal the same argument?
7. Does the ending create the need for the next excavation?
