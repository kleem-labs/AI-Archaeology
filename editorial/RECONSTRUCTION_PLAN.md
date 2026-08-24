# Manuscript Reconstruction Plan

## Diagnosis

The repository has locally correct explanations but not yet a book-length
causal argument. A `Previous` link establishes file order, not intellectual
necessity. Repeated phrases such as “A reasonable place to begin” expose the
authoring template and interrupt the reader’s situation model. Several part
boundaries also change domain without explaining why the expedition moved.

The manuscript will therefore be judged at three levels:

1. **Local causality** — every operation answers a failure visible in the same
   scene.
2. **Chapter causality** — every new problem is created by a capability earned
   in the preceding chapter.
3. **Book causality** — every part advances one evolving system rather than
   beginning an unrelated syllabus unit.

## Research translated into editorial rules

- Readers must explain why an action is needed, not merely see a worked step.
  This follows the self-explanation findings of Chi, Bassok, Lewis, Reimann,
  and Glaser (1989).
- A failed proposal is useful only when the failure identifies the missing
  knowledge. Productive-failure research therefore supports a concrete impasse,
  followed by consolidation—not ritual “wrong idea” headings.
- Causal links must be explicit enough for the reader to build one situation
  model across chapters. A chapter begins with the consequence of the previous
  chapter, not a fresh definition.
- Interesting material that does not advance the causal argument belongs in a
  companion file. Harp and Mayer’s experiments on seductive details motivate
  protecting the central line of reasoning.
- Worked examples reduce unproductive search for novices, but the example must
  expose subgoals and reasons. Numbers without named jobs fail this standard.

## The six-volume story

### Volume I — We build a mind (000–045)

A community first needs to recognize and compare animals, then preserve and
transform observations, then understand language, then build and train a tiny
language model. The object under construction never resets.

### Volume II — We let the mind enter the world (046–100)

The tiny language model speaks, but speech is not yet reliability. We evaluate
it, ground it, give it tools and authority, observe deployment feedback, inspect
its representations, extend its senses, teach it to act, and confront the cost
and governance of operating it at scale.

### Volume III — We let the mind keep learning (101–150)

The deployed system must distinguish kinds of ignorance, update beliefs,
retain old knowledge, model causes, plan and verify, protect people and data,
and finally propose improvements that cannot deploy themselves without
reproducible evidence and authorization.

### Volume IV — We rebuild the engine (151–175)

Return to the tiny language model under the bounded research loop. Preserve a
reproducible reference path while profiling, repairing attention and the block,
stabilizing optimization, crossing device boundaries, and verifying faster
decoding against the target distribution.

### Volume V — We account for pretraining (176–200)

Give the modern engine a traceable body of evidence and a recoverable training
plan. Preserve document identity through curation, make data and compute choices
explicit, make many workers behave like one experiment, and require validation,
memorization audits, documentation, and release gates before the final artifact
may leave the factory.

### Volume VI — We descend to the mathematical roots (201–225)

Return beneath the completed system and recover the mathematical inheritance it
has been using: boundaries and mappings, directions and transformations, local
and accumulated change, uncertain worlds and evidence, reusable futures,
trustworthy landscapes, and stable finite computation. Every familiar name is
covered until a concrete failure makes its responsibility necessary.

## Boundary contract

For adjacent chapters A → B:

1. A ends with a concrete capability now available.
2. The closing scene uses that capability and reveals one unresolved failure.
3. B opens in the same scene, with the same objects and goal.
4. B may name its topic only after the failure has made the missing operation
   clear.
5. No stock coaching sentence may appear.

## Equation contract

Before a displayed equation, the reader must have:

1. named objects;
2. performed each operation in ordinary language;
3. seen what breaks when an operation is omitted;
4. substituted concrete values where arithmetic is involved;
5. encountered every symbol as a nickname for a known job.

Every mathematical operation must also answer a counterfactual: why this move
rather than the nearest plausible alternative? “Sum combines the terms” is not
enough. The prose must show what a product would falsely claim, what would
cancel without a square, why a log is needed when probabilities multiply but
information must add, or why an exponential has the exact order-and-ratio
behavior the problem requires. The chapter then links that move to
`MATHEMATICAL_MOVES.md` so the reader can reuse it beyond one formula.

The notation must render in GitHub-compatible Markdown. Spacing macros that the
renderer misreads are prohibited.

## Sources informing the reconstruction

- [Chi, Bassok, Lewis, Reimann, and Glaser (1989), “Self-explanations: How
  students study and use examples in learning to solve problems.”](https://doi.org/10.1016/0364-0213(89)90002-5)
- [Harp and Mayer (1998), “How Seductive Details Do Their Damage.”](https://doi.org/10.1037/0022-0663.90.3.414)
- [Kapur (2008), “Productive Failure.”](https://doi.org/10.1080/07370000802212669)
- [DeCaro and Rittle-Johnson (2012), “Exploring mathematics problems prepares
  children to learn from instruction.”](https://doi.org/10.1016/j.jecp.2012.06.009)
- [Graesser, Millis, and Zwaan (1997), “Discourse Comprehension.”](https://doi.org/10.1146/annurev.psych.48.1.163)
