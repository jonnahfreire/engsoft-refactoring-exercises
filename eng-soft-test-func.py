# run command
# python -m unittest -v eng-soft-test-func.py

import unittest


class EngSoftTest(unittest.TestCase):

    def test_f(self):
        self.assertEqual(f(1, 2), 6)
        self.assertEqual(f(-4, 3), -1)
        self.assertEqual(f(-9, -2), -11)
        self.assertEqual(f(4, -3), 5)
        self.assertEqual(f(3, 0), 6)
        self.assertEqual(f(0, 4), 4)


def f(x, y):
    if (x > 0):
        x = 2 * x
        if (y > 0):
            y = y * 2
    return x + y


if __name__ == "__main__":
    unittest.main()
