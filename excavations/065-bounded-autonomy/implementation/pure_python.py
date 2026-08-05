def within_envelope(action,envelope): return action["tool"] in envelope["tools"] and action["cost"]<=envelope["remaining_budget"]
