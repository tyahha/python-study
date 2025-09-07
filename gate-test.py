import unittest
from gate import AND

class TestGate(unittest.TestCase):
  def test_AND(self):
    self.assertEqual(AND(0,0),0)
    self.assertEqual(AND(0,1),0)
    self.assertEqual(AND(1,0),0)
    self.assertEqual(AND(1,1),1)

if __name__ == "__main__":
  unittest.main()
