def review(experiment,evaluate,approve):
 evidence=evaluate(experiment());return {"evidence":evidence,"deploy":approve(evidence)}
