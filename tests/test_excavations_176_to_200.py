"""Executable checks for the accountable pretraining factory in Part XIII."""
from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.parents[1].name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PartXIIITests(unittest.TestCase):
    def test_every_pure_python_experiment_runs(self):
        paths=[]
        for number in range(176,201):
            paths.append(next((ROOT/"excavations").glob(f"{number:03d}-*/implementation/pure_python.py")))
        self.assertEqual(len(paths),25)
        for path in paths:
            result=load(path).demo()
            self.assertIsInstance(result,dict,path)
            self.assertTrue(result,path)

    def test_curation_and_recovery_invariants(self):
        exact=load(ROOT/"excavations/179-exact-deduplication/implementation/pure_python.py")
        near=load(ROOT/"excavations/180-near-deduplication/implementation/pure_python.py")
        resume=load(ROOT/"excavations/195-deterministic-resume/implementation/pure_python.py")
        factory=load(ROOT/"excavations/200-tiny-pretraining-factory/implementation/pure_python.py")
        self.assertEqual(exact.fingerprint("Tiger  river"),exact.fingerprint(" tiger river "))
        self.assertEqual(near.jaccard({1,2,3},{2,3,4}),.5)
        state={"weights":[1.],"moments":[.2],"step":200,"cursor":800,"rng":7}
        self.assertEqual(resume.next_step(state),resume.next_step(state))
        clean={"manifest_signed":True,"resume_verified":True,"validation_passed":True,"memorization_passed":True,"approved":True,"rollback_ready":True}
        self.assertTrue(factory.release(clean))
        self.assertFalse(factory.release(dict(clean,memorization_passed=False)))

    def test_all_three_stages_are_specific_and_compile(self):
        for number in range(176,201):
            folder=next((ROOT/"excavations").glob(f"{number:03d}-*"))/"implementation"
            for name in ("pure_python.py","numpy.py","pytorch.py"):
                text=(folder/name).read_text()
                self.assertIn(f"Excavation {number:03d}",text)
                compile(text,str(folder/name),"exec")


if __name__=="__main__":
    unittest.main()
