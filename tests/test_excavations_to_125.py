import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]/"excavations"
def load(number):
    path=next(ROOT.glob(number+"-*/implementation/pure_python.py"))
    spec=importlib.util.spec_from_file_location("e"+number,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class ExcavationsTo125Tests(unittest.TestCase):
    def test_bayesian_update_normalizes(self):
        result=load("102").update([.1,.9],[.8,.1])
        self.assertAlmostEqual(sum(result),1)
        self.assertGreater(result[0],.1)
    def test_tree_exploration_rewards_uncertainty(self):
        f=load("115").ucb
        self.assertGreater(f(.5,1,100),f(.5,50,100))
    def test_program_synthesis(self):
        candidates=[lambda x:x+2,lambda x:x*2]
        self.assertEqual(len(load("120").synthesize(candidates,[(2,4),(3,6)])),1)
    def test_research_requires_approval(self):
        result=load("125").review(lambda:3,lambda x:{"gain":x},lambda evidence:False)
        self.assertFalse(result["deploy"])

if __name__=="__main__":unittest.main()
