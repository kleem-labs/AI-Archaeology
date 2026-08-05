def ready(step,evidence): return all(item in evidence for item in step["requires"])
