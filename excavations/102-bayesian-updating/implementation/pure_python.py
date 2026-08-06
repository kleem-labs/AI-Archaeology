def update(priors,likelihoods):
 scores=[p*l for p,l in zip(priors,likelihoods)];total=sum(scores);return [s/total for s in scores]
