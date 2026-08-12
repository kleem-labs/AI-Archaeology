# Excavation 097 — Inference Serving

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

We first try to run one request at a time on one full model.

The trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

That failure tells us to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

## Let the case decide

Four prompts share one matrix operation while each retains separate token state.

## The boundary of the discovery

Batching improves throughput but can worsen individual latency.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 098](../098-red-teaming/README.md)
