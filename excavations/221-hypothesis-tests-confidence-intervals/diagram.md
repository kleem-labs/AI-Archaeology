# Diagram — Excavation 221: Hypothesis Tests and Confidence Intervals — When Is an Improvement Convincing?

```mermaid
flowchart LR
  P["previous excavation"] --> Q["new unanswered question"]
  Q --> X["counterexample"]
  X --> C["Hypothesis Tests and Confidence Intervals"]
  C --> L["known limitation"]
```

```text
temptation : declare every positive sample difference a discovery
break      : another sample from unchanged systems can land above zero by chance. A positive sign says which side won this sample; it does not say how surprising that victory would be if the true average difference were zero.
repair     : state the no-improvement claim, measure the observed mean difference in units of its standard error, and report both a test statistic and the range of effects compatible with the sampling noise
```

The diagram is deliberately causal. Its arrows mean “this failure made the next responsibility necessary,” not merely “read this box next.”
