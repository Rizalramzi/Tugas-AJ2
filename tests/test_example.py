import unittest
from app.main import add, subtract

class TestMainFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)

if __name__ == "__main__":
    unittest.main()
