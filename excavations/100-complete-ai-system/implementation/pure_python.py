def run(observation,retrieve,predict,authorize,act,verify):
 evidence=retrieve(observation);proposal=predict(observation,evidence)
 if not authorize(proposal): return {"status":"approval_required","proposal":proposal}
 result=act(proposal);return {"status":"verified" if verify(result) else "failed","result":result}
