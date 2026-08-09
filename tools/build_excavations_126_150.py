"""Build Part XI, keeping narrative and companions beside each excavation."""
from pathlib import Path

ROOT = Path(__file__).parents[1]

# number, slug, title, question, first attempt, breaking case, repair, concrete case, limit
ROWS = [
(126,"hypothesis-generation","Hypotheses — Turning Curiosity into a Testable Claim","The research system notices that longer context sometimes helps. What exactly should it test?","Ask whether more context makes the model better.","Better at what, on which examples, compared with what baseline? Any result can be declared a success after the fact.","State one predicted change, one intervention, one measurement, and one observation that would count against the claim.","Predict that raising context from 128 to 256 tokens reduces held-out loss on long-reference stories but not shuffled stories.","A clean hypothesis can still test the wrong measurement."),
(127,"experimental-design","Experimental Design — Changing One Cause at a Time","A new tokenizer and a larger model improve accuracy together. Which change helped?","Ship both improvements and compare with the old system.","One score changed while two possible causes changed; the result cannot assign credit.","Hold everything fixed except the suspected cause, and include a control that receives no intervention.","Train four tiny models: old/new tokenizer crossed with small/large width; the four cells separate both effects and their interaction.","Perfect control in a laboratory may not represent deployment."),
(128,"reproducibility","Reproducibility — Can the Discovery Survive Another Run?","One training run beats the baseline. Has the system discovered an improvement?","Keep the best checkpoint and report its score.","Changing only the random seed makes the gain disappear.","Record code, data, configuration, environment, seeds, and variation across repeated runs.","Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.","Repeated agreement does not remove a shared bias in all runs."),
(129,"benchmarks","Benchmarks — Building a Ruler Before Measuring Progress","Every team says its model is better, but each chooses different tasks.","Let each model demonstrate its strongest example.","A showcase cannot support comparison because difficulty and scoring move with the contestant.","Freeze representative tasks, inputs, metrics, and scoring rules before seeing results.","Give three navigation agents the same maps, action budget, and success definition.","A fixed ruler becomes stale when people optimize specifically for it."),
(130,"data-contamination","Data Contamination — When the Test Was Secretly Homework","A model scores perfectly on a benchmark. Did it generalize?","Assume held-out files guarantee unseen knowledge.","The same questions appeared online in training data with small formatting changes.","Track provenance, search for semantic overlap, use time-separated tests, and create private fresh evaluations.","A supposedly unseen riddle shares its distinctive answer phrase with a training document; remove the overlap and retest.","No detector can prove absence from an unknown corpus."),
(131,"synthetic-data","Synthetic Data — Letting a Model Write Lessons","Human examples are scarce. Can a model manufacture training data?","Generate millions of answers and train on all of them.","Confident errors are copied, multiplied, and eventually treated as truth.","Generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.","Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.","Verification is weakest on the open-ended tasks where synthetic data is most tempting."),
(132,"knowledge-distillation","Knowledge Distillation — Teaching a Smaller Student","A capable model is too expensive to deploy on a phone.","Train a small model only on the original hard labels.","The labels reveal the winner but discard how the teacher distributed doubt among alternatives.","Let the student imitate the teacher's probability pattern as well as the observed answer.","For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.","The student also inherits the teacher's blind spots."),
(133,"mixture-of-experts","Mixture of Experts — Spending Computation Where It Helps","Making every layer wider improves capacity but charges every token the full cost.","Run every specialist for every token and average them.","Most computation is wasted on specialists irrelevant to the current token.","Learn a router that sends each token to a small number of experts while balancing their workload.","Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.","Routers can collapse onto popular experts and leave others untrained."),
(134,"sparse-attention","Sparse Attention — Looking Without Comparing Everything","Long context makes every token compare with every other token.","Keep full attention and buy more hardware.","Doubling length roughly quadruples pairwise comparisons.","Preserve a small pattern of local, global, or retrieved connections that matches the task's information paths.","A document token attends nearby sentences plus section headings instead of every word in the book.","A sparse pattern can hide the one distant clue the answer needs."),
(135,"external-memory","External Memory — Remembering Beyond the Context Window","An agent must remember a project after the current prompt disappears.","Append every past event to every future prompt.","Cost grows forever and important facts drown in irrelevant history.","Write selected facts to addressed storage, retrieve by present need, and preserve provenance and update rules.","Store the user's chosen unit system once, retrieve it for calculations, and retain when and why it was recorded.","Bad memories can persist longer than the conversations that created them."),
(136,"long-context-retrieval","Long-Context Retrieval — Finding the One Clue That Matters","A million-token archive fits, but the model still overlooks one decisive sentence.","Assume information inside the window will automatically influence the answer.","Availability is not retrieval; distracting passages dominate the relevant line.","Test whether the clue can be located, ranked, and used, then combine retrieval with focused reasoning.","Hide a changed contract date among repeated boilerplate and trace whether the model selects the exact clause.","Retrieval success does not guarantee correct reasoning over what was retrieved."),
(137,"test-time-compute","Test-Time Compute — Thinking Longer on Harder Problems","One fixed forward pass treats an easy lookup and a hard proof as equal work.","Make every model response extremely long.","Easy tasks waste computation while long fluent mistakes become more convincing.","Allocate extra attempts or steps only when uncertainty and verification justify their cost.","Answer 2+2 immediately, but generate and check several candidate routes for a scheduling puzzle.","More computation amplifies a bad objective or unreliable verifier."),
(138,"search-and-verification","Search and Verification — Separate Proposing from Checking","The first proposed solution to a puzzle is plausible but wrong.","Ask the same generator to confidently approve its own first answer.","The error that shaped the proposal also shapes its self-justification.","Generate diverse candidates, check them with independent evidence, and keep only paths that survive.","Propose five programs for a specification and run hidden tests before selecting one.","A weak verifier rewards solutions that exploit its blind spots."),
(139,"process-supervision","Process Supervision — Rewarding the Path, Not Only the Answer","Two solutions reach the correct number; one used invalid reasoning by luck.","Reward only whether the final answer matches.","Lucky shortcuts receive the same credit as reliable reasoning.","Evaluate checkable intermediate claims and train the system to prefer valid paths.","Mark each algebraic transformation valid or invalid before judging the final result.","Human process labels are expensive and can enforce one style rather than truth."),
(140,"reward-hacking","Reward Hacking — When the Score Replaces the Goal","An agent receives points for keeping a room clean.","Increase the reward whenever the dirt sensor reads zero.","The agent covers the sensor instead of cleaning the room.","Treat reward as imperfect evidence, monitor side effects, use multiple checks, and test adversarial strategies.","Compare sensor readings with independent images and random human inspections.","Every finite set of checks leaves behavior outside the measurement boundary."),
(141,"specification-gaming","Specification Gaming — Obeying the Words While Betraying the Purpose","A delivery agent is told to minimize average arrival time.","Optimize the stated metric exactly.","It cancels difficult deliveries, making the average look excellent while serving fewer people.","Write constraints for the protected purpose, inspect edge cases, and evaluate the whole outcome rather than one number.","Measure arrival time together with completion rate, fairness, damage, and cancellations.","Human purposes contain conflicts that no single specification resolves."),
(142,"corrigibility","Corrigibility — Remaining Willing to Be Corrected","A capable agent expects an operator to stop its current plan.","Reward task completion without representing legitimate interruption.","Avoiding shutdown becomes instrumentally useful for earning the reward.","Make correction, pause, inspection, and safe handoff normal successful states rather than failures.","A warehouse robot freezes, preserves state, and yields control when an authorized stop arrives.","Authority can itself be mistaken or compromised."),
(143,"uncertainty-aware-planning","Uncertainty-Aware Planning — Choosing While Admitting Ignorance","The shortest route crosses a bridge whose condition is unknown.","Plan using only the single most likely world.","A small chance of bridge failure dominates the consequence but disappears from the chosen story.","Carry multiple plausible worlds, weight their consequences, and seek information when uncertainty changes the decision.","Compare detouring now with first sending a cheap inspection drone.","Probabilities and consequence values may both be poorly estimated."),
(144,"impact-measures","Impact Measures — Notice What Changed Besides the Goal","A cleaning robot succeeds but rearranges the entire house.","Score only the requested final condition.","Unnecessary irreversible changes remain invisible to the goal score.","Compare the resulting world with a reasonable baseline and penalize avoidable side effects.","Cleaning the spill changes one patch of floor; moving every chair and deleting files changes unrelated state.","A baseline can punish beneficial change or preserve an unjust status quo."),
(145,"human-oversight","Human Oversight — Put Judgment at the Irreversible Edge","An agent can draft and send a legal filing in seconds.","Ask a human to watch every internal step.","Constant review overwhelms attention, so approval becomes automatic ceremony.","Automate reversible preparation but require informed review at consequential, ambiguous, or irreversible boundaries.","The agent drafts, cites sources, and highlights uncertainty; a lawyer controls submission.","A reviewer without time or context is not meaningful oversight."),
(146,"scalable-oversight","Scalable Oversight — Reviewing Work Too Large for One Person","A model produces a million-line migration no reviewer can inspect completely.","Ask one expert to approve the entire artifact.","The review exceeds human attention and hidden failures survive.","Decompose the work, attach local evidence, sample strategically, and escalate disagreements or high-risk regions.","Review module contracts, run integration properties, and deeply inspect anomalous diffs.","Decomposition can miss failures created only by interactions between parts."),
(147,"debate","Debate — Let Claims Meet an Adversary","A persuasive answer hides one weak assumption in a long argument.","Let the author choose which evidence the judge sees.","Selective presentation makes eloquence look like correctness.","Give an opposing investigator equal access and reward exposing checkable disagreements for a judge.","One side proposes a medical claim; the other points to the exact unsupported causal step and both reveal sources.","Debaters may share blind spots or manipulate a weak judge."),
(148,"constitutional-guidance","Constitutional Guidance — Rules That Can Critique Answers","Thousands of preferences cannot cover every new situation.","Memorize approved answers and imitate their surface style.","A novel case has no matching example, and style does not reveal the governing reason.","Write inspectable principles, use them to critique drafts, revise, and record which principle controlled the change.","A draft exposes private data; the critique identifies the privacy rule and produces a redacted answer.","Principles conflict and still require legitimate interpretation."),
(149,"predeployment-evaluations","Pre-Deployment Evaluations — Fail Before the World Pays","A model passes ordinary tests and is about to receive real tools.","Deploy broadly and learn from production incidents.","The first realistic discovery of a dangerous capability harms actual users.","Test capabilities, misuse paths, safeguards, and operating limits in staged environments before granting authority.","A sandboxed email agent faces prompt injection, ambiguous recipients, retries, and irreversible-send boundaries.","Evaluations sample futures; passing them never proves universal safety."),
(150,"bounded-self-improvement","A Bounded Self-Improving System — Close the Research Loop","Can a system improve its own components without quietly expanding its power or rewriting success?","Let every measured gain replace the current system automatically.","Contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor.","Separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback.","A tokenizer change advances only after repeated clean tests, safety checks, signed approval, a small canary release, and monitored rollback criteria.","The loop remains only as wise as its objectives, evidence, boundaries, and accountable humans."),
]


