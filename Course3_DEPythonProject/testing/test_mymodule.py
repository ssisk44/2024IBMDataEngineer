import unittest
from mymodule import square, doubler


class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_doubler(self):
        self.assertEqual(doubler(4), 8)


if __name__ == '__main__':
    unittest.main()
