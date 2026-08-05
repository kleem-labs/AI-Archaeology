import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]/"excavations"
def load(number):
    path=next(ROOT.glob(number+"-*/implementation/pure_python.py"))
    spec=importlib.util.spec_from_file_location("e"+number,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class FinalArcTests(unittest.TestCase):
    def test_convolution(self):
        self.assertEqual(load("077").convolve([1,2,4],[-1,1]),[1,2])
    def test_pooling(self):
        self.assertEqual(load("078").max_pool([1,7,2,3],2),[7,3])
    def test_q_target(self):
        self.assertEqual(load("089").q_target(0,[4,10],.9),9)
    def test_quantization(self):
        m=load("095");q=m.quantize(.76,.1);self.assertAlmostEqual(m.dequantize(q,.1),.8)
    def test_complete_system_respects_authority(self):
        m=load("100")
        result=m.run("question",lambda x:"evidence",lambda x,e:{"action":"refund"},lambda p:False,lambda p:"done",lambda r:True)
        self.assertEqual(result["status"],"approval_required")

if __name__=="__main__":unittest.main()
