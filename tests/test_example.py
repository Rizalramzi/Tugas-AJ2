import unittest

class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_subtract(self):
        self.assertEqual(4 - 2, 2)

if __name__ == "__main__":
    unittest.main()