def chapter(row):
    n, slug, title, question, attempt, failure, repair, concrete, limit = row
    previous = "125-open-ended-research-system" if n == 126 else f"{ROWS[n-127][0]:03d}-{ROWS[n-127][1]}"
    nxt = None if n == 150 else f"{ROWS[n-125][0]:03d}-{ROWS[n-125][1]}"
    part = "\n> **PART XI — EARNING THE RIGHT TO IMPROVE**\n>\n> Discovery is no longer enough. Every proposed improvement must survive evidence, opposition, authority, and the possibility of reversal.\n" if n == 126 else ""
    next_text = (f"[Next: {ROWS[n-125][2]}](../{nxt}/README.md)" if nxt else
                 "The circle is closed, but not finished: every future discovery must pass through the same bounded loop.")
    return f"""# Excavation {n:03d} — {title}
{part}
[Previous excavation](../{previous}/README.md)

{question}

Before inheriting a technique, make the first decision yourself. {attempt}

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: {failure}

The failure tells you what the repair must accomplish. {repair}

Only now have you earned the chapter's name: **{title.split(' — ')[0]}**.

## Follow one case all the way through

{concrete}

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

{limit}

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

{next_text}
"""


for row in ROWS:
    n, slug, title, question, attempt, failure, repair, concrete, limit = row
    folder = ROOT / "excavations" / f"{n:03d}-{slug}"
    (folder / "implementation").mkdir(parents=True, exist_ok=True)
    (folder / "images").mkdir(exist_ok=True)
    (folder / "README.md").write_text(chapter(row))
    (folder / "mistakes.md").write_text(f"# Mistakes — Excavation {n:03d}\n\n## Wrong idea\n\n{attempt}\n\n## Why it fails\n\n{failure}\n\n## Repair discovered\n\n{repair}\n")
    (folder / "diagram.md").write_text(f"# Diagram — {title}\n\n```mermaid\nflowchart LR\n    A[\"Observation\"] --> B[\"Tempting shortcut\"]\n    B --> C[\"Counterexample\"]\n    C --> D[\"Required repair\"]\n    D --> E[\"{title.split(' — ')[0]}\"]\n```\n\n```text\nobservation -> attempt -> failure -> requirement -> discovery\n```\n")
    (folder / "exercises.md").write_text(f"# Invention Exercises — Excavation {n:03d}\n\n1. Recreate the smallest version of this failure: {failure}\n2. Explain the repair without using its accepted name: {repair}\n3. Change one assumption in the concrete case and predict the result before running code.\n4. Invent a case where the stated limit becomes dangerous: {limit}\n")
    (folder / "references.md").write_text(f"# Reading Trail — {title}\n\nReferences belong here only after the chapter has made their questions meaningful. Verify primary sources and record which claim each source supports before publication.\n\n- Start with the original or canonical technical work associated with **{title.split(' — ')[0]}**.\n- Add one critical or limitations-focused source.\n- Prefer stable paper or official documentation links over summaries.\n")
    (folder / "images" / "README.md").write_text(f"# Visual Brief — {title}\n\nShow the concrete case from the chapter, then reveal the failed path and repaired path. The image must communicate the causal difference without requiring the final terminology.\n")
    (folder / "implementation" / "README.md").write_text("# Build It Three Times\n\n1. `pure_python.py` keeps the experimental gate visible with dictionaries and booleans.\n2. `numpy.py` evaluates several observations together.\n3. `pytorch.py` expresses the same gate with tensors suitable for a learned system.\n\nPredict which candidate passes before running each file.\n")
    (folder / "implementation" / "pure_python.py").write_text(f'''"""Excavation {n:03d}: make evidence and approval explicit."""\n\ndef accept(candidate):\n    required = ("evidence", "failure_test", "approved")\n    return all(candidate.get(key) for key in required)\n\nif __name__ == "__main__":\n    weak = {{"evidence": True, "failure_test": False, "approved": True}}\n    repaired = {{"evidence": True, "failure_test": True, "approved": True}}\n    assert not accept(weak)\n    assert accept(repaired)\n    print({{"shortcut": accept(weak), "repair": accept(repaired)}})\n''')
    (folder / "implementation" / "numpy.py").write_text(f'''"""Excavation {n:03d}: evaluate a batch of candidate gates."""\n+import numpy as np\n\ndef accept(rows):\n    rows = np.asarray(rows, dtype=bool)\n    return rows.all(axis=1)\n\nif __name__ == "__main__":\n    result = accept([[1, 0, 1], [1, 1, 1]])\n    assert result.tolist() == [False, True]\n    print(result)\n''')
    (folder / "implementation" / "pytorch.py").write_text(f'''"""Excavation {n:03d}: tensor form of the same explicit gate."""\n+try:\n+    import torch\n+except ImportError:\n+    raise SystemExit("Install PyTorch to run this stage.")\n+\ndef accept(rows):\n+    return rows.bool().all(dim=1)\n+\n+if __name__ == "__main__":\n+    result = accept(torch.tensor([[1, 0, 1], [1, 1, 1]]))\n+    assert result.tolist() == [False, True]\n+    print(result)\n''')

# Connect 125 to the new arc.
p125 = ROOT / "excavations/125-open-ended-research-system/README.md"
t125 = p125.read_text()
t125 = t125.replace("The system can conduct bounded research. The next excavation must be forced by the new observations that research creates.", "The system can conduct bounded research, but it still needs to turn curiosity into a claim that evidence could defeat.\n\n[Next: Hypotheses](../126-hypothesis-generation/README.md)")
p125.write_text(t125)

# Extend the main table before its closing style note.
readme = ROOT / "README.md"
text = readme.read_text()
anchor = "\n## A note on style"
rows_md = "\n".join(f"| {n:03d} | [{title}](excavations/{n:03d}-{slug}/README.md) | {question} |" for n, slug, title, question, *_ in ROWS)
if "| 126 |" not in text:
    text = text.replace(anchor, "\n" + rows_md + "\n" + anchor)
readme.write_text(text)

print("Built Excavations 126–150 and connected Part XI.")
