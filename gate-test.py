import unittest
from gate import AND, OR

class TestGate(unittest.TestCase):
  def test_AND(self):
    self.assertEqual(AND(0,0),0)
    self.assertEqual(AND(0,1),0)
    self.assertEqual(AND(1,0),0)
    self.assertEqual(AND(1,1),1)

  def test_OR(self):
    self.assertEqual(OR(0,0),0)
    self.assertEqual(OR(1,0),1)
    self.assertEqual(OR(0,1),1)
    self.assertEqual(OR(1,1),1)

if __name__ == "__main__":
  unittest.main()
